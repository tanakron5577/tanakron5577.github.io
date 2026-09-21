#!/usr/bin/env python3
"""Render basecamp.ics into basecamp/index.html so answer engines can read it.

The page fetches the feed with JavaScript, which most crawlers and answer
engines never run. This writes the same events into the HTML as static markup
plus schema.org JSON-LD, between marker comments, so the page is answerable
without JS. The client script still replaces the list with live data on load.

Re-run this whenever basecamp.ics changes:  python3 build_basecamp.py
"""
import re, html, json, datetime, pathlib

ROOT = pathlib.Path(__file__).parent
ICS  = ROOT / "basecamp.ics"
PAGE = ROOT / "basecamp/index.html"
SITE = "https://randomstorytelling.com"

MON = ["January","February","March","April","May","June","July","August",
       "September","October","November","December"]
DOW = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

def unesc(s):
    return (s.replace("\\n","\n").replace("\\,",",")
             .replace("\;",";").replace("\\\\","\\"))

def parse(text):
    # unfold continuation lines
    lines, out = text.replace("\r\n","\n").split("\n"), []
    for ln in lines:
        if ln[:1] in (" ","\t") and out: out[-1] += ln[1:]
        else: out.append(ln)
    evs, cur = [], None
    for l in out:
        if l == "BEGIN:VEVENT": cur = {}; continue
        if l == "END:VEVENT":
            if cur is not None: evs.append(cur)
            cur = None; continue
        if cur is None: continue
        k = l.find(":")
        if k < 0: continue
        head, val = l[:k], l[k+1:]
        cur[head.split(";")[0]] = {"v": val, "allday": "VALUE=DATE" in head}
    return evs

def dt(p):
    v = p["v"]
    y, m, d = int(v[:4]), int(v[4:6]), int(v[6:8])
    if p["allday"]: return datetime.datetime(y, m, d)
    return datetime.datetime(y, m, d, int(v[9:11] or 0), int(v[11:13] or 0))

def fmt_time(a, b):
    def f(x):
        h, mi = x.hour, x.minute
        ap = "pm" if h >= 12 else "am"
        h = h % 12 or 12
        return f"{h}" + (f":{mi:02d}" if mi else "") + ap
    return f(a) + (f" to {f(b)}" if b else "")

# ---------- read ----------
evs = []
for e in parse(ICS.read_text()):
    if "DTSTART" not in e: continue
    s  = dt(e["DTSTART"])
    en = dt(e["DTEND"]) if "DTEND" in e else None
    evs.append({
        "s": s, "en": en, "allday": e["DTSTART"]["allday"],
        "title": unesc(e.get("SUMMARY", {}).get("v", "")).strip(),
        "loc":   unesc(e.get("LOCATION", {}).get("v", "")).strip(),
        "url":   e.get("URL", {}).get("v", "").strip(),
        "desc":  unesc(e.get("DESCRIPTION", {}).get("v", "")).strip(),
        "cat":   e.get("CATEGORIES", {}).get("v", "").strip().lower(),
    })

today = datetime.datetime.combine(datetime.date.today(), datetime.time())
def still_upcoming(e):
    last = (e["en"] - datetime.timedelta(days=1)) if (e["en"] and e["allday"]) else (e["en"] or e["s"])
    return last >= today
evs = sorted([e for e in evs if still_upcoming(e)], key=lambda e: e["s"])

# ---------- static list ----------
rows, last_month = [], None
for e in evs:
    key = (e["s"].year, e["s"].month)
    if key != last_month:
        if last_month is not None: rows.append("</div>")
        rows.append(f'<div class="month"><h3>{MON[e["s"].month-1]} {e["s"].year}</h3>')
        last_month = key
    when = f'{DOW[e["s"].weekday()]} {e["s"].day}'
    if e["allday"] and e["en"]:
        l = e["en"] - datetime.timedelta(days=1)
        if l > e["s"]: when += f" to {l.day}"
    meta = []
    if not e["allday"]: meta.append(fmt_time(e["s"], e["en"]))
    if e["loc"]: meta.append(re.sub(r",\s*TX$", "", e["loc"]))
    t = html.escape(e["title"])
    if e["url"]:
        t = f'<a href="{html.escape(e["url"])}" target="_blank" rel="noopener">{t}</a>'
    m = f'<span class="m">{html.escape(" · ".join(meta))}</span>' if meta else ""
    rows.append(f'<div class="ev"><div class="d">{when}</div><div class="t">{t}{m}</div></div>')
if last_month is not None: rows.append("</div>")
static_list = "\n".join(rows)

# ---------- schema.org ----------
def iso(x, allday):
    return x.strftime("%Y-%m-%d") if allday else x.strftime("%Y-%m-%dT%H:%M:00-05:00")

items = []
for i, e in enumerate([x for x in evs if x["cat"] != "deadline"], 1):
    ev = {
        "@type": "Event",
        "name": e["title"],
        "startDate": iso(e["s"], e["allday"]),
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
    }
    if e["en"]: ev["endDate"] = iso(e["en"], e["allday"])
    if e["loc"]:
        ev["location"] = {"@type": "Place", "name": e["loc"],
                          "address": {"@type": "PostalAddress", "addressRegion": "TX",
                                      "addressCountry": "US"}}
    if e["url"]: ev["url"] = e["url"]
    first = e["desc"].split("\n")[0].strip()
    if first and not first.lower().startswith("source:"): ev["description"] = first
    items.append({"@type": "ListItem", "position": i, "item": ev})

counts = {}
for e in evs: counts[e["cat"]] = counts.get(e["cat"], 0) + 1
n_total    = len(evs)
n_deadline = counts.get("deadline", 0)
n_class    = counts.get("class", 0)

def venues(cats, limit=6):
    seen = []
    for e in evs:
        if e["cat"] in cats and e["loc"]:
            name = e["loc"].split(",")[0].strip()
            if name and name not in seen and name.lower() != "various locations":
                seen.append(name)
        if len(seen) >= limit: break
    return seen

# Curated from the feed rather than auto-derived: the LOCATION field holds
# whichever cinema a one-off screening booked, which is not an answer to
# "where do people meet". Review this list when the feed's regulars change.
MEET_ORGS = ["Austin Film Meet", "Austin Film Society", "The Hideout Theatre",
             "ColdTowne Theater", "Austin Film Festival", "Women Writing for Film and Television ATX"]
present = [o for o in MEET_ORGS
           if any(o.lower() in (e["title"] + " " + e["loc"]).lower() for e in evs)]
meet_rooms = present or MEET_ORGS
class_rooms = venues({"class"})
def listify(xs):
    return ", ".join(xs[:-1]) + " and " + xs[-1] if len(xs) > 1 else (xs[0] if xs else "")

FAQ = [
 ("What film and TV events are happening in Austin right now?",
  f"Base Camp tracks {n_total} upcoming rooms across Texas film and TV, including classes, screenings, "
  f"showcases, mixers and festival submission deadlines. The full list is on this page and in a calendar "
  f"feed you can subscribe to at {SITE}/basecamp.ics."),
 ("Where do filmmakers and actors meet in Austin?",
  f"The recurring rooms on Base Camp include {listify(meet_rooms)}. Base Camp puts their dates on one "
  f"calendar so you can show up to the same room twice, which is how crews actually form."),
 ("How do I meet people in the Austin film industry?",
  "Pick two or three rooms and go back to them. Base Camp exists so that is easy: one calendar of the "
  "mixers, classes, screenings and showcases in Texas film and TV, instead of a dozen separate sites "
  "and mailing lists."),
 ("Where can I take film or acting classes in Austin?",
  f"Base Camp currently lists {n_class} upcoming classes and workshops, from {listify(class_rooms)}. "
  f"Dates and links are on this page."),
 ("Are there upcoming Texas film festival deadlines?",
  f"Yes. Base Camp is tracking {n_deadline} upcoming submission deadlines for Texas and Texas-adjacent "
  f"festivals, listed alongside the events so a deadline does not sneak past you."),
 ("Is there a calendar of Austin film and TV events I can subscribe to?",
  f"Yes, and it is free. Subscribe to {SITE}/basecamp.ics with the Apple or Google buttons on this page, "
  f"or paste that address into any calendar app. It updates as the list updates. There is also a free "
  f"monthly email."),
]

graph = [
 {"@type":"WebPage","@id":f"{SITE}/basecamp/#webpage","url":f"{SITE}/basecamp/",
  "name":"Base Camp, the Austin and Texas film and TV calendar",
  "description":"One calendar of the rooms where Texas film and TV people meet: classes, screenings, "
                "showcases, mixers and festival deadlines. Austin rooted, Texas wide.",
  "inLanguage":"en-US",
  "isPartOf":{"@type":"WebSite","@id":f"{SITE}/#website","url":SITE,"name":"Random Storytelling"},
  "about":[{"@type":"Thing","name":"Austin film industry"},
           {"@type":"Thing","name":"Texas film and television"},
           {"@type":"Thing","name":"Film and TV networking events"}]},
 {"@type":"ItemList","@id":f"{SITE}/basecamp/#events","name":"Upcoming Texas film and TV events",
  "numberOfItems":len(items),"itemListOrder":"https://schema.org/ItemListOrderAscending",
  "itemListElement":items},
 {"@type":"FAQPage","@id":f"{SITE}/basecamp/#faq",
  "mainEntity":[{"@type":"Question","name":q,
                 "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]},
]
jsonld = json.dumps({"@context":"https://schema.org","@graph":graph}, indent=1, ensure_ascii=False)

faq_html = "\n".join(
  f'    <div class="qa"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></div>' for q,a in FAQ)

# ---------- patch ----------
page = PAGE.read_text()
def swap(marker, payload, page):
    a, b = f"<!--{marker}:start-->", f"<!--{marker}:end-->"
    pat = re.compile(re.escape(a) + r".*?" + re.escape(b), re.S)
    if not pat.search(page): raise SystemExit(f"marker {marker} missing")
    return pat.sub(lambda _: f"{a}\n{payload}\n{b}", page)

page = swap("aeo-jsonld", f'<script type="application/ld+json">\n{jsonld}\n</script>', page)
page = swap("aeo-events", static_list, page)
page = swap("aeo-faq",    faq_html, page)
page = re.sub(r'(<span id="count">)[^<]*(</span>)', rf'\g<1>{n_total} upcoming\g<2>', page)
PAGE.write_text(page)
print(f"rendered {n_total} upcoming events ({len(items)} as schema Events, {n_deadline} deadlines), {len(FAQ)} FAQs")

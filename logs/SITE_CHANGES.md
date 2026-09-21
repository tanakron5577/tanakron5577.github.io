
## 2026-09-21 — Swish row on the studio homepage pulled back

**Why:** Lawrence's order, this session: "remove that from site. well keep it blank until were truly ready. everything else lives tho," then "Up to 25 players · players free / Start your roster → those too." The trainer claims are ahead of what we can stand behind today.

**Changed:** `index.html`, the Swish row (05).

**BEFORE — benefit line:**
> Your players put in the hours between sessions and you have no idea what happened. **Every rep comes back to you as a number, so you walk into the next session already knowing what to fix, and the parent writing the check can watch the month go up.** Your players download it free and their week lands on your roster. Progress on the page is what renews a client. Video never leaves the phone.

**AFTER:** empty `<div class="ben">` holding an HTML comment. The div stays so the row's grid does not collapse.

**BEFORE — price block:**
`$29 / mo` + `<small>Up to 25 players · players free</small>` + two CTAs: "Try it free, one shot →" (/swish/) and "Start your roster →" (Stripe link buy.stripe.com/aFa9ANglv13jeY8aYb3ZK00)

**AFTER (final, after three further instructions the same session):** the row holds the number 05, the Swish name linking to /swish/, and one CTA reading "Try it free, 10 shots →". Nothing else.

Removed in the same pass, each as an empty div with a dated comment so the grid does not collapse:
- `.for` — "Skills trainers · programs · schools"
- `.pr` price — "$29 / mo"
- `.pr` seat line — "Up to 25 players · players free"
- `.pr` CTA — "Start your roster →" (Stripe buy.stripe.com/aFa9ANglv13jeY8aYb3ZK00)

Kept and reworded on his order ("try it here stays for sure" / "and make it 10 shots"): the try-it CTA, from **"Try it free, one shot →"** to **"Try it free, 10 shots →"**.

**Note on that claim:** the free player seat has no shot cap, so "10 shots" is an invitation, not a limit. It does not promise anything the app withholds.

**Backup:** `index.html.bak-2026-09-21-pre-swish-ben` (full file, pre-change).

**Undo:** restore that backup, or paste the BEFORE blocks above back into the row, then read the live page back.

**Resolved in session:** the price came out too. The Stripe payment link itself is untouched and still live; it is only unlinked from this row.

**Metric:** unmeasurable on its own (no analytics split by row). Recorded so it can be undone exactly.

## 2026-09-21 — Custom denim row (03) pulled back, and renamed

**Why:** Lawrence's order, same session as the Swish pullback: he quoted the copy block and said remove, then "change to CUSTOM DENIM JACKET."

**Changed:** `index.html`, row 03.

**BEFORE — name:** `Custom denim`
**AFTER — name:** `Custom denim jacket` (same link, instagram.com/craneseyeview)

**BEFORE — collaborator line (`.for`):**
> With @craneseyeview · One of one

**BEFORE — benefit line (`.ben`):**
> That jacket had a whole life before it got to you. **We find it, then build your story into the patches and the placement.** Yours is the second life it gets. Priced by how many patches your story takes.

**BEFORE — price block:**
`$250 to start` + `<small>Credited to the piece</small>`

**AFTER:** all three are empty divs carrying dated comments, so the grid keeps its shape.

**Still live in this row:** the number 03, the name "Custom denim jacket" linking to the @craneseyeview instagram, and both CTAs: "Start a jacket →" (Stripe buy.stripe.com/fZu28l8T313j03e8Q33ZK04) and "Free 15 minute call →" (Calendly, prefilled a2=Custom denim jacket).

**Flag for Lawrence:** the Stripe button still charges **$250** on the other side, but the page no longer says so. Someone clicks "Start a jacket" and meets a price they were not shown. Decide whether the price goes back, the button comes out, or it stays as is.

**Backup:** `index.html.bak-2026-09-21-pre-denim` (full file, pre-change).

**Undo:** restore that backup, or paste the BEFORE blocks back in, then read the live page back.

**Metric:** unmeasurable on its own. Recorded so it can be undone exactly.

## 2026-09-21 — Home Team row (06) benefit copy pulled

**Why:** Lawrence's order, same session as the Swish and denim pullbacks. He quoted the benefit paragraph alone this time, so only that came out.

**Changed:** `index.html`, row 06.

**BEFORE — benefit line (`.ben`):**
> You cannot actually leave. Not a weekend, not a day, because what breaks breaks quietly and you are the only one looking. **Thirteen stations watch all of it overnight.** You wake up to one short list, most of it already handled.

**AFTER:** empty `<div class="ben">` with a dated comment.

**Still live in this row, untouched:** the number 06, the name "Home Team" (no link, same as before), "Founder run Shopify & Amazon brands", the price `$4,000 + $1,500 / mo`, the sub-line "Install, then monthly", and both CTAs: "Book the install →" (Stripe buy.stripe.com/28EfZb6KV4fv5ny9U73ZK02) and "Free 15 minute call →" (Calendly).

**Note:** unlike rows 03 and 05, this row still carries its price and its audience line. Nothing here is a mismatch.

**Backup:** `index.html.bak-2026-09-21-pre-hometeam` (full file, pre-change).

**Undo:** restore that backup, or paste the BEFORE paragraph back into the row, then read the live page back.

**Metric:** unmeasurable on its own. Recorded so it can be undone exactly.

### 2026-09-21 (same day, follow-up) — Portfolio link added to row 03

**Why:** Lawrence: "add PORTFOLIO and that leads to instagram.com/craneseyeview".

**Added:** a first CTA on row 03, `Portfolio →`, to `https://instagram.com/craneseyeview`, ahead of "Start a jacket →" and "Free 15 minute call →".

**Row 03 now:** 03 · Custom denim jacket · Portfolio → · Start a jacket → · Free 15 minute call →

**Note:** the row name already links to the same instagram, so that destination is now reachable two ways from one row. Left as asked.

**Undo:** delete the `Portfolio &rarr;` anchor from the `.pr` block.

### 2026-09-21 (same day, follow-up) — Home Team sub-line removed

**Why:** Lawrence: remove "Install, then monthly".

**BEFORE:** `<div class="pr">$4,000 + $1,500 / mo<small>Install, then monthly</small>`
**AFTER:** `<div class="pr">$4,000 + $1,500 / mo`

**Row 06 now:** 06 · Home Team · Founder run Shopify & Amazon brands · $4,000 + $1,500 / mo · Book the install → · Free 15 minute call →

**Note:** the price still reads `$4,000 + $1,500 / mo`, which carries the install-then-monthly shape on its own, so nothing became unclear.

**Undo:** put the `<small>Install, then monthly</small>` back immediately after the price.

### 2026-09-21 (same day, follow-up) — Agencies linked on row 02

**Why:** Lawrence: "these hyperlink to the googlesheets page at the bottom to contact them" — TAG Talent (TX) · Rage Talent (CA).

**BEFORE:** `<div class="pr">Represented<small>TAG Talent (TX) &middot; Rage Talent (CA)</small></div>` — plain text, not clickable.

**AFTER:** each agency name is its own link to the credits sheet, the same destination the bottom "Credits →" button opens:
`https://docs.google.com/spreadsheets/d/1e1U3E8objQgBxJlchwm96cCpPX10MO0QR6YbripdG94/edit`

**Also added, one CSS rule:** `.pr small a` gets the house red underline (same treatment as `.nm a`, offset tightened to 4px for the smaller type). Without it the global `a{color:inherit;text-decoration:none}` would have rendered them as plain grey text and nobody would know to tap.

**Verified:** on a local copy at phone width, both anchors resolve to the sheet and the computed underline colour is rgb(142, 22, 32).

**Undo:** unwrap the two anchors back to plain text, and delete the `.pr small a` rule.

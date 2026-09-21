
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

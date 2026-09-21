#!/usr/bin/env python3
"""patch_denim_row.py DEPOSIT STRIPE_URL "LINE1" "LINE2" : rewrite the Custom denim row on index.html.
Backup first (index.html.bak-<stamp>-pre-denim-price). Idempotent: re-running replaces the whole row block."""
import re, sys, shutil, datetime as dt
dep, stripe_url, line1, line2 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
p = 'index.html'; s = open(p, encoding='utf-8').read()
stamp = dt.datetime.now().strftime('%Y-%m-%d-%H%M')
shutil.copy(p, f'{p}.bak-{stamp}-pre-denim-price')
start = s.index('<div class="row">', s.index('Custom denim') - 400)
end = s.index('</div>\n    </div>', start) + len('</div>\n    </div>')
old = s[start:end]
new = f'''<div class="row">
      <div class="n">03</div>
      <div><div class="nm"><a href="https://instagram.com/craneseyeview" target="_blank" rel="noopener">Custom denim</a></div><div class="for">With @craneseyeview &middot; One of one</div></div>
      <div class="ben">Everything you own was designed for a million people. None of it says anything about the one wearing it. <b>One of one, every time.</b> We find the vintage jacket, we build the story into the patches and the placement, and you get the only one there is. Priced by how many patches your story takes.</div>
      <div class="pr">${dep} to start<small>{line1}</small><small>{line2}</small>
        <a class="cta" href="{stripe_url}" target="_blank" rel="noopener">Start a jacket &rarr;</a>
        <a class="cta" href="https://calendly.com/randomstorytelling/free-intro-call?a2=Custom%20denim%20jacket" target="_blank" rel="noopener">Free 15 minute call &rarr;</a></div>
    </div>'''
assert 'Custom denim' in old and old.count('<div class="row">') == 1, old[:200]
s = s.replace(old, new); open(p, 'w', encoding='utf-8').write(s)
print('row replaced; backup', f'{p}.bak-{stamp}-pre-denim-price'); print(new)

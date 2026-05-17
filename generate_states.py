#!/usr/bin/env python3
"""
USATaxRefund — State Tax Page Generator
Add any US state to STATES list and run to generate pages.
Usage: python3 generate_states.py
Output: ./generated/states/
"""
import os, datetime

ALINK = "https://www.linkconnector.com/ta.php?lc=007949061588005142&atid=UsaTaxRefunds"
BASE  = "https://brightlane.github.io/UsaTaxRefund"
DATE  = datetime.date.today().isoformat()
OUT   = "generated/states"
os.makedirs(OUT, exist_ok=True)

CSS = """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>:root{--blue:#003087;--blue2:#0050c8;--red:#cc0000;--gold:#f5a623;--dark:#0a0d14;--card:#111520;--border:#1e2540;--text:#eef0f8;--muted:#7a8aa8;--green:#00c853;}*{box-sizing:border-box;margin:0;padding:0;}body{font-family:Inter,sans-serif;background:var(--dark);color:var(--text);line-height:1.6;}nav{position:sticky;top:0;z-index:100;background:rgba(10,13,20,.96);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 28px;height:60px;}.logo{font-size:20px;font-weight:900;color:var(--text);text-decoration:none;}.logo span{color:var(--gold);}.nc{background:var(--red);color:#fff;padding:9px 20px;border-radius:8px;font-weight:700;font-size:13px;text-decoration:none;}.tk{background:var(--blue);overflow:hidden;white-space:nowrap;padding:8px 0;}.ti{display:inline-block;animation:tk 30s linear infinite;}.ti span{margin:0 36px;font-size:12px;font-weight:700;color:#fff;}@keyframes tk{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}.hero{background:linear-gradient(180deg,#00082a 0%,var(--dark) 100%);padding:64px 24px 44px;text-align:center;border-bottom:1px solid var(--border);}.badge{display:inline-flex;align-items:center;gap:8px;background:rgba(0,80,200,.15);border:1px solid rgba(0,80,200,.4);color:#7ab0ff;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:6px 16px;border-radius:20px;margin-bottom:20px;}h1{font-size:clamp(26px,5vw,54px);font-weight:900;line-height:1.05;letter-spacing:-2px;margin-bottom:16px;}h1 em{color:var(--gold);font-style:normal;}.hs{color:var(--muted);font-size:16px;max-width:560px;margin:0 auto 28px;line-height:1.6;}.btn{background:var(--red);color:#fff;font-weight:800;padding:16px 36px;border-radius:10px;text-decoration:none;font-size:15px;display:inline-flex;align-items:center;gap:8px;}.s{padding:56px 24px;max-width:940px;margin:0 auto;}.ey{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:10px;}h2{font-size:clamp(20px,3vw,32px);font-weight:800;letter-spacing:-1px;margin-bottom:12px;}.sub{color:var(--muted);font-size:14px;margin-bottom:28px;}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;margin-bottom:24px;}.c{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;}.c.gr{border-color:rgba(0,200,83,.3);background:#050f05;}.c.go{border-color:rgba(245,166,35,.3);background:#0f0a00;}.c.re{border-color:rgba(204,0,0,.3);background:#150505;}.ci{font-size:24px;margin-bottom:8px;}.ct{font-weight:700;font-size:13px;margin-bottom:5px;}.c.gr .ct{color:var(--green);}.c.go .ct{color:var(--gold);}.c.re .ct{color:#ff8888;}.cd{color:var(--muted);font-size:12px;line-height:1.5;}.w{background:#1a0800;border:1px solid rgba(245,166,35,.4);border-radius:12px;padding:20px;margin:16px 0;}.w h4{color:var(--gold);font-size:14px;font-weight:700;margin-bottom:6px;}.w p{color:#c0b080;font-size:13px;line-height:1.6;margin:0;}.cb{background:linear-gradient(135deg,#001a6e,#003087);border:1px solid rgba(0,80,200,.4);border-radius:14px;padding:40px 32px;text-align:center;margin:36px 0;}.cb h2{margin-bottom:10px;}.cb p{color:#a0b8e8;font-size:14px;margin-bottom:20px;}.fqs{display:flex;flex-direction:column;gap:10px;}.fq{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;}.fqq{font-weight:700;font-size:14px;margin-bottom:6px;}.fqa{color:var(--muted);font-size:13px;line-height:1.6;}footer{background:var(--card);border-top:1px solid var(--border);padding:20px 24px;text-align:center;font-size:12px;color:var(--muted);line-height:2;}@media(max-width:600px){.hero,.s{padding:40px 16px;}}</style>"""

def cta(state, form):
    return f'<div class="cb"><h2>File Your Federal 1040-NR with e-file.com</h2><p>Handle your federal return with e-file.com. Then file your {state} {form} through the state tax authority website. IRS authorized · A+ BBB · Refund in 10-21 days.</p><a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored" style="font-size:16px;padding:17px 40px;display:inline-flex;">🚀 File Federal 1040-NR Free</a><p style="color:#7ab0ff;font-size:12px;margin-top:12px;">IRS Authorized · A+ BBB · 10-21 Day Refund</p></div>'

def faq(q, a):
    return f'<div class="fq"><div class="fqq">{q}</div><div class="fqa">{a}</div></div>'

def cards(*items):
    o = '<div class="g">'
    for cls, icon, title, desc in items:
        o += f'<div class="c {cls}"><div class="ci">{icon}</div><div class="ct">{title}</div><div class="cd">{desc}</div></div>'
    return o + '</div>'

def build(fname, title, desc, badge, h1, hs, body):
    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/{fname}">
{CSS}</head><body>
<nav><a class="logo" href="/UsaTaxRefund/"><span>🇺🇸</span> USATaxRefund</a><a class="nc" href="{ALINK}" target="_blank" rel="noopener sponsored">File Free →</a></nav>
<div class="tk"><div class="ti"><span>🗺️ STATE TAX GUIDE 2026</span><span>🏛️ IRS AUTHORIZED</span><span>✅ FREE FEDERAL FILING</span><span>⚡ REFUND 10-21 DAYS</span><span>📋 1040-NR SUPPORTED</span><span>🗺️ STATE TAX GUIDE 2026</span></div></div>
<div class="hero"><div class="badge">{badge}</div><h1>{h1}</h1><p class="hs">{hs}</p>
<a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored">🚀 File Federal 1040-NR Free</a></div>
<div class="s">{body}
<p style="text-align:center;margin-top:28px;"><a href="/UsaTaxRefund/" style="color:var(--muted);font-size:13px;">← USATaxRefund Home</a></p></div>
<footer><p>USATaxRefund is an independent affiliate site earning commissions from e-file.com links.</p>
<p>Not tax or legal advice. e-file.com is IRS-authorized, A+ BBB rated since 2014.</p>
<p>© 2026 USATaxRefund · <a href="{ALINK}" style="color:var(--gold)">File Free →</a></p></footer>
</body></html>"""
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)
    return fname

# ════════════════════════════════════════════════════════════════════
# ADD STATES HERE
# Format:
#   slug          = filename without .html
#   flag          = emoji for the state
#   state         = state name
#   form          = state tax form name  e.g. "540NR" or "None"
#   rate          = tax rate  e.g. "4.95% flat" or "No state income tax"
#   no_tax        = True if state has no income tax
#   treaty        = how state treats federal treaties
#   universities  = list of major universities in the state
#   extra_notes   = any special state-specific notes
#   faq1_q/a      = first FAQ
#   faq2_q/a      = second FAQ
# ════════════════════════════════════════════════════════════════════
STATES = [
    {
        "slug": "california-state-taxes-f1",
        "flag": "🌴", "state": "California", "form": "CA 540NR",
        "rate": "up to 13.3%", "no_tax": False,
        "treaty": "California does NOT honor any federal tax treaties",
        "universities": ["UCLA", "UC Berkeley", "Stanford", "USC", "UC San Diego", "UC Davis", "Caltech"],
        "extra_notes": "California has the highest state income tax in the US. Even treaty-exempt federal income is fully taxable in California.",
        "faq1_q": "Does California recognize the China or India tax treaty?",
        "faq1_a": "No — California does not honor any federal tax treaties for state income tax purposes. Income that is exempt from federal tax under the US-China or US-India treaty is fully taxable in California at regular state rates.",
        "faq2_q": "What forms do California F-1 students file?",
        "faq2_a": "Federal Form 1040-NR (with e-file.com) and California Form 540NR (through the California Franchise Tax Board at ftb.ca.gov). File both by April 15. Complete federal first — California uses your federal AGI as the starting point.",
    },
    {
        "slug": "new-york-state-taxes-f1",
        "flag": "🗽", "state": "New York", "form": "IT-203",
        "rate": "up to 10.9%", "no_tax": False,
        "treaty": "New York partially recognizes some federal tax treaties",
        "universities": ["NYU", "Columbia", "Cornell", "Fordham", "Syracuse", "RPI", "Stony Brook"],
        "extra_notes": "New York City residents pay additional NYC income tax on top of NY State tax. If you live in the 5 boroughs, budget for both.",
        "faq1_q": "Does New York recognize federal tax treaties?",
        "faq1_a": "New York partially recognizes some federal tax treaties per NY Publication 901. Check the publication for your specific treaty country and article. Some treaty-exempt federal income may also be exempt for New York purposes.",
        "faq2_q": "Do I pay NYC income tax as an F-1 student?",
        "faq2_a": "If you live in any of the 5 NYC boroughs (Manhattan, Brooklyn, Queens, Bronx, Staten Island), yes — NYC income tax applies. It is calculated on the same IT-203 form as New York State tax. Commuters from New Jersey or Connecticut who work in NYC do not pay NYC income tax.",
    },
    {
        "slug": "texas-state-taxes-f1",
        "flag": "⭐", "state": "Texas", "form": "None",
        "rate": "No state income tax", "no_tax": True,
        "treaty": "No state tax — treaty benefits apply federally in full",
        "universities": ["UT Austin", "Texas A&M", "Rice University", "SMU", "TCU", "Baylor", "Texas Tech"],
        "extra_notes": "Texas is one of the best states for international students — no state income tax means federal treaty benefits are your complete and total tax saving.",
        "faq1_q": "Do F-1 students in Texas file a state return?",
        "faq1_a": "No — Texas has no individual state income tax. F-1 and J-1 students at Texas universities only need to file their federal 1040-NR. No Texas state return is required.",
        "faq2_q": "I work on OPT at a company in Austin — do I pay Texas state tax?",
        "faq2_a": "No — Texas has no state income tax. Your OPT wages are subject to federal income tax (1040-NR, with any applicable treaty benefits) and FICA is exempt as a nonresident F-1 student. Zero Texas state income tax on wages.",
    },
    {
        "slug": "florida-state-taxes-f1",
        "flag": "🌴", "state": "Florida", "form": "None",
        "rate": "No state income tax", "no_tax": True,
        "treaty": "No state tax — treaty benefits apply federally in full",
        "universities": ["University of Florida", "Florida State", "University of Miami", "UCF", "USF", "FAU", "FIU"],
        "extra_notes": "Florida has no individual income tax — one of the most tax-friendly states for international students. Federal 1040-NR only.",
        "faq1_q": "Do F-1 students at UF or FSU file a Florida state return?",
        "faq1_a": "No — Florida has no individual state income tax. F-1 and J-1 students at all Florida universities (UF, FSU, Miami, UCF, USF) only need to file their federal 1040-NR. No Florida state return exists for individuals.",
        "faq2_q": "Does Florida have any taxes that affect international students?",
        "faq2_a": "Florida has a 6% sales tax on most goods (groceries exempt) and a corporate income tax, but no individual income tax. The only tax obligation for most F-1 students is federal income tax via Form 1040-NR.",
    },
    {
        "slug": "washington-state-taxes-f1",
        "flag": "🌲", "state": "Washington", "form": "None",
        "rate": "No state income tax", "no_tax": True,
        "treaty": "No state tax — treaty benefits apply federally in full",
        "universities": ["University of Washington", "Washington State", "Seattle University", "SPU", "Gonzaga", "WWU"],
        "extra_notes": "Washington State has no individual income tax — great for OPT workers at Amazon, Microsoft and Boeing in the Seattle area.",
        "faq1_q": "I am on OPT working at Amazon in Seattle — do I pay Washington state tax?",
        "faq1_a": "No — Washington State has no individual income tax. Your Amazon OPT wages are subject to federal income tax (1040-NR) and FICA is exempt as a nonresident F-1 student. Zero Washington state income tax. This is a significant advantage over OPT workers in California or New York.",
        "faq2_q": "Does Washington have a capital gains tax?",
        "faq2_a": "Washington enacted a 7% capital gains tax in 2023 on long-term capital gains above $250,000. This affects very few F-1 students. Ordinary income (wages, stipends) is not subject to this tax.",
    },
    {
        "slug": "massachusetts-state-taxes-f1",
        "flag": "🦞", "state": "Massachusetts", "form": "MA Form 1-NR/PY",
        "rate": "5% flat", "no_tax": False,
        "treaty": "Massachusetts partially recognizes some federal tax treaties",
        "universities": ["MIT", "Harvard", "Boston University", "Northeastern", "Tufts", "Boston College", "UMass Amherst"],
        "extra_notes": "Massachusetts has a flat 5% income tax rate. MIT, Harvard and BU students with stipends or TA/RA income must file both federal 1040-NR and Massachusetts Form 1-NR/PY.",
        "faq1_q": "Does Massachusetts recognize the China or India tax treaty?",
        "faq1_a": "Massachusetts partially recognizes some federal tax treaties but its treatment is limited. Generally, Massachusetts does not fully exempt treaty income that is exempt federally. Budget for Massachusetts income tax on amounts that are federally exempt under a treaty.",
        "faq2_q": "What is the Massachusetts filing deadline?",
        "faq2_a": "April 15, 2026 — same as federal. Massachusetts offers an automatic extension if you have a federal extension, but any Massachusetts tax owed is still due April 15 to avoid penalty and interest.",
    },
    {
        "slug": "illinois-state-taxes-f1",
        "flag": "🌽", "state": "Illinois", "form": "IL-1040 + Schedule NR",
        "rate": "4.95% flat", "no_tax": False,
        "treaty": "Illinois does not recognize federal tax treaties",
        "universities": ["University of Chicago", "Northwestern", "UIUC", "DePaul", "Loyola", "IIT", "Lake Forest"],
        "extra_notes": "Illinois has a flat 4.95% income tax. Unlike New York or California, Illinois has a simpler single-rate system but does not recognize any federal tax treaties.",
        "faq1_q": "Does Illinois recognize the China or India tax treaty?",
        "faq1_a": "No — Illinois does not recognize federal tax treaties for state income tax purposes. Income that is exempt from federal tax under a treaty is still fully taxable in Illinois at the 4.95% flat rate. Budget accordingly.",
        "faq2_q": "What do UChicago and Northwestern F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Illinois Form IL-1040 with Schedule NR (Nonresident) through the Illinois Department of Revenue at mytax.illinois.gov. File both by April 15.",
    },
    {
        "slug": "pennsylvania-state-taxes-f1",
        "flag": "🏔️", "state": "Pennsylvania", "form": "PA-40",
        "rate": "3.07% flat", "no_tax": False,
        "treaty": "Pennsylvania does not recognize federal tax treaties",
        "universities": ["Penn State", "University of Pennsylvania", "Carnegie Mellon", "Drexel", "Temple", "Villanova", "Lehigh"],
        "extra_notes": "Pennsylvania has a low flat 3.07% income tax rate — one of the lower state rates in the country. However, many PA cities (Philadelphia, Pittsburgh) add a local income tax on top.",
        "faq1_q": "Does Pennsylvania recognize the China or India tax treaty?",
        "faq1_a": "No — Pennsylvania does not recognize federal tax treaties. Income exempt federally under a treaty is still taxable in Pennsylvania at the 3.07% flat rate.",
        "faq2_q": "Do UPenn F-1 students in Philadelphia pay city tax?",
        "faq2_a": "Yes — Philadelphia has a wage tax of 3.75% for residents and 3.44% for nonresidents who work in Philadelphia. UPenn students working as TAs or RAs in Philadelphia are subject to the Philadelphia wage tax in addition to federal and Pennsylvania state tax.",
    },
    {
        "slug": "michigan-state-taxes-f1",
        "flag": "〽️", "state": "Michigan", "form": "MI-1040",
        "rate": "4.25% flat", "no_tax": False,
        "treaty": "Michigan does not fully recognize federal tax treaties",
        "universities": ["University of Michigan", "Michigan State", "Wayne State", "Western Michigan", "Central Michigan", "Oakland University"],
        "extra_notes": "Michigan has a flat 4.25% income tax. Ann Arbor (home of UMich) also has a city income tax of 1% for residents and 0.5% for nonresidents working in Ann Arbor.",
        "faq1_q": "Does Michigan recognize federal tax treaties?",
        "faq1_a": "Michigan generally does not fully recognize federal tax treaties. Income that is exempt from federal tax under a treaty (China Article 20, India Article 21) may still be taxable in Michigan at the 4.25% flat rate.",
        "faq2_q": "Ann Arbor city tax for UMich students?",
        "faq2_a": "Ann Arbor has a city income tax of 1% for city residents and 0.5% for nonresidents who work in Ann Arbor. Most F-1 students at UMich are nonresidents for Ann Arbor city tax purposes and pay 0.5% on Ann Arbor-source income.",
    },
    {
        "slug": "north-carolina-state-taxes-f1",
        "flag": "🏔️", "state": "North Carolina", "form": "NC D-400",
        "rate": "4.5% flat", "no_tax": False,
        "treaty": "North Carolina does not fully honor federal tax treaties",
        "universities": ["UNC Chapel Hill", "Duke University", "NC State", "Wake Forest", "Davidson", "Elon"],
        "extra_notes": "North Carolina has a 4.5% flat income tax rate. UNC, Duke and NC State students with income must file both federal 1040-NR and North Carolina Form D-400.",
        "faq1_q": "Does North Carolina recognize federal tax treaties?",
        "faq1_a": "North Carolina does not fully recognize federal tax treaties. Some treaties may provide partial relief — check the NC Department of Revenue guidance for your specific treaty country and article.",
        "faq2_q": "What do Duke and UNC F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus North Carolina Form D-400 as a nonresident through ncdor.gov. File both by April 15, 2026.",
    },
    {
        "slug": "georgia-state-taxes-f1",
        "flag": "🍑", "state": "Georgia", "form": "GA Form 500",
        "rate": "5.49% flat", "no_tax": False,
        "treaty": "Georgia does not fully recognize federal tax treaties",
        "universities": ["Georgia Tech", "Emory", "UGA", "Georgia State", "Mercer", "Kennesaw State"],
        "extra_notes": "Georgia has a 5.49% flat income tax rate (reduced from graduated rates). Georgia Tech in Atlanta is one of the top engineering schools with a large international student population.",
        "faq1_q": "Does Georgia recognize the India or China treaty?",
        "faq1_a": "Georgia does not fully recognize federal tax treaties. Georgia-source income is taxed at Georgia state rates regardless of federal treaty exemptions.",
        "faq2_q": "What do Georgia Tech and Emory F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Georgia Form 500 as a nonresident through the Georgia Department of Revenue website. File both by April 15.",
    },
    {
        "slug": "virginia-state-taxes-f1",
        "flag": "🦅", "state": "Virginia", "form": "VA Form 763",
        "rate": "2-5.75% graduated", "no_tax": False,
        "treaty": "Virginia partially recognizes some federal tax treaties",
        "universities": ["University of Virginia", "Virginia Tech", "George Mason", "William & Mary", "JMU", "Virginia Commonwealth"],
        "extra_notes": "Virginia has graduated income tax rates from 2% to 5.75%. George Mason University near DC has a particularly large international student population.",
        "faq1_q": "Does Virginia recognize federal tax treaties?",
        "faq1_a": "Virginia partially recognizes some federal tax treaties. Check the Virginia Department of Taxation guidance for your specific treaty country and article.",
        "faq2_q": "What do UVA and Virginia Tech F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Virginia Form 763 (Nonresident Return) through the Virginia Tax website at tax.virginia.gov. File both by April 15.",
    },
    {
        "slug": "ohio-state-taxes-f1",
        "flag": "🌰", "state": "Ohio", "form": "OH IT-1040",
        "rate": "2.765-3.99% graduated", "no_tax": False,
        "treaty": "Ohio does not fully honor federal tax treaties",
        "universities": ["Ohio State", "Case Western Reserve", "University of Cincinnati", "Miami University", "Ohio University", "Kent State"],
        "extra_notes": "Ohio has graduated income tax rates. Columbus (home of Ohio State) has a 2.5% city income tax. Cleveland has a 2% city tax for Case Western students.",
        "faq1_q": "Does Ohio recognize the China or India treaty?",
        "faq1_a": "Ohio does not fully recognize federal tax treaties. Ohio-source income may be fully taxable at Ohio rates regardless of federal treaty exemptions.",
        "faq2_q": "Ohio State F-1 students — do they pay Columbus city tax?",
        "faq2_a": "Columbus has a 2.5% city income tax. Ohio State TAs and RAs working in Columbus are subject to this city tax on top of Ohio state and federal income tax. The city tax is in addition to your Ohio Form IT-1040.",
    },
    {
        "slug": "arizona-state-taxes-f1",
        "flag": "🌵", "state": "Arizona", "form": "AZ Form 140NR",
        "rate": "2.5% flat", "no_tax": False,
        "treaty": "Arizona does not recognize federal tax treaties",
        "universities": ["Arizona State", "University of Arizona", "Northern Arizona", "Grand Canyon University"],
        "extra_notes": "Arizona has one of the lowest state income tax rates in the US — a flat 2.5%. ASU is one of the largest universities in the US with a major international student population.",
        "faq1_q": "Does Arizona recognize the China or India treaty?",
        "faq1_a": "No — Arizona does not recognize federal tax treaties. All Arizona-source income is taxable at the 2.5% flat rate regardless of treaty status.",
        "faq2_q": "What do ASU and U of A F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Arizona Form 140NR (Nonresident Return) through the Arizona Department of Revenue at azdor.gov. File both by April 15.",
    },
    {
        "slug": "colorado-state-taxes-f1",
        "flag": "🏔️", "state": "Colorado", "form": "CO Form 104",
        "rate": "4.4% flat", "no_tax": False,
        "treaty": "Colorado does not recognize federal tax treaties",
        "universities": ["University of Colorado Boulder", "Colorado State", "DU", "Colorado School of Mines", "CU Denver", "UCCS"],
        "extra_notes": "Colorado has a flat 4.4% income tax rate. Denver also has an occupational privilege tax (OPT) of $5.75/month for workers earning over $500/month — separate from OPT work authorization.",
        "faq1_q": "Does Colorado recognize the China or India treaty?",
        "faq1_a": "No — Colorado does not recognize federal tax treaties. All Colorado-source income is taxable at the 4.4% flat rate.",
        "faq2_q": "CU Boulder F-1 students — what do they file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Colorado Form 104 as a nonresident through the Colorado Department of Revenue at colorado.gov/tax. File both by April 15.",
    },
    {
        "slug": "alaska-state-taxes-f1",
        "flag": "🏔️", "state": "Alaska", "form": "None",
        "rate": "No state income tax", "no_tax": True,
        "treaty": "No state tax — treaty benefits apply federally in full",
        "universities": ["University of Alaska Fairbanks", "UAA", "UAS"],
        "extra_notes": "Alaska has no state income tax — one of only 9 states. F-1 students at University of Alaska file only federal taxes.",
        "faq1_q": "Do F-1 students in Alaska file a state tax return?",
        "faq1_a": "No — Alaska has no individual state income tax. F-1 and J-1 students at University of Alaska only need to file their federal 1040-NR.",
        "faq2_q": "Does Alaska give residents a dividend?",
        "faq2_a": "Alaska has the Permanent Fund Dividend (PFD) for Alaska residents. F-1 students on nonimmigrant visas generally do not qualify as Alaska residents for PFD purposes.",
    },
    {
        "slug": "hawaii-state-taxes-f1",
        "flag": "🌺", "state": "Hawaii", "form": "HI Form N-15",
        "rate": "1.4-11% graduated", "no_tax": False,
        "treaty": "Hawaii does not fully recognize federal tax treaties",
        "universities": ["University of Hawaii Manoa", "Hawaii Pacific University", "Chaminade", "UH Hilo"],
        "extra_notes": "Hawaii has high living costs and graduated income tax rates up to 11%. F-1 students at UH Manoa with income file both federal 1040-NR and Hawaii Form N-15.",
        "faq1_q": "Does Hawaii recognize federal tax treaties?",
        "faq1_a": "Hawaii does not fully recognize federal tax treaties. Hawaii-source income is taxable at Hawaii state rates regardless of federal treaty exemptions.",
        "faq2_q": "What do UH Manoa F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Hawaii Form N-15 (Nonresident Return) through the Hawaii Department of Taxation. File both by April 15.",
    },
    {
        "slug": "nevada-state-taxes-f1",
        "flag": "🎲", "state": "Nevada", "form": "None",
        "rate": "No state income tax", "no_tax": True,
        "treaty": "No state tax — treaty benefits apply federally in full",
        "universities": ["UNLV", "University of Nevada Reno", "Nevada State University"],
        "extra_notes": "Nevada has no state income tax. UNLV and UNR F-1 students only file federal taxes. Las Vegas is growing as a tech and hospitality hub with OPT opportunities.",
        "faq1_q": "Do UNLV F-1 students file a Nevada state return?",
        "faq1_a": "No — Nevada has no state income tax. F-1 and J-1 students at UNLV and UNR only need to file their federal 1040-NR. No Nevada state return required.",
        "faq2_q": "Is Nevada a good state for OPT workers?",
        "faq2_a": "Nevada's lack of state income tax makes it financially attractive for OPT workers. Las Vegas and Reno have growing industries. No state income tax means your federal treaty benefits are your complete tax saving.",
    },
    {
        "slug": "oregon-state-taxes-f1",
        "flag": "🌲", "state": "Oregon", "form": "OR Form 40N",
        "rate": "4.75-9.9% graduated", "no_tax": False,
        "treaty": "Oregon does not fully recognize federal tax treaties",
        "universities": ["University of Oregon", "Oregon State", "Portland State", "Reed College", "Lewis & Clark"],
        "extra_notes": "Oregon has some of the highest state income tax rates in the US — up to 9.9%. F-1 students at UO and OSU with income file both federal 1040-NR and Oregon Form 40N.",
        "faq1_q": "Does Oregon recognize federal tax treaties?",
        "faq1_a": "Oregon does not fully recognize federal tax treaties. Oregon-source income is taxable at Oregon rates regardless of federal treaty exemptions. Budget for significant Oregon state tax.",
        "faq2_q": "What do UO and OSU F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Oregon Form 40N (Nonresident Return) through the Oregon Department of Revenue at oregon.gov/dor. File both by April 15.",
    },
    {
        "slug": "utah-state-taxes-f1",
        "flag": "⛷️", "state": "Utah", "form": "UT TC-40B",
        "rate": "4.65% flat", "no_tax": False,
        "treaty": "Utah does not fully recognize federal tax treaties",
        "universities": ["University of Utah", "BYU", "Utah State", "Westminster College", "SUU"],
        "extra_notes": "Utah has a flat 4.65% income tax rate. University of Utah and BYU have significant international student populations. BYU has a particularly large international community.",
        "faq1_q": "Does Utah recognize federal tax treaties?",
        "faq1_a": "Utah does not fully recognize federal tax treaties. Utah-source income is taxable at the 4.65% flat rate regardless of federal treaty exemptions.",
        "faq2_q": "What do University of Utah and BYU F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Utah Form TC-40B (Nonresident Schedule) through the Utah State Tax Commission at tap.utah.gov. File both by April 15.",
    },
    {
        "slug": "minnesota-state-taxes-f1",
        "flag": "🏒", "state": "Minnesota", "form": "MN Form M1NR",
        "rate": "5.35-9.85% graduated", "no_tax": False,
        "treaty": "Minnesota does not fully recognize federal tax treaties",
        "universities": ["University of Minnesota", "Carleton College", "Macalester", "St. Thomas", "Hamline"],
        "extra_notes": "Minnesota has among the highest state income tax rates in the US — up to 9.85%. University of Minnesota Twin Cities has a large international graduate student population.",
        "faq1_q": "Does Minnesota recognize federal tax treaties?",
        "faq1_a": "Minnesota does not fully recognize federal tax treaties. Minnesota-source income is taxable at Minnesota's graduated rates regardless of federal treaty exemptions.",
        "faq2_q": "What do UMN F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Minnesota Form M1NR (Nonresident) through the Minnesota Department of Revenue at revenue.state.mn.us. File both by April 15.",
    },
    {
        "slug": "missouri-state-taxes-f1",
        "flag": "🎵", "state": "Missouri", "form": "MO Form MO-1040",
        "rate": "2-4.95% graduated", "no_tax": False,
        "treaty": "Missouri does not fully recognize federal tax treaties",
        "universities": ["Washington University St. Louis", "University of Missouri", "St. Louis University", "Mizzou", "Missouri State"],
        "extra_notes": "Missouri has graduated income tax rates with a relatively low top rate of 4.95%. WashU St. Louis is a top research university with many international graduate students.",
        "faq1_q": "Does Missouri recognize federal tax treaties?",
        "faq1_a": "Missouri does not fully recognize federal tax treaties. Missouri-source income is taxable at Missouri graduated rates regardless of federal treaty exemptions.",
        "faq2_q": "What do WashU and Mizzou F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Missouri Form MO-1040 (Nonresident Schedule) through the Missouri Department of Revenue. File both by April 15.",
    },
    {
        "slug": "maryland-state-taxes-f1",
        "flag": "🦀", "state": "Maryland", "form": "MD Form 505",
        "rate": "2-5.75% graduated", "no_tax": False,
        "treaty": "Maryland partially recognizes some federal tax treaties",
        "universities": ["Johns Hopkins", "University of Maryland College Park", "Towson", "UMBC", "Morgan State", "UMCP"],
        "extra_notes": "Maryland has graduated income tax plus county income taxes. Many Maryland counties add 2.25-3.2% on top of state tax. JHU and UMD are major international student universities.",
        "faq1_q": "Does Maryland recognize federal tax treaties?",
        "faq1_a": "Maryland partially recognizes some federal tax treaties. Check the Maryland Comptroller guidance for your specific treaty country and article.",
        "faq2_q": "Do Maryland F-1 students pay county income tax?",
        "faq2_a": "Yes — Maryland residents (including F-1 students) pay both Maryland state income tax and county income tax. The county rate varies from 2.25-3.2% depending on which county you live in. Baltimore City has a separate city income tax.",
    },
    {
        "slug": "connecticut-state-taxes-f1",
        "flag": "🎓", "state": "Connecticut", "form": "CT Form CT-1040NR/PY",
        "rate": "2-6.99% graduated", "no_tax": False,
        "treaty": "Connecticut partially recognizes some federal tax treaties",
        "universities": ["Yale University", "UConn", "Trinity College", "Wesleyan University", "Fairfield"],
        "extra_notes": "Connecticut has graduated income tax rates. Yale University in New Haven is the most prominent university — many Yale F-1 students have fellowship and TA income subject to Connecticut tax.",
        "faq1_q": "Does Connecticut recognize federal tax treaties?",
        "faq1_a": "Connecticut partially recognizes some federal tax treaties. Check the Connecticut DRS guidance for your specific treaty country and article.",
        "faq2_q": "What do Yale and UConn F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Connecticut Form CT-1040NR/PY through the Connecticut Department of Revenue Services at portal.ct.gov/DRS. File both by April 15.",
    },
    {
        "slug": "new-jersey-state-taxes-f1",
        "flag": "🏙️", "state": "New Jersey", "form": "NJ Form NJ-1040NR",
        "rate": "1.4-10.75% graduated", "no_tax": False,
        "treaty": "New Jersey partially recognizes some federal tax treaties",
        "universities": ["Princeton University", "Rutgers University", "Stevens Institute", "Seton Hall", "Drew University", "Montclair State"],
        "extra_notes": "New Jersey has graduated income tax rates up to 10.75% — among the highest in the US. Princeton is in NJ; Rutgers is the state university. NJ also has a 0.4% payroll assessment.",
        "faq1_q": "Does New Jersey recognize federal tax treaties?",
        "faq1_a": "New Jersey partially recognizes some federal tax treaties. Check the NJ Division of Taxation guidance for your specific treaty country and article.",
        "faq2_q": "What do Princeton and Rutgers F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus New Jersey Form NJ-1040NR through the NJ Division of Taxation at nj.gov/treasury/taxation. File both by April 15.",
    },
    {
        "slug": "tennessee-state-taxes-f1",
        "flag": "🎸", "state": "Tennessee", "form": "None",
        "rate": "No income tax on wages", "no_tax": True,
        "treaty": "No income tax on wages — treaty benefits apply federally in full",
        "universities": ["Vanderbilt University", "University of Tennessee", "Tennessee State", "Belmont", "Sewanee", "Rhodes"],
        "extra_notes": "Tennessee has no income tax on wages or salaries. The Hall Income Tax on investments was fully repealed in 2021. F-1 students with wage income have no Tennessee tax obligation.",
        "faq1_q": "Do F-1 students at Vanderbilt or UT file a Tennessee state return?",
        "faq1_a": "No — Tennessee has no income tax on wages, salaries, stipends or fellowships. F-1 and J-1 students only need to file their federal 1040-NR. Tennessee has zero state income tax obligation for most students.",
        "faq2_q": "Does Tennessee tax investment income?",
        "faq2_a": "Tennessee's Hall Income Tax on investment income (interest and dividends) was fully repealed effective January 1, 2021. There is now effectively no income tax in Tennessee for individuals including F-1 students.",
    },
    {
        "slug": "indiana-state-taxes-f1",
        "flag": "🏎️", "state": "Indiana", "form": "IN Form IT-40PNR",
        "rate": "3.15% flat", "no_tax": False,
        "treaty": "Indiana does not recognize federal tax treaties",
        "universities": ["Purdue University", "Indiana University", "University of Notre Dame", "Butler", "Ball State", "IUPUI"],
        "extra_notes": "Indiana has a flat 3.15% state income tax. Additionally, most Indiana counties have local income taxes ranging from 0.5% to 2.9% on top of state tax. Purdue and IU are major international student universities.",
        "faq1_q": "Does Indiana recognize federal tax treaties?",
        "faq1_a": "Indiana does not recognize federal tax treaties. Indiana-source income is taxable at the 3.15% flat rate regardless of any federal treaty exemptions. Many Indiana counties also add local income taxes.",
        "faq2_q": "What do Purdue and IU F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Indiana Form IT-40PNR (Part-Year/Nonresident Return) through the Indiana Department of Revenue at intime.dor.in.gov. File both by April 15.",
    },
    {
        "slug": "wisconsin-state-taxes-f1",
        "flag": "🧀", "state": "Wisconsin", "form": "WI Form 1NPR",
        "rate": "3.54-7.65% graduated", "no_tax": False,
        "treaty": "Wisconsin partially recognizes some federal tax treaties",
        "universities": ["University of Wisconsin Madison", "Marquette University", "UW Milwaukee", "Lawrence University", "Beloit College"],
        "extra_notes": "Wisconsin has graduated income tax rates. UW Madison is a top research university with a large international graduate student community across engineering, sciences and business.",
        "faq1_q": "Does Wisconsin recognize federal tax treaties?",
        "faq1_a": "Wisconsin partially recognizes some federal tax treaties. Check the Wisconsin Department of Revenue guidance for your specific treaty country and article.",
        "faq2_q": "What do UW Madison F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Wisconsin Form 1NPR (Nonresident and Part-Year Resident Return) through the Wisconsin Department of Revenue at revenue.wi.gov. File both by April 15.",
    },
    {
        "slug": "washington-dc-taxes-f1",
        "flag": "🏛️", "state": "Washington DC", "form": "DC Form D-40B",
        "rate": "4-10.75% graduated", "no_tax": False,
        "treaty": "DC does not fully recognize federal tax treaties",
        "universities": ["Georgetown University", "George Washington University", "American University", "Howard University", "Catholic University", "UDC"],
        "extra_notes": "Washington DC has graduated income tax rates up to 10.75%. Georgetown, GWU and American University all have large international student populations. DC is also home to many international organizations employing visa holders.",
        "faq1_q": "Does DC recognize federal tax treaties?",
        "faq1_a": "DC does not fully recognize federal tax treaties. DC-source income is taxable at DC graduated rates regardless of federal treaty exemptions.",
        "faq2_q": "What do Georgetown and GWU F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus DC Form D-40B (Nonresident Request for Refund) through the DC Office of Tax and Revenue at mytax.dc.gov. File both by April 15.",
    },
    {
        "slug": "south-carolina-state-taxes-f1",
        "flag": "🌴", "state": "South Carolina", "form": "SC Form I-290",
        "rate": "0-7% graduated", "no_tax": False,
        "treaty": "South Carolina does not fully recognize federal tax treaties",
        "universities": ["Clemson University", "University of South Carolina", "Furman University", "College of Charleston", "Wofford"],
        "extra_notes": "South Carolina has graduated income tax rates up to 7%. Clemson and USC Columbia have growing international student populations in engineering and business.",
        "faq1_q": "Does South Carolina recognize federal tax treaties?",
        "faq1_a": "South Carolina does not fully recognize federal tax treaties. SC-source income is taxable at SC graduated rates regardless of federal treaty exemptions.",
        "faq2_q": "What do Clemson and USC F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus South Carolina Form I-290 (Nonresident Return) through the SC Department of Revenue at dor.sc.gov. File both by April 15.",
    },
    {
        "slug": "louisiana-state-taxes-f1",
        "flag": "🎺", "state": "Louisiana", "form": "LA Form IT-540B",
        "rate": "1.85-4.25% graduated", "no_tax": False,
        "treaty": "Louisiana does not fully recognize federal tax treaties",
        "universities": ["Tulane University", "LSU", "Loyola New Orleans", "Xavier University", "Southern University"],
        "extra_notes": "Louisiana has relatively low graduated income tax rates. Tulane University in New Orleans has a significant international student population. LSU is a major research university.",
        "faq1_q": "Does Louisiana recognize federal tax treaties?",
        "faq1_a": "Louisiana does not fully recognize federal tax treaties. Louisiana-source income is taxable at Louisiana graduated rates regardless of federal treaty exemptions.",
        "faq2_q": "What do Tulane and LSU F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Louisiana Form IT-540B (Nonresident Return) through the Louisiana Department of Revenue at revenue.louisiana.gov. File both by April 15.",
    },
    {
        "slug": "kentucky-state-taxes-f1",
        "flag": "🏇", "state": "Kentucky", "form": "KY Form 740-NP",
        "rate": "4.5% flat", "no_tax": False,
        "treaty": "Kentucky does not fully recognize federal tax treaties",
        "universities": ["University of Kentucky", "University of Louisville", "Bellarmine University", "Transylvania University", "EKU"],
        "extra_notes": "Kentucky has a flat 4.5% income tax rate. University of Kentucky in Lexington and University of Louisville both have international graduate student programs in engineering and business.",
        "faq1_q": "Does Kentucky recognize federal tax treaties?",
        "faq1_a": "Kentucky does not fully recognize federal tax treaties. Kentucky-source income is taxable at the 4.5% flat rate regardless of federal treaty exemptions.",
        "faq2_q": "What do UK and UofL F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Kentucky Form 740-NP (Nonresident Return) through the Kentucky Department of Revenue at revenue.ky.gov. File both by April 15.",
    },
    {
        "slug": "new-hampshire-state-taxes-f1",
        "flag": "🏔️", "state": "New Hampshire", "form": "None",
        "rate": "No income tax on wages", "no_tax": True,
        "treaty": "No income tax on wages — treaty benefits apply federally in full",
        "universities": ["Dartmouth College", "University of New Hampshire", "Southern New Hampshire University", "Plymouth State"],
        "extra_notes": "New Hampshire has no income tax on wages or salaries. The tax on interest and dividends was fully repealed as of 2025. Dartmouth F-1 students have no New Hampshire state income tax obligation.",
        "faq1_q": "Do Dartmouth F-1 students file a New Hampshire state return?",
        "faq1_a": "No — New Hampshire has no income tax on wages, salaries, stipends or most other income. F-1 and J-1 students at Dartmouth and UNH only need to file their federal 1040-NR.",
        "faq2_q": "Does New Hampshire have any taxes that affect F-1 students?",
        "faq2_a": "New Hampshire has no individual income tax on wages or most income types as of 2025. There is a meals and rooms tax (9%) and real estate transfer tax, but these do not directly affect F-1 student income tax obligations.",
    },
    {
        "slug": "vermont-state-taxes-f1",
        "flag": "🍁", "state": "Vermont", "form": "VT Form IN-111",
        "rate": "3.35-8.75% graduated", "no_tax": False,
        "treaty": "Vermont does not fully recognize federal tax treaties",
        "universities": ["University of Vermont", "Middlebury College", "Norwich University", "Champlain College"],
        "extra_notes": "Vermont has graduated income tax rates. UVM in Burlington has a smaller international student population but graduate programs in engineering and sciences attract F-1 students.",
        "faq1_q": "Does Vermont recognize federal tax treaties?",
        "faq1_a": "Vermont does not fully recognize federal tax treaties. Vermont-source income is taxable at Vermont graduated rates regardless of federal treaty exemptions.",
        "faq2_q": "What do UVM F-1 students file?",
        "faq2_a": "Federal Form 1040-NR with e-file.com, plus Vermont Form IN-111 (Nonresident Schedule) through the Vermont Department of Taxes at tax.vermont.gov. File both by April 15.",
    },
    {
        "slug": "wyoming-state-taxes-f1",
        "flag": "🤠", "state": "Wyoming", "form": "None",
        "rate": "No state income tax", "no_tax": True,
        "treaty": "No state tax — treaty benefits apply federally in full",
        "universities": ["University of Wyoming"],
        "extra_notes": "Wyoming has no state income tax. The University of Wyoming in Laramie is the state's only four-year university. F-1 students file only federal taxes.",
        "faq1_q": "Do University of Wyoming F-1 students file a state return?",
        "faq1_a": "No — Wyoming has no individual state income tax. University of Wyoming F-1 and J-1 students only need to file their federal 1040-NR and Form 8843.",
        "faq2_q": "Is Wyoming tax-friendly for international students?",
        "faq2_a": "Yes — Wyoming's lack of state income tax means federal treaty benefits are the only tax saving needed. No state return to file, no state tax to pay on wages or stipends.",
    },

    # ── ADD MORE STATES BELOW ─────────────────────────────────────────
    # {
    #     "slug": "statename-state-taxes-f1",
    #     "flag": "🏴", "state": "StateName", "form": "Form XXX",
    #     "rate": "X% flat", "no_tax": False,
    #     "treaty": "StateName does/does not recognize federal tax treaties",
    #     "universities": ["Uni 1", "Uni 2", "Uni 3"],
    #     "extra_notes": "Key facts about this state's tax situation.",
    #     "faq1_q": "FAQ question 1", "faq1_a": "FAQ answer 1",
    #     "faq2_q": "FAQ question 2", "faq2_a": "FAQ answer 2",
    # },
]

generated = []
for s in STATES:
    slug    = s["slug"]
    flag    = s["flag"]
    state   = s["state"]
    form    = s["form"]
    rate    = s["rate"]
    no_tax  = s["no_tax"]
    treaty  = s["treaty"]
    unis    = s["universities"]
    notes   = s["extra_notes"]

    state_note = f"No {state} state income tax — federal 1040-NR only" if no_tax else f"{state} {form} required — {rate} state income tax rate"
    uni_cards  = "".join(f'<div class="c go"><div class="ci">🎓</div><div class="ct">{u}</div><div class="cd">International students with {state}-source income must file {form} by April 15.</div></div>' for u in unis) if not no_tax else "".join(f'<div class="c gr"><div class="ci">✅</div><div class="ct">{u}</div><div class="cd">Federal 1040-NR only — no {state} state return required.</div></div>' for u in unis)

    body = f"""<div class="w"><h4>{flag} {state} — Key Tax Facts for F-1 Students</h4><p>{notes} {treaty}.</p></div>
<div class="ey">Filing Requirements</div><h2>Who Must File a {state} Return?</h2>
{cards(
('gr','✅',f'No {state} State Tax!',f'Zero {state} income tax. Federal 1040-NR is your only return. Treaty benefits are fully effective.') if no_tax else ('re','⚠️',f'{state}-Source Income Required',f'Wages, stipends or fellowship income from a {state} employer or university — file {form}.'),
('gr','✅','Treaty Benefits Fully Effective',f'No state tax means your federal treaty exemptions (China, India, Korea etc.) are your complete tax saving.') if no_tax else ('go','⚠️',f'{state} Tax Rate: {rate}',f'Applies to all {state}-source income for nonresident filers.'),
('go','⚠️','Federal 1040-NR Still Required','F-1 and J-1 students with US income still file federal Form 1040-NR and Form 8843. e-file.com handles both.'),
('gr','✅','FICA Exempt','F-1 and J-1 nonresident students are exempt from Social Security and Medicare taxes regardless of state.'),
)}
<div class="ey">Top {state} Universities</div><h2>Filing at These Schools</h2>
<div class="g">{uni_cards}</div>
{cta(state, form)}
<div class="ey">FAQ</div><h2 style="margin-bottom:20px;">{state} F-1 Tax FAQ</h2>
<div class="fqs">
{faq(s["faq1_q"], s["faq1_a"])}
{faq(s["faq2_q"], s["faq2_a"])}
{faq(f"When is the {state} tax filing deadline?",f"April 15, 2026 — same as the federal deadline." + (f" Check the {state} Department of Revenue website for extension rules and any tax owed must be paid by April 15." if not no_tax else f" Since there is no {state} state income tax, you only need to worry about your federal filing deadline."))}
</div>"""

    fname = build(f"{slug}.html",
        f"{state} State Taxes for F-1 Students 2026 — Complete Filing Guide",
        f"F-1 and J-1 students in {state} with income must {state_note}. Complete guide for {', '.join(unis[:3])} and all {state} universities. File federal 1040-NR with e-file.com.",
        f"{flag} {state} F-1 Tax Guide 2026",
        f"{state} State Taxes for <em>F-1 Students</em> 2026",
        f"F-1 and J-1 students in {state} — {state_note}. Complete guide covering {', '.join(unis[:2])} and all {state} universities.",
        body)
    generated.append(fname)
    print(f"✅ {fname}")

print(f"\n✅ Done — {len(generated)} state pages in ./{OUT}/")

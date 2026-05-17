#!/usr/bin/env python3
"""
USATaxRefund — University Page Generator
Add any university to UNIVERSITIES list and run to generate pages.
Usage: python3 generate_universities.py
Output: ./generated/universities/
"""
import os, datetime

ALINK = "https://www.linkconnector.com/ta.php?lc=007949061588005142&atid=UsaTaxRefunds"
BASE  = "https://brightlane.github.io/UsaTaxRefund"
DATE  = datetime.date.today().isoformat()
OUT   = "generated/universities"
os.makedirs(OUT, exist_ok=True)

CSS = """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>:root{--blue:#003087;--blue2:#0050c8;--red:#cc0000;--gold:#f5a623;--dark:#0a0d14;--card:#111520;--border:#1e2540;--text:#eef0f8;--muted:#7a8aa8;--green:#00c853;}*{box-sizing:border-box;margin:0;padding:0;}body{font-family:Inter,sans-serif;background:var(--dark);color:var(--text);line-height:1.6;}nav{position:sticky;top:0;z-index:100;background:rgba(10,13,20,.96);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 28px;height:60px;}.logo{font-size:20px;font-weight:900;color:var(--text);text-decoration:none;}.logo span{color:var(--gold);}.nc{background:var(--red);color:#fff;padding:9px 20px;border-radius:8px;font-weight:700;font-size:13px;text-decoration:none;}.tk{background:var(--blue);overflow:hidden;white-space:nowrap;padding:8px 0;}.ti{display:inline-block;animation:tk 30s linear infinite;}.ti span{margin:0 36px;font-size:12px;font-weight:700;color:#fff;}@keyframes tk{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}.hero{background:linear-gradient(180deg,#00082a 0%,var(--dark) 100%);padding:64px 24px 44px;text-align:center;border-bottom:1px solid var(--border);}.badge{display:inline-flex;align-items:center;gap:8px;background:rgba(0,80,200,.15);border:1px solid rgba(0,80,200,.4);color:#7ab0ff;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:6px 16px;border-radius:20px;margin-bottom:20px;}h1{font-size:clamp(26px,5vw,54px);font-weight:900;line-height:1.05;letter-spacing:-2px;margin-bottom:16px;}h1 em{color:var(--gold);font-style:normal;}.hs{color:var(--muted);font-size:16px;max-width:560px;margin:0 auto 28px;line-height:1.6;}.btn{background:var(--red);color:#fff;font-weight:800;padding:16px 36px;border-radius:10px;text-decoration:none;font-size:15px;display:inline-flex;align-items:center;gap:8px;}.s{padding:56px 24px;max-width:940px;margin:0 auto;}.ey{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:10px;}h2{font-size:clamp(20px,3vw,32px);font-weight:800;letter-spacing:-1px;margin-bottom:12px;}.sub{color:var(--muted);font-size:14px;margin-bottom:28px;}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;margin-bottom:24px;}.c{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;}.c.gr{border-color:rgba(0,200,83,.3);background:#050f05;}.c.go{border-color:rgba(245,166,35,.3);background:#0f0a00;}.c.re{border-color:rgba(204,0,0,.3);background:#150505;}.ci{font-size:24px;margin-bottom:8px;}.ct{font-weight:700;font-size:13px;margin-bottom:5px;}.c.gr .ct{color:var(--green);}.c.go .ct{color:var(--gold);}.c.re .ct{color:#ff8888;}.cd{color:var(--muted);font-size:12px;line-height:1.5;}.w{background:#1a0800;border:1px solid rgba(245,166,35,.4);border-radius:12px;padding:20px;margin:16px 0;}.w h4{color:var(--gold);font-size:14px;font-weight:700;margin-bottom:6px;}.w p{color:#c0b080;font-size:13px;line-height:1.6;margin:0;}.cb{background:linear-gradient(135deg,#001a6e,#003087);border:1px solid rgba(0,80,200,.4);border-radius:14px;padding:40px 32px;text-align:center;margin:36px 0;}.cb h2{margin-bottom:10px;}.cb p{color:#a0b8e8;font-size:14px;margin-bottom:20px;}.fqs{display:flex;flex-direction:column;gap:10px;}.fq{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;}.fqq{font-weight:700;font-size:14px;margin-bottom:6px;}.fqa{color:var(--muted);font-size:13px;line-height:1.6;}footer{background:var(--card);border-top:1px solid var(--border);padding:20px 24px;text-align:center;font-size:12px;color:var(--muted);line-height:2;}@media(max-width:600px){.hero,.s{padding:40px 16px;}}</style>"""

def cta(h="File with e-file.com", p="IRS authorized · A+ BBB · 1040-NR supported · Refund in 10-21 days"):
    return f'<div class="cb"><h2>{h}</h2><p>{p}</p><a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored" style="font-size:16px;padding:17px 40px;display:inline-flex;">🚀 Start Filing Free</a><p style="color:#7ab0ff;font-size:12px;margin-top:12px;">IRS Authorized · A+ BBB · 10-21 Day Refund</p></div>'

def faq(q, a):
    return f'<div class="fq"><div class="fqq">{q}</div><div class="fqa">{a}</div></div>'

def cards(*items):
    o = '<div class="g">'
    for cls, icon, title, desc in items:
        o += f'<div class="c {cls}"><div class="ci">{icon}</div><div class="ct">{title}</div><div class="cd">{desc}</div></div>'
    return o + '</div>'

def build(fname, title, desc, badge, h1, hs, tick, body):
    canonical = f"{BASE}/{fname}"
    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{CSS}</head><body>
<nav><a class="logo" href="/UsaTaxRefund/"><span>🇺🇸</span> USATaxRefund</a><a class="nc" href="{ALINK}" target="_blank" rel="noopener sponsored">File Free →</a></nav>
<div class="tk"><div class="ti"><span>{tick}</span><span>🏛️ IRS AUTHORIZED</span><span>✅ FREE FEDERAL FILING</span><span>⚡ REFUND 10-21 DAYS</span><span>📋 1040-NR SUPPORTED</span><span>{tick}</span></div></div>
<div class="hero"><div class="badge">{badge}</div><h1>{h1}</h1><p class="hs">{hs}</p>
<a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored">🚀 File with e-file.com</a></div>
<div class="s">{body}
<p style="text-align:center;margin-top:28px;"><a href="/UsaTaxRefund/" style="color:var(--muted);font-size:13px;">← USATaxRefund Home</a></p></div>
<footer><p>USATaxRefund is an independent affiliate site earning commissions from e-file.com links.</p>
<p>Not tax or legal advice. e-file.com is IRS-authorized, A+ BBB rated since 2014.</p>
<p>© 2026 USATaxRefund · <a href="{ALINK}" style="color:var(--gold)">File Free →</a></p></footer>
</body></html>"""
    path = os.path.join(OUT, fname)
    with open(path, "w") as f:
        f.write(html)
    return fname

# ════════════════════════════════════════════════════════════════════
# ADD UNIVERSITIES HERE
# Format: (slug, emoji, name, city, state, state_form, state_rate, treaty_note, specific_detail)
# slug       = filename without .html  e.g. "nyu-international-student-taxes"
# emoji      = single emoji for the university
# name       = full university name
# city       = city name
# state      = state name
# state_form = state tax form name  e.g. "IT-203" or "None"
# state_rate = tax rate string      e.g. "4.95% flat" or "No state tax"
# treaty_note= how that state treats treaties
# specific   = one sentence about the university's specific tax situation
# ════════════════════════════════════════════════════════════════════
UNIVERSITIES = [
    ("nyu-international-student-taxes",        "🗽", "NYU",                     "New York City",    "New York",       "IT-203",      "up to 10.9%",   "New York partially honors treaties",          "NYU Tandon, Stern, Tisch — Manhattan location means NYC income tax on top of NY State"),
    ("johns-hopkins-international-taxes",      "🔬", "Johns Hopkins",           "Baltimore",        "Maryland",       "MD Form 505", "2-5.75%",       "Maryland partially honors treaties",          "JHU Homewood, SAIS, Bloomberg School — Maryland graduated income tax"),
    ("carnegie-mellon-international-taxes",    "🤖", "Carnegie Mellon",         "Pittsburgh",       "Pennsylvania",   "PA-40",       "3.07% flat",    "Pennsylvania does not recognize treaties",    "CMU School of CS, Tepper, CIT — Pennsylvania flat income tax 3.07%"),
    ("georgia-tech-international-taxes",       "🐝", "Georgia Tech",            "Atlanta",          "Georgia",        "GA Form 500", "1-5.75%",       "Georgia does not fully honor treaties",       "GT College of Computing, Engineering — Georgia graduated income tax"),
    ("purdue-international-student-taxes",     "🚂", "Purdue University",       "West Lafayette",   "Indiana",        "IN IT-40PNR", "3.15% flat",    "Indiana does not recognize treaties",         "Purdue Engineering, Krannert — Indiana flat income tax 3.15%"),
    ("uiuc-international-student-taxes",       "🌽", "UIUC",                    "Champaign",        "Illinois",       "IL-1040",     "4.95% flat",    "Illinois does not recognize treaties",        "U of I Engineering, Gies, Grainger — Illinois flat income tax 4.95%"),
    ("caltech-international-student-taxes",    "🔭", "Caltech",                 "Pasadena",         "California",     "CA 540NR",    "up to 13.3%",   "California does NOT honor treaties",          "Caltech Pasadena — California highest state tax, no treaty recognition"),
    ("ucsd-international-student-taxes",       "🌊", "UC San Diego",            "La Jolla",         "California",     "CA 540NR",    "up to 13.3%",   "California does NOT honor treaties",          "UCSD Jacobs Engineering, Rady — California 540NR, no treaty benefit"),
    ("ucla-international-student-taxes",       "🐻", "UCLA",                    "Los Angeles",      "California",     "CA 540NR",    "up to 13.3%",   "California does NOT honor treaties",          "UCLA Anderson, Engineering, Arts — California 540NR required, no treaty"),
    ("boston-university-international-taxes",  "🦁", "Boston University",       "Boston",           "Massachusetts",  "MA 1-NR/PY",  "5% flat",       "Massachusetts partially honors treaties",     "BU COM, Engineering, Questrom — Massachusetts 5% flat income tax"),
    ("northeastern-international-taxes",       "🐾", "Northeastern University", "Boston",           "Massachusetts",  "MA 1-NR/PY",  "5% flat",       "Massachusetts partially honors treaties",     "Northeastern co-op programs — Massachusetts 5% flat income tax"),
    ("university-of-washington-intl-taxes",   "🐺", "University of Washington","Seattle",          "Washington",     "None",        "No state tax",  "Washington has NO state income tax",          "UW Paul Allen, Foster — no Washington state income tax, federal only"),
    ("unc-international-student-taxes",        "🐏", "UNC Chapel Hill",         "Chapel Hill",      "North Carolina", "NC D-400",    "4.5% flat",     "NC does not fully honor treaties",            "UNC Kenan-Flagler, Gillings — North Carolina 4.5% flat income tax"),
    ("duke-international-student-taxes",       "😈", "Duke University",         "Durham",           "North Carolina", "NC D-400",    "4.5% flat",     "NC does not fully honor treaties",            "Duke Fuqua, Pratt Engineering — North Carolina 4.5% flat income tax"),
    ("rice-international-student-taxes",       "🦉", "Rice University",         "Houston",          "Texas",          "None",        "No state tax",  "Texas has NO state income tax",               "Rice Jones, Engineering — no Texas state income tax, federal only"),
    ("vanderbilt-international-taxes",         "⭐", "Vanderbilt University",   "Nashville",        "Tennessee",      "TN Form INC", "No wage tax",   "Tennessee has no income tax on wages",        "Vanderbilt Owen, Engineering — Tennessee no wage income tax"),
    ("brown-international-student-taxes",      "🐻", "Brown University",        "Providence",       "Rhode Island",   "RI-1040NR",   "3.75-5.99%",   "Rhode Island does not fully honor treaties",  "Brown RISD, Engineering — Rhode Island graduated income tax"),
    ("dartmouth-international-taxes",          "🟢", "Dartmouth College",       "Hanover",          "New Hampshire",  "NH DP-10",    "No wage tax",   "New Hampshire has no income tax on wages",    "Dartmouth Tuck, Thayer — New Hampshire no wage income tax"),
    ("cornell-international-student-taxes",    "🐻", "Cornell University",      "Ithaca",           "New York",       "IT-203",      "up to 10.9%",   "New York partially honors treaties",          "Cornell Engineering, Dyson, ILR — Ithaca not NYC so no NYC city tax"),
    ("university-of-texas-international",      "🤘", "UT Austin",               "Austin",           "Texas",          "None",        "No state tax",  "Texas has NO state income tax",               "UT McCombs, Cockrell Engineering — no Texas state income tax, federal only"),
    # ── ADD MORE UNIVERSITIES BELOW ─────────────────────────────────
    # ("slug", "emoji", "University Name", "City", "State", "Form", "Rate", "Treaty note", "Specific detail"),
]

generated = []
for slug, emoji, uni, city, state, form, rate, treaty_note, specific in UNIVERSITIES:
    no_state = "No state" in rate or "No wage" in rate
    state_note = f"No {state} state income tax — federal 1040-NR only" if no_state else f"{state} {form} required — {rate} state income tax rate"

    body = f"""<div class="w"><h4>{emoji} {uni} — Key Tax Facts</h4><p>{specific}. {treaty_note}.</p></div>
<div class="ey">What to File</div><h2>{uni} International Students — Filing Requirements</h2>
{cards(
('re','📋','Federal: Form 1040-NR',f'File with e-file.com by April 15. Claim treaty benefits on Schedule OI. Report W-2 and 1042-S income.'),
('gr' if no_state else 're','✅' if no_state else '📋',f'State: No {state} Tax!' if no_state else f'State: {form}',state_note),
('go','⚠️','File Federal First',f'Complete your federal 1040-NR first. Your {state} return uses your federal income as the starting point.') if not no_state else ('gr','✅','Treaty Benefits Fully Effective',f'No {state} state tax means your federal treaty exemptions are your total and only tax saving.'),
('gr','✅','FICA Exempt','As an F-1 nonresident student you are exempt from Social Security and Medicare taxes. If withheld, file IRS Form 843 to recover it.'),
)}
{cta(f"File Your {uni} 1040-NR with e-file.com","IRS authorized · Treaty benefits applied · W-2 and 1042-S handled · A+ BBB · Refund in 10-21 days")}
<div class="ey">FAQ</div><h2 style="margin-bottom:20px;">{uni} International Student Tax FAQ</h2>
<div class="fqs">
{faq(f"Does {uni} file taxes for me?",f"No — {uni}'s International Students Office provides guidance but filing is your responsibility. {uni} issues your W-2 and 1042-S by January 31. Use those to file your 1040-NR with e-file.com.")}
{faq(f"Can I claim my home country tax treaty at {uni}?",f"Yes — claim applicable treaty benefits (China Article 20, India Article 21, Korea Article 21, Germany, UK etc.) on Schedule OI of your federal 1040-NR. {'However, '+state+' does not fully recognize treaty benefits for state tax purposes.' if not no_state else state+' has no income tax so your federal treaty savings are your complete savings.'}")}
{faq("I received a 1042-S from the university — what do I do?","Form 1042-S reports fellowship income, scholarship stipends, and treaty-exempt wages. Use it along with your W-2 to complete Form 1040-NR. e-file.com handles both W-2 and 1042-S reporting correctly on the same return.")}
</div>"""

    fname = build(f"{slug}.html",
        f"{uni} International Student Taxes 2026 — 1040-NR Filing Guide",
        f"{uni} F-1 and J-1 students with fellowship, RA or TA income must file 1040-NR. {state_note}. Complete guide. File with e-file.com — IRS authorized, A+ BBB.",
        f"{emoji} {uni} Tax Guide 2026",
        f"{uni} International Student <em>Tax Guide 2026</em>",
        f"{uni} F-1 and J-1 students in {city}, {state} with income must file federal Form 1040-NR. {state_note}.",
        f"{emoji} {uni.upper()} INTERNATIONAL STUDENT TAX FILING GUIDE 2026",
        body)
    generated.append(fname)
    print(f"✅ {fname}")

print(f"\n✅ Done — {len(generated)} university pages in ./{OUT}/")

#!/usr/bin/env python3
"""
USATaxRefund — Master Page Generator
Run once to generate thousands of targeted tax pages.
Usage: python3 generate_all_pages.py
All pages output to ./generated/ folder, ready to upload to GitHub.
"""

import os, json, datetime

ALINK = "https://www.linkconnector.com/ta.php?lc=007949061588005142&atid=UsaTaxRefunds"
BASE  = "https://brightlane.github.io/UsaTaxRefund"
DATE  = datetime.date.today().isoformat()
OUT   = "generated"
os.makedirs(OUT, exist_ok=True)

# ── SHARED CSS ───────────────────────────────────────────────────────
CSS = """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root{--blue:#003087;--blue2:#0050c8;--red:#cc0000;--gold:#f5a623;--dark:#0a0d14;--card:#111520;--border:#1e2540;--text:#eef0f8;--muted:#7a8aa8;--green:#00c853;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:Inter,sans-serif;background:var(--dark);color:var(--text);line-height:1.6;}
nav{position:sticky;top:0;z-index:100;background:rgba(10,13,20,.96);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 28px;height:60px;}
.logo{font-size:20px;font-weight:900;color:var(--text);text-decoration:none;}.logo span{color:var(--gold);}
.nc{background:var(--red);color:#fff;padding:9px 20px;border-radius:8px;font-weight:700;font-size:13px;text-decoration:none;}
.tk{background:var(--blue);overflow:hidden;white-space:nowrap;padding:8px 0;}
.ti{display:inline-block;animation:tk 30s linear infinite;}
.ti span{margin:0 36px;font-size:12px;font-weight:700;color:#fff;}
@keyframes tk{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}
.hero{background:linear-gradient(180deg,#00082a 0%,var(--dark) 100%);padding:64px 24px 44px;text-align:center;border-bottom:1px solid var(--border);}
.badge{display:inline-flex;align-items:center;gap:8px;background:rgba(0,80,200,.15);border:1px solid rgba(0,80,200,.4);color:#7ab0ff;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:6px 16px;border-radius:20px;margin-bottom:20px;}
h1{font-size:clamp(26px,5vw,54px);font-weight:900;line-height:1.05;letter-spacing:-2px;margin-bottom:16px;}
h1 em{color:var(--gold);font-style:normal;}
.hs{color:var(--muted);font-size:16px;max-width:560px;margin:0 auto 28px;line-height:1.6;}
.btn{background:var(--red);color:#fff;font-weight:800;padding:16px 36px;border-radius:10px;text-decoration:none;font-size:15px;display:inline-flex;align-items:center;gap:8px;}
.s{padding:56px 24px;max-width:940px;margin:0 auto;}
.ey{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:10px;}
h2{font-size:clamp(20px,3vw,32px);font-weight:800;letter-spacing:-1px;margin-bottom:12px;}
.sub{color:var(--muted);font-size:14px;margin-bottom:28px;}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;margin-bottom:24px;}
.c{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;}
.c.gr{border-color:rgba(0,200,83,.3);background:#050f05;}
.c.go{border-color:rgba(245,166,35,.3);background:#0f0a00;}
.c.re{border-color:rgba(204,0,0,.3);background:#150505;}
.ci{font-size:24px;margin-bottom:8px;}
.ct{font-weight:700;font-size:13px;margin-bottom:5px;}
.c.gr .ct{color:var(--green);}.c.go .ct{color:var(--gold);}.c.re .ct{color:#ff8888;}
.cd{color:var(--muted);font-size:12px;line-height:1.5;}
.w{background:#1a0800;border:1px solid rgba(245,166,35,.4);border-radius:12px;padding:20px;margin:16px 0;}
.w h4{color:var(--gold);font-size:14px;font-weight:700;margin-bottom:6px;}
.w p{color:#c0b080;font-size:13px;line-height:1.6;margin:0;}
.cb{background:linear-gradient(135deg,#001a6e,#003087);border:1px solid rgba(0,80,200,.4);border-radius:14px;padding:40px 32px;text-align:center;margin:36px 0;}
.cb h2{margin-bottom:10px;}.cb p{color:#a0b8e8;font-size:14px;margin-bottom:20px;}
.fqs{display:flex;flex-direction:column;gap:10px;}
.fq{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;}
.fqq{font-weight:700;font-size:14px;margin-bottom:6px;}
.fqa{color:var(--muted);font-size:13px;line-height:1.6;}
footer{background:var(--card);border-top:1px solid var(--border);padding:20px 24px;text-align:center;font-size:12px;color:var(--muted);line-height:2;}
@media(max-width:600px){.hero,.s{padding:40px 16px;}}
</style>"""

# ── HELPERS ──────────────────────────────────────────────────────────
def cta(h="File with e-file.com", p="IRS authorized · A+ BBB · 1040-NR supported · Refund in 10-21 days"):
    return f'<div class="cb"><h2>{h}</h2><p>{p}</p><a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored" style="font-size:16px;padding:17px 40px;display:inline-flex;">🚀 Start Filing Free</a><p style="color:#7ab0ff;font-size:12px;margin-top:12px;">IRS Authorized · A+ BBB · 10-21 Day Refund · Free Federal</p></div>'

def faq(q, a):
    return f'<div class="fq"><div class="fqq">{q}</div><div class="fqa">{a}</div></div>'

def cards(*items):
    o = '<div class="g">'
    for cls, icon, title, desc in items:
        o += f'<div class="c {cls}"><div class="ci">{icon}</div><div class="ct">{title}</div><div class="cd">{desc}</div></div>'
    return o + '</div>'

def build(fname, title, desc, badge, h1, hs, tick, body, subdir=""):
    folder = os.path.join(OUT, subdir) if subdir else OUT
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, fname)
    canonical = f"{BASE}/{subdir}/{fname}" if subdir else f"{BASE}/{fname}"
    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ">
<title>{title}</title>
<meta name="description" content="{desc}">
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
<p>© 2026 USATaxRefund · <a href="{ALINK}" style="color:var(--gold)">File Free with e-file.com →</a></p></footer>
</body></html>"""
    with open(path, "w") as f:
        f.write(html)
    return path

generated = []

# ════════════════════════════════════════════════════════════════════
# 1. UNIVERSITY PAGES — auto-generate for any university
# ════════════════════════════════════════════════════════════════════
UNIVERSITIES = [
    # (slug, emoji, name, city, state, state_form, state_rate, treaty_note, specifics)
    ("nyu-international-student-taxes",        "🗽", "NYU",                    "New York City",    "New York",      "IT-203",       "up to 10.9%",  "NYC income tax applies on top of NY State", "NYU Tandon, Stern, Tisch and all schools — Manhattan location means NYC income tax"),
    ("johns-hopkins-international-taxes",      "🔬", "Johns Hopkins",          "Baltimore",        "Maryland",      "MD Form 505",  "2-5.75%",      "Maryland partially honors treaties",         "JHU Homewood, SAIS, Bloomberg School — Maryland graduated income tax"),
    ("carnegie-mellon-international-taxes",    "🤖", "Carnegie Mellon",        "Pittsburgh",       "Pennsylvania",  "PA-40",        "3.07% flat",   "Pennsylvania does not recognize treaties",   "CMU School of CS, Tepper, CIT — Pennsylvania flat income tax 3.07%"),
    ("georgia-tech-international-taxes",       "🐝", "Georgia Tech",           "Atlanta",          "Georgia",       "GA Form 500",  "1-5.75%",      "Georgia does not fully honor treaties",      "GT College of Computing, Engineering — Georgia graduated income tax"),
    ("purdue-international-student-taxes",     "🚂", "Purdue University",      "West Lafayette",   "Indiana",       "IN IT-40PNR",  "3.15% flat",   "Indiana does not recognize treaties",        "Purdue Engineering, Krannert — Indiana flat income tax 3.15%"),
    ("uiuc-international-student-taxes",       "🌽", "UIUC",                   "Champaign",        "Illinois",      "IL-1040",      "4.95% flat",   "Illinois does not recognize treaties",       "U of I Engineering, Gies, Grainger — Illinois flat income tax 4.95%"),
    ("caltech-international-student-taxes",    "🔭", "Caltech",                "Pasadena",         "California",    "CA 540NR",     "up to 13.3%",  "California does NOT honor treaties",         "Caltech Pasadena — California highest state tax, no treaty recognition"),
    ("ucsd-international-student-taxes",       "🌊", "UC San Diego",           "La Jolla",         "California",    "CA 540NR",     "up to 13.3%",  "California does NOT honor treaties",         "UCSD Jacobs Engineering, Rady — California 540NR, no treaty benefit"),
    ("ucla-international-student-taxes",       "🐻", "UCLA",                   "Los Angeles",      "California",    "CA 540NR",     "up to 13.3%",  "California does NOT honor treaties",         "UCLA Anderson, Engineering, Arts — California 540NR required, no treaty"),
    ("boston-university-international-taxes",  "🦁", "Boston University",      "Boston",           "Massachusetts", "MA 1-NR/PY",   "5% flat",      "Massachusetts partially honors treaties",    "BU COM, Engineering, Questrom — Massachusetts 5% flat income tax"),
    ("northeastern-international-taxes",       "🐾", "Northeastern University","Boston",           "Massachusetts", "MA 1-NR/PY",   "5% flat",      "Massachusetts partially honors treaties",    "Northeastern co-op programs — Massachusetts 5% flat income tax"),
    ("university-of-washington-intl-taxes",   "🐺", "University of Washington","Seattle",         "Washington",    "None",         "No state tax", "Washington has NO state income tax",         "UW Paul Allen, Foster — no Washington state income tax, federal only"),
    ("unc-international-student-taxes",        "🐏", "UNC Chapel Hill",        "Chapel Hill",      "North Carolina","NC D-400",     "4.5% flat",    "NC does not fully honor treaties",           "UNC Kenan-Flagler, Gillings — North Carolina 4.5% flat income tax"),
    ("duke-international-student-taxes",       "😈", "Duke University",        "Durham",           "North Carolina","NC D-400",     "4.5% flat",    "NC does not fully honor treaties",           "Duke Fuqua, Pratt Engineering — North Carolina 4.5% flat income tax"),
    ("rice-international-student-taxes",       "🦉", "Rice University",        "Houston",          "Texas",         "None",         "No state tax", "Texas has NO state income tax",              "Rice Jones, Engineering — no Texas state income tax, federal only"),
    ("vanderbilt-international-taxes",         "⭐", "Vanderbilt University",  "Nashville",        "Tennessee",     "TN Form INC",  "No income tax","Tennessee has no income tax on wages",       "Vanderbilt Owen, Engineering — Tennessee no wage income tax"),
    ("brown-international-student-taxes",      "🐻", "Brown University",       "Providence",       "Rhode Island",  "RI-1040NR",    "3.75-5.99%",   "Rhode Island does not fully honor treaties", "Brown RISD, Engineering — Rhode Island graduated income tax"),
    ("dartmouth-international-taxes",          "🟢", "Dartmouth College",      "Hanover",          "New Hampshire", "NH DP-10",     "No income tax","New Hampshire has no income tax on wages",   "Dartmouth Tuck, Thayer — New Hampshire no wage income tax"),
    ("cornell-international-student-taxes",    "🐻", "Cornell University",     "Ithaca",           "New York",      "IT-203",       "up to 10.9%",  "New York partially honors treaties",         "Cornell Engineering, Dyson, ILR — Ithaca not NYC, no city tax"),
    ("university-of-texas-international",      "🤘", "UT Austin",              "Austin",           "Texas",         "None",         "No state tax", "Texas has NO state income tax",              "UT McCombs, Cockrell Engineering — no Texas state income tax, federal only"),
]

for slug, emoji, uni, city, state, form, rate, treaty, specific in UNIVERSITIES:
    no_state = "No state tax" in rate or "No income" in rate
    state_note = f"No {state} state income tax — federal 1040-NR only" if no_state else f"{state} {form} required — {rate} state income tax rate"
    body = f"""<div class="w"><h4>{emoji} {uni} — Key Tax Facts</h4><p>{specific}. {treaty}.</p></div>
<div class="ey">What to File</div><h2>{uni} International Students — Filing Requirements</h2>
{cards(
('re','📋','Federal: Form 1040-NR','File with e-file.com by April 15. Claim treaty benefits on Schedule OI. Report W-2 and 1042-S income correctly.'),
('re' if not no_state else 'gr', '📋' if not no_state else '✅', f'State: {form}' if not no_state else f'{state}: No State Tax!', state_note),
('go','⚠️','File Federal First','Complete your federal 1040-NR first — your state return uses your federal income figures as the starting point.') if not no_state else ('gr','✅','Treaty Benefits Fully Effective','No state tax means your federal treaty exemptions (China, India, Korea, Germany, UK etc.) are your total and only tax saving.'),
('gr','✅','FICA Exempt','As an F-1 nonresident student, you are exempt from Social Security and Medicare taxes. If withheld, claim a refund via Form 843 or your employer.'),
)}
{cta(f"File Your {uni} 1040-NR with e-file.com","IRS authorized, treaty benefits applied, W-2 and 1042-S handled. A+ BBB rated. Refund in 10-21 days.")}
<div class="ey">FAQ</div><h2 style="margin-bottom:20px;">{uni} International Student Tax FAQ</h2>
<div class="fqs">
{faq(f"Does {uni} file taxes for me?",f"No — {uni}'s International Students Office provides resources and guidance but tax filing is your personal responsibility. {uni} issues your W-2 and 1042-S forms by January 31. File your 1040-NR with e-file.com using those documents.")}
{faq(f"Can I claim my home country tax treaty at {uni}?",f"Yes — if your home country has a US tax treaty (China Article 20, India Article 21, Korea Article 21, Germany, UK, France, Japan etc.), claim it on Schedule OI of your federal Form 1040-NR. {'However, ' + state + ' does not fully recognize this treaty benefit for state tax purposes.' if not no_state else state + ' has no state income tax so your federal treaty savings are your full savings.'}")}
{faq("I received a 1042-S from the university — what do I do with it?","Form 1042-S reports fellowship income, scholarship stipends, and treaty-exempt wages paid to nonresident aliens. Use it to complete your Form 1040-NR. e-file.com handles 1042-S reporting correctly. Report both your W-2 (for TA/RA wages) and 1042-S (for fellowship income) on the same 1040-NR return.")}
</div>"""
    p = build(f"{slug}.html",
        f"{uni} International Student Taxes 2026 — 1040-NR Filing Guide",
        f"{uni} F-1 and J-1 students with fellowship, RA or TA income must file 1040-NR. {state_note}. Complete guide. File with e-file.com.",
        f"{emoji} {uni} Tax Guide 2026",
        f"{uni} International Student <em>Tax Guide 2026</em>",
        f"{uni} F-1 and J-1 students in {city}, {state} with income must file federal Form 1040-NR. {state_note}.",
        f"{emoji} {uni.upper()} INTERNATIONAL STUDENT TAX FILING GUIDE 2026",
        body)
    generated.append(p)
    print(f"✅ {slug}.html")

# ════════════════════════════════════════════════════════════════════
# 2. TREATY COUNTRY PAGES — auto-generate for any country
# ════════════════════════════════════════════════════════════════════
TREATIES = [
    # (slug, flag, country, article, exemption, visa_types, duration, faq1_q, faq1_a, faq2_q, faq2_a)
    ("brazil-tax-treaty-1040nr","🇧🇷","Brazil","No Treaty","No US-Brazil income tax treaty exists","F-1, J-1","N/A",
     "I am from Brazil — do I still file 1040-NR?","Yes — Brazilian nationals with US income must file Form 1040-NR like all nonresident aliens. Without a tax treaty, standard nonresident rates apply to all US-source income. You are still FICA exempt as a nonresident F-1 student.",
     "Is there any tax relief for Brazilian students in the US?","Without a tax treaty, federal income tax applies at standard rates. However, you are still exempt from FICA (Social Security and Medicare), and the FICA exemption can save 7.65% of your wages. File 1040-NR with e-file.com to correctly report your income and claim your FICA exemption."),
    ("australia-tax-treaty-1040nr","🇦🇺","Australia","Article 19","Student maintenance and education payments from Australian sources exempt","F-1, J-1","Limited period",
     "Does the US-Australia treaty cover my OPT wages?","Article 19 of the US-Australia treaty covers payments received from Australian sources for maintenance, education and training. OPT wages earned from a US employer are US-source income and generally not covered. You remain FICA exempt as a nonresident F-1 student.",
     "How do I claim the Australia treaty on my 1040-NR?","On Schedule OI of Form 1040-NR: Treaty Country = Australia, Treaty Article = 19, enter the exempt amount. Only Australian-source payments qualify — document your payment source carefully."),
    ("netherlands-tax-treaty-1040nr","🇳🇱","Netherlands","Article 22","Student and business apprentice maintenance payments exempt","F-1, J-1","Limited to study period",
     "I study in the US on a Dutch scholarship — is it tax-free?","If your scholarship is from a Netherlands source (Dutch government, Dutch university, Dutch foundation), the payments for your maintenance and study may be exempt under Article 22 of the US-Netherlands treaty. US-source TA/RA wages are not covered.",
     "Does the Netherlands treaty cover TU Delft exchange students?","Yes — if you are a Netherlands national studying in the US and receiving maintenance payments from Dutch sources, Article 22 may apply. Claim on Schedule OI of Form 1040-NR."),
    ("sweden-tax-treaty-1040nr","🇸🇪","Sweden","Article 19","Student and business apprentice maintenance payments from Swedish sources exempt","F-1, J-1","Limited to study period",
     "Swedish F-1 student — what does Article 19 cover?","Article 19 of the US-Sweden treaty exempts payments received from Swedish sources for maintenance, education and training. If your stipend or scholarship comes from a Swedish university or government agency, it may be exempt from US tax.",
     "Does Sweden treaty cover wages from a US university?","No — Article 19 covers payments from Swedish sources only. TA/RA wages paid by your US university are US-source income and fully taxable. You remain FICA exempt as a nonresident F-1 student."),
    ("china-tax-treaty-business","🇨🇳","China (Business Income)","Article 7","Business profits of a Chinese enterprise not subject to US tax unless through a permanent establishment","H-1B, L-1","> 5 years",
     "I am Chinese on H-1B — do I still get treaty benefits?","Once you become a US tax resident (by passing the Substantial Presence Test), most student treaty benefits under Article 20 no longer apply. However, other treaty articles may benefit H-1B residents — consult a tax professional. Most H-1B workers file Form 1040 as residents after 1-2 years.",
     "What treaty benefits apply to Chinese H-1B workers who are now US residents?","The US-China treaty has provisions on pensions, Social Security, and business income that may apply to US residents. The student exemption under Article 20 is for nonresident aliens only. A qualified tax professional can identify applicable treaty provisions for your specific situation."),
    ("india-tax-treaty-business","🇮🇳","India (Business & Standard Deduction)","Article 21","Standard deduction same as US citizens + student income exemption","F-1, J-1, H-1B","No strict limit",
     "Can Indian H-1B workers use the India tax treaty?","The student and trainee provisions of Article 21 apply to F-1 and J-1 visa holders who are nonresident aliens. H-1B workers who have become US tax residents may not use the nonresident student exemption. However, the unique standard deduction provision (allowing Indian students to claim US standard deduction) may still apply in some cases — consult a tax professional.",
     "What is the unique India standard deduction benefit?","Unlike most nonresident aliens who cannot claim the standard deduction, Indian nationals can claim the same standard deduction as US citizens under the US-India treaty — $14,600 for single filers in 2025. This is a major benefit not available under most other treaties. Claim it on your Form 1040-NR."),
]

for row in TREATIES:
    slug, flag, country, article, exemption, visas, duration = row[:7]
    faq1_q, faq1_a, faq2_q, faq2_a = row[7:]
    no_treaty = article == "No Treaty"
    body = f"""<div class="w"><h4>{flag} US-{country} Tax Treaty — Key Facts</h4><p>{'The United States does not have an income tax treaty with Brazil. Standard nonresident rates apply.' if no_treaty else f'Article {article} of the US-{country} income tax treaty provides: {exemption}. Visa types covered: {visas}.'}</p></div>
<div class="ey">Treaty Details</div><h2>US-{country} Tax Treaty — What It Covers</h2>
{cards(
('re','❌','No Treaty — Standard Rates','The US has no income tax treaty with Brazil. All US-source income is taxed at standard nonresident rates. No special exemptions apply.',) if no_treaty else ('gr','✅',f'Exemption: {exemption}',f'Must be claimed on Schedule OI of Form 1040-NR — not automatic.'),
('gr','✅','FICA Exempt Regardless','F-1 and J-1 nonresident students are exempt from FICA (Social Security and Medicare) taxes regardless of treaty status. This saves 7.65% of wages.'),
('go','⚠️','File 1040-NR','Nonresident aliens with US income must file Form 1040-NR. e-file.com is one of the only IRS-authorized platforms supporting 1040-NR e-filing.'),
('go','⚠️','Form 8843 Required','All F-1 and J-1 visa holders must file Form 8843 regardless of income or treaty status. Included automatically with e-file.com 1040-NR filing.'),
)}
{cta(f"File 1040-NR — {country} Nationals","e-file.com supports 1040-NR for all nationalities. IRS authorized, A+ BBB rated, refund in 10-21 days.")}
<div class="ey">FAQ</div><h2 style="margin-bottom:20px;">US-{country} Tax FAQ</h2>
<div class="fqs">
{faq(faq1_q, faq1_a)}
{faq(faq2_q, faq2_a)}
{faq(f"Where do I file my US tax return as a {country} national?","File Form 1040-NR with e-file.com — one of the only IRS-authorized platforms that supports nonresident alien e-filing. Include Form 8843. File by April 15 if you have wage income, or June 15 if you have no US wage withholding.")}
</div>"""
    p = build(f"{slug}.html",
        f"1040-NR {country} Nationals 2026 — US Tax Guide | e-file.com",
        f"Complete US tax guide for {country} nationals on F-1, J-1 and other visas. {'No US-'+country+' tax treaty — standard rates apply.' if no_treaty else 'Treaty '+article+' may reduce your US tax.'} File with e-file.com.",
        f"{flag} US-{country} Tax Guide 2026",
        f"1040-NR for <em>{country} Nationals</em> — 2026 Guide",
        f"{'No US-'+country+' income tax treaty exists.' if no_treaty else 'The US-'+country+' tax treaty '+article+' provides: '+exemption+'.'} File Form 1040-NR correctly with e-file.com — IRS authorized, A+ BBB rated.",
        f"{flag} US-{country.upper()} TAX TREATY 1040-NR GUIDE 2026",
        body)
    generated.append(p)
    print(f"✅ {slug}.html")

# ════════════════════════════════════════════════════════════════════
# 3. COMPARISON PAGES — vs competitors
# ════════════════════════════════════════════════════════════════════
COMPARISONS = [
    ("sprintax-vs-efile","Sprintax","$51.95+","Limited","Yes","Sprintax charges $51.95+ for a 1040-NR return. e-file.com supports 1040-NR at a fraction of the cost with IRS authorization and A+ BBB rating.","Sprintax is targeted at nonresident aliens and international students","international students looking for a cheaper 1040-NR alternative"),
    ("taxact-vs-efile","TaxAct","$49.99+","No","No","TaxAct is cheaper than TurboTax but does not support 1040-NR e-filing for nonresident aliens. e-file.com supports 1040-NR and is IRS authorized.","TaxAct targets US residents and citizens","filers looking for a TaxAct alternative that supports 1040-NR"),
    ("hrblock-vs-efile","H&R Block","$35+","No","Partial","H&R Block online does not support 1040-NR e-filing. Their in-person service does but costs significantly more. e-file.com supports 1040-NR online at far lower cost.","H&R Block is a major national tax preparation chain","filers comparing H&R Block vs e-file.com on cost and 1040-NR support"),
    ("turbotax-vs-efile-nonresident","TurboTax","$69+","No","No","TurboTax does not support Form 1040-NR at all. Nonresident aliens cannot use TurboTax to file their US tax return. e-file.com is the IRS-authorized alternative.","TurboTax is the most marketed tax software in the US","nonresident aliens who discovered TurboTax doesn't support 1040-NR"),
    ("taxslayer-vs-efile","TaxSlayer","$34.95+","No","No","TaxSlayer offers affordable filing for US residents but does not support 1040-NR for nonresident aliens. e-file.com fills this gap with full 1040-NR support.","TaxSlayer targets budget-conscious US filers","filers comparing TaxSlayer vs e-file.com"),
]

for slug, competitor, price, nr_support, free_support, summary, competitor_desc, audience in COMPARISONS:
    body = f"""<div class="w"><h4>⚖️ {competitor} vs e-file.com — The Key Difference</h4><p>{summary}</p></div>
<div class="ey">Side by Side</div><h2>{competitor} vs e-file.com — Full Comparison</h2>
{cards(
('re','💸',f'{competitor} Starting Price',f'{price} for federal filing. Additional state fees apply.'),
('gr','✅','e-file.com Starting Price','$0 free federal filing for most returns. State $22.49. No upgrade screens.'),
('re' if nr_support == 'No' else 'gr', '❌' if nr_support == 'No' else '✅',f'{competitor} 1040-NR Support',f'{"❌ Not supported — nonresident aliens cannot file with "+competitor+"." if nr_support == "No" else "✅ Supported"}'),
('gr','✅','e-file.com 1040-NR Support','✅ Fully supported — one of the only IRS-authorized platforms for 1040-NR e-filing.'),
('gr','✅','e-file.com BBB Rating','⭐ A+ Better Business Bureau rating since 2014. Independently accredited.'),
('gr','✅','e-file.com Refund Speed','10-21 days direct deposit after IRS acceptance — same as any major platform.'),
)}
{cta(f"Switch to e-file.com — File Free Today",f"IRS authorized · A+ BBB · Free federal filing · 70% cheaper than {competitor} · 1040-NR supported")}
<div class="ey">FAQ</div><h2 style="margin-bottom:20px;">{competitor} vs e-file.com — FAQ</h2>
<div class="fqs">
{faq(f"Can nonresident aliens use {competitor}?","No" if nr_support == "No" else "Limited — check current support",)}
{faq(f"Is e-file.com cheaper than {competitor}?",f"Yes — e-file.com federal filing is free for most returns. {competitor} starts at {price}. Even on paid plans e-file.com is significantly cheaper.")}
{faq(f"Will I get the same refund if I switch from {competitor} to e-file.com?",f"Yes — your refund is determined entirely by your income and the tax code, not which software you use. Both transmit returns to the IRS identically. The only difference is what you pay for the software.")}
</div>"""
    p = build(f"{slug}.html",
        f"{competitor} vs e-file.com 2026 — Which is Better for 1040-NR?",
        f"Comparing {competitor} vs e-file.com for US tax filing in 2026. e-file.com is cheaper, IRS authorized, and supports 1040-NR for nonresident aliens. {summary}",
        f"⚖️ {competitor} vs e-file.com 2026",
        f"{competitor} vs e-file.com — <em>Which to Choose?</em>",
        f"{competitor_desc}. But for {audience}, e-file.com wins on price, 1040-NR support, and IRS authorization.",
        f"⚖️ {competitor.upper()} VS E-FILE.COM — COMPLETE COMPARISON 2026",
        body)
    generated.append(p)
    print(f"✅ {slug}.html")

# ════════════════════════════════════════════════════════════════════
# 4. STATE PAGES — auto-generate any state
# ════════════════════════════════════════════════════════════════════
STATES = [
    ("pennsylvania-state-taxes-f1","🏔️","Pennsylvania","PA-40","3.07% flat","does not recognize federal tax treaties",["Penn State","University of Pennsylvania","Carnegie Mellon","Drexel","Temple"],
     "Does Pennsylvania recognize the China or India treaty?","No — Pennsylvania does not recognize federal tax treaties for state income tax purposes. Income that is exempt from federal tax under a treaty is still fully taxable in Pennsylvania at the 3.07% flat rate.",
     "What is the Pennsylvania filing deadline for F-1 students?","April 15, 2026 — same as federal. Pennsylvania offers an extension but any PA tax owed is still due April 15."),
    ("michigan-state-taxes-f1","〽️","Michigan","MI-1040","4.25% flat","does not fully recognize federal tax treaties",["University of Michigan","Michigan State","Wayne State","Western Michigan"],
     "Does Michigan recognize the China or India treaty?","Michigan generally does not fully recognize federal tax treaties. Income exempt federally may still be taxable in Michigan at the 4.25% flat rate.",
     "Ann Arbor city tax for UMich students?","Ann Arbor has a city income tax of 1% for residents and 0.5% for nonresidents working in Ann Arbor. Most F-1 students at UMich are nonresidents for Ann Arbor purposes."),
    ("north-carolina-state-taxes-f1","🏔️","North Carolina","NC D-400","4.5% flat","does not fully honor federal tax treaties",["UNC Chapel Hill","Duke","NC State","Wake Forest"],
     "Does North Carolina recognize federal tax treaties?","North Carolina does not fully recognize federal tax treaties. Some treaties may provide partial relief — check the NC DOR guidance for your specific treaty country.",
     "What forms do Duke and UNC F-1 students file?","Federal Form 1040-NR with e-file.com, plus North Carolina Form D-400 as a nonresident. File both by April 15, 2026."),
    ("georgia-state-taxes-f1","🍑","Georgia","GA Form 500","1-5.75% graduated","does not fully recognize federal tax treaties",["Georgia Tech","Emory","UGA","Georgia State"],
     "Does Georgia recognize the India or China treaty?","Georgia does not fully recognize federal tax treaties. Georgia-source income is taxed at Georgia rates regardless of federal treaty exemptions.",
     "What do Georgia Tech F-1 students file?","Federal Form 1040-NR with e-file.com, plus Georgia Form 500 as a nonresident. Georgia Tech is in Atlanta, Georgia — Georgia income tax applies to all GA-source income."),
    ("virginia-state-taxes-f1","🦅","Virginia","VA Form 763","2-5.75% graduated","partially recognizes some federal tax treaties",["University of Virginia","Virginia Tech","George Mason","William & Mary"],
     "Does Virginia recognize federal tax treaties?","Virginia partially recognizes some federal tax treaties. Check the Virginia Department of Taxation guidance for your specific treaty country and article.",
     "What do UVA and Virginia Tech F-1 students file?","Federal Form 1040-NR with e-file.com, plus Virginia Form 763 (Nonresident Return) for Virginia-source income. File both by April 15."),
    ("ohio-state-taxes-f1","🌰","Ohio","OH IT-1040","2.765-3.99% graduated","does not fully honor federal tax treaties",["Ohio State","Case Western","University of Cincinnati","Miami University"],
     "Does Ohio recognize the China or India treaty?","Ohio does not fully recognize federal tax treaties. Ohio-source income may be fully taxable at Ohio rates regardless of federal treaty exemptions.",
     "What do Ohio State F-1 students file?","Federal Form 1040-NR with e-file.com, plus Ohio Form IT-1040 as a nonresident for Ohio-source income. Columbus also has a 2.5% city income tax for residents."),
    ("arizona-state-taxes-f1","🌵","Arizona","AZ Form 140NR","2.5% flat","does not recognize federal tax treaties",["Arizona State","University of Arizona","NAU"],
     "Does Arizona recognize the China or India treaty?","No — Arizona does not recognize federal tax treaties. All Arizona-source income is taxable at the 2.5% flat rate regardless of federal treaty status.",
     "What do ASU and U of A F-1 students file?","Federal Form 1040-NR with e-file.com, plus Arizona Form 140NR as a nonresident. Arizona has a simple 2.5% flat income tax rate."),
    ("colorado-state-taxes-f1","🏔️","Colorado","CO Form 104","4.4% flat","does not recognize federal tax treaties",["University of Colorado Boulder","Colorado State","DU","Colorado School of Mines"],
     "Does Colorado recognize the China or India treaty?","No — Colorado does not recognize federal tax treaties. All Colorado-source income is taxable at the 4.4% flat rate.",
     "What do CU Boulder F-1 students file?","Federal Form 1040-NR with e-file.com, plus Colorado Form 104 as a nonresident for Colorado-source income. Denver also has a small city income tax."),
]

for row in STATES:
    slug, flag, state, form, rate, treaty_note, unis, faq1_q, faq1_a, faq2_q, faq2_a = row
    no_tax = "No state" in rate or "No income" in rate
    uni_cards = "".join(f'<div class="c go"><div class="ci">🎓</div><div class="ct">{u}</div><div class="cd">International students with {state}-source income must file {form} by April 15.</div></div>' for u in unis)
    body = f"""<div class="w"><h4>{flag} {state} State Tax — Key Facts for F-1 Students</h4><p>{state} {treaty_note}. State form: {form}. Rate: {rate}.</p></div>
<div class="ey">Filing Requirements</div><h2>Who Must File a {state} Return?</h2>
{cards(
('re','⚠️',f'{state}-Source Income',f'If you earned wages, stipends or fellowship income from a {state} employer or university, you must file {form}.'),
('go','⚠️',f'{state} Tax Rate: {rate}',f'Applies to all {state}-source income for nonresident filers.'),
('gr','✅','File Federal First',f'Complete your federal 1040-NR first. Your {state} return uses your federal income figures as the starting point.'),
('gr','✅','Two Potential Refunds',f'You may receive both a federal IRS refund and a {state} state refund if more was withheld than you owe.'),
)}
<div class="ey">Top {state} Universities</div><h2>Filing at These Schools</h2>
<div class="g">{uni_cards}</div>
{cta(f"File Your Federal 1040-NR with e-file.com",f"Handle your federal return with e-file.com. File your {state} {form} through the state tax authority website. IRS authorized, A+ BBB.")}
<div class="ey">FAQ</div><h2 style="margin-bottom:20px;">{state} F-1 Tax FAQ</h2>
<div class="fqs">
{faq(faq1_q, faq1_a)}
{faq(faq2_q, faq2_a)}
{faq(f"When is the {state} tax filing deadline for F-1 students?",f"April 15, 2026 — same as the federal deadline. Check the {state} Department of Revenue website for extension options.")}
</div>"""
    p = build(f"{slug}.html",
        f"{state} State Taxes for F-1 Students 2026 — {form} Nonresident Guide",
        f"F-1 students in {state} with income must file {form}. {rate} state income tax. {treaty_note.capitalize()}. Complete guide for {unis[0]} and other {state} universities.",
        f"{flag} {state} F-1 Tax Guide 2026",
        f"{state} State Taxes for <em>F-1 Students</em> 2026",
        f"F-1 and J-1 students in {state} who earned income must file {form}. {rate} state income tax rate. Complete guide covering {', '.join(unis[:3])} and all {state} universities.",
        f"{flag} {state.upper()} STATE TAXES FOR F-1 INTERNATIONAL STUDENTS 2026",
        body)
    generated.append(p)
    print(f"✅ {slug}.html")

# ════════════════════════════════════════════════════════════════════
# 5. SITEMAP — auto-generate covering everything
# ════════════════════════════════════════════════════════════════════
existing_pages = [
    "", "wheremyrefund.html", "turbotax-alternative.html", "free-tax-filing.html",
    "freefile.html", "taxrefundusa.html", "irsespanola.html", "1040-nr-cn.html",
    "international-tax-refund.html", "form-8843.html", "fica-refund-f1-opt.html",
    "itin-application-w7.html", "opt-stem-opt-taxes.html", "stipend-taxable-income-f1.html",
    "tax-extension-4868-nonresident.html", "j1-visa-taxes.html", "h1b-tax-return.html",
    "dual-status-tax-return.html", "india-tax-treaty-1040nr.html", "korea-tax-treaty-1040nr.html",
    "germany-tax-treaty-1040nr.html", "france-tax-treaty-1040nr.html", "japan-tax-treaty-1040nr.html",
    "uk-tax-treaty-1040nr.html", "canada-tax-treaty-1040nr.html", "mexico-tax-treaty-1040nr.html",
    "california-state-taxes-f1.html", "new-york-state-taxes-f1.html", "texas-state-taxes-f1.html",
    "florida-state-taxes-f1.html", "washington-state-taxes-f1.html", "massachusetts-state-taxes-f1.html",
    "illinois-state-taxes-f1.html", "mit-international-student-taxes.html",
    "stanford-international-student-taxes.html", "harvard-international-student-taxes.html",
    "columbia-international-student-taxes.html", "princeton-international-student-taxes.html",
    "yale-international-student-taxes.html", "uc-berkeley-international-student-taxes.html",
    "university-of-michigan-international-taxes.html", "usc-international-student-taxes.html",
]

# Add all newly generated pages
new_slugs = [os.path.basename(p) for p in generated]

all_pages = existing_pages + new_slugs

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for slug in all_pages:
    url = f"{BASE}/{slug}" if slug else f"{BASE}/"
    pri = "1.0" if slug == "" else "0.9" if any(x in slug for x in ["treaty","fica","form-8843","opt-stem","j1","h1b"]) else "0.8" if any(x in slug for x in ["university","international-taxes","intl"]) else "0.7"
    xml += f'  <url><loc>{url}</loc><lastmod>{DATE}</lastmod><changefreq>monthly</changefreq><priority>{pri}</priority></url>\n'
xml += '</urlset>'

sitemap_path = os.path.join(OUT, "sitemap.xml")
with open(sitemap_path, "w") as f:
    f.write(xml)

# ════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════
print(f"\n{'='*50}")
print(f"✅ GENERATION COMPLETE")
print(f"{'='*50}")
print(f"Universities:  {len(UNIVERSITIES)} pages")
print(f"Treaties:      {len(TREATIES)} pages")
print(f"Comparisons:   {len(COMPARISONS)} pages")
print(f"State pages:   {len(STATES)} pages")
print(f"Total new:     {len(generated)} pages")
print(f"Sitemap URLs:  {len(all_pages)}")
print(f"Output folder: ./{OUT}/")
print(f"\nUpload everything in ./{OUT}/ to brightlane/UsaTaxRefund")
print(f"Then submit sitemap: {BASE}/sitemap.xml")

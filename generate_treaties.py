#!/usr/bin/env python3
"""
USATaxRefund — Treaty Page Generator
Add any country to TREATIES list and run to generate pages.
Usage: python3 generate_treaties.py
Output: ./generated/treaties/
"""
import os, datetime

ALINK = "https://www.linkconnector.com/ta.php?lc=007949061588005142&atid=UsaTaxRefunds"
BASE  = "https://brightlane.github.io/UsaTaxRefund"
DATE  = datetime.date.today().isoformat()
OUT   = "generated/treaties"
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
    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/{fname}">
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
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)
    return fname

# ════════════════════════════════════════════════════════════════════
# ADD COUNTRIES HERE
# Format:
#   slug        = filename without .html
#   flag        = emoji flag
#   country     = country name
#   article     = treaty article e.g. "Article 20" or "No Treaty"
#   exemption   = what is exempt e.g. "Up to $5,000 wages exempt"
#   visas       = applicable visa types
#   duration    = how long benefit lasts
#   note        = important detail about this treaty
#   faq1_q/a    = first FAQ question and answer
#   faq2_q/a    = second FAQ question and answer
# ════════════════════════════════════════════════════════════════════
TREATIES = [
    # slug, flag, country, article, exemption, visas, duration, note, faq1_q, faq1_a, faq2_q, faq2_a
    ("china-tax-treaty-1040nr",    "🇨🇳","China",       "Article 20",  "Up to $5,000 wages exempt per year",                  "F-1, J-1",    "First 5 years", "Must be claimed on Schedule OI — not automatic",
     "Does China treaty cover OPT wages?", "Yes — as long as you are within your first 5 calendar years in F-1 status, the Article 20 exemption applies to OPT wages. This can save $750-$1,200 in federal tax.",
     "Does California recognize the China treaty?", "No — California does not honor the US-China tax treaty. Your full California-source income is taxable at California state rates."),

    ("india-tax-treaty-1040nr",    "🇮🇳","India",       "Article 21",  "Up to $15,750 exempt + standard deduction allowed",   "F-1, J-1",    "No strict limit","Unique: Indian students can claim the same standard deduction as US citizens",
     "Can Indian H-1B workers use the treaty?","The student provisions of Article 21 apply to F-1/J-1 nonresidents. Once you become a US tax resident on H-1B, the standard deduction benefit may still apply — consult a tax professional.",
     "What is the standard deduction benefit for Indian students?","Indian nationals can claim the same standard deduction as US citizens — $14,600 single in 2025. This is unique among tax treaties and significantly reduces taxable income."),

    ("korea-tax-treaty-1040nr",    "🇰🇷","Korea",       "Article 21",  "Student maintenance payments from Korean sources exempt","F-1, J-1",    "Study period",  "Primarily covers payments from Korean sources — US-source OPT wages still taxable",
     "Does Korea treaty cover my OPT wages from a US employer?","Article 21 primarily covers maintenance payments from Korean sources. OPT wages earned from a US employer are generally fully taxable. You remain FICA exempt as a nonresident.",
     "How do I claim the Korea treaty on my 1040-NR?","On Schedule OI of Form 1040-NR: Treaty Country = Korea, Treaty Article = 21, enter the exempt income amount. Only Korean-source payments qualify."),

    ("germany-tax-treaty-1040nr",  "🇩🇪","Germany",     "Article 20",  "Education and maintenance payments from German sources exempt","F-1, J-1","Study period",  "German students receiving payments from German sources may exempt them from US tax",
     "Does Germany treaty cover my TA wages at a US university?","Article 20 covers payments from German sources for education and maintenance. TA/RA wages from a US university are US-source income and are generally taxable. You remain FICA exempt.",
     "How do I claim the Germany treaty?","Schedule OI of Form 1040-NR: Treaty Country = Federal Republic of Germany, Treaty Article = 20, exempt amount, income type. Attach a statement if amounts are significant."),

    ("france-tax-treaty-1040nr",   "🇫🇷","France",      "Article 21",  "Student and apprentice income payments from French sources exempt","F-1, J-1","Study period", "French students receiving payments from France for maintenance and training",
     "I am a French PhD student — does Article 21 cover my stipend?","If your stipend comes from a French source (French government, French university), it may be exempt. US-source TA/RA wages are generally taxable regardless of treaty.",
     "Does France treaty apply after I become a US resident?","No — once you pass the Substantial Presence Test, the nonresident student exemptions generally no longer apply."),

    ("japan-tax-treaty-1040nr",    "🇯🇵","Japan",       "Article 20",  "Student maintenance, education and training payments exempt","F-1, J-1", "Study period",  "Applies for the period reasonably necessary to complete education",
     "How long does the Japan treaty exemption last?","The IRS generally accepts up to 5 years for most degree programs, though the treaty does not specify an exact time limit.",
     "Does Japan treaty cover payments from a Japanese scholarship?","Yes — if the scholarship comes from a Japanese government agency, Japanese university or Japanese foundation, Article 20 may apply even if paid directly to your US institution."),

    ("uk-tax-treaty-1040nr",       "🇬🇧","United Kingdom","Article 20", "UK-source maintenance and education payments exempt", "F-1, J-1",    "Study period",  "Covers Chevening, Commonwealth and other UK-source scholarships",
     "Does UK treaty cover my RA pay from a US university?","No — Article 20 covers payments from UK sources. RA/TA wages from a US university are US-source income and not covered. You remain FICA exempt.",
     "I am on a Chevening Scholarship — is it exempt?","Yes — Chevening scholarship payments from the UK for maintenance and study in the US are generally exempt under Article 20 of the US-UK treaty."),

    ("canada-tax-treaty-1040nr",   "🇨🇦","Canada",      "Article XXI", "Student and business apprentice income from Canadian sources exempt","F-1, J-1, TN","Study period","Canadian students and TN visa holders — extensive treaty provisions",
     "Does Canada treaty cover TN visa workers?","TN visa holders may benefit from other treaty provisions on business income and pensions. The student exemption under Article XXI applies to F-1/J-1 students.",
     "I am a Canadian F-1 student — what does Article XXI exempt?","Payments received from Canadian sources for maintenance, education and training while studying in the US. RA/TA wages from a US university are not covered."),

    ("mexico-tax-treaty-1040nr",   "🇲🇽","Mexico",      "Article 22",  "Student and business apprentice maintenance payments from Mexican sources exempt","F-1, J-1, TN","Study period","Mexican students receiving payments from Mexico for US study",
     "Does Article 22 cover my OPT wages from a US employer?","No — Article 22 exempts maintenance payments from Mexican sources only. OPT wages from a US employer are US-source income and taxable.",
     "I have a Mexican government scholarship — is it exempt?","If the scholarship is from a Mexican source (government, university, foundation) and covers maintenance for study in the US, Article 22 may apply. Document the source carefully."),

    ("australia-tax-treaty-1040nr","🇦🇺","Australia",   "Article 19",  "Australian-source student maintenance payments exempt","F-1, J-1",   "Study period",  "Covers Australian government scholarships and university maintenance payments",
     "Does Australia treaty cover OPT wages?","Article 19 covers payments from Australian sources for maintenance and training. OPT wages from a US employer are US-source and generally not covered.",
     "How do I claim the Australia treaty?","Schedule OI of Form 1040-NR: Treaty Country = Australia, Treaty Article = 19, exempt amount. Only Australian-source payments qualify."),

    ("netherlands-tax-treaty-1040nr","🇳🇱","Netherlands","Article 22", "Student and apprentice maintenance payments from Dutch sources exempt","F-1, J-1","Study period","Dutch students receiving payments from Netherlands sources",
     "I have a Dutch government scholarship — is it exempt?","If your scholarship is from a Netherlands source (Dutch government, TU Delft, NWO), the maintenance payments may be exempt under Article 22.",
     "Does Netherlands treaty cover wages from a US university?","No — Article 22 covers payments from Dutch sources only. TA/RA wages from a US university are US-source income and taxable."),

    ("sweden-tax-treaty-1040nr",   "🇸🇪","Sweden",      "Article 19",  "Swedish-source student maintenance and training payments exempt","F-1, J-1","Study period", "Swedish government scholarships and university payments covered",
     "Swedish F-1 student — what does Article 19 cover?","Payments received from Swedish sources for maintenance, education and training. If your stipend or scholarship comes from a Swedish university or government agency, it may be exempt.",
     "Does Sweden treaty cover wages from a US employer?","No — Article 19 covers payments from Swedish sources only. US-source TA/RA wages are taxable."),

    ("brazil-tax-treaty-1040nr",   "🇧🇷","Brazil",      "No Treaty",   "No US-Brazil income tax treaty — standard rates apply","F-1, J-1",  "N/A",           "Brazil is one of the few major countries with no US income tax treaty",
     "I am from Brazil — what tax rate applies to my US income?","Without a treaty, standard nonresident alien tax rates apply — 10-37% on wages depending on amount. No special exemptions. You are still FICA exempt as a nonresident F-1 student.",
     "Is there any tax relief for Brazilian students?","FICA exemption saves 7.65% of wages. The personal exemption of $4,400 reduces taxable income. These apply regardless of treaty status. File 1040-NR with e-file.com to claim all available deductions."),

    ("india-tax-treaty-business",  "🇮🇳","India (H-1B)","Article 21",  "Standard deduction same as US citizens — unique benefit","H-1B",      "No limit",      "Indian H-1B workers who are US residents may still claim standard deduction",
     "Can Indian H-1B workers who are US residents use the treaty?","Indian nationals who are US tax residents may still claim the same standard deduction as US citizens under the treaty — $14,600 single in 2025. This is a significant benefit not available to most other nonresident or resident alien filers.",
     "What other treaty benefits apply to Indian H-1B residents?","Consult a tax professional for your specific situation. The standard deduction provision is the most commonly cited benefit for Indian nationals who have become US residents."),

    # ── ADD MORE COUNTRIES BELOW ─────────────────────────────────────
    # ("slug","🏳️","Country","Article X","What is exempt","Visa types","Duration","Key note","FAQ1 Q","FAQ1 A","FAQ2 Q","FAQ2 A"),
]

generated = []
for row in TREATIES:
    slug, flag, country, article, exemption, visas, duration, note, faq1_q, faq1_a, faq2_q, faq2_a = row
    no_treaty = article == "No Treaty"

    body = f"""<div class="w"><h4>{flag} US-{country} Tax Treaty — Key Facts</h4><p>{'The United States does not have an income tax treaty with '+country+'. Standard nonresident rates apply to all US-source income.' if no_treaty else 'US-'+country+' Tax Treaty '+article+': '+exemption+'. Applies to: '+visas+'. Duration: '+duration+'. Important: '+note+'.'}</p></div>
<div class="ey">Treaty Details</div><h2>US-{country} — What You Need to Know</h2>
{cards(
('re','❌','No Treaty — Standard Rates',f'No US-{country} income tax treaty. All US-source income taxed at standard nonresident rates (10-37%).') if no_treaty else ('gr','✅',f'Exemption: {exemption}',f'Applies to {visas} visa holders. Duration: {duration}. Must be claimed on Schedule OI of Form 1040-NR.'),
('go','⚠️','Must Claim on 1040-NR',f'Treaty benefits are NOT automatic. Claim on Schedule OI of Form 1040-NR. Enter: Treaty Country = {country}, Treaty Article = {article.replace("No Treaty","N/A")}.') if not no_treaty else ('gr','✅','FICA Exempt Regardless',f'F-1 and J-1 nonresident students are FICA exempt regardless of treaty status. This saves 7.65% of all wages earned.'),
('gr','✅','FICA Exempt','F-1 and J-1 nonresident students are exempt from Social Security (6.2%) and Medicare (1.45%) taxes — saves 7.65% of wages.'),
('go','⚠️','Form 8843 Required','All F-1 and J-1 visa holders must file Form 8843 regardless of income or treaty status. Included automatically with e-file.com 1040-NR filing.'),
)}
{cta(f"File 1040-NR — {country} Nationals",f"e-file.com supports 1040-NR for all nationalities. {'Treaty '+article+' applied correctly.' if not no_treaty else 'Standard nonresident rates applied correctly.'} IRS authorized, A+ BBB.")}
<div class="ey">FAQ</div><h2 style="margin-bottom:20px;">US-{country} Tax FAQ</h2>
<div class="fqs">
{faq(faq1_q, faq1_a)}
{faq(faq2_q, faq2_a)}
{faq(f"Where do I file my US tax return as a {country} national?","File Form 1040-NR with e-file.com — one of the only IRS-authorized platforms that supports nonresident alien e-filing. Include Form 8843 if you are on F-1 or J-1. File by April 15 if you have wage income, or June 15 if you have no US wage withholding.")}
</div>"""

    fname = build(f"{slug}.html",
        f"1040-NR {country} Nationals 2026 — US Tax Treaty Guide | e-file.com",
        f"Complete US tax guide for {country} nationals on F-1, J-1 and other visas. {'No US-'+country+' tax treaty.' if no_treaty else 'US-'+country+' treaty '+article+': '+exemption+'.'} File Form 1040-NR with e-file.com.",
        f"{flag} US-{country} Tax Guide 2026",
        f"1040-NR for <em>{country} Nationals</em> — 2026 Guide",
        f"{'No US-'+country+' income tax treaty exists — standard nonresident rates apply.' if no_treaty else 'The US-'+country+' tax treaty '+article+' provides: '+exemption+'.'} File Form 1040-NR correctly with e-file.com.",
        f"{flag} US-{country.upper()} TAX TREATY 1040-NR GUIDE 2026",
        body)
    generated.append(fname)
    print(f"✅ {fname}")

print(f"\n✅ Done — {len(generated)} treaty pages in ./{OUT}/")

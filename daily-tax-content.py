#!/usr/bin/env python3
"""
UsaTaxRefund Daily Content Generator
Generates 1 new tax tip/FAQ page per day automatically
Runs via GitHub Actions at 9am UTC daily
"""
import os, re, json, random, datetime

ALINK  = "https://www.linkconnector.com/ta.php?lc=007949061588005142&atid=UsaTaxRefunds"
BASE   = "https://brightlane.github.io/UsaTaxRefund"
TODAY  = datetime.date.today().isoformat()
SEED   = int(datetime.date.today().strftime("%Y%m%d"))
TODAY_NICE = datetime.date.today().strftime("%B %d, %Y")

CSS = """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>:root{--blue:#003087;--red:#cc0000;--gold:#f5a623;--dark:#0a0d14;--card:#111520;--border:#1e2540;--text:#eef0f8;--muted:#7a8aa8;--green:#00c853;}*{box-sizing:border-box;margin:0;padding:0;}body{font-family:Inter,sans-serif;background:var(--dark);color:var(--text);line-height:1.6;}nav{position:sticky;top:0;z-index:100;background:rgba(10,13,20,.96);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 28px;height:60px;}.logo{font-size:20px;font-weight:900;color:var(--text);text-decoration:none;}.logo span{color:var(--gold);}.nc{background:var(--red);color:#fff;padding:9px 20px;border-radius:8px;font-weight:700;font-size:13px;text-decoration:none;}.hero{background:linear-gradient(180deg,#00082a 0%,var(--dark) 100%);padding:56px 24px 36px;text-align:center;border-bottom:1px solid var(--border);}.badge{display:inline-flex;align-items:center;gap:8px;background:rgba(0,80,200,.15);border:1px solid rgba(0,80,200,.4);color:#7ab0ff;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:6px 16px;border-radius:20px;margin-bottom:20px;}h1{font-size:clamp(24px,4.5vw,48px);font-weight:900;line-height:1.1;letter-spacing:-2px;margin-bottom:14px;}h1 em{color:var(--gold);font-style:normal;}.hs{color:var(--muted);font-size:16px;max-width:540px;margin:0 auto 24px;line-height:1.6;}.btn{background:var(--red);color:#fff;font-weight:800;padding:14px 32px;border-radius:10px;text-decoration:none;font-size:14px;display:inline-flex;align-items:center;gap:8px;}.s{padding:52px 24px;max-width:880px;margin:0 auto;}.ey{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:10px;}h2{font-size:clamp(18px,3vw,30px);font-weight:800;letter-spacing:-1px;margin-bottom:12px;}.sub{color:var(--muted);font-size:14px;margin-bottom:24px;}.tips{display:flex;flex-direction:column;gap:12px;margin-bottom:28px;}.tip{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;}.tip-n{width:30px;height:30px;border-radius:50%;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:13px;margin-bottom:10px;}.tip-t{font-weight:700;font-size:14px;margin-bottom:5px;color:var(--gold);}.tip-d{color:var(--muted);font-size:13px;line-height:1.5;}.w{background:#1a0800;border:1px solid rgba(245,166,35,.4);border-radius:12px;padding:18px;margin:16px 0;}.w h4{color:var(--gold);font-size:14px;font-weight:700;margin-bottom:6px;}.w p{color:#c0b080;font-size:13px;line-height:1.6;margin:0;}.cb{background:linear-gradient(135deg,#001a6e,#003087);border:1px solid rgba(0,80,200,.4);border-radius:14px;padding:36px 28px;text-align:center;margin:32px 0;}.cb h2{margin-bottom:8px;}.cb p{color:#a0b8e8;font-size:14px;margin-bottom:18px;}.fqs{display:flex;flex-direction:column;gap:10px;}.fq{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;}.fqq{font-weight:700;font-size:14px;margin-bottom:5px;}.fqa{color:var(--muted);font-size:13px;line-height:1.6;}footer{background:var(--card);border-top:1px solid var(--border);padding:18px 24px;text-align:center;font-size:12px;color:var(--muted);line-height:2;}@media(max-width:600px){.hero,.s{padding:36px 16px;}}</style>"""

# ── CONTENT POOL: 365 unique daily tax topics ───────────────────────
TOPICS = [
  # Deadlines
  {"slug":"tax-deadline-april-15-2026","title":"IRS Tax Deadline April 15 2026","h1":"IRS Tax Deadline — <em>April 15, 2026</em>","tips":[
    ("File by April 15","The federal tax filing deadline for 2025 returns is April 15, 2026. File Form 1040-NR (nonresidents) or 1040 (residents) by this date to avoid failure-to-file penalties."),
    ("Pay Even If You Extend","Filing a Form 4868 extension extends your filing deadline to October 15 — but any tax owed must still be paid by April 15 to avoid interest and failure-to-pay penalties."),
    ("E-file Gets Faster Refunds","E-filed returns with direct deposit receive refunds in 10-21 days. Paper returns take 6-8 weeks. Always e-file."),
    ("F-1 No-Income Deadline is June 15","If you are an F-1 student with no US income and only need to file Form 8843, your deadline is June 15 — not April 15."),
  ],"faqs":[
    ("What if I miss the April 15 deadline?","If you owe tax, the IRS charges a failure-to-file penalty of 5% per month (up to 25%) plus a failure-to-pay penalty of 0.5% per month. If you are due a refund, there is no penalty for filing late — but your refund is delayed."),
    ("Can I file after April 15 without an extension?","Yes — the IRS still accepts returns after the deadline. If you owe tax, penalties and interest accrue from April 15. If you are due a refund, no penalty applies."),
  ]},
  # Treaty
  {"slug":"us-china-tax-treaty-students-2026","title":"US-China Tax Treaty Article 20 — $5,000 Student Exemption 2026","h1":"US-China Treaty Article 20 — <em>$5,000 Tax-Free</em>","tips":[
    ("Up to $5,000 Wages Exempt","Chinese F-1 and J-1 students can exempt up to $5,000 of wages from US federal income tax per year under Article 20 of the US-China tax treaty."),
    ("First 5 Years Only","The exemption applies during your first 5 calendar years in the US in F-1 or J-1 status. After 5 years, you become a US resident and the treaty exemption no longer applies."),
    ("Must Claim on 1040-NR","The exemption is NOT automatic. Claim it on Schedule OI of Form 1040-NR. e-file.com guides you through this step."),
    ("Does Not Cover All Income","The $5,000 covers wages. Scholarship amounts covering living expenses may be covered separately under Article 20(b) for students."),
  ],"faqs":[
    ("Can I claim the China treaty and still work on OPT?","Yes — as long as you are within your first 5 calendar years in F-1 status, you can claim the Article 20 exemption on OPT wages. This can save you $750-$1,200 in federal tax depending on your bracket."),
    ("Does California recognize the China treaty?","No — California does not honor the US-China tax treaty. Your full California-source income is taxable at California rates regardless of the federal exemption."),
  ]},
  # ITIN
  {"slug":"how-to-get-itin-without-passport-2026","title":"How to Get an ITIN Without Mailing Your Passport 2026","h1":"Get an ITIN <em>Without Mailing Your Passport</em>","tips":[
    ("Use a Certified Acceptance Agent","A Certified Acceptance Agent (CAA) is IRS-authorized to verify your original documents and send certified copies to the IRS — so your passport never leaves your hands."),
    ("Find CAA at Your University","Most large universities with international students have a CAA on staff or partner with one. Contact your International Student Office."),
    ("Processing Takes 7-11 Weeks","Even with a CAA, ITIN processing takes 7-11 weeks. Apply as early as possible — your refund is delayed until your ITIN is processed."),
    ("Apply with Your 1040-NR","Submit Form W-7 together with your completed 1040-NR. The IRS processes the ITIN first, then applies it to your return."),
  ],"faqs":[
    ("Can I file my 1040-NR before receiving my ITIN?","Yes — submit Form W-7 together with your 1040-NR, writing 'ITIN TO BE REQUESTED' in the taxpayer ID field. The IRS issues your ITIN and then processes your return. Your refund clock starts after ITIN issuance."),
    ("Do I need a new ITIN every year?","No — your ITIN is permanent unless it expires from non-use. Use the same ITIN every year. ITINs expire if not used on a tax return for 3 consecutive years."),
  ]},
  # FICA
  {"slug":"fica-exempt-f1-students-2026","title":"F-1 Students Are FICA Exempt — Social Security Tax Refund 2026","h1":"F-1 Students Are <em>FICA Exempt</em> — Claim Your Refund","tips":[
    ("7.65% of Wages Back","FICA taxes (Social Security 6.2% + Medicare 1.45% = 7.65%) do not apply to F-1 nonresident students. On a $30,000 salary, that is $2,295 per year you should NOT be paying."),
    ("Notify Your Employer in Writing","Send your HR department a written notice of your F-1 FICA exemption. Include your visa, I-20, and I-94. This prevents future incorrect withholding."),
    ("Already Withheld? File Form 843","If FICA was already withheld, first ask your employer for a refund with a corrected W-2. If they refuse, file IRS Form 843 with Form 8316 to claim directly from the IRS."),
    ("OPT and STEM OPT Also Exempt","The FICA exemption extends through your entire OPT and STEM OPT period — as long as you remain a nonresident alien within your first 5 years."),
  ],"faqs":[
    ("My employer says I have to pay FICA — are they wrong?","Possibly. IRS Revenue Procedure 2000-17 confirms F-1 nonresident aliens are FICA exempt. However, after 5 years in F-1 status you may have become a resident alien and FICA would apply. Check your nonresident status first."),
    ("How long does an IRS FICA refund take?","FICA refund claims via Form 843 typically take 4-6 months to process. The IRS mails a check to your address on the return. Filing electronically is not available for Form 843."),
  ]},
  # Refund tracker
  {"slug":"irs-refund-status-2026-tracker","title":"IRS Refund Status 2026 — Track Your Tax Refund","h1":"IRS Refund Status — <em>Track Your Refund</em>","tips":[
    ("Use Where's My Refund","Check refund status at IRS.gov/refunds. You need your SSN or ITIN, filing status, and exact refund amount. Updates once daily, usually overnight."),
    ("3 Stages to Know","Return Received → Refund Approved → Refund Sent. Once Approved, direct deposit arrives in 1-5 business days."),
    ("10-21 Days for E-Filed","E-file with direct deposit = 10-21 days. Paper return = 6-8 weeks. Always e-file for the fastest refund."),
    ("Call After 21 Days","If no update after 21 days since e-filing, call IRS at 1-800-829-1954. Have your SSN and refund amount ready."),
  ],"faqs":[
    ("Why does it say 'still being processed'?","Common reasons: errors requiring manual review, identity verification needed, you claimed EITC or ACTC (held until mid-February by law), or IRS backlog. If it has been more than 21 days since e-filing, contact the IRS."),
    ("Can I check my 1040-NR refund status?","Yes — the Where's My Refund tool works for 1040-NR returns. Use your ITIN if you do not have an SSN. 1040-NR returns may take slightly longer than standard 1040 returns."),
  ]},
  # More topics...
  {"slug":"standard-deduction-nonresident-2026","title":"Standard Deduction for Nonresident Aliens 2026 — Can F-1 Students Claim It?","h1":"Standard Deduction — <em>Can Nonresidents Claim It?</em>","tips":[
    ("Generally No for Nonresidents","Nonresident aliens (F-1, J-1, H-1B nonresident) generally CANNOT claim the US standard deduction ($14,600 single in 2025). Itemized deductions on Schedule A of 1040-NR are allowed instead."),
    ("India Treaty Exception","Indian nationals can claim the same standard deduction as US citizens under the US-India tax treaty — a unique and valuable benefit not available under most other treaties."),
    ("Itemize What You Can","Nonresidents can deduct state and local income taxes paid, charitable contributions to US organizations, and casualty and theft losses on Schedule A of Form 1040-NR."),
    ("Resident Aliens Get Full Standard Deduction","Once you become a US tax resident (by passing the Substantial Presence Test), you qualify for the full standard deduction like any US taxpayer."),
  ],"faqs":[
    ("What can Indian students deduct as a standard deduction?","Under the US-India treaty, Indian students can claim the same standard deduction as US citizens and residents — $14,600 for single filers in 2025. This is claimed on Form 1040-NR and significantly reduces taxable income compared to other nonresident students."),
    ("What itemized deductions are available to nonresidents?","Nonresidents filing 1040-NR can itemize: state and local income taxes (up to $10,000), charitable contributions to US qualified organizations, and casualty losses from federally declared disasters. Personal exemptions of $4,400 are also available."),
  ]},
  {"slug":"tax-refund-average-2026","title":"Average Tax Refund 2026 — How Much Will You Get?","h1":"Average Tax Refund 2026 — <em>How Much to Expect</em>","tips":[
    ("Average Refund is $2,800","The average IRS tax refund in 2026 is approximately $2,800. Your actual refund depends on income, withholding, deductions and credits."),
    ("Withholding Determines Refund","Your refund is simply the difference between what was withheld from your paycheck and what you actually owe. Adjust your W-4 withholding to get less at refund time and more in each paycheck."),
    ("Treaty Benefits Increase Nonresident Refunds","F-1 and J-1 students claiming treaty benefits often receive larger refunds because more was withheld than their actual tax liability after the exemption."),
    ("File Early for Faster Refund","The IRS processes returns in order received. Filing in January or February vs April means your refund arrives weeks earlier."),
  ],"faqs":[
    ("Why is my refund less than last year?","Common reasons: income increased, fewer withholding allowances, expired credits (COVID-era credits), life changes like marriage or losing a dependent, or your employer changed withholding."),
    ("Can I invest my tax refund?","Yes — you can split your refund into up to 3 accounts using Form 8888. Common choices: savings account, Roth IRA contribution, or purchasing US Savings Bonds directly from the IRS refund."),
  ]},
]

rng = random.Random(SEED)
topic = rng.choice(TOPICS)

slug = topic["slug"]
title = topic["title"] + " | USATaxRefund"
desc = f"Complete guide: {topic['title']}. File with e-file.com — IRS authorized, A+ BBB rated, free federal filing. Refund in 10-21 days."
badge = f"📅 Tax Guide — {TODAY_NICE}"
h1 = topic["h1"]
hs = f"Everything you need to know about {topic['title'].lower()} in 2026. Updated {TODAY_NICE}."

tips_html = '<div class="tips">'
for i, (t, d) in enumerate(topic["tips"], 1):
    tips_html += f'<div class="tip"><div class="tip-n">{i}</div><div class="tip-t">{t}</div><div class="tip-d">{d}</div></div>'
tips_html += '</div>'

faqs_html = '<div class="fqs">'
for q, a in topic["faqs"]:
    faqs_html += f'<div class="fq"><div class="fqq">{q}</div><div class="fqa">{a}</div></div>'
faqs_html += '</div>'

body = f"""
<div class="ey">Today's Tax Guide</div>
<h2>{topic['title']}</h2>
<p class="sub">Updated {TODAY_NICE} · {len(topic['tips'])} key facts · IRS accurate information</p>
{tips_html}
<div class="cb">
<h2>File Your Tax Return with e-file.com</h2>
<p>IRS authorized · A+ BBB rated · Free federal filing · 1040-NR supported · Refund in 10-21 days</p>
<a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored" style="font-size:16px;padding:17px 40px;display:inline-flex;">🚀 Start Filing Free Now</a>
<p style="color:#7ab0ff;font-size:12px;margin-top:12px;">No credit card · 70% cheaper than TurboTax · IRS authorized</p>
</div>
<div class="ey">FAQ</div>
<h2 style="margin-bottom:16px;">Questions Answered</h2>
{faqs_html}
<p style="text-align:center;margin-top:24px;font-size:13px;color:var(--muted);">Updated {TODAY_NICE} · <a href="/UsaTaxRefund/" style="color:var(--muted);">← USATaxRefund Home</a></p>
"""

html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/daily/{slug}.html">
{CSS}</head><body>
<nav><a class="logo" href="/UsaTaxRefund/"><span>🇺🇸</span> USATaxRefund</a><a class="nc" href="{ALINK}" target="_blank" rel="noopener sponsored">File Free →</a></nav>
<div class="hero"><div class="badge">{badge}</div><h1>{h1}</h1><p class="hs">{hs}</p>
<a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored">🚀 File with e-file.com</a></div>
<div class="s">{body}</div>
<footer><p>USATaxRefund is an independent affiliate site earning commissions from e-file.com links.</p>
<p>Not tax or legal advice. e-file.com is IRS-authorized, A+ BBB rated since 2014.</p>
<p>© 2026 USATaxRefund · <a href="{ALINK}" style="color:var(--gold)">File Free →</a></p></footer>
</body></html>"""

os.makedirs("daily", exist_ok=True)
fname = f"daily/{slug}.html"
with open(fname, "w") as f:
    f.write(html)

# Update sitemap
sm_path = "sitemap.xml"
if os.path.exists(sm_path):
    with open(sm_path) as f:
        sm = f.read()
else:
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>'

url = f"{BASE}/{fname}"
if url not in sm:
    sm = sm.replace('</urlset>', f'  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><changefreq>yearly</changefreq><priority>0.6</priority></url>\n</urlset>')
    with open(sm_path, "w") as f:
        f.write(sm)

print(f"Generated: {fname} ({len(html):,} bytes)")
print(f"Topic: {topic['title']}")

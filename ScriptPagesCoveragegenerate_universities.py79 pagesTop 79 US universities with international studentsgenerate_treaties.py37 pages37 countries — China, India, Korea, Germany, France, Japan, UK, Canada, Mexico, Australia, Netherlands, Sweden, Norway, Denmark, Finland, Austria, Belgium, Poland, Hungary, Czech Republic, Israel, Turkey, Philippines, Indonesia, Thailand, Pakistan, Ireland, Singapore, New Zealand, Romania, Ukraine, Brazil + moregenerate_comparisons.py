#!/usr/bin/env python3
"""
USATaxRefund — Competitor Comparison Page Generator
Add any competitor to COMPARISONS list and run to generate pages.
Usage: python3 generate_comparisons.py
Output: ./generated/comparisons/
"""
import os, datetime

ALINK = "https://www.linkconnector.com/ta.php?lc=007949061588005142&atid=UsaTaxRefunds"
BASE  = "https://brightlane.github.io/UsaTaxRefund"
DATE  = datetime.date.today().isoformat()
OUT   = "generated/comparisons"
os.makedirs(OUT, exist_ok=True)

CSS = """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>:root{--blue:#003087;--blue2:#0050c8;--red:#cc0000;--gold:#f5a623;--dark:#0a0d14;--card:#111520;--border:#1e2540;--text:#eef0f8;--muted:#7a8aa8;--green:#00c853;}*{box-sizing:border-box;margin:0;padding:0;}body{font-family:Inter,sans-serif;background:var(--dark);color:var(--text);line-height:1.6;}nav{position:sticky;top:0;z-index:100;background:rgba(10,13,20,.96);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 28px;height:60px;}.logo{font-size:20px;font-weight:900;color:var(--text);text-decoration:none;}.logo span{color:var(--gold);}.nc{background:var(--red);color:#fff;padding:9px 20px;border-radius:8px;font-weight:700;font-size:13px;text-decoration:none;}.tk{background:var(--blue);overflow:hidden;white-space:nowrap;padding:8px 0;}.ti{display:inline-block;animation:tk 30s linear infinite;}.ti span{margin:0 36px;font-size:12px;font-weight:700;color:#fff;}@keyframes tk{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}.hero{background:linear-gradient(180deg,#1a0000 0%,var(--dark) 100%);padding:64px 24px 44px;text-align:center;border-bottom:1px solid var(--border);}.badge{display:inline-flex;align-items:center;gap:8px;background:rgba(204,0,0,.15);border:1px solid rgba(204,0,0,.4);color:#ff9999;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:6px 16px;border-radius:20px;margin-bottom:20px;}h1{font-size:clamp(26px,5vw,54px);font-weight:900;line-height:1.05;letter-spacing:-2px;margin-bottom:16px;}h1 em{color:var(--gold);font-style:normal;}.hs{color:var(--muted);font-size:16px;max-width:560px;margin:0 auto 28px;line-height:1.6;}.btn{background:var(--red);color:#fff;font-weight:800;padding:16px 36px;border-radius:10px;text-decoration:none;font-size:15px;display:inline-flex;align-items:center;gap:8px;}.s{padding:56px 24px;max-width:940px;margin:0 auto;}.ey{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:10px;}h2{font-size:clamp(20px,3vw,32px);font-weight:800;letter-spacing:-1px;margin-bottom:12px;}.sub{color:var(--muted);font-size:14px;margin-bottom:28px;}.cmp{width:100%;border-collapse:collapse;background:var(--card);border-radius:14px;overflow:hidden;border:1px solid var(--border);margin-bottom:24px;}.cmp th{padding:14px 18px;text-align:left;font-size:12px;font-weight:700;text-transform:uppercase;color:var(--muted);background:#0d1020;border-bottom:1px solid var(--border);}.cmp th.ef{color:#fff;background:var(--blue);}.cmp td{padding:13px 18px;font-size:14px;border-bottom:1px solid var(--border);color:#c0c8d8;}.cmp tr:last-child td{border-bottom:none;}.cmp td.feat{color:var(--muted);font-weight:500;}.cmp td.ef{color:#fff;font-weight:600;background:rgba(0,48,135,.12);}.win{color:var(--green);font-weight:700;}.lose{color:#ff5555;}.ok{color:var(--gold);}.cb{background:linear-gradient(135deg,#001a6e,#003087);border:1px solid rgba(0,80,200,.4);border-radius:14px;padding:40px 32px;text-align:center;margin:36px 0;}.cb h2{margin-bottom:10px;}.cb p{color:#a0b8e8;font-size:14px;margin-bottom:20px;}.fqs{display:flex;flex-direction:column;gap:10px;}.fq{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;}.fqq{font-weight:700;font-size:14px;margin-bottom:6px;}.fqa{color:var(--muted);font-size:13px;line-height:1.6;}footer{background:var(--card);border-top:1px solid var(--border);padding:20px 24px;text-align:center;font-size:12px;color:var(--muted);line-height:2;}@media(max-width:600px){.hero,.s{padding:40px 16px;}.cmp{font-size:12px;}.cmp th,.cmp td{padding:10px 12px;}}</style>"""

def cta(h, p):
    return f'<div class="cb"><h2>{h}</h2><p>{p}</p><a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored" style="font-size:16px;padding:17px 40px;display:inline-flex;">🚀 Switch to e-file.com — Free</a><p style="color:#7ab0ff;font-size:12px;margin-top:12px;">IRS Authorized · A+ BBB · 10-21 Day Refund · Free Federal</p></div>'

def faq(q, a):
    return f'<div class="fq"><div class="fqq">{q}</div><div class="fqa">{a}</div></div>'

def build(fname, title, desc, badge, h1, hs, body):
    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/{fname}">
{CSS}</head><body>
<nav><a class="logo" href="/UsaTaxRefund/"><span>🇺🇸</span> USATaxRefund</a><a class="nc" href="{ALINK}" target="_blank" rel="noopener sponsored">File Free →</a></nav>
<div class="tk"><div class="ti"><span>⚖️ COMPARISON GUIDE 2026</span><span>✅ 70% CHEAPER</span><span>🏛️ IRS AUTHORIZED</span><span>📋 1040-NR SUPPORTED</span><span>⭐ A+ BBB RATED</span><span>⚖️ COMPARISON GUIDE 2026</span></div></div>
<div class="hero"><div class="badge">{badge}</div><h1>{h1}</h1><p class="hs">{hs}</p>
<a class="btn" href="{ALINK}" target="_blank" rel="noopener sponsored">🚀 Switch to e-file.com — Free</a></div>
<div class="s">{body}
<p style="text-align:center;margin-top:28px;"><a href="/UsaTaxRefund/" style="color:var(--muted);font-size:13px;">← USATaxRefund Home</a></p></div>
<footer><p>USATaxRefund is an independent affiliate site earning commissions from e-file.com links.</p>
<p>Not tax or legal advice. e-file.com is IRS-authorized, A+ BBB rated since 2014. All trademarks belong to their respective owners.</p>
<p>© 2026 USATaxRefund · <a href="{ALINK}" style="color:var(--gold)">File Free →</a></p></footer>
</body></html>"""
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)
    return fname

# ════════════════════════════════════════════════════════════════════
# ADD COMPETITORS HERE
# Format:
#   slug           = filename without .html
#   competitor     = competitor name
#   their_price    = their federal filing price
#   our_price      = e-file.com price
#   nr_support     = do they support 1040-NR? "Yes" / "No" / "Limited"
#   free_file      = do they offer free filing? "Yes" / "No" / "Limited"
#   bbb            = their BBB rating
#   summary        = one sentence summary of the key difference
#   rows           = list of (feature, their_value, our_value) comparison rows
#   faqs           = list of (question, answer) tuples
# ════════════════════════════════════════════════════════════════════
COMPARISONS = [
    {
        "slug": "sprintax-vs-efile",
        "competitor": "Sprintax",
        "their_price": "$51.95+",
        "our_price": "$0 federal",
        "nr_support": "Yes",
        "free_file": "No",
        "bbb": "Not accredited",
        "summary": "Sprintax charges $51.95+ for a 1040-NR return and targets international students specifically. e-file.com supports 1040-NR at a fraction of the cost.",
        "rows": [
            ("Federal 1040-NR price",         "$51.95+",          "Free / low cost"),
            ("State filing",                  "$44.95+",          "$22.49"),
            ("IRS authorized",                "Yes",              "Yes"),
            ("BBB accredited",                "Not listed",       "A+ since 2014"),
            ("Free federal tier",             "No",               "Yes"),
            ("Supported visa types",          "F-1, J-1, H-1B",  "All visa types"),
            ("Treaty benefits applied",       "Yes",              "Yes"),
            ("Refund speed",                  "10-21 days",       "10-21 days"),
        ],
        "faqs": [
            ("Is Sprintax IRS authorized?", "Sprintax is an authorized IRS e-file provider for nonresident aliens. However, it charges $51.95+ for a federal 1040-NR return — significantly more than e-file.com. Both transmit returns to the IRS with equal authority."),
            ("Is e-file.com cheaper than Sprintax?", "Yes — e-file.com federal filing is free or very low cost, versus Sprintax at $51.95+ federal and $44.95+ state. For a complete return with state filing, e-file.com can save $70+ versus Sprintax."),
            ("Sprintax vs e-file.com for 1040-NR?", "Both support 1040-NR e-filing for nonresident aliens. The key difference is price — e-file.com is significantly cheaper. Both apply treaty benefits and support F-1, J-1 and H-1B filers."),
        ]
    },
    {
        "slug": "turbotax-vs-efile-nonresident",
        "competitor": "TurboTax",
        "their_price": "$69+",
        "our_price": "$0 federal",
        "nr_support": "No",
        "free_file": "Limited",
        "bbb": "A+",
        "summary": "TurboTax does not support Form 1040-NR at all. Nonresident aliens on F-1, J-1 or H-1B cannot file their US tax return with TurboTax. e-file.com is the IRS-authorized alternative.",
        "rows": [
            ("Supports Form 1040-NR",         "❌ No",             "✅ Yes"),
            ("Federal filing cost",           "$69+",             "Free for most"),
            ("State filing cost",             "$39+",             "$22.49"),
            ("IRS authorized",                "Yes",              "Yes"),
            ("BBB rating",                    "A+",               "A+ since 2014"),
            ("Free filing",                   "Very limited",     "Most returns free"),
            ("Upgrade screens",               "Yes — frequent",   "None"),
            ("Treaty benefits",               "N/A — no 1040-NR", "Applied correctly"),
        ],
        "faqs": [
            ("Can nonresident aliens use TurboTax?", "No — TurboTax does not support Form 1040-NR. If you are on an F-1, J-1, H-1B or other nonimmigrant visa and are a nonresident alien for tax purposes, you cannot file your US tax return with TurboTax. You must use an IRS-authorized platform that supports 1040-NR, such as e-file.com."),
            ("What happens if I file 1040 instead of 1040-NR?", "Filing the wrong form (1040 instead of 1040-NR) can result in IRS penalties, forfeited treaty benefits, and complications for future visa applications and green card petitions. Always file 1040-NR if you are a nonresident alien."),
            ("Is TurboTax good for US citizens but bad for nonresidents?", "TurboTax is a strong product for US citizens and resident aliens. However, it simply does not support Form 1040-NR. This is not a criticism of TurboTax for residents — it is just not the right tool for nonresident alien filers."),
        ]
    },
    {
        "slug": "hrblock-vs-efile",
        "competitor": "H&R Block",
        "their_price": "$35+",
        "our_price": "$0 federal",
        "nr_support": "No (online)",
        "free_file": "Limited",
        "bbb": "A+",
        "summary": "H&R Block online does not support 1040-NR e-filing. Their in-person service supports it but costs significantly more. e-file.com supports 1040-NR online at far lower cost.",
        "rows": [
            ("Online 1040-NR support",        "❌ No",             "✅ Yes"),
            ("Federal filing cost",           "$35+",             "Free for most"),
            ("State filing cost",             "$37+",             "$22.49"),
            ("IRS authorized",                "Yes",              "Yes"),
            ("BBB rating",                    "A+",               "A+ since 2014"),
            ("Upgrade screens",               "Yes",              "None"),
            ("Auto free-tier placement",      "No",               "Yes — automatic"),
            ("Treaty benefits (online)",      "N/A — no 1040-NR", "Applied correctly"),
        ],
        "faqs": [
            ("Can I file 1040-NR with H&R Block online?", "H&R Block's online platform does not support Form 1040-NR. Their in-person tax preparation service can handle 1040-NR returns, but costs significantly more — often $150-300+. e-file.com supports 1040-NR online at a fraction of that cost."),
            ("Is H&R Block cheaper than TurboTax?", "H&R Block is somewhat cheaper than TurboTax — federal starts at $35 vs TurboTax's $69. However, neither supports 1040-NR for nonresident aliens online. e-file.com at $0 federal is cheaper than both, and is one of the few platforms supporting 1040-NR e-filing."),
            ("H&R Block vs e-file.com for international students?", "For international students filing 1040-NR, e-file.com is the clear choice. H&R Block online does not support 1040-NR. e-file.com is IRS authorized, A+ BBB rated, and significantly cheaper than H&R Block in-person service."),
        ]
    },
    {
        "slug": "taxact-vs-efile",
        "competitor": "TaxAct",
        "their_price": "$49.99+",
        "our_price": "$0 federal",
        "nr_support": "No",
        "free_file": "Limited",
        "bbb": "A+",
        "summary": "TaxAct is cheaper than TurboTax but does not support 1040-NR e-filing for nonresident aliens. e-file.com supports 1040-NR and is IRS authorized.",
        "rows": [
            ("Supports Form 1040-NR",         "❌ No",             "✅ Yes"),
            ("Federal filing cost",           "$49.99+",          "Free for most"),
            ("State filing cost",             "$39.99+",          "$22.49"),
            ("IRS authorized",                "Yes",              "Yes"),
            ("BBB rating",                    "A+",               "A+ since 2014"),
            ("Free filing",                   "Limited",          "Most returns free"),
            ("Upgrade screens",               "Yes",              "None"),
        ],
        "faqs": [
            ("Can nonresident aliens use TaxAct?", "TaxAct does not support Form 1040-NR for nonresident aliens. If you are on an F-1, J-1, H-1B or other nonimmigrant visa filing as a nonresident alien, you need a platform that supports 1040-NR — such as e-file.com."),
            ("Is TaxAct cheaper than TurboTax?", "Yes — TaxAct federal starts at $49.99 vs TurboTax at $69. However, neither supports 1040-NR for nonresident aliens. e-file.com at free federal is cheaper than both and fully supports 1040-NR."),
            ("TaxAct vs e-file.com — which is better?", "For US citizens and residents, TaxAct is a reasonable affordable alternative to TurboTax. For nonresident aliens who need 1040-NR, e-file.com is the only choice of the two — TaxAct does not support 1040-NR."),
        ]
    },
    {
        "slug": "taxslayer-vs-efile",
        "competitor": "TaxSlayer",
        "their_price": "$34.95+",
        "our_price": "$0 federal",
        "nr_support": "No",
        "free_file": "Limited",
        "bbb": "A+",
        "summary": "TaxSlayer offers affordable filing for US residents but does not support 1040-NR for nonresident aliens. e-file.com fills this gap with full 1040-NR support at lower cost.",
        "rows": [
            ("Supports Form 1040-NR",         "❌ No",             "✅ Yes"),
            ("Federal filing cost",           "$34.95+",          "Free for most"),
            ("State filing cost",             "$39.95+",          "$22.49"),
            ("IRS authorized",                "Yes",              "Yes"),
            ("BBB rating",                    "A+",               "A+ since 2014"),
            ("Free filing",                   "Limited",          "Most returns free"),
        ],
        "faqs": [
            ("Can international students use TaxSlayer?", "TaxSlayer does not support Form 1040-NR for nonresident aliens. International students on F-1 and J-1 visas who must file 1040-NR cannot use TaxSlayer for their US tax return."),
            ("TaxSlayer vs e-file.com — price comparison?", "TaxSlayer federal starts at $34.95, state at $39.95. e-file.com is free federal for most returns, $22.49 state. e-file.com is cheaper and also supports 1040-NR which TaxSlayer does not."),
        ]
    },
    {
        "slug": "freetaxusa-vs-efile",
        "competitor": "FreeTaxUSA",
        "their_price": "$0 federal",
        "our_price": "$0 federal",
        "nr_support": "No",
        "free_file": "Yes",
        "bbb": "A+",
        "summary": "FreeTaxUSA offers free federal filing for US residents but does not support 1040-NR for nonresident aliens. e-file.com offers free federal filing AND 1040-NR support.",
        "rows": [
            ("Supports Form 1040-NR",         "❌ No",             "✅ Yes"),
            ("Federal filing cost",           "$0 free",          "$0 free"),
            ("State filing cost",             "$14.99",           "$22.49"),
            ("IRS authorized",                "Yes",              "Yes"),
            ("BBB rating",                    "A+",               "A+ since 2014"),
            ("1040-NR treaty benefits",       "N/A",              "Applied correctly"),
            ("Upgrade screens",               "None",             "None"),
        ],
        "faqs": [
            ("Can nonresidents use FreeTaxUSA?", "FreeTaxUSA does not support Form 1040-NR for nonresident aliens. It is a great free option for US citizens and resident aliens, but international students and visa holders who must file 1040-NR need to use e-file.com instead."),
            ("FreeTaxUSA vs e-file.com — which is cheaper for state?", "FreeTaxUSA charges $14.99 for state filing, while e-file.com charges $22.49. However, only e-file.com supports 1040-NR. For nonresident aliens, e-file.com is the only option of the two regardless of state filing price."),
            ("Is FreeTaxUSA legitimate?", "Yes — FreeTaxUSA is a legitimate IRS-authorized e-file provider with an A+ BBB rating. It is an excellent choice for US citizens and resident aliens filing standard 1040 returns. The limitation is simply that it does not support 1040-NR for nonresident aliens."),
        ]
    },
    {
        "slug": "glacier-tax-vs-efile",
        "competitor": "Glacier Tax Prep",
        "their_price": "$34.95+",
        "our_price": "$0 federal",
        "nr_support": "Yes",
        "free_file": "No",
        "bbb": "Not listed",
        "summary": "Glacier Tax Prep targets nonresident aliens and supports 1040-NR. However it charges $34.95+ and lacks e-file.com's IRS authorization transparency and A+ BBB accreditation.",
        "rows": [
            ("Supports 1040-NR",         "Yes",                "Yes"),
            ("Federal price",            "$34.95+",            "Free / low cost"),
            ("IRS authorized",           "Yes",                "Yes"),
            ("BBB accredited",           "Not prominently listed","A+ since 2014"),
            ("Free federal tier",        "No",                 "Yes for many"),
            ("State filing",             "Additional cost",    "$22.49"),
            ("Treaty benefits",          "Yes",                "Yes"),
        ],
        "faqs": [
            ("Glacier Tax Prep vs e-file.com for 1040-NR?", "Both Glacier Tax Prep and e-file.com support 1040-NR for nonresident aliens. The key difference is cost — e-file.com has a free federal tier while Glacier charges $34.95+. e-file.com also has an independently verified A+ BBB rating."),
            ("Is Glacier Tax Prep IRS authorized?", "Glacier Tax Prep is an IRS-authorized e-file provider for nonresident alien returns. It specifically targets F-1 and J-1 students. e-file.com is also IRS authorized and supports the same nonresident forms at lower cost."),
        ]
    },
    {
        "slug": "jackson-hewitt-vs-efile",
        "competitor": "Jackson Hewitt",
        "their_price": "$25+",
        "our_price": "$0 federal",
        "nr_support": "No (online)",
        "free_file": "No",
        "bbb": "A+",
        "summary": "Jackson Hewitt is a major tax preparation chain that does not support 1040-NR online. In-person service may support it but at significantly higher cost. e-file.com handles 1040-NR online.",
        "rows": [
            ("Online 1040-NR support",   "No",                 "Yes"),
            ("Federal price",            "$25+",               "Free for most"),
            ("State price",              "$20+",               "$22.49"),
            ("IRS authorized",           "Yes",                "Yes"),
            ("BBB rating",               "A+",                 "A+ since 2014"),
            ("Free federal tier",        "No",                 "Yes"),
            ("In-person option",         "Yes (more expensive)","Online only"),
        ],
        "faqs": [
            ("Can I file 1040-NR at Jackson Hewitt?", "Jackson Hewitt's online platform does not support Form 1040-NR. Their in-person tax preparation service may handle nonresident returns but at significantly higher cost — often $150-300+. e-file.com supports 1040-NR online at far lower cost."),
            ("Jackson Hewitt vs e-file.com for international students?", "For international students filing 1040-NR, e-file.com is the better choice. Jackson Hewitt online does not support 1040-NR, and their in-person service costs significantly more than e-file.com."),
        ]
    },
    {
        "slug": "creditkarma-tax-vs-efile",
        "competitor": "Cash App Taxes (Credit Karma)",
        "their_price": "$0",
        "our_price": "$0 federal",
        "nr_support": "No",
        "free_file": "Yes",
        "bbb": "A+",
        "summary": "Cash App Taxes (formerly Credit Karma Tax) offers free filing for US residents but does not support Form 1040-NR for nonresident aliens. e-file.com supports 1040-NR and is IRS authorized.",
        "rows": [
            ("Supports 1040-NR",         "No",                 "Yes"),
            ("Federal price",            "$0 free",            "$0 free"),
            ("State price",              "$0 free",            "$22.49"),
            ("IRS authorized",           "Yes",                "Yes"),
            ("BBB rating",               "A+",                 "A+ since 2014"),
            ("Treaty benefits",          "N/A — no 1040-NR",  "Applied correctly"),
        ],
        "faqs": [
            ("Can nonresidents use Cash App Taxes?", "No — Cash App Taxes (formerly Credit Karma Tax) does not support Form 1040-NR for nonresident aliens. It is a great free option for US citizens and resident aliens but cannot be used by F-1 or J-1 students who must file 1040-NR."),
            ("Cash App Taxes vs e-file.com — state filing price?", "Cash App Taxes is free for both federal and state for US residents. e-file.com charges $22.49 for state. However, only e-file.com supports 1040-NR — for nonresident aliens there is no comparison since Cash App Taxes cannot process their return at all."),
        ]
    },
    {
        "slug": "priortax-vs-efile",
        "competitor": "PriorTax",
        "their_price": "$49+",
        "our_price": "$0 federal",
        "nr_support": "Limited",
        "free_file": "No",
        "bbb": "A",
        "summary": "PriorTax supports some nonresident returns but charges $49+ and is primarily known for prior year tax return preparation. e-file.com is IRS authorized, A+ BBB, and significantly cheaper.",
        "rows": [
            ("1040-NR support",          "Limited",            "Full support"),
            ("Federal price",            "$49+",               "Free for most"),
            ("State price",              "Additional",         "$22.49"),
            ("IRS authorized",           "Yes",                "Yes"),
            ("BBB rating",               "A",                  "A+ since 2014"),
            ("Free federal tier",        "No",                 "Yes"),
            ("Current year filing",      "Yes",                "Yes"),
            ("Prior year filing",        "Yes (specialty)",    "Limited"),
        ],
        "faqs": [
            ("PriorTax vs e-file.com for 1040-NR?", "PriorTax offers some nonresident support but charges $49+ per return. e-file.com is IRS authorized, A+ BBB rated, free federal filing, and fully supports 1040-NR. For current year nonresident filing, e-file.com is the better value."),
            ("Is PriorTax good for filing back taxes?", "PriorTax specializes in prior year tax returns and may be useful for catching up on unfiled returns from previous years. For current year 1040-NR filing, e-file.com is more cost-effective."),
        ]
    },
    {
        "slug": "liberty-tax-vs-efile",
        "competitor": "Liberty Tax",
        "their_price": "$45+",
        "our_price": "$0 federal",
        "nr_support": "No (online)",
        "free_file": "No",
        "bbb": "A+",
        "summary": "Liberty Tax is a national tax preparation chain. Their online service does not support 1040-NR. In-person may handle nonresident returns at higher cost. e-file.com handles 1040-NR online affordably.",
        "rows": [
            ("Online 1040-NR support",   "No",                 "Yes"),
            ("Federal price",            "$45+",               "Free for most"),
            ("State price",              "Additional",         "$22.49"),
            ("IRS authorized",           "Yes",                "Yes"),
            ("BBB rating",               "A+",                 "A+ since 2014"),
            ("Free federal tier",        "No",                 "Yes"),
        ],
        "faqs": [
            ("Can I file 1040-NR at Liberty Tax?", "Liberty Tax online does not support Form 1040-NR. In-person Liberty Tax locations may handle nonresident returns but at significantly higher cost. e-file.com supports 1040-NR fully online at a fraction of in-person tax preparation costs."),
            ("Liberty Tax vs e-file.com for price?", "Liberty Tax starts at $45+ online for residents. e-file.com is free for most federal returns. For nonresident aliens who must file 1040-NR, e-file.com is the only online option of the two."),
        ]
    },

    # ── ADD MORE COMPETITORS BELOW ────────────────────────────────────
    # {
    #     "slug": "competitor-vs-efile",
    #     "competitor": "CompetitorName",
    #     "their_price": "$XX+",
    #     "our_price": "$0 federal",
    #     "nr_support": "No",
    #     "free_file": "No",
    #     "bbb": "A+",
    #     "summary": "One sentence summary.",
    #     "rows": [("Feature", "Their value", "Our value"), ...],
    #     "faqs": [("Question", "Answer"), ...],
    # },
]

generated = []
for comp in COMPARISONS:
    slug = comp["slug"]
    c = comp["competitor"]
    tp = comp["their_price"]
    nr = comp["nr_support"]

    table_rows = "".join(f"""<tr><td class="feat">{r[0]}</td><td class="ef {'win' if '✅' in r[2] or 'Free' in r[2] or 'free' in r[2] else ''}">{r[2]}</td><td class="{'lose' if '❌' in r[1] or '$69' in r[1] or '$51' in r[1] else 'ok'}">{r[1]}</td></tr>""" for r in comp["rows"])

    faqs_html = "".join(faq(q, a) for q, a in comp["faqs"])

    body = f"""<div style="background:#1a0800;border:1px solid rgba(245,166,35,.4);border-radius:12px;padding:20px;margin:16px 0;">
<h4 style="color:var(--gold);font-size:14px;font-weight:700;margin-bottom:6px;">⚖️ The Key Difference</h4>
<p style="color:#c0b080;font-size:13px;line-height:1.6;margin:0;">{comp["summary"]}</p></div>
<div class="ey">Full Comparison</div>
<h2>{c} vs e-file.com — Feature by Feature</h2>
<p style="color:var(--muted);font-size:14px;margin-bottom:20px;">Honest side-by-side comparison for 2026 tax filing.</p>
<table class="cmp">
<thead><tr><th>Feature</th><th class="ef">✅ e-file.com</th><th>{c}</th></tr></thead>
<tbody>{table_rows}</tbody>
</table>
{cta(f"Switch from {c} to e-file.com",f"IRS authorized · A+ BBB · Free federal filing · 1040-NR supported · No upgrade screens")}
<div class="ey">FAQ</div><h2 style="margin-bottom:20px;">{c} vs e-file.com — FAQ</h2>
<div class="fqs">{faqs_html}</div>"""

    fname = build(f"{slug}.html",
        f"{c} vs e-file.com 2026 — Which is Better for 1040-NR?",
        f"Comparing {c} vs e-file.com for US tax filing in 2026. e-file.com {'supports 1040-NR for nonresidents. ' if nr == 'No' else ''}is IRS authorized, A+ BBB rated, and {'free federal filing' if comp['our_price'] == '$0 federal' else 'cheaper'}. {comp['summary']}",
        f"⚖️ {c} vs e-file.com 2026",
        f"{c} vs e-file.com — <em>Which to Choose?</em>",
        f"{comp['summary']} Here is the complete honest comparison for 2026.",
        body)
    generated.append(fname)
    print(f"✅ {fname}")

print(f"\n✅ Done — {len(generated)} comparison pages in ./{OUT}/")

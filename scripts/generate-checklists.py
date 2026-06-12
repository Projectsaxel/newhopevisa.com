#!/usr/bin/env python3
"""New Hope Visa — Checklist Generator v2 (Jun 2026)
Generates 5 interactive HTML checklist pages under /en/blog/{cluster}/checklist/
"""
import os, json

OUT = "/tmp/nhv-push/en/blog"

CHECKLISTS = [
    {
        "cluster": "adjustment-of-status",
        "cluster_name": "Adjustment of Status",
        "title": "Adjustment of Status (I-485) Document Checklist",
        "meta": "Interactive checklist for your I-485 adjustment of status application — track every document you need for your Green Card case.",
        "wa_msg": "Hi! I'm working through your Adjustment of Status (I-485) document checklist on newhopevisa.com and I'd like to schedule a consultation to review my documents.",
        "categories": [
            ("Core Forms", [
                "Form I-485 completed and signed",
                "Form I-864 (Affidavit of Support) completed by petitioner",
                "Form I-765 (Employment Authorization) — optional but recommended",
                "Form I-131 (Advance Parole) — if you may need to travel",
                "Correct USCIS filing fee payment",
            ]),
            ("Identity & Civil Documents", [
                "Birth certificate (original + certified English translation)",
                "Valid passport (all pages, all passports)",
                "Form I-94 printout from cbp.dhs.gov",
                "Marriage certificate (if applicable, + translation)",
                "Divorce decree(s) for all prior marriages",
                "Children's birth certificates (if applicable)",
            ]),
            ("Medical Exam", [
                "Form I-693 signed by USCIS-designated civil surgeon",
                "Vaccination records (given or updated by civil surgeon)",
                "I-693 in sealed envelope — DO NOT OPEN",
                "Appointment scheduled with designated civil surgeon",
            ]),
            ("Evidence of Status", [
                "Copy of approved I-130 or I-140 (petition approval notice)",
                "Proof of most recent lawful entry into the U.S.",
                "All prior visa documents and immigration notices",
                "Two recent passport-style photos (if filing by mail)",
            ]),
            ("Affidavit of Support (I-864)", [
                "Sponsor's last 3 years of federal tax returns or IRS transcripts",
                "Most recent W-2s or 1099s",
                "Current pay stubs or employer letter with salary",
                "Bank statements (if supplementing income)",
                "Proof of U.S. citizenship or permanent residence of sponsor",
            ]),
            ("If Applying as a Married Couple", [
                "Evidence of joint financial life (bank accounts, credit cards)",
                "Joint lease or mortgage documents",
                "Joint utility bills or insurance policies",
                "Photos together (at different events and dates)",
                "Joint tax returns if filed together",
                "Affidavits from friends/family who know the couple",
            ]),
        ]
    },
    {
        "cluster": "naturalization",
        "cluster_name": "Naturalization",
        "title": "Naturalization (N-400) Document Checklist",
        "meta": "Interactive checklist for your N-400 citizenship application — track every document needed for U.S. naturalization.",
        "wa_msg": "Hi! I'm working through your Naturalization (N-400) document checklist on newhopevisa.com and I'd like to schedule a consultation about my citizenship application.",
        "categories": [
            ("Core Forms & Fees", [
                "Form N-400 completed and signed",
                "Correct USCIS filing fee ($760 as of 2025 — verify at uscis.gov)",
                "Two passport-style photos (if filing by mail)",
            ]),
            ("Permanent Residence Evidence", [
                "Copy of current Green Card (front and back)",
                "Copies of all prior Green Cards held",
                "Copy of I-94 if applicable",
            ]),
            ("Identity Documents", [
                "Copy of valid passport (all passports held)",
                "State-issued ID or driver's license",
            ]),
            ("Travel History", [
                "List of all trips outside U.S. during past 5 years (dates, countries, purpose)",
                "Passport copies showing entry/exit stamps",
                "Any re-entry permits used",
            ]),
            ("Tax Returns", [
                "Federal income tax returns for past 5 years (or 3 for spousal path)",
                "IRS transcripts if returns unavailable",
                "Statement explaining any years not filed (if applicable)",
            ]),
            ("Marital Status Documents", [
                "Marriage certificate (if married)",
                "All divorce decrees (if previously married)",
                "Spouse's proof of U.S. citizenship (if applying under 3-year rule)",
                "Joint evidence of marital life (3-year rule applicants)",
            ]),
            ("Criminal & Immigration History", [
                "Certified court dispositions for all arrests/charges",
                "Immigration court records (if any proceedings occurred)",
                "Selective Service registration proof (males born 1960–2003)",
            ]),
        ]
    },
    {
        "cluster": "removal-of-conditions",
        "cluster_name": "Removal of Conditions",
        "title": "Removal of Conditions (I-751) Document Checklist",
        "meta": "Interactive checklist for your I-751 petition to remove conditions — gather every document needed for your joint filing or waiver.",
        "wa_msg": "Hi! I'm working through your Removal of Conditions (I-751) document checklist on newhopevisa.com and I need help gathering evidence for my case.",
        "categories": [
            ("Core Forms & Fees", [
                "Form I-751 completed and signed by both spouses (joint filing)",
                "Correct USCIS filing fee (verify current amount at uscis.gov)",
                "Copy of conditional Green Card (front and back)",
                "Cover letter summarizing evidence",
            ]),
            ("Evidence of Bona Fide Marriage — Financial", [
                "Joint bank account statements (12+ months)",
                "Joint credit card statements",
                "Joint tax returns (IRS Form 1040 filed jointly)",
                "Joint mortgage or lease in both names",
                "Joint utility bills (electricity, water, gas, phone)",
                "Joint car or home insurance policies",
            ]),
            ("Evidence of Bona Fide Marriage — Personal", [
                "Photos together (chronological, different events and dates)",
                "Photos with each other's families",
                "Communication records (emails, texts, travel together)",
                "Evidence of shared social activities",
                "Records of joint travel",
            ]),
            ("Statements & Affidavits", [
                "Personal statement from petitioner (your story of the marriage)",
                "Personal statement from U.S. spouse",
                "Affidavits from 2–4 people who know you as a couple",
                "Children's birth certificates (if children born of marriage)",
            ]),
            ("Identity Documents", [
                "Copy of both spouses' passports",
                "Marriage certificate with certified translation if applicable",
                "I-94 arrival record",
            ]),
            ("If Filing a Waiver (No Joint Filing)", [
                "Divorce decree (waiver for divorce)",
                "Death certificate of spouse (waiver for death)",
                "Police reports / protective orders (abuse waiver)",
                "Medical records documenting abuse (abuse waiver)",
                "Statements from domestic violence advocates or social workers (abuse waiver)",
                "Detailed personal declaration of abuse (abuse waiver)",
            ]),
        ]
    },
    {
        "cluster": "green-card-renewal",
        "cluster_name": "Green Card Renewal",
        "title": "Green Card Renewal (I-90) Document Checklist",
        "meta": "Interactive checklist for your Form I-90 Green Card renewal or replacement application.",
        "wa_msg": "Hi! I'm working through your Green Card Renewal (I-90) document checklist on newhopevisa.com and I'd like help filing my renewal.",
        "categories": [
            ("Core Forms & Fees", [
                "Form I-90 completed (online at my.uscis.gov or paper)",
                "Correct USCIS filing fee ($455 + $85 biometrics as of 2025)",
                "Reason for filing selected (renewal, replacement, correction)",
            ]),
            ("Identity & Immigration Documents", [
                "Copy of current or expired Green Card (front and back)",
                "Copy of valid passport",
                "I-94 Arrival/Departure record printout",
                "Any prior Green Cards",
            ]),
            ("If Replacing a Lost/Stolen Card", [
                "Police report (if card was stolen)",
                "Written explanation of circumstances of loss",
                "FTC identity theft report (if identity may be compromised)",
            ]),
            ("If Correcting an Error on the Card", [
                "Documentation showing correct information (birth certificate, passport)",
                "Written explanation of the USCIS error",
            ]),
            ("Two Passport-Style Photos", [
                "Two recent passport-style photos (if filing by mail)",
                "Photos meet USCIS requirements (white background, 2x2 inches)",
            ]),
        ]
    },
    {
        "cluster": "student-visa",
        "cluster_name": "Student Visa",
        "title": "F-1 Student Visa Document Checklist",
        "meta": "Interactive checklist for your F-1 student visa application — from school acceptance to visa interview and maintaining status.",
        "wa_msg": "Hi! I'm working through your F-1 Student Visa document checklist on newhopevisa.com and I need help with my application.",
        "categories": [
            ("Before You Apply — Getting Your I-20", [
                "Acceptance letter from SEVP-certified U.S. school",
                "Form I-20 issued by school's DSO",
                "SEVIS ID number from I-20",
                "SEVIS fee paid ($350 at fmjfee.com — keep receipt)",
            ]),
            ("Visa Application Documents", [
                "DS-160 form completed online at ceac.state.gov",
                "Valid passport (valid at least 6 months beyond intended stay)",
                "One passport-style photo per DS-160 requirements",
                "Visa application fee receipt (MRV fee — amount varies by country)",
                "SEVIS fee receipt I-901",
                "Form I-20 (original, signed by DSO and applicant)",
            ]),
            ("Financial Evidence", [
                "Bank statements showing sufficient funds (covering 1+ year of tuition + living)",
                "Scholarship or financial aid award letter (if applicable)",
                "Sponsor's bank statements and income evidence",
                "Affidavit of financial support from sponsor (if applicable)",
            ]),
            ("Ties to Home Country", [
                "Evidence of strong ties to home country (property, family, job offer)",
                "Explanation of study plans and intent to return home after studies",
            ]),
            ("If Already in the U.S. (Change of Status)", [
                "Current visa and I-94 showing valid nonimmigrant status",
                "Form I-539 (Application to Extend/Change Nonimmigrant Status)",
                "I-539 filing fee",
                "Proof of current status maintenance",
            ]),
            ("Maintaining F-1 Status — Ongoing", [
                "Keep I-20 updated and signed for travel",
                "Report address changes to DSO within 10 days",
                "Enroll full-time every semester",
                "Obtain CPT/OPT authorization before any off-campus work",
                "Renew passport before it expires",
            ]),
        ]
    },
]

CSS = """<link rel="stylesheet" href="/wp-content/themes/hello-elementor/style.min.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;}
body{margin:0;font-family:'Manrope',sans-serif;color:#1e293b;background:#fff;}
.nhv-cl-wrap{max-width:820px;margin:0 auto;padding:40px 20px 80px;}
.nhv-breadcrumb{font-size:13px;color:#64748b;margin-bottom:24px;}
.nhv-breadcrumb a{color:#64748b;text-decoration:none;}
.nhv-cl-header{margin-bottom:40px;}
.nhv-cl-header h1{font-size:clamp(24px,4vw,36px);font-weight:900;color:#0f172a;margin:0 0 12px;}
.nhv-progress-bar{background:#e2e8f0;border-radius:99px;height:10px;margin:24px 0 8px;overflow:hidden;}
.nhv-progress-fill{background:#469A3D;height:100%;width:0%;border-radius:99px;transition:width .3s;}
#nhv-progress-label{font-size:14px;color:#64748b;margin:0 0 32px;}
.nhv-category{margin-bottom:36px;}
.nhv-category h2{font-size:18px;font-weight:800;color:#0f172a;margin:0 0 16px;padding-bottom:8px;border-bottom:2px solid #e2e8f0;}
.nhv-item{display:flex;align-items:flex-start;gap:12px;padding:10px 0;border-bottom:1px solid #f1f5f9;}
.nhv-item:last-child{border-bottom:none;}
.nhv-item input[type=checkbox]{width:20px;height:20px;margin-top:2px;accent-color:#469A3D;cursor:pointer;flex-shrink:0;}
.nhv-item label{font-size:15px;line-height:1.6;cursor:pointer;color:#374151;}
.nhv-item.checked label{color:#94a3b8;text-decoration:line-through;}
.nhv-cta-box{background:linear-gradient(135deg,#469A3D,#357a2f);color:#fff;border-radius:16px;padding:32px 36px;margin:48px 0;text-align:center;}
.nhv-cta-box h3{font-size:20px;font-weight:800;margin:0 0 10px;color:#fff;}
.nhv-cta-box p{margin:0 0 20px;font-size:15px;opacity:.92;}
.nhv-cta-box a{display:inline-block;background:#fff;color:#469A3D;font-weight:800;padding:12px 28px;border-radius:9px;text-decoration:none;font-size:15px;margin:4px;}
.nhv-wa-cta{background:#25D366;border-radius:16px;padding:28px 32px;text-align:center;margin:32px 0;}
.nhv-wa-cta a{display:inline-block;color:#fff;font-weight:800;font-size:16px;text-decoration:none;}
</style>"""

NAV = """<nav style="background:#fff;border-bottom:1px solid #e2e8f0;padding:0 20px;">
  <div style="max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:64px;">
    <a href="/en/" style="display:flex;align-items:center;gap:10px;text-decoration:none;">
      <img src="/wp-content/uploads/2023/06/new-hope-logo.png" alt="New Hope Immigration Services" style="height:40px;" onerror="this.style.display='none'">
      <span style="font-weight:800;font-size:18px;color:#0f172a;font-family:'Manrope',sans-serif;">New Hope Immigration</span>
    </a>
    <div style="display:flex;gap:24px;font-family:'Manrope',sans-serif;font-size:14px;font-weight:600;">
      <a href="/en/services/" style="color:#475569;text-decoration:none;">Services</a>
      <a href="/en/blog/" style="color:#469A3D;text-decoration:none;">Blog</a>
      <a href="/en/contact-us/" style="color:#fff;background:#469A3D;padding:8px 18px;border-radius:8px;text-decoration:none;">Contact</a>
    </div>
  </div>
</nav>"""

FOOTER = """<footer style="background:#0f172a;color:#94a3b8;padding:40px 20px 28px;font-family:'Manrope',sans-serif;margin-top:0;">
  <div style="max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:32px;margin-bottom:32px;">
    <div style="flex:2;min-width:200px;">
      <p style="font-weight:800;color:#fff;margin:0 0 6px;">New Hope Immigration Services</p>
      <p style="font-size:13px;margin:0 0 3px;">4300 Lake Margaret Dr, Orlando, FL 32812</p>
      <p style="font-size:13px;margin:0;"><a href="tel:+14072756163" style="color:#94a3b8;text-decoration:none;">(407) 275-6163</a> · <a href="mailto:nhois@ineorlando.org" style="color:#94a3b8;text-decoration:none;">nhois@ineorlando.org</a></p>
    </div>
    <div style="flex:1;min-width:140px;font-size:13px;">
      <p style="font-weight:700;color:#e2e8f0;margin:0 0 10px;">Blog</p>
      <p style="margin:0 0 6px;"><a href="/en/blog/adjustment-of-status/" style="color:#94a3b8;text-decoration:none;">Adjustment of Status</a></p>
      <p style="margin:0 0 6px;"><a href="/en/blog/naturalization/" style="color:#94a3b8;text-decoration:none;">Naturalization</a></p>
      <p style="margin:0 0 6px;"><a href="/en/blog/green-card-renewal/" style="color:#94a3b8;text-decoration:none;">Green Card Renewal</a></p>
    </div>
  </div>
  <div style="border-top:1px solid #1e293b;padding-top:20px;font-size:12px;text-align:center;">
    © 2024 New Hope Immigration Services. DOJ-accredited nonprofit. Not a law firm.
  </div>
</footer>"""

GA = """<script async src="https://www.googletagmanager.com/gtag/js?id=GT-K8DVG7VR"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','GT-K8DVG7VR');</script>"""

def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

generated = 0
for cl in CHECKLISTS:
    cslug = cl["cluster"]
    cname = cl["cluster_name"]
    url = f"/en/blog/{cslug}/checklist/"
    out_path = f"{OUT}/{cslug}/checklist/index.html"

    # Build checkbox items with IDs
    all_items = []
    cat_html = ""
    item_idx = 0
    for cat_name, items in cl["categories"]:
        cat_html += f'<div class="nhv-category"><h2>{cat_name}</h2>\n'
        for item_text in items:
            iid = f"chk-{item_idx}"
            cat_html += f'''<div class="nhv-item" id="row-{item_idx}">
  <input type="checkbox" id="{iid}" data-idx="{item_idx}" onchange="nhvCheck(this)">
  <label for="{iid}">{item_text}</label>
</div>\n'''
            all_items.append(item_text)
            item_idx += 1
        cat_html += '</div>\n'

    total = len(all_items)
    wa_href = "https://wa.me/14072756163?text=" + cl["wa_msg"].replace(" ", "%20").replace("'", "%27").replace("!", "%21").replace("(", "%28").replace(")", "%29").replace(".", "%2E")

    # HowTo schema
    how_to_steps = []
    for cat_name, items in cl["categories"]:
        for item_text in items:
            how_to_steps.append({"@type":"HowToStep","text":item_text})
    howto_schema = json.dumps({
        "@context":"https://schema.org","@type":"HowTo",
        "name":cl["title"],
        "description":cl["meta"],
        "step":how_to_steps[:10]  # schema limit sensible
    }, indent=2)

    js = f"""<script>
var STORAGE_KEY = 'nhv-cl-{cslug}';
var TOTAL = {total};

function nhvCheck(el) {{
  var idx = el.dataset.idx;
  var row = document.getElementById('row-' + idx);
  if (el.checked) row.classList.add('checked');
  else row.classList.remove('checked');
  saveState();
  updateProgress();
}}

function saveState() {{
  var state = {{}};
  document.querySelectorAll('input[type=checkbox]').forEach(function(c) {{
    state[c.dataset.idx] = c.checked;
  }});
  try {{ localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }} catch(e) {{}}
}}

function loadState() {{
  try {{
    var state = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{{}}');
    Object.keys(state).forEach(function(idx) {{
      var el = document.querySelector('[data-idx="'+idx+'"]');
      if (el && state[idx]) {{
        el.checked = true;
        document.getElementById('row-'+idx).classList.add('checked');
      }}
    }});
  }} catch(e) {{}}
}}

function updateProgress() {{
  var checked = document.querySelectorAll('input[type=checkbox]:checked').length;
  var pct = Math.round((checked / TOTAL) * 100);
  document.querySelector('.nhv-progress-fill').style.width = pct + '%';
  document.getElementById('nhv-progress-label').textContent = checked + ' of ' + TOTAL + ' items checked (' + pct + '% complete)';
}}

document.addEventListener('DOMContentLoaded', function() {{
  loadState();
  updateProgress();
}});
</script>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{cl["title"]} | New Hope Immigration</title>
<meta name="description" content="{cl["meta"]}">
<link rel="canonical" href="https://newhopevisa.com{url}">
{CSS}
{GA}
</head>
<body>
{NAV}
<main>
  <div style="background:#f8fafc;border-bottom:1px solid #e2e8f0;padding:12px 20px;">
    <div style="max-width:820px;margin:0 auto;">
      <p class="nhv-breadcrumb"><a href="/en/">Home</a> › <a href="/en/blog/">Blog</a> › <a href="/en/blog/{cslug}/">{cname}</a> › Checklist</p>
    </div>
  </div>
  <div class="nhv-cl-wrap">
    <header class="nhv-cl-header">
      <div style="display:inline-block;background:#f0faf0;color:#469A3D;font-weight:700;padding:4px 12px;border-radius:20px;font-size:13px;margin-bottom:12px;">{cname}</div>
      <h1>{cl["title"]}</h1>
      <p style="font-size:16px;color:#475569;margin:0;">Track your progress by checking off each item as you gather it. Your progress is saved automatically.</p>
    </header>

    <div class="nhv-progress-bar"><div class="nhv-progress-fill"></div></div>
    <p id="nhv-progress-label">0 of {total} items checked</p>

    <div class="nhv-wa-cta">
      <p style="color:#fff;font-size:15px;margin:0 0 12px;font-weight:600;">Have questions while reviewing your documents?</p>
      <a href="{wa_href}" target="_blank" rel="noopener">💬 Ask us on WhatsApp</a>
    </div>

    {cat_html}

    <div class="nhv-cta-box">
      <h3>Ready to Review Your Documents?</h3>
      <p>Schedule a $50 consultation and our DOJ-accredited team will review your case in Orlando or online.</p>
      <a href="/en/contact-us/?src=checklist-{cslug}">Book a Consultation →</a>
      <a href="tel:+14072756163">Call (407) 275-6163</a>
    </div>

    <p style="text-align:center;margin-top:24px;"><a href="/en/blog/{cslug}/" style="color:#469A3D;font-weight:700;">← Back to {cname} Guides</a></p>
  </div>
</main>
{FOOTER}
<script type="application/ld+json">{howto_schema}</script>
{js}
<script src="/exit-popup.js" defer></script>
</body></html>"""

    write(out_path, html)
    generated += 1
    print(f"OK: /en/blog/{cslug}/checklist/ ({total} items)")

print(f"\nGenerated {generated} checklist pages")

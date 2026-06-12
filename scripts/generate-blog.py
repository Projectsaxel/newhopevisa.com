#!/usr/bin/env python3
"""New Hope Visa — Blog Generator v2  (Jun 2026)
Generates: 1 index + 5 hub pages + 25 articles = 31 HTML files
Output: /tmp/nhv-push/en/blog/
"""
import os, json, textwrap

OUT = "/tmp/nhv-push/en/blog"

# ── shared head / foot helpers ────────────────────────────────────────────────
NAV = """<nav class="nhv-blog-nav" style="background:#fff;border-bottom:1px solid #e2e8f0;padding:0 20px;">
  <div style="max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:64px;">
    <a href="/en/" style="display:flex;align-items:center;gap:10px;text-decoration:none;">
      <img src="/wp-content/uploads/2023/06/new-hope-logo.png" alt="New Hope Immigration Services" style="height:40px;" onerror="this.style.display='none'">
      <span style="font-weight:800;font-size:18px;color:#0f172a;font-family:'Manrope',sans-serif;">New Hope Immigration</span>
    </a>
    <div style="display:flex;gap:24px;font-family:'Manrope',sans-serif;font-size:14px;font-weight:600;">
      <a href="/en/services/" style="color:#475569;text-decoration:none;">Services</a>
      <a href="/en/blog/" style="color:#469A3D;text-decoration:none;">Blog</a>
      <a href="/en/about-us/" style="color:#475569;text-decoration:none;">About</a>
      <a href="/en/contact-us/" style="color:#fff;background:#469A3D;padding:8px 18px;border-radius:8px;text-decoration:none;">Contact</a>
    </div>
  </div>
</nav>"""

FOOTER = """<footer style="background:#0f172a;color:#94a3b8;padding:48px 20px 32px;font-family:'Manrope',sans-serif;margin-top:0;">
  <div style="max-width:1100px;margin:0 auto;">
    <div style="display:flex;flex-wrap:wrap;gap:40px;margin-bottom:40px;">
      <div style="flex:2;min-width:220px;">
        <p style="font-weight:800;font-size:18px;color:#fff;margin:0 0 8px;">New Hope Immigration Services</p>
        <p style="font-size:14px;margin:0 0 4px;">4300 Lake Margaret Dr, Orlando, FL 32812</p>
        <p style="font-size:14px;margin:0 0 4px;"><a href="tel:+14072756163" style="color:#94a3b8;text-decoration:none;">(407) 275-6163</a></p>
        <p style="font-size:14px;margin:0;"><a href="mailto:nhois@ineorlando.org" style="color:#94a3b8;text-decoration:none;">nhois@ineorlando.org</a></p>
      </div>
      <div style="flex:1;min-width:160px;">
        <p style="font-weight:700;color:#e2e8f0;margin:0 0 12px;">Services</p>
        <p style="margin:0 0 8px;font-size:14px;"><a href="/en/adjustment-of-status/" style="color:#94a3b8;text-decoration:none;">Adjustment of Status</a></p>
        <p style="margin:0 0 8px;font-size:14px;"><a href="/en/naturalization/" style="color:#94a3b8;text-decoration:none;">Naturalization</a></p>
        <p style="margin:0 0 8px;font-size:14px;"><a href="/en/residence-renewals-i-90/" style="color:#94a3b8;text-decoration:none;">Green Card Renewal</a></p>
        <p style="margin:0 0 8px;font-size:14px;"><a href="/en/family-petitions/" style="color:#94a3b8;text-decoration:none;">Family Petitions</a></p>
      </div>
      <div style="flex:1;min-width:160px;">
        <p style="font-weight:700;color:#e2e8f0;margin:0 0 12px;">Resources</p>
        <p style="margin:0 0 8px;font-size:14px;"><a href="/en/blog/" style="color:#94a3b8;text-decoration:none;">Blog</a></p>
        <p style="margin:0 0 8px;font-size:14px;"><a href="/en/fee-schedule/" style="color:#94a3b8;text-decoration:none;">Fee Schedule</a></p>
        <p style="margin:0 0 8px;font-size:14px;"><a href="/en/about-us/" style="color:#94a3b8;text-decoration:none;">About Us</a></p>
        <p style="margin:0 0 8px;font-size:14px;"><a href="/en/contact-us/" style="color:#94a3b8;text-decoration:none;">Contact</a></p>
      </div>
    </div>
    <div style="border-top:1px solid #1e293b;padding-top:24px;display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;align-items:center;font-size:13px;">
      <p style="margin:0;">© 2024 New Hope Immigration Services. DOJ-accredited nonprofit. Not a law firm.</p>
      <div style="display:flex;gap:16px;">
        <a href="/en/privacy-policy/" style="color:#64748b;text-decoration:none;">Privacy</a>
        <a href="/en/terms-of-use/" style="color:#64748b;text-decoration:none;">Terms</a>
        <a href="/en/cookie-policy/" style="color:#64748b;text-decoration:none;">Cookies</a>
      </div>
    </div>
  </div>
</footer>"""

CSS = """<link rel="stylesheet" href="/wp-content/themes/hello-elementor/style.min.css">
<link rel="stylesheet" href="/wp-content/plugins/elementor/assets/css/frontend.min.css">
<style>
*{box-sizing:border-box;}
body{margin:0;font-family:'Manrope',sans-serif;color:#1e293b;background:#fff;line-height:1.7;}
a{color:#469A3D;}
.nhv-blog-wrap{max-width:820px;margin:0 auto;padding:40px 20px 80px;}
.nhv-breadcrumb{font-size:13px;color:#64748b;margin-bottom:24px;}
.nhv-breadcrumb a{color:#64748b;text-decoration:none;}
.nhv-breadcrumb a:hover{color:#469A3D;}
.nhv-article-header{margin-bottom:40px;}
.nhv-article-header h1{font-size:clamp(26px,4vw,38px);font-weight:900;color:#0f172a;margin:0 0 16px;line-height:1.25;}
.nhv-article-meta{display:flex;flex-wrap:wrap;gap:16px;align-items:center;font-size:14px;color:#64748b;}
.nhv-badge{background:#f0faf0;color:#469A3D;font-weight:700;padding:4px 12px;border-radius:20px;font-size:13px;}
.nhv-article-body h2{font-size:24px;font-weight:800;color:#0f172a;margin:40px 0 16px;}
.nhv-article-body h3{font-size:19px;font-weight:700;color:#0f172a;margin:28px 0 12px;}
.nhv-article-body p{margin:0 0 18px;font-size:16px;line-height:1.8;}
.nhv-article-body ul,.nhv-article-body ol{margin:0 0 18px;padding-left:24px;}
.nhv-article-body li{margin-bottom:8px;font-size:16px;line-height:1.7;}
.nhv-cta-box{background:linear-gradient(135deg,#469A3D,#357a2f);color:#fff;border-radius:16px;padding:32px 36px;margin:48px 0;text-align:center;}
.nhv-cta-box h3{font-size:22px;font-weight:800;margin:0 0 10px;color:#fff;}
.nhv-cta-box p{margin:0 0 20px;font-size:15px;opacity:.92;}
.nhv-cta-box a{display:inline-block;background:#fff;color:#469A3D;font-weight:800;padding:13px 32px;border-radius:9px;text-decoration:none;font-size:15px;}
.nhv-cta-box a:hover{background:#f0fdf4;}
.nhv-faq-item{border-bottom:1px solid #e2e8f0;padding:20px 0;}
.nhv-faq-item h3{font-size:17px;font-weight:700;color:#0f172a;margin:0 0 10px;}
.nhv-faq-item p{margin:0;font-size:15px;color:#475569;}
.nhv-related-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;margin-top:24px;}
.nhv-related-card{background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:18px;text-decoration:none;display:block;transition:border-color .15s;}
.nhv-related-card:hover{border-color:#469A3D;}
.nhv-related-card span{display:block;font-size:13px;color:#64748b;margin-bottom:6px;}
.nhv-related-card strong{display:block;font-size:15px;font-weight:700;color:#0f172a;line-height:1.4;}
.nhv-hub-hero{background:linear-gradient(135deg,#0f172a,#1e3a2f);color:#fff;padding:80px 20px;text-align:center;}
.nhv-hub-hero h1{font-size:clamp(28px,5vw,46px);font-weight:900;margin:0 0 16px;}
.nhv-hub-hero p{font-size:18px;opacity:.85;max-width:640px;margin:0 auto;}
.nhv-hub-articles{max-width:1100px;margin:0 auto;padding:60px 20px;}
.nhv-hub-articles h2{font-size:28px;font-weight:800;color:#0f172a;margin:0 0 32px;}
.nhv-article-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px;}
.nhv-article-card{border:1px solid #e2e8f0;border-radius:12px;padding:24px;background:#fff;transition:box-shadow .15s;}
.nhv-article-card:hover{box-shadow:0 4px 20px rgba(0,0,0,.1);}
.nhv-article-card h3{font-size:18px;font-weight:700;color:#0f172a;margin:0 0 10px;line-height:1.4;}
.nhv-article-card p{font-size:14px;color:#64748b;margin:0 0 16px;line-height:1.6;}
.nhv-article-card a.hub-card-link{font-size:14px;font-weight:700;color:#469A3D;text-decoration:none;}
.hub-article-checklist{border-left:3px solid #25D366;}
.nhv-index-hero{background:#0f172a;color:#fff;padding:80px 20px;text-align:center;}
.nhv-index-hero h1{font-size:clamp(28px,5vw,48px);font-weight:900;margin:0 0 16px;}
.nhv-index-hero p{font-size:18px;opacity:.8;max-width:580px;margin:0 auto;}
.nhv-cluster-section{max-width:1100px;margin:0 auto;padding:60px 20px 20px;}
.nhv-cluster-section h2{font-size:26px;font-weight:800;color:#0f172a;margin:0 0 8px;}
.nhv-cluster-section p.cluster-desc{font-size:15px;color:#64748b;margin:0 0 24px;}
</style>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800;900&display=swap" rel="stylesheet">"""

GA = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GT-K8DVG7VR"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','GT-K8DVG7VR');</script>"""

def head(title, description, canonical, extra_meta=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://newhopevisa.com{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="New Hope Immigration Services">
{extra_meta}{CSS}
{GA}
</head>
<body>
{NAV}"""

def cta_box(title, body, cta_text, href):
    return f"""<div class="nhv-cta-box">
  <h3>{title}</h3>
  <p>{body}</p>
  <a href="{href}">{cta_text}</a>
</div>"""

def breadcrumb(cluster_slug, cluster_name, article_title=None):
    bc = f'<p class="nhv-breadcrumb"><a href="/en/">Home</a> › <a href="/en/blog/">Blog</a> › <a href="/en/blog/{cluster_slug}/">{cluster_name}</a>'
    if article_title:
        bc += f' › {article_title}'
    bc += '</p>'
    return bc

def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

# ── DATA ──────────────────────────────────────────────────────────────────────
CLUSTERS = [
    {
        "slug": "adjustment-of-status",
        "name": "Adjustment of Status",
        "service_url": "/en/adjustment-of-status/",
        "desc": "Everything you need to know about adjusting your status to permanent resident (Green Card) inside the United States.",
        "hero_subtitle": "Your complete guide to the I-485 process, eligibility, timelines, and what to expect at each step.",
        "articles": [
            {
                "slug": "what-is-adjustment-of-status",
                "title": "What Is Adjustment of Status? A Plain-English Guide to Form I-485",
                "meta": "Learn what adjustment of status means, who qualifies, and how Form I-485 works to get a Green Card inside the U.S.",
                "intro": "Adjustment of status (AOS) is the process that allows eligible foreign nationals already in the United States to apply for lawful permanent residence — commonly called a Green Card — without leaving the country. It is one of the most pursued immigration benefits in the U.S. each year, and understanding how it works can save you thousands of dollars in travel and legal fees.",
                "body": [
                    ("What Does 'Adjustment of Status' Actually Mean?", "When someone 'adjusts status,' they are changing their immigration classification from a temporary visa category to permanent resident, all while remaining on U.S. soil. The alternative — consular processing — requires you to attend an interview at a U.S. embassy abroad. AOS lets you skip that international trip if you are already in the country and meet the eligibility requirements."),
                    ("Who Can Apply?", "To file Form I-485, you generally need: (1) an approved immigrant petition (such as Form I-130 for family-based or I-140 for employment-based cases), (2) an available immigrant visa number, (3) a valid entry into the United States, and (4) admissibility, meaning no disqualifying grounds such as certain criminal records, health issues, or immigration violations. Immediate relatives of U.S. citizens — spouses, unmarried children under 21, and parents — typically have priority because visa numbers are always available for them."),
                    ("Key Steps in the I-485 Process", "The AOS process involves several stages: filing the I-485 package with supporting documents, receiving a biometrics (fingerprint) appointment notice, attending a medical exam with a USCIS-designated civil surgeon, and attending an adjustment of status interview at a local USCIS field office. Not everyone is called for an interview — employment-based applicants are sometimes approved based on the file alone — but family-based cases almost always require one."),
                    ("Common Documents in the I-485 Package", "A typical I-485 filing includes the form itself, Form I-864 Affidavit of Support (signed by your U.S. petitioner), Form I-131 (if you want advance parole to travel while pending), Form I-765 (work authorization/EAD), passport photos, birth certificate, passport copies, and evidence of your qualifying immigrant visa petition. The exact list varies by case type."),
                    ("How Long Does It Take?", "Processing times vary significantly by USCIS field office and case category. As of 2025, family-based I-485 cases can take 12 to 36 months at many offices. Employment-based cases may be faster or slower depending on visa availability and the applicant's country of birth. You can check current estimated processing times on the USCIS website or call our office for a case-specific assessment."),
                ],
                "faqs": [
                    ("Can I travel while my I-485 is pending?", "Yes, but only if you obtain Advance Parole (Form I-131) before leaving. Traveling without Advance Parole can result in your I-485 being considered abandoned."),
                    ("Can I work while waiting for my Green Card?", "Yes, once USCIS approves your Form I-765 (EAD/work permit), which is filed alongside I-485. EAD approvals currently take a few months."),
                    ("What happens if my visa expires while I-485 is pending?", "Being out of status can complicate your case. However, if you filed I-485 properly while in valid status, the pending application itself provides a form of protection called 'period of authorized stay.' Consult a professional for your specific situation."),
                    ("Is a lawyer required?", "No, but immigration rules are complex and errors can cause delays or denials. A DOJ-accredited representative can prepare and review your application at a fraction of attorney fees."),
                ],
                "related_within": ["how-long-does-adjustment-of-status-take","adjustment-of-status-documents-checklist","i-485-interview-what-to-expect"],
                "related_cross": [("naturalization","naturalization-eligibility-requirements"),("green-card-renewal","green-card-renewal-i-90-complete-guide")],
            },
            {
                "slug": "adjustment-of-status-documents-checklist",
                "title": "Adjustment of Status Documents Checklist: Everything You Need for I-485",
                "meta": "Complete document checklist for the I-485 Adjustment of Status application — forms, evidence, photos, and supporting documents.",
                "intro": "Gathering the right documents before you file Form I-485 is one of the most important steps you can take to avoid delays, Requests for Evidence (RFEs), or denials. This checklist covers the core documents required for most family-based adjustment of status cases, plus notes on employment-based variations.",
                "body": [
                    ("Core Forms to File With I-485", "At a minimum, your I-485 package should include: Form I-485 (Application to Register Permanent Residence), Form I-864 (Affidavit of Support from your petitioner), Form I-765 (Application for Employment Authorization — filed concurrently to get your EAD faster), and Form I-131 (Application for Advance Parole, if you need to travel). Filing I-765 and I-131 concurrently with I-485 is standard practice and does not cost extra in most family-based cases."),
                    ("Civil Documents", "You will need certified copies of: your full birth certificate with English translation (if not in English), marriage certificate (if married), divorce decrees (if previously married), police clearances from any country where you lived for more than 6 months since age 16 (required for some nationalities), and any court records related to arrests or criminal matters."),
                    ("Identity and Travel Documents", "Gather: passport bio page (valid or expired), all prior visa stamps and entry stamps, Form I-94 Arrival/Departure record (print from the CBP website), any prior immigration documents (prior visa petitions, EADs, etc.), and two passport-style photos taken within the last 30 days."),
                    ("Medical Exam", "You must complete Form I-693 (Medical Examination) with a USCIS-designated civil surgeon. The civil surgeon will vaccinate you and examine you. Do NOT open the sealed envelope — submit it sealed with your package or bring it to your interview. The medical exam is valid for 2 years from the date of signature."),
                    ("Proof of Status and Entry", "Include evidence of your last lawful entry into the U.S. This might be your I-94, a visa stamp, or other entry documentation. If you entered without inspection, consult a professional — this can affect eligibility."),
                    ("Affidavit of Support (I-864) Requirements", "The petitioning sponsor must show income at or above 125% of the Federal Poverty Guidelines for their household size. They need: last 3 years of tax returns (or IRS transcripts), most recent W-2s or 1099s, current pay stubs or employment letter, and bank statements if income needs to be supplemented."),
                ],
                "faqs": [
                    ("Do I need certified translations?", "Yes. Any document not in English must be accompanied by a complete English translation and a translator's certification of accuracy."),
                    ("What if my birth certificate is unavailable?", "If your country of birth does not issue birth certificates or yours was lost, USCIS may accept secondary evidence such as baptismal records, school records, or sworn affidavits from relatives."),
                    ("How recent must the medical exam be?", "The civil surgeon must sign Form I-693 within 60 days before you file. However, the results remain valid for 2 years after signing."),
                    ("What if the sponsor's income is too low?", "A joint sponsor — any U.S. citizen or permanent resident who meets the income threshold — can sign a separate I-864 to fulfill the support requirement."),
                ],
                "related_within": ["what-is-adjustment-of-status","i-485-interview-what-to-expect","how-long-does-adjustment-of-status-take"],
                "related_cross": [("naturalization","n-400-documents-checklist"),("removal-of-conditions","i-751-documents-checklist")],
            },
            {
                "slug": "i-485-interview-what-to-expect",
                "title": "I-485 Interview: What to Expect and How to Prepare",
                "meta": "Wondering what happens at the USCIS I-485 interview? Learn what officers ask, what to bring, and how to prepare for your adjustment of status interview.",
                "intro": "The I-485 adjustment of status interview is one of the final hurdles before USCIS approves your Green Card. For many applicants, it is also the most anxiety-inducing step. The good news: if your documents are in order and your answers are consistent with your application, most interviews conclude smoothly and quickly.",
                "body": [
                    ("Who Has to Attend the Interview?", "Most family-based I-485 applicants are required to attend an in-person interview at a local USCIS field office. Your U.S. citizen or permanent resident petitioner (e.g., spouse or parent) is also required to attend in spousal cases. Employment-based applicants are sometimes interview-waived, but USCIS can always schedule one if needed."),
                    ("What Documents to Bring", "Bring originals of everything you submitted, plus your interview notice. Key items: passport(s), all prior I-94 records, marriage certificate (and joint evidence for spousal cases), driver's license or state ID, any new documents not previously submitted, and your approved I-797 petition receipt notices."),
                    ("What the Officer Will Ask", "For spousal cases, officers verify the bona fides of the marriage. Expect questions about how you met, your daily routine, who does the cooking, who wakes up first, joint bank accounts, lease agreements, photos together, and travel history. For parent-child or sibling cases, questions focus on identity, background, and the relationship. Officers will also go through your I-485 form to confirm your answers."),
                    ("Potential Outcomes", "At the end of the interview, the officer may: (1) approve your case on the spot, (2) request additional evidence (called an RFE or 'additional evidence' request), (3) place your case in administrative processing (rare, for security checks), or (4) recommend denial. Most routine cases end with approval or an evidence request."),
                    ("Tips for a Successful Interview", "Dress professionally. Arrive early — Orlando field offices can be busy. Bring organized, tabbed documents. Answer only what is asked — do not volunteer extra information. It is okay to say 'I don't remember' if you genuinely don't. Be consistent with what you wrote on your forms. If you bring a representative, introduce them at the start."),
                ],
                "faqs": [
                    ("Can I bring a representative?", "Yes. A DOJ-accredited representative or immigration attorney can accompany you, answer procedural questions, and ensure your rights are protected during the interview."),
                    ("What if I need an interpreter?", "You may bring your own interpreter, or the officer may use a telephonic interpreter. The interpreter must be fluent in both English and your language and cannot be your attorney or representative."),
                    ("What if the officer finds inconsistencies?", "Minor inconsistencies (e.g., different spellings of a name) are usually resolved with documentation. Major inconsistencies about the genuineness of a marriage can trigger further investigation or denial."),
                    ("How long does the interview last?", "Most I-485 interviews last 20 to 45 minutes for straightforward cases. Complex or spousal cases may run longer."),
                ],
                "related_within": ["what-is-adjustment-of-status","adjustment-of-status-documents-checklist","adjustment-of-status-denial-reasons"],
                "related_cross": [("naturalization","naturalization-interview-tips"),("removal-of-conditions","removal-of-conditions-interview")],
            },
            {
                "slug": "how-long-does-adjustment-of-status-take",
                "title": "How Long Does Adjustment of Status Take in 2025?",
                "meta": "Current I-485 processing times in 2025 — what affects your wait, how to check status, and what to do if your case is delayed.",
                "intro": "Processing times for I-485 adjustment of status applications vary widely based on your USCIS field office, the type of case, and whether USCIS requests additional evidence. Here is what applicants in Orlando and across Florida should realistically expect in 2025.",
                "body": [
                    ("Average Processing Times by Case Type", "Family-based I-485 cases filed by immediate relatives (spouses, parents, and unmarried children under 21 of U.S. citizens) currently process in 12 to 36 months at most field offices. Non-immediate relatives face additional wait times for visa number availability. Employment-based cases range from 8 to 24 months, depending on the preference category and the applicant's country of birth."),
                    ("Why Times Vary So Much", "USCIS processing times depend on: the volume of applications received, available staffing, interview scheduling capacity at your local field office, security and background check clearances, and whether USCIS issues an RFE that pauses the clock. The Orlando Field Office processes cases for Central Florida — historically a busy office with moderate to long wait times."),
                    ("How to Check Your Case Status", "You can check your case status 24/7 at the USCIS Case Status Online portal using your receipt number (starts with IOE, LIN, SRC, EAC, or WAC). You can also sign up for case status email updates. If your case is outside the estimated processing time shown on the USCIS website, you may be eligible to submit a case inquiry or contact the USCIS Contact Center."),
                    ("When to Take Action", "If your case is outside the processing time shown on the USCIS website, submit an e-Request through the USCIS portal. If you have a pressing need (medical, employment, travel), contact a representative or attorney about options. If your EAD has expired or is about to expire, you can file a renewal while your I-485 is still pending."),
                    ("Factors That Can Speed Up Your Case", "Responding to RFEs quickly and completely, attending biometrics and interviews promptly, ensuring your application has no errors, and submitting a complete evidence package from the start can all minimize delays. Cases with missing evidence or incomplete forms are often put on hold, extending wait times significantly."),
                ],
                "faqs": [
                    ("Can I expedite my I-485?", "USCIS allows expedite requests in specific circumstances: severe financial loss, emergency situations, humanitarian reasons, USCIS error, or nonprofit requests in the national interest. Approval is not guaranteed and must be well-documented."),
                    ("Does moving affect my case?", "Yes. You must file Form AR-11 within 10 days of any address change. For I-485 cases, you should also file Form I-865 to notify USCIS. Failure to update your address can result in missed notices and case closures."),
                    ("Does getting an EAD mean my Green Card is coming soon?", "Not necessarily. EAD approval does not indicate where your I-485 is in processing. The two are tracked separately."),
                    ("What if USCIS loses my case?", "If you cannot locate your case in the system or receive conflicting information, contact the USCIS Contact Center and consider requesting an Infopass appointment or working with a representative to escalate."),
                ],
                "related_within": ["what-is-adjustment-of-status","adjustment-of-status-documents-checklist","adjustment-of-status-denial-reasons"],
                "related_cross": [("naturalization","how-long-does-naturalization-take"),("green-card-renewal","when-to-renew-green-card")],
            },
            {
                "slug": "adjustment-of-status-denial-reasons",
                "title": "Top Reasons Adjustment of Status Is Denied (and How to Avoid Them)",
                "meta": "Understand the most common reasons USCIS denies Form I-485 and what steps you can take to protect your Green Card application.",
                "intro": "An I-485 denial can be devastating, but many denials stem from avoidable errors. Understanding the most common grounds for denial — and addressing them before you file — dramatically improves your chances of approval.",
                "body": [
                    ("Unlawful Presence or Prior Immigration Violations", "One of the leading denial grounds is accrued unlawful presence or prior immigration violations. If you overstayed a prior visa or were previously removed, these issues can trigger bars to adjustment. A three-year bar applies to those who accrued more than 180 days of unlawful presence; a ten-year bar applies to those with more than one year. These bars can sometimes be waived."),
                    ("Criminal History", "USCIS conducts thorough background checks. Certain criminal convictions — particularly aggravated felonies, crimes involving moral turpitude, drug offenses, and domestic violence — can be permanent bars to adjustment. Even arrests without convictions must be disclosed. Failure to disclose criminal history is itself a ground for denial (and potentially deportation)."),
                    ("Failure to Maintain Status", "If you were out of status before filing I-485, your eligibility may be compromised. Immediate relatives of U.S. citizens generally have more flexibility here, but non-immediate relatives must have maintained valid status throughout their stay."),
                    ("Errors on the Application", "Simple mistakes — incorrect dates, missing signatures, wrong fee amounts, or inconsistent information across forms — can lead to rejection or an RFE that delays your case. Always have your application reviewed before filing."),
                    ("Public Charge Ground", "Since 2022, USCIS has applied the public charge inadmissibility ground under the final rule. Applicants must demonstrate they are not likely to become primarily dependent on the government for subsistence. This is evaluated using the totality of circumstances, not just one factor."),
                    ("Failure to Appear at Biometrics or Interview", "Missing your biometrics appointment or USCIS interview without notifying USCIS can result in abandonment of your application. If you cannot attend, reschedule as early as possible and keep documentation of why you missed."),
                ],
                "faqs": [
                    ("Can I appeal an I-485 denial?", "Yes. Depending on the reason, you may file a Motion to Reconsider (if USCIS made a legal error) or a Motion to Reopen (if new evidence is available). You can also refile if you remain eligible."),
                    ("Can I reapply after a denial?", "In most cases, yes — if the underlying issue is resolved. For example, if your case was denied for a missing document, you can refile with that document included."),
                    ("Does a DUI affect my I-485?", "A single DUI is not automatically disqualifying, but it may raise admissibility questions. Multiple DUIs, or a DUI combined with other issues, can be more problematic. Disclose all arrests and let a professional review your specific situation."),
                    ("What if I was denied because of a USCIS error?", "File a Motion to Reconsider with evidence demonstrating the legal or factual error. Act quickly — there are filing deadlines."),
                ],
                "related_within": ["what-is-adjustment-of-status","i-485-interview-what-to-expect","how-long-does-adjustment-of-status-take"],
                "related_cross": [("naturalization","naturalization-eligibility-requirements"),("removal-of-conditions","removal-of-conditions-denial")],
            },
        ]
    },
    {
        "slug": "naturalization",
        "name": "Naturalization",
        "service_url": "/en/naturalization/",
        "desc": "Your path to U.S. citizenship explained — from the N-400 application to the oath ceremony and everything in between.",
        "hero_subtitle": "Everything you need to know about applying for U.S. citizenship, including the civics test, language requirements, and interview process.",
        "articles": [
            {
                "slug": "naturalization-eligibility-requirements",
                "title": "U.S. Naturalization Eligibility: Do You Qualify for Citizenship?",
                "meta": "Find out if you meet the requirements for U.S. naturalization — Green Card hold time, continuous residence, physical presence, and good moral character.",
                "intro": "Becoming a U.S. citizen through naturalization is one of the most significant milestones in an immigrant's journey. Before you file Form N-400, you must ensure you meet all the eligibility requirements set by USCIS. Missing even one can result in a denial that delays your citizenship by years.",
                "body": [
                    ("The Basic Requirements", "To be eligible for naturalization, you generally must: (1) be at least 18 years old, (2) be a lawful permanent resident (Green Card holder) for the required period, (3) have continuous residence in the U.S., (4) have been physically present in the U.S. for the required amount of time, (5) be able to read, write, and speak basic English, (6) have knowledge of U.S. history and government (the civics test), (7) have good moral character, and (8) be willing to take the Oath of Allegiance."),
                    ("The 5-Year vs. 3-Year Rule", "Most Green Card holders must wait 5 years from the date of permanent residence before applying. However, if you obtained your Green Card as the spouse of a U.S. citizen and have been living in marital union with that citizen, you only need to wait 3 years. There are additional shortened pathways for military members and certain other groups."),
                    ("Continuous Residence vs. Physical Presence", "These are two distinct requirements. Continuous residence means you have not abandoned your U.S. residence. Physical presence means you have been physically on U.S. soil for at least 30 months out of the past 60 months (for the 5-year path) or 18 months out of the past 36 months (for the 3-year path). A single trip abroad of more than 6 months can break continuous residence unless you take proactive steps."),
                    ("Good Moral Character", "USCIS looks at your conduct during the statutory period (usually the past 5 years). Certain acts are permanent bars — such as murder or an aggravated felony. Others may be conditional bars that can be overcome with evidence or waivers. You must disclose all arrests, criminal charges, and any prior immigration violations on your N-400."),
                    ("English Language Exceptions", "The English requirement is waived for applicants who are over 50 and have held a Green Card for at least 20 years (the '50/20 rule') or over 55 with 15 years of permanent residence (the '55/15 rule'). Applicants with certain disabilities may also qualify for an exception by submitting Form N-648 completed by a licensed medical professional."),
                ],
                "faqs": [
                    ("Can I apply 90 days before I reach the 5-year mark?", "Yes. USCIS allows you to file up to 90 days before you meet the continuous residence requirement, as long as you will fully meet it by your interview date."),
                    ("Does time as a conditional resident (2-year Green Card) count?", "Yes. Time as a conditional resident counts toward the 5-year (or 3-year) requirement."),
                    ("What if I traveled abroad for more than a year?", "Trips of more than one year generally break continuous residence unless you obtained a re-entry permit before departing. Talk to a professional about your options if this applies."),
                    ("Does my child automatically become a citizen when I naturalize?", "Under the Child Citizenship Act, children under 18 who are lawful permanent residents and reside in the U.S. with a naturalizing parent may automatically acquire citizenship. Conditions apply."),
                ],
                "related_within": ["how-long-does-naturalization-take","n-400-documents-checklist","naturalization-civics-test-guide"],
                "related_cross": [("adjustment-of-status","what-is-adjustment-of-status"),("removal-of-conditions","removal-of-conditions-overview")],
            },
            {
                "slug": "n-400-documents-checklist",
                "title": "N-400 Documents Checklist: What to Include With Your Citizenship Application",
                "meta": "Complete checklist of documents to submit with your Form N-400 naturalization application for U.S. citizenship.",
                "intro": "Filing Form N-400 without the right supporting documents is a common mistake that leads to Requests for Evidence (RFEs), delays, or denials. This checklist covers everything most applicants need when applying for U.S. citizenship through naturalization.",
                "body": [
                    ("Required Forms and Fees", "You will need: completed Form N-400 (Application for Naturalization), the current filing fee ($760 as of 2025, or $640 for military), and two passport-style photos (only required if filing by mail). Always check the USCIS website for the current fee before filing."),
                    ("Proof of Permanent Residence", "Submit a copy (front and back) of your Permanent Resident Card (Green Card). If your card is expired or about to expire, you should renew it via Form I-90 before or alongside your N-400. Include copies of all Green Cards you have held."),
                    ("Identity Documents", "Include: copies of all passports (current and expired), your state-issued ID or driver's license, and any other government-issued photo ID."),
                    ("Travel History", "You must account for all trips outside the U.S. during the statutory period. Include a list of all trips — dates of departure and return, countries visited, and purpose. Supporting documentation (passport stamps, airline records) may be requested."),
                    ("Marital History Documents", "If married: marriage certificate (and English translation if applicable). If divorced: divorce decree for all prior marriages. If widowed: death certificate of former spouse. If you are applying under the 3-year rule as a spouse of a U.S. citizen, you also need: evidence of joint life (joint bank statements, lease/mortgage, photos, joint insurance)."),
                    ("Tax Returns", "Include copies of your federal income tax returns for the past 5 years (or 3 years if applying under the spousal path). If you were not required to file, include a statement explaining why."),
                    ("Criminal or Immigration History", "If you have any arrests, criminal charges, or prior immigration court proceedings, include certified court dispositions for each incident. Failure to disclose can result in denial and possible removal proceedings."),
                    ("Selective Service Registration", "Male applicants who were required to register with Selective Service (ages 18–26) must provide proof of registration or an explanation if they failed to register."),
                ],
                "faqs": [
                    ("Do I need certified copies?", "USCIS generally accepts clear photocopies. However, if you are asked to bring originals to your interview, you must produce them. For documents in a foreign language, you need a certified English translation."),
                    ("What if I filed taxes jointly with my spouse?", "Joint tax returns are fine. Include the full return or a transcript from the IRS."),
                    ("Can I use IRS transcripts instead of full returns?", "Yes. IRS tax transcripts are accepted and sometimes easier to obtain than full returns, especially for older years."),
                    ("What if I never filed taxes?", "If you were legally required to file and did not, USCIS may question your good moral character. Consider consulting a tax professional and filing any missing returns before your interview."),
                ],
                "related_within": ["naturalization-eligibility-requirements","naturalization-civics-test-guide","naturalization-interview-tips"],
                "related_cross": [("adjustment-of-status","adjustment-of-status-documents-checklist"),("removal-of-conditions","i-751-documents-checklist")],
            },
            {
                "slug": "naturalization-civics-test-guide",
                "title": "U.S. Civics Test for Naturalization: How to Study and Pass",
                "meta": "Study guide for the USCIS civics test required for naturalization. Learn the 100 questions, tips for the interview, and exemptions.",
                "intro": "The U.S. civics test is a required component of the naturalization interview. USCIS officers ask applicants up to 10 questions from a standardized list of 100 civics questions about American history and government. You need to answer at least 6 correctly to pass. Here is everything you need to know to prepare.",
                "body": [
                    ("How the Test Works", "During your naturalization interview, the USCIS officer will ask you up to 10 of the 100 official civics questions. You must answer at least 6 correctly to pass. The questions are asked orally — the officer asks in English and you answer in English (unless you qualify for an exception). If you fail the civics test on your first attempt, you get one more chance at a second interview scheduled within 60 to 90 days."),
                    ("The 100 Official Questions", "USCIS publishes all 100 civics questions and answers on its website. Topics include: the principles of American democracy, the system of government (three branches, checks and balances), U.S. history (colonial period, Civil War, 20th century), rights and responsibilities of citizens, and geography (states, capitals, bordering countries and oceans)."),
                    ("High-Frequency Questions to Know Cold", "Certain questions appear more often or are particularly important: What is the supreme law of the land? (The Constitution.) What do we call the first ten amendments? (The Bill of Rights.) What are the two major political parties in the U.S.? (Democratic and Republican.) Who is the President? (Know the current president on your exam date.) How many senators does each state have? (Two.) What ocean is on the East Coast? (The Atlantic Ocean.)"),
                    ("Study Methods That Work", "The most effective study approach: (1) download the USCIS flashcard app or use free online flashcard sets, (2) practice daily for 15 minutes rather than cramming, (3) watch the USCIS civics test preparation videos on YouTube, (4) take timed practice quizzes to simulate exam conditions, (5) ask a family member or friend to quiz you using the official question list."),
                    ("Exemptions and Accommodations", "Applicants 65 or older who have held a Green Card for at least 20 years take a shorter 'easier' version of the civics test (marked with an asterisk in the official list — only 20 questions to study). Applicants with qualifying physical or developmental disabilities or mental impairment can seek a medical exception to the civics test via Form N-648."),
                ],
                "faqs": [
                    ("Are the questions always the same?", "The 100 questions are standardized, but the officer chooses which 10 to ask. Some questions have answers that change over time — such as the name of the current President or the number of representatives — so check for updates before your interview."),
                    ("Can I answer in Spanish or Portuguese?", "No, unless you qualify for an English-language exception (the 50/20 or 55/15 rule). The test is conducted in English for most applicants."),
                    ("What if I fail the civics test?", "You get one retake within 60 to 90 days. You are only tested on the failed components (civics or English), not the entire application again."),
                    ("Is there a study guide from USCIS?", "Yes. USCIS provides a free study guide, flashcards, practice test tools, and video series at uscis.gov/citizenship/find-study-materials-and-resources."),
                ],
                "related_within": ["naturalization-eligibility-requirements","naturalization-interview-tips","n-400-documents-checklist"],
                "related_cross": [("student-visa","f1-visa-to-green-card-paths"),("adjustment-of-status","what-is-adjustment-of-status")],
            },
            {
                "slug": "naturalization-interview-tips",
                "title": "Naturalization Interview Tips: How to Prepare for Your N-400 Interview",
                "meta": "Practical tips for preparing for your N-400 naturalization interview — what to bring, what to expect, and how to answer common officer questions.",
                "intro": "The N-400 naturalization interview is the final step before taking your Oath of Allegiance and becoming a U.S. citizen. Most applicants find the interview straightforward if they are well-prepared. These tips will help you walk in with confidence.",
                "body": [
                    ("What Happens at the Interview", "The interview typically lasts 20 to 30 minutes. The USCIS officer will: place you under oath, review your N-400 answers, conduct the English reading and writing test (unless you qualify for an exception), administer the civics test, and ask follow-up questions about your application, travel history, or background. At the end, the officer will either approve, continue (request more evidence), or deny your application."),
                    ("What to Bring", "Bring: your original Green Card, a valid unexpired passport (all passports held during the statutory period), your interview notice, any new documents not previously submitted (updated tax returns, marriage/divorce records), evidence of joint marital life if applying as a spouse, and any criminal court records or dispositions if applicable."),
                    ("The English Reading and Writing Test", "The officer will show you a sentence to read aloud and ask you to write a sentence in English that they dictate. You get up to three tries for each. The sentences are drawn from a standardized list of simple English sentences using vocabulary from the civics questions. Practice reading and writing sentences about American history and government topics."),
                    ("Common Interview Questions", "Officers typically ask: Have you been a member of any organization, group, or party? Have you ever claimed to be a U.S. citizen? Have you registered to vote? Have you ever failed to file income taxes? Have you ever been arrested, cited, or detained? Is the information on your N-400 still accurate? Answer honestly — inconsistencies are grounds for denial."),
                    ("Arrive Prepared and Calm", "Arrive 15 minutes early. Dress neatly — professional or business casual is appropriate. Bring all documents in organized folders. Answer questions clearly and concisely. If you don't understand a question, politely ask the officer to rephrase it. Do not guess — it is acceptable to say 'I'm not sure' and explain."),
                ],
                "faqs": [
                    ("Can someone accompany me to the interview?", "You may bring a representative (DOJ-accredited or attorney) who can advise you on procedural matters. A translator may also attend if you qualify for the language exception."),
                    ("What if I'm approved at the interview?", "If approved, USCIS will typically schedule your oath ceremony for the same day or provide a date within a few weeks. At the ceremony, you officially become a U.S. citizen."),
                    ("What happens if I'm denied at the interview?", "USCIS must provide a written explanation of the denial. You can request a hearing before an immigration officer or appeal to the federal district court."),
                    ("Can USCIS ask about my social media?", "USCIS may review publicly available social media. Since 2019, certain visa applicants must provide social media handles. For N-400, honesty on the form and consistency with your public presence are the main concerns."),
                ],
                "related_within": ["naturalization-eligibility-requirements","n-400-documents-checklist","naturalization-civics-test-guide"],
                "related_cross": [("adjustment-of-status","i-485-interview-what-to-expect"),("removal-of-conditions","removal-of-conditions-interview")],
            },
            {
                "slug": "how-long-does-naturalization-take",
                "title": "How Long Does Naturalization Take? N-400 Processing Times in 2025",
                "meta": "Current N-400 naturalization processing times in 2025, what affects your wait, and how to track your citizenship application.",
                "intro": "After years of building your life in the United States as a permanent resident, the wait for naturalization approval can feel long. Here is a realistic breakdown of N-400 processing times for 2025, what factors affect your wait, and what you can do if your case seems stuck.",
                "body": [
                    ("Current N-400 Processing Times", "As of 2025, USCIS reports median processing times for N-400 applications ranging from 5 to 14 months, depending on the field office and applicant background. The Orlando Field Office, which serves Central Florida applicants, has historically had processing times in the 8 to 18 month range. These times fluctuate with application volume and staffing."),
                    ("Key Milestones After Filing", "After filing, expect these milestones: (1) receipt notice within 2 to 4 weeks confirming USCIS received your application, (2) biometrics appointment notice within 1 to 3 months, (3) interview notice typically several months after biometrics, (4) interview, (5) oath ceremony, usually within a few weeks of approval."),
                    ("What Can Delay Your Case", "Common causes of delays: security or background check holds, name check clearances, requests for evidence (RFEs), high application volume at your field office, failure to update your address, or missing biometrics appointments. Cases involving criminal history, travel issues, or prior immigration violations typically take longer."),
                    ("How to Track Your Application", "Use the USCIS Case Status Online tool with your receipt number. Sign up for email and text notifications. If your case is outside the published processing time range, you can submit a case inquiry online or call the USCIS Contact Center at 1-800-375-5283."),
                    ("Requesting Expedited Processing", "USCIS may expedite N-400 cases in specific circumstances: you are a member of the military on active duty or were recently honorably discharged, you have a severe financial loss, there is an urgent humanitarian need, or there is a USCIS error in your case. Requests must be submitted in writing with supporting documentation."),
                ],
                "faqs": [
                    ("Can I vote while waiting for naturalization?", "No. Voting before you are a citizen is a federal crime that can also result in deportation. Wait until you receive your Certificate of Naturalization and register to vote through proper channels."),
                    ("Does filing early hurt my case?", "No. Filing up to 90 days before you meet the continuous residence requirement is allowed and does not negatively affect your application."),
                    ("What if my Green Card expires while waiting?", "File Form I-90 to renew your Green Card. A pending N-400 does not extend the validity of your Green Card for identity purposes."),
                    ("Can I travel abroad while my N-400 is pending?", "Yes, but avoid long trips. Extended absences can raise questions about continuous residence. Trips of more than 6 months can interrupt continuous residence and potentially disqualify you."),
                ],
                "related_within": ["naturalization-eligibility-requirements","n-400-documents-checklist","naturalization-interview-tips"],
                "related_cross": [("adjustment-of-status","how-long-does-adjustment-of-status-take"),("green-card-renewal","when-to-renew-green-card")],
            },
        ]
    },
    {
        "slug": "removal-of-conditions",
        "name": "Removal of Conditions",
        "service_url": "/en/adjustment-of-status/",
        "desc": "Guide to removing conditions from your 2-year conditional Green Card and converting it to a 10-year permanent resident card.",
        "hero_subtitle": "Everything conditional Green Card holders need to know about filing Form I-751 to remove conditions on residence.",
        "articles": [
            {
                "slug": "removal-of-conditions-overview",
                "title": "Removal of Conditions on Residence: What Is Form I-751?",
                "meta": "Understand what Form I-751 is, who needs to file it, and how to convert your conditional Green Card to a 10-year permanent resident card.",
                "intro": "If you received a 2-year conditional Green Card as the spouse of a U.S. citizen or permanent resident, you must file Form I-751 (Petition to Remove Conditions on Residence) before your conditional Green Card expires. Failing to file on time can put your immigration status at risk.",
                "body": [
                    ("Who Has a Conditional Green Card?", "Immigrants who obtain permanent residence through a marriage that was less than 2 years old at the time of approval receive a conditional Green Card valid for only 2 years. This applies to both immigrant spouses of U.S. citizens (family-based) and certain investor immigrants (EB-5). This guide focuses on marriage-based conditional residents."),
                    ("What Is Form I-751?", "Form I-751 is the petition you file to remove the conditions on your residence and convert your 2-year conditional Green Card into a standard 10-year permanent resident card. It must be filed jointly with your U.S. citizen or permanent resident spouse — unless you qualify for a waiver."),
                    ("When to File", "You must file Form I-751 during the 90-day window before your conditional Green Card expires. For example, if your card expires on October 15, you can file as early as July 17. Filing outside this window — either too early or too late — can cause serious problems. USCIS will typically deny late filings unless there is a good explanation."),
                    ("What Happens After Filing", "After USCIS receives your I-751, you will receive a receipt notice (Form I-797) that extends the validity of your conditional Green Card for 18 to 24 months while your petition is pending. You can use this receipt notice along with your expired conditional Green Card as proof of your continued lawful status for employment and travel purposes."),
                    ("Waivers of the Joint Filing Requirement", "If you cannot file jointly — because you divorced, your spouse died, or your spouse subjected you to battery or extreme cruelty — you may file alone with a waiver request. USCIS may also waive the joint requirement if terminating your status would cause extreme hardship. Waivers require substantial supporting documentation."),
                ],
                "faqs": [
                    ("What if I miss the 90-day filing window?", "USCIS may still accept a late filing with a written explanation of the extenuating circumstances. However, late filers risk being placed in removal proceedings. File as soon as possible if you have missed the window."),
                    ("Does my spouse need to be present at filing?", "Your spouse must sign the I-751. They do not need to be physically present when you mail it, but their signature must appear on the form."),
                    ("Can I travel abroad while I-751 is pending?", "Yes. Your I-797 receipt notice combined with your (expired) conditional Green Card serves as proof of status for re-entry during the extension period."),
                    ("How long does I-751 processing take?", "Processing times vary significantly — historically 12 to 36 months. USCIS may schedule an interview for some cases."),
                ],
                "related_within": ["i-751-documents-checklist","removal-of-conditions-interview","removal-of-conditions-denial"],
                "related_cross": [("naturalization","naturalization-eligibility-requirements"),("adjustment-of-status","what-is-adjustment-of-status")],
            },
            {
                "slug": "i-751-documents-checklist",
                "title": "I-751 Documents Checklist: What to Submit to Remove Conditions on Your Green Card",
                "meta": "Complete I-751 document checklist — evidence of a bona fide marriage, identity documents, and supporting materials for removing conditions on residence.",
                "intro": "The most critical element of an I-751 petition is evidence that your marriage was entered in good faith — not solely to obtain immigration benefits. USCIS officers look for concrete, consistent, and compelling proof of a real marital relationship. Here is what to gather.",
                "body": [
                    ("Core Filing Documents", "Your I-751 package must include: the completed Form I-751, the filing fee ($750 as of 2025 — check uscis.gov for current fees), a copy of your conditional Green Card (front and back), evidence of the qualifying marriage, and a cover letter summarizing your evidence."),
                    ("Evidence of a Bona Fide Marriage", "This is the heart of your case. Provide as many of the following as possible: joint bank account statements (going back to your marriage date), joint lease or mortgage documents, joint utility bills (electricity, water, gas, phone), joint health or auto insurance policies, joint tax returns (IRS Form 1040 filed jointly), mortgage or property deeds in both names, photos of you together (at events, holidays, with family — dated throughout the marriage), evidence of children born of the marriage, and correspondence addressed to both of you at the same address."),
                    ("Travel and Communication Evidence", "If you lived separately at any point or spent time apart due to work or family, document it: travel records, employment letters, or explanatory declarations. You may also include emails, text message logs, or video call records to demonstrate ongoing communication."),
                    ("Identity Documents", "Include: copies of both spouses' passports, your I-94, your current conditional Green Card, and your marriage certificate with English translation if applicable."),
                    ("Statements and Affidavits", "A personal statement from each spouse explaining how you met, your relationship history, and your current life together can be powerful. Affidavits from people who know you as a couple — friends, neighbors, coworkers, religious community members — add credibility. These should be original, signed, and dated."),
                ],
                "faqs": [
                    ("How many pages of bank statements should I submit?", "Submit at least 12 months of statements for each joint account, highlighting transactions that show shared financial life. More is generally better, up to about 3 years."),
                    ("What if we don't have a joint bank account?", "No single piece of evidence is required. Compensate by providing more of the other evidence types. A written explanation of why you maintain separate accounts is also helpful."),
                    ("What if we separated or divorced before filing?", "You may still qualify for a waiver if the marriage was entered in good faith and the relationship broke down through no fault of your own, or if your spouse subjected you to abuse. Consult a professional before filing."),
                    ("Should I organize the evidence?", "Yes. Use tabs or section dividers and include a table of contents in your cover letter. Well-organized petitions make a better impression and reduce the risk of USCIS overlooking key evidence."),
                ],
                "related_within": ["removal-of-conditions-overview","removal-of-conditions-interview","removal-of-conditions-denial"],
                "related_cross": [("adjustment-of-status","adjustment-of-status-documents-checklist"),("naturalization","n-400-documents-checklist")],
            },
            {
                "slug": "removal-of-conditions-interview",
                "title": "I-751 Interview: What to Expect When USCIS Calls You In",
                "meta": "What happens at an I-751 removal of conditions interview, what officers ask about, and how to prepare your evidence for the USCIS meeting.",
                "intro": "Not all I-751 petitions require an interview — USCIS approves many based on the paper record alone. However, when an interview is scheduled, it usually means the officer has questions about the authenticity of your marriage. Here is how to prepare.",
                "body": [
                    ("Why USCIS Schedules Interviews", "USCIS may schedule an I-751 interview if: the petition was filed by one spouse alone (waiver cases), there are inconsistencies in the evidence, the marriage is relatively brief, one spouse has a significant age gap from the other, or there are prior immigration violations in the file. Being called for an interview is not necessarily a sign of impending denial — it is an opportunity to clarify the record."),
                    ("How the Interview Works", "You and your spouse will typically be interviewed together first, then possibly separately. Officers compare answers to look for inconsistencies that would indicate a fraudulent marriage. Questions focus on your daily life, home, routines, family, and relationship history. You are under oath, so all answers must be truthful."),
                    ("Common Interview Questions", "Expect questions like: What time does your spouse wake up? Whose side of the bed do you each sleep on? What do you typically eat for breakfast? What appliances do you own? What is your spouse's best friend's name? Describe your last vacation together. When is your spouse's birthday? What did you give each other as gifts recently? These detail-oriented questions aim to distinguish couples with a genuine shared life from those with a rehearsed story."),
                    ("Preparing Your Evidence Binder", "Bring a well-organized binder with all your evidence: photos organized chronologically, financial documents, housing records, affidavits, and any new evidence since you filed. Bring originals when possible and clearly labeled copies as backup."),
                    ("If Interviewed Separately", "If the officer separates you, this is not unusual for contested or questionable cases. Stay calm and answer consistently. Discrepancies in minor details are human and expected — major discrepancies in significant facts are more problematic. Know the major facts of your shared life cold."),
                ],
                "faqs": [
                    ("Does my U.S. citizen spouse have to attend?", "In joint filing cases, the petitioning spouse is generally required to attend. In waiver cases, the interview focuses on the conditional resident's credibility and evidence."),
                    ("What happens if we fail the interview?", "USCIS will issue a Notice of Intent to Deny (NOID). You have a specified period to respond with additional evidence before a final decision is made."),
                    ("Can a representative attend with us?", "Yes. A DOJ-accredited representative can accompany you, object to improper questions, and help you understand your rights during the interview."),
                    ("What should we study together before the interview?", "Review your entire shared life timeline: when you met, first date, proposal, wedding, where you have lived together, major life events. Practice answering the common questions with each other until the answers feel natural, not rehearsed."),
                ],
                "related_within": ["removal-of-conditions-overview","i-751-documents-checklist","removal-of-conditions-denial"],
                "related_cross": [("adjustment-of-status","i-485-interview-what-to-expect"),("naturalization","naturalization-interview-tips")],
            },
            {
                "slug": "removal-of-conditions-denial",
                "title": "I-751 Denial: What Happens If USCIS Denies Your Petition to Remove Conditions?",
                "meta": "Understand what happens after an I-751 denial, your appeal options, and how to protect your immigration status after removal of conditions is denied.",
                "intro": "An I-751 denial is a serious matter, but it is not the end of the road. Understanding what happens next — and acting quickly — is essential to protecting your status. Here is what you need to know.",
                "body": [
                    ("Consequences of Denial", "If USCIS denies your I-751, your conditional permanent residence is terminated and USCIS will issue a Notice to Appear (NTA) — placing you in removal proceedings before an immigration judge. This is alarming, but the immigration court process gives you another chance to prove your case."),
                    ("Defending Before an Immigration Judge", "In removal proceedings, you can present your evidence of a bona fide marriage to an immigration judge. The judge reviews the case de novo — meaning fresh, without deference to USCIS's decision. Many applicants who were denied by USCIS have ultimately prevailed before an immigration judge with strong evidence and effective representation."),
                    ("Common Reasons for I-751 Denial", "Denials typically stem from: insufficient evidence of a bona fide marriage, significant inconsistencies in testimony at a USCIS interview, evidence suggesting the marriage was entered for immigration purposes, failure to appear at a scheduled interview, or procedural problems with the filing itself (late filing, missing signatures, insufficient fee)."),
                    ("Motion to Reopen or Reconsider", "If you believe USCIS made a factual or legal error, you may file a Motion to Reconsider (legal error) or a Motion to Reopen (new evidence). These must be filed within 33 days of the denial notice. They do not halt removal proceedings on their own."),
                    ("If You Divorced After Filing", "A divorce finalized after you filed the joint I-751 does not automatically disqualify you if the underlying marriage was genuine. You can amend your petition to seek a good-faith marriage waiver and present evidence that the marriage was real at the time of its inception."),
                ],
                "faqs": [
                    ("Is deportation immediate after a denial?", "No. You receive notice of the denial and are placed in removal proceedings, where you have the right to a hearing before an immigration judge and to appeal adverse decisions."),
                    ("Can I refile if denied?", "In some circumstances, yes — particularly if new evidence has emerged or the marriage has been re-evaluated. Consult a professional immediately after any denial."),
                    ("Should I get a lawyer after an I-751 denial?", "This is highly advisable. Removal proceedings are complex, and the consequences of a negative outcome are severe. A DOJ-accredited representative or immigration attorney can significantly improve your chances."),
                    ("What if USCIS made an error in my denial?", "Document the error carefully, file a Motion to Reconsider within 33 days, and consult a professional. USCIS errors are correctable but require prompt action."),
                ],
                "related_within": ["removal-of-conditions-overview","i-751-documents-checklist","removal-of-conditions-interview"],
                "related_cross": [("adjustment-of-status","adjustment-of-status-denial-reasons"),("naturalization","naturalization-eligibility-requirements")],
            },
            {
                "slug": "removal-of-conditions-waiver",
                "title": "I-751 Waiver: Filing Without Your Spouse After Divorce, Abuse, or Death",
                "meta": "Learn how to file Form I-751 without your spouse — including waivers for divorce, domestic violence (VAWA), and hardship cases.",
                "intro": "The standard I-751 petition is filed jointly with your U.S. citizen or permanent resident spouse. But what happens when the marriage ends through divorce, your spouse passes away, or you have experienced abuse? USCIS provides waiver options that allow you to file alone — but they require careful documentation.",
                "body": [
                    ("The Three Main Waiver Grounds", "You can request a waiver of the joint filing requirement if: (1) termination of the marriage through divorce or annulment — you must show the marriage was entered in good faith; (2) your spouse's death — with documentation and evidence of the genuine marriage; or (3) your spouse subjected you to battery or extreme cruelty — including physical violence, emotional abuse, and coercive control."),
                    ("Good Faith Marriage Waiver After Divorce", "This is the most common waiver scenario. You must demonstrate that although the marriage has ended, it was entered genuinely — not for immigration purposes. Evidence of the relationship at the time of marriage and during your time together is essential: photos, financial records, communications, affidavits from people who knew you as a couple."),
                    ("VAWA Protection for Abuse Survivors", "If you were subjected to battery or extreme cruelty by your U.S. citizen or permanent resident spouse, you have special protections under the Violence Against Women Act (VAWA). You can file the I-751 waiver with evidence of the abuse, which may include police reports, protective orders, medical records, statements from social workers, therapists, or domestic violence advocates, and your own detailed declaration."),
                    ("Extreme Hardship Waiver", "A standalone hardship waiver is rarely granted but applies if your removal would cause extreme hardship to you or your U.S. citizen or permanent resident children. Documentation of medical conditions, financial ties, community involvement, and the conditions in your home country all support this claim."),
                    ("What to Include in a Waiver Filing", "Beyond the Form I-751, include: a detailed personal declaration telling the story of your marriage in your own words, all evidence of the bona fide marriage you have gathered, documentation of the divorce (divorce decree) or abuse (police reports, hospital records, protective orders), and supporting affidavits from people who can attest to your situation."),
                ],
                "faqs": [
                    ("Can I file the waiver before the divorce is final?", "Yes. USCIS allows you to file based on a pending divorce and update the file when finalized. You can also file jointly while pursuing divorce as a protective measure, then amend to a waiver if the divorce finalizes before USCIS adjudicates."),
                    ("Do I still need to file within the 90-day window?", "Yes, the filing window applies to waiver cases as well. However, if you are a victim of abuse, USCIS may be more flexible about timing — consult a professional."),
                    ("What if I don't have police reports or medical records?", "Not all abuse survivors have police reports. A detailed personal statement combined with statements from advocates, therapists, or witnesses can still support your claim. Document what you have."),
                    ("Will USCIS notify my abuser that I filed?", "USCIS has confidentiality protections for VAWA-based petitions. Information is not disclosed to the abusing spouse without your consent."),
                ],
                "related_within": ["removal-of-conditions-overview","i-751-documents-checklist","removal-of-conditions-interview"],
                "related_cross": [("adjustment-of-status","adjustment-of-status-denial-reasons"),("naturalization","naturalization-eligibility-requirements")],
            },
        ]
    },
    {
        "slug": "green-card-renewal",
        "name": "Green Card Renewal",
        "service_url": "/en/residence-renewals-i-90/",
        "desc": "Step-by-step guidance for renewing or replacing your Permanent Resident Card (Green Card) using Form I-90.",
        "hero_subtitle": "Everything you need to know about renewing your Green Card with Form I-90 — timelines, costs, and what to do when your card is lost or stolen.",
        "articles": [
            {
                "slug": "green-card-renewal-i-90-complete-guide",
                "title": "Green Card Renewal: Complete Guide to Form I-90 in 2025",
                "meta": "Everything you need to know about renewing your Green Card with Form I-90 — when to file, what it costs, and how long it takes.",
                "intro": "Your Permanent Resident Card (Green Card) is one of the most important immigration documents you hold. Keeping it current is not just a legal obligation — it is essential for employment, travel, and accessing services. This complete guide covers everything about Form I-90 in 2025.",
                "body": [
                    ("When Do You Need to Renew?", "Green Cards issued to most permanent residents are valid for 10 years. You should file Form I-90 to renew your card during the 6-month window before it expires. USCIS recommends not waiting until the last few months, as processing times can extend beyond the expiration date. Conditional Green Cards (valid 2 years) are renewed through Form I-751, not I-90."),
                    ("Other Reasons to File I-90", "Beyond renewal, Form I-90 is used to: replace a lost, stolen, or damaged card; correct errors on your card (such as misspelled name or wrong birthdate); update your card after a legal name change; obtain a new card if your previous one was issued more than 10 years ago; or replace a card never received in the mail."),
                    ("Filing Options: Online vs. Mail", "USCIS strongly recommends filing Form I-90 online through the myUSCIS account portal. Online filing is faster, allows you to track your case, and reduces the chance of errors. You can also file by mail, but processing is generally slower. The filing fee is $455 plus an $85 biometrics fee (total $540 as of 2025 — verify at uscis.gov)."),
                    ("After You File", "After filing, you will receive a receipt notice (I-797) that temporarily extends your Green Card's validity for 18 to 24 months. This extension notice, combined with your expired card, can be used as evidence of lawful status for employment (I-9 compliance), travel, and other purposes. You will then receive a biometrics appointment notice, followed eventually by your new card in the mail."),
                    ("Processing Times", "Form I-90 processing times ranged from 12 to 24 months as of 2025, depending on the service center handling your case. Check the USCIS website for current estimates. For urgent situations (employment, travel), consult a professional about expedite options."),
                ],
                "faqs": [
                    ("Is there a penalty for having an expired Green Card?", "Your permanent resident status does not expire — only the card itself does. However, an expired card can cause problems with employment authorization verification (I-9), travel, and accessing certain benefits. Keep it current."),
                    ("Can I travel with an expired Green Card?", "Generally no — airlines and border officers expect a valid card or receipt notice extending validity. If you have the I-90 receipt notice and your expired card, you should be able to re-enter the U.S. after international travel, but check with your airline before departing."),
                    ("What if my Green Card was never delivered?", "File Form I-90 with a basis of 'not received' if your card was mailed but never arrived. Contact the USPS and USCIS first to verify whether it was returned. Also consider changing your address if it may have been delivered to a prior address."),
                    ("Do I need to renew if I'm applying for citizenship?", "You do not need to renew before applying for naturalization, but you do need a valid Green Card for the N-400 biometrics appointment and interview. If your card will expire before those steps, consider renewing it while your N-400 is pending."),
                ],
                "related_within": ["when-to-renew-green-card","green-card-renewal-cost","green-card-lost-or-stolen"],
                "related_cross": [("naturalization","naturalization-eligibility-requirements"),("removal-of-conditions","removal-of-conditions-overview")],
            },
            {
                "slug": "when-to-renew-green-card",
                "title": "When to Renew Your Green Card: Timing Your I-90 Application",
                "meta": "Find out exactly when to file Form I-90 to renew your Green Card — the 6-month window, what happens if your card expires, and tips to avoid gaps.",
                "intro": "Timing your Green Card renewal correctly prevents gaps in your documentation that can disrupt employment verification, travel plans, and access to benefits. Here is what you need to know about the optimal window for filing Form I-90.",
                "body": [
                    ("The 6-Month Filing Window", "USCIS recommends filing Form I-90 within 6 months of your Green Card's expiration date — no sooner. Filing too early may result in rejection. Filing too late risks having an expired card while USCIS processes your renewal, which can cause practical problems even though your underlying permanent resident status is unaffected."),
                    ("What If Your Card Is Already Expired?", "If your Green Card has already expired, file Form I-90 immediately. Your permanent residence has not expired — only the card. USCIS will issue a receipt notice that extends your card's apparent validity, which you can use alongside the expired card for I-9 employment eligibility verification."),
                    ("Planning Around Travel", "If you have international travel planned, time your I-90 filing carefully. Airlines and border officers may not accept an expired card even with a receipt notice at some checkpoints. If you must travel with an expired card, bring your receipt notice and contact the U.S. consulate in your destination country for guidance."),
                    ("Early Renewal Scenario", "If you become a naturalization candidate soon, you may wonder whether to renew your Green Card or just apply for citizenship. If your citizenship application might take longer than your card is valid, renew the card. If you are close to citizenship and processing times suggest you will naturalize within a year, you can often wait — but discuss your situation with a professional before deciding."),
                    ("Reminders to Set Up", "Green Cards expire on the same date each decade from the date they were issued. Set a calendar reminder 7 months before your expiration date so you have 30 days to gather documents and file within the 6-month window."),
                ],
                "faqs": [
                    ("Can I file I-90 more than 6 months before expiration?", "USCIS discourages early filing and may return your application. Wait until you are within 6 months of expiration."),
                    ("Does renewal affect my permanent resident status?", "No. Renewing your card is administrative — it updates your documentation. Your permanent resident status remains intact."),
                    ("What if USCIS takes longer than my card's validity?", "The receipt notice (I-797) you receive after filing extends your card's validity for 18 to 24 months. Use it with your expired card as proof of status."),
                    ("Does my employer need a copy of the receipt notice?", "Your employer can accept the I-90 receipt notice combined with your expired Green Card for I-9 re-verification. Show them both documents."),
                ],
                "related_within": ["green-card-renewal-i-90-complete-guide","green-card-renewal-cost","green-card-lost-or-stolen"],
                "related_cross": [("naturalization","how-long-does-naturalization-take"),("adjustment-of-status","how-long-does-adjustment-of-status-take")],
            },
            {
                "slug": "green-card-renewal-cost",
                "title": "How Much Does Green Card Renewal Cost? I-90 Fees Explained",
                "meta": "Current cost to renew your Green Card with Form I-90 in 2025 — filing fee, biometrics, and tips to avoid unnecessary charges.",
                "intro": "Understanding the cost of Green Card renewal helps you budget and avoid surprises. Here is a complete breakdown of Form I-90 fees for 2025 and what is included.",
                "body": [
                    ("Official USCIS Fees", "As of 2025, the filing fee for Form I-90 online is $455. An additional biometrics fee of $85 is required for most applicants, bringing the total to $540. If filing by mail, the same fees apply. Always verify the current fee at uscis.gov before submitting — fees are updated periodically by regulation."),
                    ("Who Pays Reduced or No Fees?", "Certain groups pay reduced or no fees: some military members and veterans may qualify for fee exemptions; applicants who need to correct USCIS errors on their card file I-90 for free; and some low-income applicants may request a fee waiver using Form I-912 (fee waiver is not always approved for I-90 and depends on circumstances)."),
                    ("The Cost of Preparing the Application", "Beyond the USCIS fee, you may incur costs for professional preparation. A DOJ-accredited representative can prepare and review your I-90 for a fraction of what an attorney charges, while ensuring accuracy and completeness. This is particularly valuable if your case is complicated (name discrepancy, multiple lost cards, or if your card contains errors)."),
                    ("Watch Out for Scams", "Immigration scams targeting Green Card renewal applicants are unfortunately common. Warning signs: someone asks for a large cash payment, promises guaranteed results, or claims to be 'notarios' or 'immigration consultants' without proper accreditation. Always verify that any representative you work with is a DOJ-accredited representative or licensed attorney."),
                    ("Total Budget Example", "A typical Green Card renewal budget: $455 (I-90 filing fee) + $85 (biometrics) + professional preparation assistance (if used) + any document costs (photos, notarization). Most straightforward renewals cost under $600 in government fees alone."),
                ],
                "faqs": [
                    ("Is there a fee waiver for I-90?", "Fee waivers are available for I-90 in limited circumstances. They must be requested via Form I-912 and are based on demonstrated financial hardship. Not all situations qualify."),
                    ("What payment methods does USCIS accept?", "USCIS accepts payment by credit card, debit card, money order, personal check, or cashier's check. Online filing allows credit/debit card payment. Do not send cash."),
                    ("What if I underpay the fee?", "USCIS will reject your application and return it. Always double-check the current fee before submitting."),
                    ("Are there any hidden fees?", "USCIS charges exactly the fees listed. There are no hidden government fees. However, professional service providers charge separately for their assistance, and it is your right to understand all charges before signing any agreement."),
                ],
                "related_within": ["green-card-renewal-i-90-complete-guide","when-to-renew-green-card","green-card-lost-or-stolen"],
                "related_cross": [("naturalization","n-400-documents-checklist"),("adjustment-of-status","adjustment-of-status-documents-checklist")],
            },
            {
                "slug": "green-card-lost-or-stolen",
                "title": "Lost or Stolen Green Card: What to Do and How to Get a Replacement",
                "meta": "Step-by-step guide for replacing a lost, stolen, or damaged Green Card — how to file Form I-90 and protect yourself from identity theft.",
                "intro": "Losing your Green Card is stressful, but it happens. Your permanent resident status does not disappear with the card — what you need is a replacement document as quickly as possible. Here is exactly what to do.",
                "body": [
                    ("Immediate Steps After Discovering Loss or Theft", "First: check thoroughly — retrace your steps and check common locations. Second: report theft to local police and obtain a police report number (useful for I-90 documentation). Third: if you believe your identity may be compromised, contact the Federal Trade Commission (FTC) at identitytheft.gov and consider placing a fraud alert on your credit. Fourth: begin the I-90 process as soon as possible."),
                    ("Filing Form I-90 for a Replacement", "Use Form I-90 with the basis 'My card has been lost, stolen, or destroyed.' Complete the form accurately, including the approximate date and circumstances of the loss. Submit the $455 filing fee plus the $85 biometrics fee. If the card was stolen, attach a copy of the police report."),
                    ("How to Prove Your Status While Waiting", "After filing I-90, you will receive an I-797 receipt notice. This receipt notice does not alone prove your status — you will need to obtain an Arrival/Departure Record from CBP or request an emergency travel document from USCIS if you need to travel urgently. For employment I-9 verification, the receipt notice combined with a List B document (like a state ID) can be used."),
                    ("Emergency Travel Situations", "If you need to travel internationally while waiting for your replacement card, contact the nearest U.S. consulate about options. In some cases, USCIS can issue a temporary transportation letter. Plan ahead — this process takes time."),
                    ("Preventing Future Loss", "Once you receive your new card: make a high-quality color copy and store it separately. Consider scanning it and storing the image securely in a password-protected file. Do not carry your Green Card daily unless necessary — a state driver's license suffices for most everyday identification purposes."),
                ],
                "faqs": [
                    ("Will USCIS know my card was lost if I find it later?", "Keep USCIS informed. If you find the card after filing I-90, you do not need to take special action — simply do not use the old card. USCIS will issue a new one and the old one will be deactivated."),
                    ("Can someone else use my Green Card?", "Your Green Card contains biometric information and is difficult to fraudulently use, but report theft to local police and monitor your credit and immigration records."),
                    ("How long does replacement take?", "Same as a standard renewal — 12 to 24 months currently. There is no fast track for lost/stolen replacements."),
                    ("Do I need a lawyer to replace a lost Green Card?", "It is a straightforward process, but if your card was lost and you are not sure how it affects your travel or employment situation, a professional review is a good investment."),
                ],
                "related_within": ["green-card-renewal-i-90-complete-guide","when-to-renew-green-card","green-card-renewal-cost"],
                "related_cross": [("removal-of-conditions","removal-of-conditions-overview"),("naturalization","naturalization-eligibility-requirements")],
            },
            {
                "slug": "green-card-after-naturalization",
                "title": "What Happens to Your Green Card After You Become a U.S. Citizen?",
                "meta": "Learn what happens to your Green Card when you naturalize, what documents you receive instead, and what to do with your old card.",
                "intro": "One of the most common questions new citizens have is: what do I do with my Green Card after naturalization? The short answer is that the Green Card is no longer needed — but the transition involves some important practical steps.",
                "body": [
                    ("Your Green Card Is Surrendered at the Oath Ceremony", "At the naturalization oath ceremony, USCIS officers collect your Permanent Resident Card. You will sign a form confirming you are surrendering it. From that moment, your identity document is your Certificate of Naturalization — Form N-550 — which you receive at the ceremony."),
                    ("Your Certificate of Naturalization", "The N-550 Certificate of Naturalization is your proof of U.S. citizenship. Guard it carefully — it is expensive and time-consuming to replace. Store it in a fireproof safe or safety deposit box. Make a certified copy and keep the original off-site."),
                    ("Applying for a U.S. Passport", "As a new citizen, your next step is usually applying for a U.S. passport. You can apply at any USPS passport acceptance facility. Bring your N-550 certificate, a completed DS-11 application form, a passport photo, and the applicable fees. First-time adult passports are valid for 10 years."),
                    ("Updating Your Records", "Update your Social Security Administration record to reflect your new citizen status — this can affect benefit eligibility. Notify your employer, bank, and other institutions. If you wish, you can now register to vote in federal, state, and local elections."),
                    ("If You Renewed Your Green Card Shortly Before Naturalizing", "If you recently paid to renew your Green Card and then naturalized before the new card arrived, the card will be issued and then immediately surrendered at the oath ceremony. Unfortunately, the fee is not refunded. This is one reason to time your naturalization and renewal carefully."),
                ],
                "faqs": [
                    ("Can I keep my Green Card as a souvenir?", "No — USCIS collects it at the oath ceremony. You may request a commemorative copy for personal records, but the actual card is surrendered."),
                    ("What if I lose my Certificate of Naturalization?", "File Form N-565 (Application for Replacement Naturalization/Citizenship Document) with USCIS. The fee is $555 as of 2025."),
                    ("Can I use a U.S. passport instead of a Green Card before the ceremony?", "No. Until you take the oath, you are not a citizen. Your Green Card (or valid receipt notice) remains your primary immigration document until then."),
                    ("Can I keep my other country's passport?", "U.S. law does not require you to renounce your other nationality at naturalization (though the oath of allegiance references renouncing foreign allegiances). Many countries do not allow dual citizenship — check your birth country's laws."),
                ],
                "related_within": ["green-card-renewal-i-90-complete-guide","when-to-renew-green-card","green-card-renewal-cost"],
                "related_cross": [("naturalization","naturalization-eligibility-requirements"),("naturalization","how-long-does-naturalization-take")],
            },
        ]
    },
    {
        "slug": "student-visa",
        "name": "Student Visa",
        "service_url": "/en/services/",
        "desc": "Everything international students need to know about F-1 visas, OPT, maintaining status, and pathways to U.S. permanent residence.",
        "hero_subtitle": "Your complete guide to F-1 student visa applications, OPT and STEM OPT extensions, maintaining status, and the path from student to permanent resident.",
        "articles": [
            {
                "slug": "f1-student-visa-complete-guide",
                "title": "F-1 Student Visa: Complete Guide for International Students in the U.S.",
                "meta": "Everything international students need to know about the F-1 visa — how to get one, how to maintain status, work authorization, and more.",
                "intro": "The F-1 student visa is the most common nonimmigrant visa for international students attending U.S. academic institutions. Whether you are applying for the first time or trying to understand your rights and responsibilities as an F-1 holder, this guide covers the essentials.",
                "body": [
                    ("What Is the F-1 Visa?", "The F-1 nonimmigrant visa allows foreign nationals to study at accredited U.S. colleges, universities, seminaries, conservatories, academic high schools, elementary schools, and language training programs. The F-1 status is tied to your enrollment in a SEVP-certified institution and is maintained as long as you comply with specific rules."),
                    ("How to Obtain an F-1 Visa", "To obtain an F-1 visa, you must: (1) be accepted to a SEVP-certified school, (2) receive a Form I-20 from your school's Designated School Official (DSO), (3) pay the SEVIS fee (currently $350), (4) apply at a U.S. consulate or embassy in your home country with your I-20, valid passport, proof of financial support, and DS-160 visa application, and (5) attend a visa interview. If you are already in the U.S. on another status, you may be able to change status without leaving."),
                    ("Maintaining F-1 Status", "To maintain valid F-1 status you must: enroll full-time every semester (exceptions require DSO authorization), make normal academic progress toward your degree, report changes of address to your DSO within 10 days, not work without authorization, keep your passport valid, and maintain a valid I-20. Violations can jeopardize your status and lead to removal."),
                    ("On-Campus vs. Off-Campus Work", "F-1 students may work on campus up to 20 hours per week during school and full-time during breaks. Off-campus work requires specific authorization: Curricular Practical Training (CPT) for jobs related to your major, or Optional Practical Training (OPT) after completing your degree. Unauthorized employment is a serious status violation."),
                    ("The Duration of Status (D/S) Concept", "Your F-1 visa stamp has an expiration date, but your status is authorized 'Duration of Status' (D/S) — meaning you are authorized to stay as long as you maintain valid enrollment and comply with F-1 rules. The visa stamp expiration and your status authorization are separate concepts that confuse many students."),
                ],
                "faqs": [
                    ("Can I travel outside the U.S. with an F-1 visa?", "Yes, if your visa stamp is still valid. If your visa has expired, you must obtain a new F-1 visa stamp at a U.S. consulate abroad before re-entering the U.S. Your DSO must sign your I-20 for travel."),
                    ("Can my family accompany me on an F-2 visa?", "Yes. Your spouse and unmarried children under 21 can apply for F-2 dependent visas. F-2 holders cannot work in the U.S."),
                    ("What is a SEVIS record?", "SEVIS (Student and Exchange Visitor Information System) is the database that tracks F-1 students. Your school maintains your SEVIS record and notifies the government if you fall out of status."),
                    ("What happens if I fail or withdraw from classes?", "Dropping below full-time status or withdrawing without DSO authorization violates your F-1 status. Contact your DSO immediately if you are considering any course load change."),
                ],
                "related_within": ["opt-stem-opt-guide","f1-visa-to-green-card-paths","f1-status-violations"],
                "related_cross": [("adjustment-of-status","what-is-adjustment-of-status"),("naturalization","naturalization-eligibility-requirements")],
            },
            {
                "slug": "opt-stem-opt-guide",
                "title": "OPT and STEM OPT: Work Authorization for F-1 Students After Graduation",
                "meta": "Complete guide to F-1 OPT and STEM OPT work authorization — how to apply, eligibility, deadlines, and how to extend your stay after graduation.",
                "intro": "Optional Practical Training (OPT) is one of the most important benefits available to F-1 students — it allows you to work in the U.S. in a job related to your field of study for up to 12 months (or 36 months for STEM graduates). Missing OPT deadlines is one of the most common and costly mistakes international students make.",
                "body": [
                    ("What Is OPT?", "OPT is work authorization available to F-1 students for practical training directly related to their major area of study. You have two types: Pre-Completion OPT (before you finish your degree) and Post-Completion OPT (after graduation, the most common). Standard OPT lasts 12 months."),
                    ("Applying for OPT: Timeline Is Critical", "You can apply for OPT up to 90 days before your graduation date and must apply no later than 60 days after your program end date. USCIS takes 3 to 5 months to process OPT applications, so apply early. Your DSO first issues an OPT I-20, and then you file Form I-765 with USCIS."),
                    ("STEM OPT Extension", "If you graduated with a degree in Science, Technology, Engineering, or Mathematics (STEM), you may qualify for a 24-month STEM OPT extension — giving you a total of 36 months of OPT work authorization. To apply, you must: be working for an E-Verify employer, have your employer sign Form I-983 (Training Plan), and apply within 60 days of your standard OPT expiration date."),
                    ("The Cap-Gap for H-1B Applicants", "If your employer files an H-1B petition for you during the annual lottery (filed April 1, starting October 1), and your OPT expires before October 1, a special 'cap-gap' rule automatically extends your OPT through September 30. This allows you to continue working without interruption while awaiting H-1B approval."),
                    ("What If OPT Is Denied or Delayed?", "OPT denials are rare but do occur — usually for late applications, incomplete filings, or eligibility issues. If denied, you cannot legally work. Delays are more common — apply as early as possible. If your EAD (work permit) does not arrive before your OPT start date, you cannot begin work until it does."),
                ],
                "faqs": [
                    ("Can I change jobs during OPT?", "Yes, as long as your new job is related to your field of study. Report employer changes to your DSO within 10 days. Unemployment periods during OPT are limited to 90 days total."),
                    ("What STEM degrees qualify for the extension?", "USCIS uses an approved STEM designated degree program list, updated periodically. Common qualifying fields include computer science, engineering, mathematics, physics, chemistry, biology, and business analytics."),
                    ("Can I use OPT to work for multiple employers?", "Yes, but each employer must be related to your field of study. If you are self-employed, your business must be in your field of study."),
                    ("Does OPT count toward the 5-year Green Card wait?", "No. F-1/OPT is nonimmigrant status and does not count toward the 5-year (or 3-year) continuous residence requirement for naturalization. Only time as a permanent resident counts."),
                ],
                "related_within": ["f1-student-visa-complete-guide","f1-visa-to-green-card-paths","f1-status-violations"],
                "related_cross": [("adjustment-of-status","what-is-adjustment-of-status"),("adjustment-of-status","how-long-does-adjustment-of-status-take")],
            },
            {
                "slug": "f1-visa-to-green-card-paths",
                "title": "F-1 Visa to Green Card: Pathways from Student Status to Permanent Residence",
                "meta": "Explore the main pathways for F-1 students to obtain a U.S. Green Card — employment-based, marriage, and other routes explained.",
                "intro": "Transitioning from F-1 student status to permanent residence is a goal for many international students. While the path is not automatic, there are multiple routes — and planning ahead significantly improves your chances.",
                "body": [
                    ("Employment-Based Green Card (EB Categories)", "The most common path for F-1 graduates: find a U.S. employer willing to sponsor you for permanent residence. Typically, this involves: (1) H-1B work visa sponsorship while employed, (2) PERM labor certification (proving no qualified U.S. worker is available), (3) Form I-140 (immigrant petition), and (4) I-485 adjustment of status. The timeline can be 5 to 10+ years depending on your country of birth and visa preference category."),
                    ("Marriage to a U.S. Citizen", "Marrying a U.S. citizen while on F-1 status can lead to a Green Card through family-based immigration. Your spouse files Form I-130, and if you are in valid F-1 status in the U.S., you may be able to adjust status without leaving. The marriage must be genuine — immigration authorities scrutinize international student marriages carefully."),
                    ("EB-1 for Extraordinary Ability or Researchers", "If you are a researcher, scientist, or academic with exceptional achievements — top publications, awards, significant contributions to your field — you may qualify for EB-1A (extraordinary ability) or EB-1B (outstanding researcher) without an employer sponsor in some cases. These categories are highly selective but have faster processing."),
                    ("Transitioning to H-1B First", "Most F-1 graduates pursue H-1B sponsorship as a first step. The H-1B annual lottery (cap) takes place every April. If selected, you transition to H-1B on October 1 and can work in specialty occupations. Many employers then begin Green Card sponsorship during H-1B employment."),
                    ("Timing Is Everything", "If you want a Green Card, start planning before you graduate. Talk to your employer about their immigration sponsorship policies during recruitment. Understand your country's visa priority date backlog (India and China face decades-long waits in employment-based categories). Explore all options with a qualified professional early."),
                ],
                "faqs": [
                    ("Can I apply for a Green Card while on OPT?", "Yes, in theory — but OPT is temporary and adjustment of status while on OPT requires active F-1 status and an approved immigrant petition. The specifics depend on your case. Consult a professional before your OPT ends."),
                    ("Does the H-1B lottery limit my chances?", "Yes. The annual H-1B cap is 85,000 visas and demand far exceeds supply. Selection is random. Some applicants apply for multiple years. Cap-exempt employers (nonprofits, government entities, universities) do not participate in the lottery."),
                    ("Can I self-petition for a Green Card as an F-1 student?", "In rare cases — EB-1A for extraordinary ability or EB-2 NIW (National Interest Waiver) — you may self-petition without an employer sponsor. These require demonstrating exceptional achievement or national interest."),
                    ("What if I fall out of F-1 status before getting a Green Card?", "This can seriously complicate your path. Some unlawful presence issues create bars to re-entry. Consult a professional immediately if you have any status concerns."),
                ],
                "related_within": ["f1-student-visa-complete-guide","opt-stem-opt-guide","f1-status-violations"],
                "related_cross": [("adjustment-of-status","what-is-adjustment-of-status"),("adjustment-of-status","how-long-does-adjustment-of-status-take")],
            },
            {
                "slug": "f1-status-violations",
                "title": "F-1 Status Violations: What Can Jeopardize Your Student Visa",
                "meta": "Learn the most common F-1 status violations — unauthorized work, enrollment drops, and travel errors — and how to fix them before it's too late.",
                "intro": "F-1 status violations are more common than most students realize, and they can have serious consequences — including removal from the U.S. and bars to re-entry. Understanding the rules is the best protection against accidental violations.",
                "body": [
                    ("Unauthorized Employment", "Working without authorization is one of the most serious F-1 violations. F-1 students may only work on campus (up to 20 hours during school) or off campus with specific authorization (CPT, OPT). Working any other jobs — including under the table — violates your status, can terminate your SEVIS record, and may result in removal."),
                    ("Dropping Below Full-Time Enrollment", "F-1 students must be enrolled full-time (usually 12 credit hours for undergrad, 9 for grad students) every semester unless your DSO authorizes a reduced course load (RCL) for specific reasons: medical condition, initial semester adjustment, or final semester with fewer required courses. Dropping below full-time without authorization violates status."),
                    ("Failing to Update Address", "You must report any address change to your DSO within 10 days and update your SEVIS record. Failure to do so is a technical violation and can complicate your record."),
                    ("Unauthorized School Transfer", "Transferring to a new school requires a formal SEVIS transfer through your current DSO before the transfer-out date. Simply enrolling in a new school without completing the transfer process is a status violation."),
                    ("Overstaying or Unauthorized Travel", "If you travel internationally and your F-1 visa has expired, you must obtain a new visa abroad before re-entering the U.S. If you remain outside the U.S. for more than 5 months, you may lose your F-1 status and need to reapply. Always consult your DSO before international travel."),
                    ("What to Do If You Have Violated Status", "If you believe you have violated F-1 status: contact your DSO immediately. They can help assess whether reinstatement is possible. You can apply to USCIS for reinstatement of F-1 status (Form I-539) if the violation was not your fault, you have not been out of status for more than 5 months, and you have maintained a full course of study since the violation. Alternatively, you can depart and re-enter on a new F-1 visa — but this has its own risks."),
                ],
                "faqs": [
                    ("What is a SEVIS termination?", "If your DSO terminates your SEVIS record due to a status violation, your F-1 status is no longer valid. You cannot remain in the U.S. in F-1 status without an active SEVIS record."),
                    ("Can I reinstate my F-1 status?", "USCIS allows reinstatement for some violations. Criteria include: violation was beyond your control, you have not been out of status more than 5 months, you have not committed certain crimes, and you are currently enrolled full-time."),
                    ("Does a status violation prevent me from getting a Green Card?", "It depends on the type and severity. Some violations create periods of unlawful presence that trigger bars to admission. Others are more manageable. Consult a professional as soon as you are aware of a potential violation."),
                    ("What is 'unlawful presence' and how does it affect me?", "Unlawful presence is time spent in the U.S. after your authorized period of stay has ended. F-1 students on D/S status do not begin accruing unlawful presence until a formal finding of a status violation (by USCIS or an immigration judge), or when the status-violation-triggering event occurs — this is a nuanced area where professional guidance is essential."),
                ],
                "related_within": ["f1-student-visa-complete-guide","opt-stem-opt-guide","f1-visa-to-green-card-paths"],
                "related_cross": [("adjustment-of-status","adjustment-of-status-denial-reasons"),("naturalization","naturalization-eligibility-requirements")],
            },
            {
                "slug": "f1-visa-extension-and-transfer",
                "title": "F-1 Visa Extension and School Transfer: What Students Need to Know",
                "meta": "How to extend your F-1 program, transfer to a new school, and update your SEVIS record — a guide for current F-1 visa holders.",
                "intro": "International students frequently need to extend their program or transfer to a new institution. Both processes involve your SEVIS record and require coordination with your Designated School Official (DSO). Here is how to do it correctly.",
                "body": [
                    ("Extending Your F-1 Program", "If you need more time to complete your degree — due to a change of major, part-time study authorization, or other academic reasons — your DSO can extend your I-20 program end date in SEVIS. There is no separate USCIS filing required for a program extension, but your DSO must update your record before your current program end date. You cannot remain in the U.S. after your program ends without either an extension or a new status."),
                    ("Preparing for a School Transfer", "To transfer between SEVP-certified schools: (1) get accepted at the new school, (2) notify your current DSO that you plan to transfer, (3) your current DSO sets a 'release date' in SEVIS (often the end of the current semester), (4) your new school's DSO issues a new I-20 after the release date. You cannot begin at the new school before the release date without risking a status violation."),
                    ("What to Do at the New School", "At the new school, report to the international student office within 15 days of the program start date on your new I-20. The DSO will update your SEVIS record to active at the new school. Keep copies of all I-20s and transfer documentation."),
                    ("Transferring Your F-1 Visa Stamp", "Your F-1 visa stamp does not need to be transferred — it remains valid as long as it has not expired and you maintain valid F-1 status. When you next travel abroad, you may need to obtain a new F-1 visa reflecting your new school if the old visa lists your previous institution (some consulates require this, others do not — check with the relevant consulate)."),
                    ("Transferring to a Non-SEVP School", "If you want to transfer to a school that is not SEVP-certified, you cannot maintain F-1 status while attending that school. You would need to change to a different visa category or adjust status through another immigration pathway. Verify your school's SEVP certification at the Study in the States SEVP school search tool."),
                ],
                "faqs": [
                    ("Can I transfer schools if I have a CPT authorization?", "CPT is granted by your current school for employment related to your current program. Transferring schools terminates your enrollment at the current school, which ends your CPT authorization. OPT that has already been approved continues to be valid after a school transfer."),
                    ("What if my new school is in a different state?", "The transfer process is the same regardless of location. You still coordinate through your DSO and complete the SEVIS transfer. If you move, update your address with your DSO within 10 days."),
                    ("How long can I stay in the U.S. between schools?", "Your authorized stay is tied to your SEVIS record. Once your current school releases your SEVIS record, you typically have a short window before the new school's program start date. Talk to your DSO about timing to avoid any gap in valid status."),
                    ("Can I take a semester off?", "F-1 students are required to be enrolled full-time. A voluntary leave of absence is generally not allowed without changing status. Some schools have approved medical or personal leave policies — talk to your DSO and international student office before making any enrollment decisions."),
                ],
                "related_within": ["f1-student-visa-complete-guide","f1-status-violations","opt-stem-opt-guide"],
                "related_cross": [("adjustment-of-status","what-is-adjustment-of-status"),("naturalization","naturalization-eligibility-requirements")],
            },
        ]
    },
]

# ── Article slug → title index (for related links) ────────────────────────────
ARTICLE_INDEX = {}
for cl in CLUSTERS:
    for art in cl["articles"]:
        ARTICLE_INDEX[(cl["slug"], art["slug"])] = art["title"]

# ── Render helpers ─────────────────────────────────────────────────────────────
def render_sections(sections):
    html = ""
    for heading, text in sections:
        html += f"<h2>{heading}</h2>\n<p>{text}</p>\n"
    return html

def render_faqs(faqs, cluster_slug, article_slug):
    schema_faqs = []
    html = '<section class="nhv-faqs"><h2>Frequently Asked Questions</h2>\n'
    for q, a in faqs:
        html += f'<div class="nhv-faq-item"><h3>{q}</h3><p>{a}</p></div>\n'
        schema_faqs.append({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}})
    html += '</section>\n'
    schema = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":schema_faqs}, indent=2)
    return html, f'<script type="application/ld+json">{schema}</script>'

def render_related(related_within, related_cross, cluster_slug):
    items = []
    for slug in related_within[:3]:
        key = (cluster_slug, slug)
        if key in ARTICLE_INDEX:
            title = ARTICLE_INDEX[key]
            label = next((cl["name"] for cl in CLUSTERS if cl["slug"]==cluster_slug), "")
            items.append((f"/en/blog/{cluster_slug}/{slug}/", label, title))
    for (cslug, aslug) in related_cross[:2]:
        key = (cslug, aslug)
        if key in ARTICLE_INDEX:
            title = ARTICLE_INDEX[key]
            label = next((cl["name"] for cl in CLUSTERS if cl["slug"]==cslug), "")
            items.append((f"/en/blog/{cslug}/{aslug}/", label, title))
    if not items:
        return ""
    html = '<section style="margin-top:56px;"><h2 style="font-size:22px;font-weight:800;color:#0f172a;margin:0 0 20px;">Related Articles</h2><div class="nhv-related-grid">'
    for href, label, title in items:
        html += f'<a class="nhv-related-card" href="{href}"><span>{label}</span><strong>{title}</strong></a>'
    html += '</div></section>'
    return html

def article_schema(cluster, article, url):
    return json.dumps({
        "@context":"https://schema.org",
        "@type":"Article",
        "headline": article["title"],
        "description": article["meta"],
        "url": f"https://newhopevisa.com{url}",
        "publisher": {
            "@type":"Organization",
            "name":"New Hope Immigration Services",
            "url":"https://newhopevisa.com",
            "logo":{"@type":"ImageObject","url":"https://newhopevisa.com/wp-content/uploads/2023/06/new-hope-logo.png"}
        },
        "author":{"@type":"Organization","name":"New Hope Immigration Services"},
        "inLanguage":"en-US",
        "mainEntityOfPage":{"@type":"WebPage","@id":f"https://newhopevisa.com{url}"}
    }, indent=2)

# ── Generate articles ──────────────────────────────────────────────────────────
generated = 0

for cluster in CLUSTERS:
    cslug = cluster["slug"]
    cname = cluster["name"]

    for article in cluster["articles"]:
        aslug = article["slug"]
        url = f"/en/blog/{cslug}/{aslug}/"
        out_path = f"{OUT}/{cslug}/{aslug}/index.html"

        bc = breadcrumb(cslug, cname, article["title"])
        body_html = render_sections(article["body"])
        faq_html, faq_schema = render_faqs(article["faqs"], cslug, aslug)
        related_html = render_related(article["related_within"], article["related_cross"], cslug)

        cta1 = cta_box(
            "Need Help With Your Case?",
            "Our DOJ-accredited team serves immigrants in Orlando and across Florida. Get answers in a $50 consultation.",
            "Schedule a Consultation →",
            f"/en/contact-us/?src=blog-cta1&cluster={cslug}"
        )
        cta2 = cta_box(
            "Questions About Your Situation?",
            "Every immigration case is different. Our team can review your documents and explain your options.",
            "Call (407) 275-6163",
            "tel:+14072756163"
        )
        cta3 = cta_box(
            f"Ready to Start Your {cname} Case?",
            "New Hope Immigration Services is a DOJ-accredited nonprofit. We help families across Central Florida.",
            f"Learn About Our {cname} Services →",
            cluster["service_url"]
        )

        schema_js = article_schema(cluster, article, url)
        og_extra = f'<meta property="og:url" content="https://newhopevisa.com{url}">'

        html = head(article["title"] + " | New Hope Immigration", article["meta"], url, og_extra)
        html += f"""
<main style="padding-top:0;">
  <div style="background:#f8fafc;border-bottom:1px solid #e2e8f0;padding:12px 20px;">
    <div style="max-width:820px;margin:0 auto;">{bc}</div>
  </div>
  <div class="nhv-blog-wrap">
    <header class="nhv-article-header">
      <div class="nhv-article-meta" style="margin-bottom:14px;">
        <span class="nhv-badge">{cname}</span>
        <span>New Hope Immigration Services</span>
        <span>Orlando, FL</span>
      </div>
      <h1>{article["title"]}</h1>
      <p style="font-size:17px;color:#475569;margin:0;line-height:1.7;">{article["intro"]}</p>
    </header>
    <div class="nhv-article-body">
      {cta1}
      {body_html}
      {cta2}
      {faq_html}
      {cta3}
      {related_html}
    </div>
  </div>
</main>
{FOOTER}
<script type="application/ld+json">{schema_js}</script>
{faq_schema}
<script src="/exit-popup.js" defer></script>
</body></html>"""

        write(out_path, html)
        generated += 1

# ── Generate cluster hub pages ─────────────────────────────────────────────────
for cluster in CLUSTERS:
    cslug = cluster["slug"]
    cname = cluster["name"]
    url = f"/en/blog/{cslug}/"
    out_path = f"{OUT}/{cslug}/index.html"

    cards_html = ""
    for art in cluster["articles"]:
        cards_html += f"""<article class="nhv-article-card">
  <h3>{art["title"]}</h3>
  <p>{art["meta"][:130]}…</p>
  <a class="hub-card-link" href="/en/blog/{cslug}/{art["slug"]}/">Read article →</a>
</article>\n"""

    # Checklist card (6th card)
    cards_html += f"""<article class="nhv-article-card hub-article-checklist">
  <h3>{cname} Document Checklist</h3>
  <p>Interactive step-by-step checklist to help you gather every document before your {cname} appointment.</p>
  <a class="hub-card-link" href="/en/blog/{cslug}/checklist/">Open checklist →</a>
</article>\n"""

    hub_schema = json.dumps({
        "@context":"https://schema.org","@type":"CollectionPage",
        "name":f"{cname} Guide — New Hope Immigration",
        "url":f"https://newhopevisa.com{url}",
        "publisher":{"@type":"Organization","name":"New Hope Immigration Services"}
    }, indent=2)

    html = head(f"{cname} Guide | New Hope Immigration", cluster["desc"], url)
    html += f"""
<main>
  <div class="nhv-hub-hero">
    <div style="max-width:1100px;margin:0 auto;">
      <p style="font-size:13px;text-transform:uppercase;letter-spacing:1px;opacity:.6;margin:0 0 12px;">New Hope Immigration Services · Blog</p>
      <h1>{cname}</h1>
      <p>{cluster["hero_subtitle"]}</p>
    </div>
  </div>
  <div class="nhv-hub-articles">
    <div style="margin-bottom:20px;">{breadcrumb(cslug, cname)}</div>
    <h2>All {cname} Articles</h2>
    <div class="nhv-article-grid">{cards_html}</div>
    <div style="margin-top:48px;">{cta_box("Have Questions?","Our DOJ-accredited team can review your case and explain your options in a $50 consultation.","Schedule a Consultation →","/en/contact-us/?src=hub-cta")}</div>
  </div>
</main>
{FOOTER}
<script type="application/ld+json">{hub_schema}</script>
<script src="/exit-popup.js" defer></script>
</body></html>"""

    write(out_path, html)
    generated += 1

# ── Blog index page ────────────────────────────────────────────────────────────
url = "/en/blog/"
out_path = f"{OUT}/index.html"
cluster_sections = ""

for cluster in CLUSTERS:
    cslug = cluster["slug"]
    cname = cluster["name"]
    top3 = cluster["articles"][:3]
    mini_cards = ""
    for art in top3:
        mini_cards += f"""<article class="nhv-article-card">
  <h3>{art["title"]}</h3>
  <p>{art["meta"][:110]}…</p>
  <a class="hub-card-link" href="/en/blog/{cslug}/{art["slug"]}/">Read →</a>
</article>\n"""

    cluster_sections += f"""<section class="nhv-cluster-section">
  <h2><a href="/en/blog/{cslug}/" style="color:#0f172a;text-decoration:none;">{cname}</a></h2>
  <p class="cluster-desc">{cluster["desc"]}</p>
  <div class="nhv-article-grid">{mini_cards}</div>
  <p style="margin-top:16px;"><a href="/en/blog/{cslug}/" style="font-weight:700;color:#469A3D;font-size:14px;">See all {cname} articles →</a></p>
</section>\n"""

index_schema = json.dumps({
    "@context":"https://schema.org","@type":"Blog",
    "name":"New Hope Immigration Services Blog",
    "url":"https://newhopevisa.com/en/blog/",
    "description":"Immigration guides in plain English — adjustment of status, naturalization, Green Card renewal, and more from New Hope Immigration Services in Orlando, FL.",
    "publisher":{"@type":"Organization","name":"New Hope Immigration Services","url":"https://newhopevisa.com"}
}, indent=2)

html = head("Immigration Blog | New Hope Immigration Services", "Plain-English immigration guides covering adjustment of status, naturalization, Green Card renewal, student visas, and more — from Orlando's DOJ-accredited nonprofit.", url)
html += f"""
<main>
  <div class="nhv-index-hero">
    <div style="max-width:820px;margin:0 auto;">
      <p style="font-size:13px;text-transform:uppercase;letter-spacing:1px;opacity:.5;margin:0 0 12px;">New Hope Immigration Services</p>
      <h1>Immigration Guides in Plain English</h1>
      <p>Adjustment of status, naturalization, Green Card renewal, removal of conditions, student visas — explained clearly by Orlando's DOJ-accredited nonprofit.</p>
    </div>
  </div>
  {cluster_sections}
  <div style="max-width:1100px;margin:0 auto;padding:0 20px 80px;">
    {cta_box("Ready to Take the Next Step?","Our team serves immigrants across Central Florida. $50 consultation — online or in person in Orlando.","Contact New Hope Immigration →","/en/contact-us/?src=blog-index")}
  </div>
</main>
{FOOTER}
<script type="application/ld+json">{index_schema}</script>
<script src="/exit-popup.js" defer></script>
</body></html>"""

write(out_path, html)
generated += 1

print(f"Generated {generated} files total")
print(f"  25 articles + 5 hubs + 1 index = 31 expected")

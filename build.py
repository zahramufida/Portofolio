import html
EMAIL="zahramufida1410@gmail.com"
IG="https://www.instagram.com/zahramufida1410/"
GH_NAME="zahramufida"
GH="https://github.com/"+GH_NAME

FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,400..600,100,1;1,9..144,400..600,100,1&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'

PROJECTS=[
 dict(name="SurabayArt",cat="web",c="c1",tags=["React","Supabase"],link="https://github.com/reisatanzil/surabayaart",
  d="A ticketing platform with a post-payment ticket flow, customer reviews and merchandise management for organizers. I also audited its ticket and payment flow against Nielsen's usability heuristics."),
 dict(name="NALAR",cat="mobile",c="c2",tags=["Flutter","Firebase","Supabase"],link=None,
  d="A learning management app with role-based access, class join-by-code and assignment submission. I moved file storage from Firebase to Supabase."),
 dict(name="DisAccess",cat="mobile",c="c3",tags=["Mobile","Accessibility","Gherkin"],link=None,
  d="A mobile app for accessible campus navigation at Universitas Airlangga, with complete feature specifications and user scenarios written in Behat/Gherkin."),
 dict(name="SATUDUKA",cat="systems",c="c4",tags=["BPMN","Use case","SRS"],link=None,
  d="Digitalizing death registration and administration for Kota Yogyakarta. Our team mapped the As-Is and To-Be processes and wrote the use cases, wireframes and software requirements."),
 dict(name="SIRKUL.KOPI",cat="systems competition",c="c5",tags=["Circular economy","PFmuda 2026"],link=None,
  d="A social entrepreneurship venture on circular economy and community empowerment, entered in PFmuda 2026. I built financial visualizations, a website mockup and an admin dashboard."),
 dict(name="Smart Parking",cat="web competition",c="c6",tags=["ESP32","Firebase","React","Flask"],link=None,
  d="An IoT parking reservation system for GEMASTIK 2026, connecting ESP32 sensors to a React and Flask web app."),
]
FILTERS=[("all","All"),("web","Web"),("mobile","Mobile"),("systems","Systems analysis"),("competition","Competitions")]

EXP=[
 ("2026","Coordinator, External","Pointer (new student orientation, study program)",["Built and maintained professional relationships with external parties to support the event's objectives and opportunities."]),
 ("2026","Coordinator, Marketing","Sci Fest 2026",["Coordinated a national-level competition with an eight-member team to keep planning and execution smooth."]),
 ("November 2025","Coordinator, Sponsorship and Fundraising","Airlangga Convention 3.0",["Led a team of more than five members, keeping workflow, communication and deadlines on track.","Worked with more than three major brands to build lasting partnerships.","Aligned goals across internal divisions to support cross-functional projects."]),
 ("October to November 2025","Staff Event and Moderator","Reformafest 2025 (National Debate Competition)",["Moderated the \u201cCakap Bicara\u201d talk show with prominent organizational speakers, guiding the discussion and the audience."]),
 ("February to December 2025","Expert Staff, Public Relations","HIMSI (Himpunan Mahasiswa Sistem Informasi)",["Coordinated two comparative study programs with external partners.","Strengthened the organization's branding and its relationships with external stakeholders.","Planned and ran events with a team of 10 members."]),
 ("February to December 2025","Best Staff","HIMSI (Himpunan Mahasiswa Sistem Informasi)",["Took part in more than five organizational committees, from planning to event day.","Kept communication clear with internal and external stakeholders."]),
]

# Add your certificates here. Example:
# dict(title="Belajar Dasar AI", issuer="Dicoding Indonesia", date="Sep 2025", tags=["AI","ML"], link="https://...")
CERTS=[
 dict(title="Getting Started with Cisco Packet Tracer",issuer="Cisco Networking Academy, offered by Universitas Airlangga",date="19 Feb 2026",tags=["Networking","Packet Tracer"],link="assets/certificates/cisco-packet-tracer.pdf"),
 # Next: Junior Web Programming (add title, issuer, date and PDF here)
]

def nav(active):
    items=[("index.html","Home"),("about.html","About"),("projects.html","Projects")]
    cur=' aria-current="page"'
    lis=""
    for h,t in items:
        c=cur if h==active else ""
        lis+='<li><a href="%s"%s>%s</a></li>' % (h,c,t)
    cc=cur if active=="contact.html" else ""
    cta='<li><a class="cta" href="contact.html"%s>Say hello</a></li>' % cc
    return '''<header class="nav"><div class="wrap"><div class="nav-in">
<a class="logo" href="index.html" aria-label="Zahra Mufida, home">Zahra.</a>
<button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
<ul class="menu">%s%s</ul></div></div></header>''' % (lis,cta)

FOOT=f'''<footer class="footer"><div class="wrap footer-in">
<div><a class="logo" href="index.html">Zahra.</a><br><small>&copy; 2026 Zahra Mufida. All rights reserved.</small></div>
<nav aria-label="Footer"><a href="about.html">About</a><a href="projects.html">Projects</a><a href="contact.html">Contact</a><a href="{GH}">GitHub</a><a href="{IG}">Instagram</a><a href="mailto:{EMAIL}">Email</a></nav>
</div></footer>'''

def page(fn,title,desc,body,active):
    out=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/zahra.jpg">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
{FONTS}<link rel="stylesheet" href="css/style.css"></head>
<body><a class="skip" href="#main">Skip to content</a>
{nav(active)}
<main id="main">{body}</main>
{FOOT}
<script src="js/main.js"></script></body></html>'''
    open(fn,"w",encoding="utf-8").write(out)

def card(p):
    link=f'<a class="more" href="{p["link"]}" target="_blank" rel="noopener">View on GitHub</a>' if p["link"] else ""
    tags="".join(f'<span class="tag">{t}</span>' for t in p["tags"])
    return f'''<article class="card" data-cat="{p["cat"]}"><div class="cover {p["c"]}"><b>{p["name"]}</b></div>
<div class="body"><p>{html.escape(p["d"],quote=False)}</p>{link}<div class="tags">{tags}</div></div></article>'''

def tool(n,icon):
    return f'<div class="tool"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{icon}.svg" alt="" width="28" height="28" onerror="this.remove()">{n}</div>'
TOOLS="".join(tool(n,i) for n,i in [("React","react/react-original"),("Tailwind CSS","tailwindcss/tailwindcss-original"),("Supabase","supabase/supabase-original"),("Flutter","flutter/flutter-original"),("Firebase","firebase/firebase-plain"),("Python","python/python-original"),("Flask","flask/flask-original")])
TOOLS+="".join(f'<div class="tool text">{t}</div>' for t in ["BPMN","UML","DFD"])

# ---------- HOME ----------
home=f'''
<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<p class="hello">Hello, I'm</p>
<h1>Zahra Mufida</h1>
<p class="lead">An Information Systems student who turns busy ideas into organized systems, well-run events and apps people can actually use.</p>
<div class="actions"><a class="btn solid" href="projects.html">View my work</a><a class="btn ghost" href="assets/Zahra-Mufida-CV.pdf" download>Download CV</a></div>
</div>
<div class="hero-art">
<div class="arch"><img src="assets/zahra.jpg" alt="Portrait of Zahra Mufida in a white shirt and a teal batik scarf" width="768" height="960"></div>
<div class="sticker">Information Systems at UNAIR</div>
<aside class="planner" aria-label="Zahra's planner for today"><h4>zahra_today</h4>
<ul><li class="done"><i class="box"></i><span>Reply to sponsors</span></li><li class="done"><i class="box"></i><span>Moderate the talk show</span></li><li><i class="box"></i><span>Ship the next feature</span></li><li><i class="box"></i><span>Sleep 8 hours</span></li></ul>
<p class="note">...rescheduled again</p></aside>
</div></div></section>

<section class="section white"><div class="wrap">
<div class="section-head"><div><h2>Tools I work with</h2><p>What I use to design, build and document software.</p></div><a class="btn ghost" href="about.html">See all skills</a></div>
<div class="tools">{TOOLS}</div></div></section>

<section class="section"><div class="wrap">
<div class="section-head"><div><h2>Featured work</h2><p>Apps and systems from my coursework, competitions and side projects.</p></div><a class="btn ghost" href="projects.html">All projects</a></div>
<div class="grid">{"".join(card(p) for p in PROJECTS[:3])}</div></div></section>

<section class="section tint"><div class="wrap">
<div class="section-head"><div><h2>Where I've led</h2><p>Beyond code, I run the people side of campus events and partnerships.</p></div><a class="btn ghost" href="about.html#experience">Full experience</a></div>
<div class="lead-list">
<div class="lead-item"><h3>Sponsorship and fundraising</h3><p>Led the sponsorship team for Airlangga Convention 3.0 and worked with more than three major brands.</p></div>
<div class="lead-item"><h3>Marketing and external relations</h3><p>Coordinating marketing for Sci Fest 2026 and external partners for the Pointer orientation.</p></div>
<div class="lead-item"><h3>Public relations</h3><p>Two years of HIMSI work, including comparative studies with external partners and a Best Staff title.</p></div>
</div></div></section>

<section class="section"><div class="wrap"><div class="band"><h2>Have a project, event or team that needs me?</h2><a class="btn" href="contact.html">Say hello</a></div></div></section>
'''
page("index.html","Zahra Mufida | Information Systems Student","Portfolio of Zahra Mufida, an Information Systems student at Universitas Airlangga who builds apps, systems and well-run events.",home,"index.html")

# ---------- ABOUT ----------
tl="".join(f'<li><p class="when">{w}</p><h3>{r}</h3><p class="org">{o}</p><ul>{"".join(f"<li>{b}</li>" for b in bl)}</ul></li>' for w,r,o,bl in EXP)
skills=[("Communication and teamwork",["Active listening","Public speaking","Moderating","Stakeholder relations"]),
 ("Leadership",["Team coordination","Sponsorship","Time management","Task prioritization"]),
 ("Build",["React","Tailwind CSS","Supabase","Flutter","Firebase","Python"]),
 ("Analyze and document",["BPMN","UML","DFD","Use cases","Microsoft Excel","Microsoft Word","PowerPoint"])]
sk="".join(f'<div class="skill-box"><h3>{t}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for t,items in skills)
def cert_card(c):
    tags="".join('<span class="tag">%s</span>' % t for t in c.get("tags",[]))
    link=('<a class="more" href="%s" target="_blank" rel="noopener">View certificate</a>' % c["link"]) if c.get("link") else ""
    return '<article class="cert"><h3>%s</h3><p class="issuer">%s</p><p class="date">%s</p><div class="tags">%s</div>%s</article>' % (c["title"],c["issuer"],c["date"],tags,link)
certs_html=""
if CERTS:
    certs_html='<section class="section white" id="certificates"><div class="wrap"><div class="section-head"><div><h2>Licenses and certifications</h2><p>Courses and credentials I have completed.</p></div></div><div class="grid">'+"".join(cert_card(c) for c in CERTS)+'</div></div></section>'
about=f'''
<section class="page-top"><div class="wrap"><h1>About me</h1><p class="lead">Adaptable, organized and happiest when a messy plan turns into something that works.</p></div></section>
<section class="section"><div class="wrap about-grid">
<div class="about-photo"><div class="arch"><img src="assets/zahra.jpg" alt="Zahra Mufida standing with her hands folded" width="768" height="960"></div></div>
<div class="about-copy">
<p>I'm Zahra, an Information Systems student at Universitas Airlangga in Surabaya. I work comfortably in fast-paced teams and with people from very different backgrounds, which has made me a better listener and a clearer communicator.</p>
<p>I manage my own time, prioritize tasks and keep learning new skills. On campus I have led sponsorship teams, coordinated marketing, represented my organization to external partners and moderated a national event's talk show.</p>
<p>On the technical side I build web and mobile apps, and I document systems with BPMN, UML and DFD so that teams share one picture of what they are building.</p>
<div class="two">
<div class="edu"><h3>Information Systems</h3><p>Airlangga University<br>2024 to now</p></div>
<div class="edu"><h3>Science Major</h3><p>76 High School of Jakarta<br>2021 to 2024</p></div>
</div>
<p style="margin-top:2rem"><a class="btn solid" href="assets/Zahra-Mufida-CV.pdf" download>Download CV</a></p>
</div></div></section>
<section class="section tint" id="experience"><div class="wrap">
<div class="section-head"><div><h2>Experience</h2><p>Organizations and events I have helped run, newest first.</p></div></div>
<ol class="timeline">{tl}</ol></div></section>
{certs_html}
<section class="section"><div class="wrap">
<div class="section-head"><div><h2>Skills</h2></div></div>
<div class="skills">{sk}</div></div></section>
'''
page("about.html","About | Zahra Mufida","Zahra Mufida is an Information Systems student at Universitas Airlangga with experience in sponsorship, marketing, public relations and software projects.",about,"about.html")

# ---------- PROJECTS ----------
fl="".join(f'<button data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{v}</button>' for k,v in FILTERS)
proj=f'''
<section class="page-top"><div class="wrap"><h1>Projects</h1><p class="lead">Web and mobile apps, systems analysis and competition work.</p></div></section>
<section class="section" style="padding-top:2rem"><div class="wrap">
<div class="filters" role="group" aria-label="Filter projects">{fl}</div>
<div class="grid">{"".join(card(p) for p in PROJECTS)}</div></div></section>
'''
page("projects.html","Projects | Zahra Mufida","Selected web, mobile, systems analysis and competition projects by Zahra Mufida.",proj,"projects.html")

# ---------- CONTACT ----------
contact=f'''
<section class="page-top"><div class="wrap"><h1>Let's talk</h1><p class="lead">For internships, collaborations, events or just a friendly hello.</p></div></section>
<section class="section" style="padding-top:2rem"><div class="wrap contact-grid">
<div><h2 style="font-size:2rem">Find me online</h2>
<ul class="links">
<li><a href="mailto:{EMAIL}"><span>Email</span><small>{EMAIL}</small></a></li>
<li><a href="{IG}" target="_blank" rel="noopener"><span>Instagram</span><small>@zahramufida1410</small></a></li>
<li><a href="{GH}" target="_blank" rel="noopener"><span>GitHub</span><small>{GH_NAME}</small></a></li>
<li><a href="assets/Zahra-Mufida-CV.pdf" download><span>Curriculum vitae</span><small>PDF</small></a></li>
</ul></div>
<form class="form" id="contact-form">
<div class="field"><label for="name">Your name</label><input id="name" name="name" required autocomplete="name"></div>
<div class="field"><label for="email">Your email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
<div class="field"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
<button class="btn solid" type="submit">Send message</button>
</form></div></section>
'''
page("contact.html","Contact | Zahra Mufida","Get in touch with Zahra Mufida for internships, collaborations and events.",contact,"contact.html")
print("built")
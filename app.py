from pathlib import Path
from html import escape
from datetime import date

import streamlit as st


# =========================================================
# PAGE SETTINGS
# =========================================================
st.set_page_config(
    page_title="Vishvas Patil | Academic & Data Science Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent


# =========================================================
# PROFILE — UPDATE YOUR DETAILS HERE
# =========================================================
PROFILE = {
    "name": "Vishvas Patil",
    "role": "Assistant Professor",
    "institution": "Ramrao Adik Institute of Technology, Nerul",
    "email": "vishvaspatil6205@gmail.com",
    "phone": "+91 84509 19887",
    "phd": (
        "Applications of Mathematics and Statistical Computing "
        "in Machine Learning and Data Science"
    ),
    "summary": (
        "I teach mathematics and statistics and develop interactive "
        "applications that connect mathematical ideas with practical "
        "data analysis. My work brings together teaching, statistical "
        "computing, machine learning, and data science."
    ),
}

PROJECTS = [
    {
        "number": "01",
        "icon": "📈",
        "title": "Two Normal Densities",
        "subtitle": "Statistical modelling · Faithful dataset",
        "description": (
            "An interactive application for exploring the fitting of "
            "two normal densities to the Faithful dataset."
        ),
        "tags": ["Statistics", "Normal distributions", "Streamlit"],
        "category": "Statistical Computing",
        "url": (
            "https://fitting-of-two-normal-densities-to-faithful-"
            "dataset-74m7fuuvy4.streamlit.app/"
        ),
    },
    {
        "number": "02",
        "icon": "💎",
        "title": "Diamond Price Predictor",
        "subtitle": "Predictive modelling · Diamonds dataset",
        "description": (
            "A prediction application focused on estimating diamond "
            "prices from diamond characteristics."
        ),
        "tags": ["Machine learning", "Prediction", "Streamlit"],
        "category": "Machine Learning",
        "url": (
            "https://diamond-price-predictor-"
            "ovfl5m6scvakqvlm84twub.streamlit.app/"
        ),
    },
    {
        "number": "03",
        "icon": "🌍",
        "title": "Disease Outbreak Analytics",
        "subtitle": "Data exploration · Public health",
        "description": (
            "An interactive dashboard for exploring disease outbreak "
            "data and communicating patterns through analytics."
        ),
        "tags": ["Data analytics", "Dashboard", "Streamlit"],
        "category": "Data Analytics",
        "url": (
            "https://disease-outbreak-analytics-dashboard-app-"
            "duw83awthwohveaumlnmc.streamlit.app/"
        ),
    },
]

EXPERIENCE = [
    {
        "period": "July 2015 – Present",
        "institution": "Ramrao Adik Institute of Technology",
        "location": "Nerul",
        "description": (
            "Teaching Applied Mathematics and Statistics across "
            "Computer, IT, EXTC, AIML, and AIDS engineering programmes. "
            "Teaching areas include linear algebra, calculus, vector "
            "algebra, probability, and statistical methods."
        ),
    },
    {
        "period": "September 2013 – July 2015",
        "institution": "VJTI",
        "location": "Matunga",
        "description": (
            "Taught first- and second-year engineering students "
            "across branches and monitored student progress."
        ),
    },
    {
        "period": "August 2012 – July 2013",
        "institution": "Pillai College of Science and Technology",
        "location": "HOC Rasayani",
        "description": (
            "Taught mathematics to first- and second-year "
            "B.Sc. students."
        ),
    },
    {
        "period": "August 2011 – August 2012",
        "institution": "Saraswati College of Engineering",
        "location": "Kharghar",
        "description": (
            "Taught Applied Mathematics and Statistics to engineering "
            "students, covering linear algebra, calculus, integral "
            "transforms, vector algebra, probability, and statistics."
        ),
    },
]

SKILLS = {
    "Programming & tools": [
        "Python",
        "NumPy",
        "Pandas",
        "SQL",
        "Scikit-learn",
        "Power BI",
        "Streamlit",
    ],
    "Mathematics & analytics": [
        "Applied Mathematics",
        "Probability",
        "Statistical Computing",
        "Regression Analysis",
        "Clustering Analysis",
        "Linear Algebra",
        "Calculus",
    ],
}


# =========================================================
# STYLE
# =========================================================
st.markdown(
    """
<style>
@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap'
);

:root {
    --navy: #132c40;
    --teal: #087f83;
    --cream: #f7f5f0;
    --ink: #1b3445;
    --muted: #60717d;
    --line: #e2e7e7;
}

.stApp {
    background: var(--cream);
}

html, body, [data-testid="stMarkdownContainer"] {
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1200px;
    padding-top: 2.5rem;
    padding-bottom: 2rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3 {
    color: var(--ink) !important;
}

p, li {
    line-height: 1.75;
}

section[data-testid="stSidebar"] {
    background: var(--navy);
}

section[data-testid="stSidebar"] * {
    color: #edf5f7;
}

section[data-testid="stSidebar"] hr {
    border-color: #365164;
}

.sidebar-initials {
    display: grid;
    place-items: center;
    width: 76px;
    height: 76px;
    margin-bottom: 18px;
    border-radius: 24px;
    background: #215365;
    border: 1px solid #4c7f8d;
    font-size: 29px;
    font-weight: 700;
}

.sidebar-name {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 29px;
    margin-bottom: 5px;
}

.sidebar-role {
    font-size: 13px;
    color: #b8d1db !important;
    line-height: 1.8;
}

.eyebrow {
    color: var(--teal);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.hero {
    background:
        radial-gradient(circle at 95% 5%, #d7eeea 0, transparent 42%),
        #ffffff;
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: 45px;
    margin-bottom: 25px;
}

.hero-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(37px, 5vw, 62px);
    line-height: 1.12;
    letter-spacing: -1.5px;
    color: var(--navy);
    margin: 12px 0 22px;
}

.hero-title span {
    color: var(--teal);
}

.hero-description {
    max-width: 750px;
    color: #536875;
    font-size: 17px;
    line-height: 1.9;
}

.pill {
    display: inline-block;
    border-radius: 999px;
    padding: 6px 12px;
    margin: 4px 5px 4px 0;
    background: #edf6f4;
    color: #176367;
    font-size: 12px;
    font-weight: 600;
}

.section-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 31px;
    color: var(--navy);
    margin: 27px 0 10px;
}

.section-note {
    color: var(--muted);
    margin-bottom: 24px;
    font-size: 15px;
}

.portfolio-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 27px;
    margin-bottom: 18px;
    box-shadow: 0 8px 26px rgba(19, 44, 64, 0.035);
    transition: transform .2s ease, box-shadow .2s ease;
}

.portfolio-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 28px rgba(19, 44, 64, 0.08);
}

.card-kicker {
    color: var(--teal);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.6px;
    margin-bottom: 12px;
}

.card-title {
    color: var(--navy);
    font-size: 22px;
    font-weight: 700;
    line-height: 1.4;
    margin-bottom: 10px;
}

.card-description {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.85;
}

.project-icon {
    font-size: 35px;
    margin-bottom: 17px;
}

.project-card {
    min-height: 355px;
}

.timeline-card {
    border-left: 4px solid var(--teal);
}

.stat {
    background: #ffffff;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 23px;
    margin-bottom: 16px;
}

.stat-number {
    color: var(--teal);
    font-size: 31px;
    font-weight: 700;
}

.stat-label {
    color: var(--muted);
    font-size: 13px;
    margin-top: 7px;
}

.contact-link {
    display: inline-block;
    background: var(--teal);
    color: white !important;
    text-decoration: none !important;
    border-radius: 10px;
    padding: 12px 20px;
    margin: 12px 10px 0 0;
    font-weight: 600;
}

.footer {
    border-top: 1px solid var(--line);
    color: var(--muted);
    font-size: 12px;
    padding-top: 20px;
    margin-top: 45px;
}

.stButton > button,
.stDownloadButton > button,
.stLinkButton > a {
    border-radius: 10px;
    font-weight: 600;
}

@media (max-width: 700px) {
    .hero {
        padding: 27px 22px;
    }

    .project-card {
        min-height: auto;
    }

    .block-container {
        padding-top: 1.3rem;
    }
}

@media (prefers-reduced-motion: reduce) {
    .portfolio-card {
        transition: none;
    }

    .portfolio-card:hover {
        transform: none;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# HELPERS
# =========================================================
def show_html(content):
    st.markdown(content, unsafe_allow_html=True)


def pills(items):
    return "".join(
        f'<span class="pill">{escape(item)}</span>'
        for item in items
    )


def section(title, description=""):
    show_html(
        f'<div class="section-title">{escape(title)}</div>'
        f'<div class="section-note">{escape(description)}</div>'
    )


def card(title, description, kicker=""):
    show_html(
        '<div class="portfolio-card">'
        f'<div class="card-kicker">{escape(kicker)}</div>'
        f'<div class="card-title">{escape(title)}</div>'
        f'<div class="card-description">{escape(description)}</div>'
        '</div>'
    )


def resume_download(key):
    resume_path = BASE_DIR / "resume.pdf"

    if resume_path.is_file():
        st.download_button(
            label="Download resume",
            data=resume_path.read_bytes(),
            file_name="Vishvas_Patil_Resume.pdf",
            mime="application/pdf",
            key=key,
            use_container_width=True,
        )
    else:
        st.caption(
            "Place resume.pdf beside app.py to enable resume downloads."
        )


def project_cards(projects):
    if not projects:
        st.info("No projects match your search.")
        return

    columns = st.columns(min(len(projects), 3))

    for index, project in enumerate(projects):
        with columns[index % len(columns)]:
            show_html(
                '<div class="portfolio-card project-card">'
                f'<div class="card-kicker">'
                f'PROJECT {escape(project["number"])}</div>'
                f'<div class="project-icon">{project["icon"]}</div>'
                f'<div class="card-title">'
                f'{escape(project["title"])}</div>'
                f'<div class="card-description">'
                f'{escape(project["subtitle"])}<br><br>'
                f'{escape(project["description"])}</div>'
                f'<div style="margin-top:18px">'
                f'{pills(project["tags"])}</div>'
                '</div>'
            )

            st.link_button(
                "Open live application ↗",
                project["url"],
                use_container_width=True,
            )


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    photo_path = BASE_DIR / "profile.jpg"

    if photo_path.is_file():
        st.image(str(photo_path), width=150)
    else:
        show_html('<div class="sidebar-initials">VP</div>')

    show_html(
        f'<div class="sidebar-name">{escape(PROFILE["name"])}</div>'
        '<div class="sidebar-role">'
        'Assistant Professor<br>'
        'Mathematics · Statistics · Data Science'
        '</div>'
    )

    st.divider()

    page = st.radio(
        "Explore",
        [
            "Overview",
            "Live Projects",
            "Experience",
            "Education & Skills",
            "Research",
            "Contact",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    resume_download("sidebar_resume")
    st.caption("Academic portfolio · Built with Python & Streamlit")


# =========================================================
# OVERVIEW
# =========================================================
if page == "Overview":
    show_html(
        '<div class="hero">'
        '<div class="eyebrow">Educator · Researcher · App Developer</div>'
        '<div class="hero-title">'
        'Mathematics.<br>Statistics.<br>'
        '<span>Ideas made interactive.</span>'
        '</div>'
        f'<div class="hero-description">'
        f'I’m <strong>{escape(PROFILE["name"])}</strong>. '
        f'{escape(PROFILE["summary"])}'
        '</div>'
        '<div style="margin-top:24px">'
        f'{pills(["Applied Mathematics", "Statistical Computing", "Machine Learning"])}'
        '</div>'
        '</div>'
    )

    a, b, c = st.columns(3)

    for column, number, label in [
        (a, "10+", "Years of teaching experience"),
        (b, str(len(PROJECTS)), "Live interactive applications"),
        (c, "Ph.D.", "Research in progress"),
    ]:
        with column:
            show_html(
                '<div class="stat">'
                f'<div class="stat-number">{number}</div>'
                f'<div class="stat-label">{label}</div>'
                '</div>'
            )

    section(
        "A bridge between theory and application",
        "Teaching mathematical foundations and building tools to explore them.",
    )

    left, right = st.columns([1.2, 1])

    with left:
        card(
            "Teaching & academic practice",
            (
                "Assistant Professor at Ramrao Adik Institute of "
                "Technology, Nerul. Teaching experience spans "
                "mathematics, probability, statistics, and "
                "engineering applications."
            ),
            "Current role",
        )

    with right:
        card(
            "Doctoral research",
            PROFILE["phd"] + ". Ph.D. currently in progress.",
            "Research direction",
        )

    section(
        "Selected live projects",
        "Open an application to explore the work.",
    )
    project_cards(PROJECTS)


# =========================================================
# LIVE PROJECTS
# =========================================================
elif page == "Live Projects":
    section(
        "Interactive applications",
        "A collection of my statistical computing and data science projects.",
    )

    left, right = st.columns([2, 1])

    with left:
        query = st.text_input(
            "Search projects",
            placeholder="Try statistics, diamond, or dashboard",
        )

    with right:
        category = st.selectbox(
            "Category",
            ["All"] + sorted(
                {project["category"] for project in PROJECTS}
            ),
        )

    filtered = [
        project
        for project in PROJECTS
        if (
            category == "All"
            or project["category"] == category
        )
        and query.casefold() in " ".join(
            [
                project["title"],
                project["description"],
                *project["tags"],
            ]
        ).casefold()
    ]

    st.write("")
    project_cards(filtered)


# =========================================================
# EXPERIENCE
# =========================================================
elif page == "Experience":
    section(
        "Teaching experience",
        "Mathematics and statistics across science and engineering programmes.",
    )

    for item in EXPERIENCE:
        show_html(
            '<div class="portfolio-card timeline-card">'
            f'<div class="card-kicker">{escape(item["period"])}</div>'
            f'<div class="card-title">'
            f'{escape(item["institution"])}</div>'
            f'<div class="card-description">'
            f'<strong>Assistant Professor · '
            f'{escape(item["location"])}</strong><br><br>'
            f'{escape(item["description"])}'
            '</div></div>'
        )


# =========================================================
# EDUCATION AND SKILLS
# =========================================================
elif page == "Education & Skills":
    section(
        "Education & qualifications",
        "Academic preparation and continued professional learning.",
    )

    card(
        "Ph.D. — In Progress(ICT,Mumbai)",
        PROFILE["phd"],
        "Doctoral studies",
    )

    left, right = st.columns(2)

    with left:
        card(
            "M.Sc. Mathematics",
            "Mumbai University, Kalina · 2009–2011 · Distinction",
            "Postgraduate education",
        )

    with right:
        card(
            "B.Sc. Mathematics",
            "Ramnarain Ruia College, Matunga · 2008 · First Class",
            "Undergraduate education",
        )

    card(
        "Competitive examinations",
        "CSIR NET — AIR 10; NET-JRF and SET qualifications.",
        "Qualifications listed in my resume",
    )

    section("Technical toolkit")

    for group, skills in SKILLS.items():
        show_html(
            '<div class="portfolio-card">'
            f'<div class="card-title">{escape(group)}</div>'
            f'<div>{pills(skills)}</div>'
            '</div>'
        )

    section("Professional development")

    training = [
        (
            "Machine Learning Training",
            "NIT Warangal · One-month Faculty Development Programme",
        ),
        (
            "Data Analysis",
            "Edulakes / NSS IIT Roorkee · Six-week Faculty Development Programme",
        ),
        (
            "Microsoft Azure Data Analysis",
            "AICTE · One-week Faculty Development Programme",
        ),
    ]

    for title, description in training:
        card(title, description, "Training / FDP")


# =========================================================
# RESEARCH
# =========================================================
elif page == "Research":
    section(
        "Research & intellectual contributions",
        "Mathematical foundations, statistical methods, and practical computing.",
    )

    card(
        "Current doctoral research",
        PROFILE["phd"] + ".",
        "Ph.D. in progress",
    )

    card(
        "Tangent Intersection Method",
        (
            "Research paper published in the International Journal "
            "of Innovative Research in Technology."
        ),
        "Publication",
    )

    section(
        "Registered copyrights",
        "Contributions listed in my resume.",
    )

    left, right = st.columns(2)

    with left:
        card(
            "A Novel Classification and Clustering Algorithm",
            (
                "Work focused on classification, clustering, "
                "and approaches to unsupervised learning."
            ),
            "Registered copyright",
        )

    with right:
        card(
            "A Novel Method for Finding Review Rating Number "
            "Based on Online Ratings and Reviews",
            (
                "Work connecting mathematical models with "
                "online ratings, reviews, and sentiment analysis."
            ),
            "Registered copyright",
        )


# =========================================================
# CONTACT
# =========================================================
elif page == "Contact":
    section(
        "Let’s connect",
        "For academic discussions, teaching, research, and data science projects.",
    )

    show_html(
        '<div class="hero">'
        '<div class="eyebrow">Contact</div>'
        '<div class="hero-title" style="font-size:43px">'
        'Start a conversation.</div>'
        f'<div class="hero-description">'
        f'{escape(PROFILE["name"])}<br>'
        f'{escape(PROFILE["role"])}<br>'
        f'{escape(PROFILE["institution"])}<br><br>'
        f'{escape(PROFILE["email"])}<br>'
        f'{escape(PROFILE["phone"])}'
        '</div>'
        f'<a class="contact-link" '
        f'href="mailto:{escape(PROFILE["email"], quote=True)}">'
        'Email me ↗</a>'
        '<a class="contact-link" href="tel:+918450919887">'
        'Call me ↗</a>'
        '</div>'
    )

    resume_download("contact_resume")


# =========================================================
# FOOTER
# =========================================================
show_html(
    '<div class="footer">'
    f'© {date.today().year} {escape(PROFILE["name"])}'
    ' &nbsp; · &nbsp; Mathematics, Statistics & Data Science'
    '</div>'
)
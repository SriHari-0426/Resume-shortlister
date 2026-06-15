# Resume Shortlisting Application - File Structure Guide

## Complete Project File Tree

```
resume-shortlisting/
│
├── 📄 README.md                           # Main documentation (800+ lines)
├── 📄 SETUP.md                            # Installation guide (400+ lines)
├── 📄 PROJECT_SUMMARY.md                  # Project overview and completion status
├── 📄 QUICK_REFERENCE.md                  # Quick lookup guide
├── 📄 API_DOCUMENTATION.md                # Complete API reference
├── 📄 .env.example                        # Environment variables template
├── 📄 .gitignore                          # Git ignore patterns
├── 📄 requirements.txt                    # Python dependencies
├── 📄 config.py                           # Flask configuration (60 lines)
├── 📄 run.py                              # Application entry point (30 lines)
│
└── 📁 app/                                # Main application package
    │
    ├── 📄 __init__.py                    # Flask app factory & routes (600+ lines)
    ├── 📄 models.py                      # Database models (380 lines)
    │
    ├── 📁 utils/                         # Utility modules
    │   ├── 📄 __init__.py                # Utils package init
    │   ├── 📄 resume_parser.py          # Resume parsing logic (450 lines)
    │   ├── 📄 skill_matcher.py          # Skill matching algorithm (400 lines)
    │   └── 📄 auth.py                    # Auth decorators (45 lines)
    │
    ├── 📁 static/                        # Static assets
    │   ├── 📁 css/
    │   │   └── 📄 style.css             # Main stylesheet (650 lines)
    │   │                                 # Features: animations, gradients,
    │   │                                 # glassmorphism, responsive design
    │   │
    │   └── 📁 js/
    │       └── 📄 main.js               # JavaScript utilities (200 lines)
    │                                     # Features: animations, form validation,
    │                                     # tooltips, counter animations
    │
    ├── 📁 templates/                     # HTML templates
    │   │
    │   ├── 📄 base.html                 # Base template with nav & footer
    │   │
    │   ├── 📄 index.html                # Homepage with hero section
    │   ├── 📄 login.html                # Login page
    │   ├── 📄 register.html             # Registration page
    │   │
    │   ├── 📁 candidate/                # Candidate templates
    │   │   ├── 📄 dashboard.html        # Candidate dashboard
    │   │   ├── 📄 upload_resume.html    # Resume upload with drag-drop
    │   │   ├── 📄 view_resume.html      # Resume details view
    │   │   ├── 📄 jobs.html             # Browse available jobs
    │   │   └── 📄 view_job.html         # Job details & match score
    │   │
    │   ├── 📁 recruiter/                # Recruiter templates
    │   │   ├── 📄 dashboard.html        # Recruiter dashboard
    │   │   ├── 📄 create_job.html       # Create job posting
    │   │   ├── 📄 edit_job.html         # Edit job posting
    │   │   ├── 📄 view_job.html         # View candidates for job
    │   │   └── 📄 shortlisted.html      # Shortlisted candidates
    │   │
    │   └── 📁 errors/                   # Error pages
    │       ├── 📄 404.html              # Page not found
    │       ├── 📄 403.html              # Access denied
    │       └── 📄 500.html              # Server error
    │
    └── 📁 uploads/                      # Resume file storage
        └── [Resume files stored here]
```

## File Statistics

### Python Files (Total: ~2000 lines)
- `app/__init__.py`: 600+ lines (routes, logic)
- `app/models.py`: 380 lines (database models)
- `app/utils/resume_parser.py`: 450 lines (parsing logic)
- `app/utils/skill_matcher.py`: 400 lines (matching algorithm)
- `config.py`: 60 lines (configuration)
- `run.py`: 30 lines (entry point)

### HTML Files (Total: ~1500 lines)
- Base template: 150 lines
- Homepage: 200 lines
- Auth pages (login/register): 300 lines
- Candidate templates (5 files): 450 lines
- Recruiter templates (5 files): 400 lines
- Error pages (3 files): 100 lines

### CSS Files (Total: 650 lines)
- `style.css`: Modern design with:
  - Color variables
  - Glassmorphism effects
  - Animation keyframes
  - Responsive design
  - Component styling

### JavaScript Files (Total: 200 lines)
- `main.js`: Utilities and interactions:
  - Scroll animations
  - Form validation
  - Toast notifications
  - Data export
  - Event handling

### Documentation Files (Total: 2000+ lines)
- `README.md`: 800+ lines
- `SETUP.md`: 400+ lines
- `API_DOCUMENTATION.md`: 500+ lines
- `QUICK_REFERENCE.md`: 300+ lines
- `PROJECT_SUMMARY.md`: 400+ lines

## Database Schema

### Users Table
```
id (INT, PK)
username (VARCHAR 80, UNIQUE)
email (VARCHAR 120, UNIQUE)
password_hash (VARCHAR 255)
first_name (VARCHAR 50)
last_name (VARCHAR 50)
role (VARCHAR 20) - 'candidate' or 'recruiter'
is_active (BOOLEAN)
created_at (DATETIME)
updated_at (DATETIME)
```

### Resumes Table
```
id (INT, PK)
user_id (INT, FK)
filename (VARCHAR 255)
file_path (VARCHAR 500)
file_type (VARCHAR 10) - 'pdf' or 'docx'
extracted_text (TEXT)
candidate_name (VARCHAR 255)
email (VARCHAR 120)
phone (VARCHAR 20)
location (VARCHAR 120)
education (JSON) - List of education entries
skills (JSON) - List of skills
experience (JSON) - List of work experience
certifications (JSON) - List of certifications
languages (JSON) - List of languages
is_parsed (BOOLEAN)
parse_error (VARCHAR 500)
created_at (DATETIME)
updated_at (DATETIME)
```

### Job Postings Table
```
id (INT, PK)
recruiter_id (INT, FK)
title (VARCHAR 255)
description (TEXT)
required_skills (JSON) - List of skills
nice_to_have_skills (JSON) - List of skills
required_experience (INT)
required_education (VARCHAR 255)
location (VARCHAR 255)
salary_range (VARCHAR 100)
employment_type (VARCHAR 50)
is_active (BOOLEAN)
created_at (DATETIME)
updated_at (DATETIME)
expires_at (DATETIME)
```

### Candidate Matches Table
```
id (INT, PK)
job_id (INT, FK)
resume_id (INT, FK)
match_score (FLOAT) - 0.0 to 1.0
skills_match (FLOAT)
experience_match (FLOAT)
education_match (FLOAT)
matched_skills (JSON)
missing_skills (JSON)
feedback (TEXT)
created_at (DATETIME)
updated_at (DATETIME)
UNIQUE(job_id, resume_id)
```

### Shortlists Table
```
id (INT, PK)
job_id (INT, FK)
resume_id (INT, FK)
status (VARCHAR 50) - 'shortlisted', 'interviewed', 'hired', 'rejected'
notes (TEXT)
rating (INT) - 1-5 stars
created_at (DATETIME)
updated_at (DATETIME)
UNIQUE(job_id, resume_id)
```

### Candidate Profiles Table
```
id (INT, PK)
user_id (INT, FK, UNIQUE)
phone (VARCHAR 20)
location (VARCHAR 120)
headline (VARCHAR 255)
summary (TEXT)
skills (JSON)
created_at (DATETIME)
updated_at (DATETIME)
```

## Key File Descriptions

### Application Core
| File | Purpose | Key Functions |
|------|---------|---|
| `app/__init__.py` | Flask app factory | create_app(), all route handlers |
| `config.py` | Configuration | Database URL, security settings |
| `run.py` | Entry point | Application startup |

### Business Logic
| File | Purpose | Key Classes/Functions |
|------|---------|---|
| `app/models.py` | Database models | User, Resume, JobPosting, CandidateMatch |
| `app/utils/resume_parser.py` | Resume parsing | ResumeParser class, extraction methods |
| `app/utils/skill_matcher.py` | Skill matching | SkillMatcher class, scoring algorithm |
| `app/utils/auth.py` | Authentication | Decorators: @recruiter_required, @candidate_required |

### Frontend
| File | Purpose | Features |
|------|---------|---|
| `style.css` | Styling | Animations, gradients, responsive, glassmorphism |
| `main.js` | Interactivity | Form validation, animations, data handling |
| `base.html` | Layout | Navigation, footer, flash messages |

### Templates
| Template | For | Features |
|----------|-----|---|
| `index.html` | Homepage | Hero section, statistics, features |
| `login.html` | Auth | Login form with modern design |
| `register.html` | Auth | Registration with role selection |
| `candidate/dashboard.html` | Candidate | Resume list, statistics |
| `recruiter/dashboard.html` | Recruiter | Job list, statistics |

## Dependencies Map

```
Flask 2.3.3
├── Werkzeug (password hashing)
├── Jinja2 (templates)
└── Click (CLI)

Flask-SQLAlchemy 3.0.5
├── SQLAlchemy (ORM)
└── MySQL-python (database driver)

Flask-Login 0.6.2
└── Session management

Resume Parsing
├── PyPDF2 (PDF extraction)
├── pdfplumber (PDF processing)
└── python-docx (DOCX extraction)

NLP & ML
├── spaCy (NLP processing)
└── scikit-learn (machine learning)

Frontend
├── Bootstrap 5.3 (CSS framework)
├── Font Awesome 6.4 (icons)
└── jQuery 3.6 (JavaScript)
```

## Directory Size Reference

```
app/
├── static/           ~50 KB (CSS + JS)
├── templates/        ~100 KB (HTML files)
├── uploads/          Variable (resume files)
└── utils/            ~40 KB (Python modules)

Total without uploads: ~600 KB
```

## How to Navigate

### For Frontend Work
Edit files in:
- `app/templates/` - HTML changes
- `app/static/css/` - Styling
- `app/static/js/` - JavaScript

### For Backend Work
Edit files in:
- `app/__init__.py` - Routes and logic
- `app/models.py` - Database models
- `app/utils/` - Business logic

### For Configuration
Edit:
- `config.py` - Application settings
- `.env` - Environment variables

### For Documentation
Edit:
- `README.md` - Main docs
- `SETUP.md` - Setup instructions
- `API_DOCUMENTATION.md` - API reference

## File Dependencies

```
run.py
└── app/__init__.py
    ├── config.py
    ├── app/models.py
    │   └── Flask-SQLAlchemy
    │       └── SQLAlchemy
    ├── app/utils/
    │   ├── resume_parser.py
    │   ├── skill_matcher.py
    │   └── auth.py
    └── app/templates/
        ├── base.html
        └── [other templates]

app/static/
├── css/style.css
└── js/main.js
```

---

This structure ensures clean separation of concerns and makes it easy to locate and modify specific components.

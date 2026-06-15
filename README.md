# Resume Shortlisting Web Application

A modern, full-stack AI-powered recruitment platform that automates resume screening and candidate matching using intelligent skill-based algorithms.

## Overview

**RecruitAI** is a comprehensive solution for recruitment professionals to streamline their hiring process. The system automatically extracts information from resumes, matches candidates with job requirements, and provides detailed analytics for informed hiring decisions.

## Key Features

### For Candidates
- ✅ User registration and profile management
- ✅ Resume upload (PDF and DOCX support)
- ✅ Automatic resume parsing and data extraction
- ✅ Browse available job opportunities
- ✅ View match scores against job requirements
- ✅ Track applications and matches

### For Recruiters
- ✅ Create and manage job postings
- ✅ Define job requirements (skills, experience, education)
- ✅ Automatic candidate matching based on skills
- ✅ View candidate ranking by match score
- ✅ Shortlist and manage candidates
- ✅ Detailed analytics dashboard
- ✅ Filter and search candidates

### Technical Features
- ✅ Secure user authentication and authorization
- ✅ Advanced resume parsing with NLP
- ✅ Intelligent skill matching algorithm
- ✅ Responsive design (Desktop, Tablet, Mobile)
- ✅ Modern UI with glassmorphism effects
- ✅ RESTful API endpoints
- ✅ Database persistence
- ✅ Error handling and logging

## Technology Stack

### Frontend
- **HTML5** - Structure and semantics
- **CSS3** - Modern styling with animations and gradients
- **JavaScript** - Interactive features and client-side logic
- **Bootstrap 5** - Responsive components
- **Font Awesome** - Icons and graphics

### Backend
- **Python 3.8+** - Programming language
- **Flask 2.3+** - Web framework
- **Flask-SQLAlchemy** - ORM for database
- **Flask-Login** - User session management
- **PyPDF2, pdfplumber** - PDF extraction
- **python-docx** - DOCX extraction
- **spaCy** - NLP capabilities
- **scikit-learn** - Machine learning for skill matching

### Database
- **MySQL 5.7+** - Relational database
- **SQLAlchemy** - Database abstraction layer

## Installation

### Prerequisites
- Python 3.8 or higher
- MySQL Server 5.7 or higher
- pip (Python package installer)

### Step 1: Clone and Setup

```bash
# Navigate to project directory
cd resume\ shortlisting

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt

# Download spaCy model for NLP
python -m spacy download en_core_web_sm
```

### Step 3: Configure Database

Create a MySQL database:
```sql
CREATE DATABASE resume_shortlisting;
```

Update database configuration in `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost:3306/resume_shortlisting'
```

### Step 4: Run Application

```bash
# Development mode
python run.py

# Or use Flask CLI
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

The application will be available at `http://localhost:5000`

## Project Structure

```
resume-shortlisting/
├── app/
│   ├── __init__.py           # Flask app factory and routes
│   ├── models.py             # Database models
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css     # Main stylesheet
│   │   └── js/
│   │       └── main.js       # JavaScript utilities
│   ├── templates/
│   │   ├── base.html         # Base template
│   │   ├── index.html        # Homepage
│   │   ├── login.html        # Login page
│   │   ├── register.html     # Registration page
│   │   ├── candidate/        # Candidate templates
│   │   ├── recruiter/        # Recruiter templates
│   │   └── errors/           # Error pages
│   └── utils/
│       ├── resume_parser.py  # Resume parsing logic
│       ├── skill_matcher.py  # Skill matching algorithm
│       └── auth.py           # Authentication decorators
├── config.py                 # Application configuration
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

## Usage Guide

### For Candidates

1. **Register Account**
   - Go to `/register` and create account with email
   - Choose "Candidate" role
   - Verify email (optional in development)

2. **Upload Resume**
   - Navigate to Dashboard
   - Click "Upload Resume"
   - Drag and drop or select PDF/DOCX file
   - System automatically parses resume

3. **Browse Jobs**
   - Go to "Available Opportunities"
   - View job details and requirements
   - See your match score for each position

### For Recruiters

1. **Register Account**
   - Go to `/register` and create account
   - Choose "Recruiter" role

2. **Create Job Posting**
   - Click "Post a Job"
   - Fill in job details:
     - Title and description
     - Required skills (comma-separated)
     - Experience level
     - Location and salary
   - Submit

3. **View Candidates**
   - See all matched candidates automatically
   - View match scores and skill matches
   - Shortlist promising candidates
   - Track interview status

## API Endpoints

### Authentication
- `POST /register` - Register new user
- `POST /login` - Login user
- `GET /logout` - Logout user

### Candidate Routes
- `GET /dashboard/candidate` - Candidate dashboard
- `GET /dashboard/candidate/upload-resume` - Resume upload page
- `POST /dashboard/candidate/upload-resume` - Upload resume
- `GET /dashboard/candidate/view-resume/<id>` - View resume details
- `POST /dashboard/candidate/delete-resume/<id>` - Delete resume
- `GET /dashboard/candidate/jobs` - Browse jobs
- `GET /dashboard/candidate/job/<id>` - View job details

### Recruiter Routes
- `GET /dashboard/recruiter` - Recruiter dashboard
- `GET /dashboard/recruiter/create-job` - Create job form
- `POST /dashboard/recruiter/create-job` - Submit new job
- `GET /dashboard/recruiter/edit-job/<id>` - Edit job form
- `POST /dashboard/recruiter/edit-job/<id>` - Update job
- `GET /dashboard/recruiter/job/<id>` - View candidates for job
- `POST /dashboard/recruiter/delete-job/<id>` - Delete job
- `GET /dashboard/recruiter/shortlisted` - View shortlisted candidates

### API Endpoints
- `GET /api/match-score/<id>` - Get detailed match score
- `GET /api/search-candidates` - Search candidates

## Resume Parsing

The system automatically extracts:
- **Contact Information**: Name, email, phone, location
- **Professional Summary**: About the candidate
- **Work Experience**: Job titles, companies, dates, descriptions
- **Education**: Degrees, institutions, graduation dates
- **Technical Skills**: Programming languages, frameworks, tools
- **Certifications**: Professional certifications and licenses
- **Languages**: Spoken languages

## Skill Matching Algorithm

The system uses a multi-factor approach:

1. **Skill Matching** (50% weight)
   - Fuzzy matching for similar skill names
   - Synonym detection
   - Partial credit for related skills

2. **Experience Matching** (30% weight)
   - Years of experience comparison
   - Job level assessment

3. **Education Matching** (20% weight)
   - Degree level comparison
   - Field of study alignment

**Formula**: `Match Score = (0.5 × skill_score) + (0.3 × exp_score) + (0.2 × edu_score)`

## Design Features

### Modern UI Components
- **Glassmorphism**: Frosted glass effect cards
- **Animated Particles**: Floating background elements
- **Gradient Text**: Vibrant color transitions
- **Smooth Animations**: Fade-in, slide-up, and zoom effects
- **Responsive Layout**: Mobile-first design

### Color Palette
- Primary: #4F46E5 (Indigo)
- Secondary: #06B6D4 (Cyan)
- Accent: #8B5CF6 (Purple)
- Background: #0F172A (Dark Navy)

## Configuration

Edit `config.py` to customize:

```python
# Database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:pass@localhost/db'

# File upload
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Matching
MIN_MATCH_SCORE = 0.3  # 30% minimum

# Pagination
ITEMS_PER_PAGE = 10
```

## Database Schema

### Users Table
- User credentials and profile information
- Role: candidate or recruiter

### Resumes Table
- Uploaded resume files
- Extracted resume data
- Parsing status

### Job Postings Table
- Job requirements and details
- Salary and location info
- Status (active/inactive)

### Candidate Matches Table
- Match scores for candidate-job pairs
- Skill matches and missing skills
- Match breakdown by category

### Shortlists Table
- Recruiter's shortlisted candidates
- Interview status and notes

## Security Features

- Password hashing with Werkzeug
- Session-based authentication
- CSRF protection
- SQL injection prevention via SQLAlchemy ORM
- File upload validation
- Role-based access control

## Deployment

### Development
```bash
export FLASK_ENV=development
python run.py
```

### Production
```bash
export FLASK_ENV=production
export SECRET_KEY='your-secret-key'
gunicorn --workers 4 --bind 0.0.0.0:8000 run:app
```

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "run:app"]
```

## Troubleshooting

### Issue: Database connection error
```
Solution: Verify MySQL is running and credentials in config.py are correct
```

### Issue: spaCy model not found
```
Solution: python -m spacy download en_core_web_sm
```

### Issue: Resume parsing fails
```
Solution: Ensure file is valid PDF or DOCX format and under 50MB
```

## Future Enhancements

- [ ] Email notifications for new matches
- [ ] Video interview integration
- [ ] Advanced analytics dashboard
- [ ] Bulk resume import
- [ ] Integration with job boards
- [ ] Machine learning improvements
- [ ] Mobile app (React Native/Flutter)
- [ ] Multi-language support
- [ ] ATS integration
- [ ] Background check automation

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For support, email support@recruitai.com or open an issue in the repository.

## Changelog

### Version 1.0.0
- Initial release
- Core functionality for candidates and recruiters
- Resume parsing and skill matching
- Modern UI design

## Acknowledgments

- Font Awesome for icons
- Bootstrap team for CSS framework
- Open source community
- Contributors and testers

---

**Built with ❤️ for better recruitment**

Made for transforming the hiring process with AI and automation.

# Setup Instructions

## Quick Start Guide

### 1. Prerequisites Check

Make sure you have the following installed:
- Python 3.8 or higher
- MySQL Server 5.7 or higher
- Git

Check versions:
```bash
python --version
mysql --version
git --version
```

### 2. Download the Application

```bash
cd /path/to/your/projects
git clone <repository-url>
cd resume\ shortlisting
```

### 3. Create Python Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Setup MySQL Database

**Connect to MySQL:**
```bash
mysql -u root -p
```

**Create database and user:**
```sql
CREATE DATABASE resume_shortlisting;
CREATE USER 'recruit_user'@'localhost' IDENTIFIED BY 'secure_password_123';
GRANT ALL PRIVILEGES ON resume_shortlisting.* TO 'recruit_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 6. Download NLP Model

```bash
python -m spacy download en_core_web_sm
```

### 7. Configure Environment Variables

```bash
# Copy example to .env
cp .env.example .env

# Edit .env file with your settings
# Windows:
notepad .env

# macOS/Linux:
nano .env
```

**Update these values in .env:**
```env
FLASK_ENV=development
SECRET_KEY=your-super-secret-key-12345
DATABASE_URL=mysql+pymysql://recruit_user:secure_password_123@localhost:3306/resume_shortlisting
```

### 8. Run the Application

```bash
# Make sure virtual environment is activated
python run.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 9. Access the Application

Open your browser and go to:
```
http://localhost:5000
```

## Create Test Accounts

### Candidate Account
- Go to http://localhost:5000/register
- Role: Candidate
- Username: `john_doe`
- Email: `john@example.com`
- Password: `SecurePass123`

### Recruiter Account
- Go to http://localhost:5000/register
- Role: Recruiter
- Username: `recruiter_jane`
- Email: `jane@company.com`
- Password: `SecurePass123`

## Test Features

### 1. Upload Resume (as Candidate)
- Login with candidate account
- Go to Dashboard → Upload Resume
- Use a sample resume file (create or use existing)
- System will parse and extract data

### 2. Create Job (as Recruiter)
- Login with recruiter account
- Go to Dashboard → Post a Job
- Fill in job details and required skills
- System will automatically match candidates

### 3. View Matches
- As recruiter, view job and see candidates ranked by match score
- As candidate, view jobs and see your match percentage

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"
```bash
# Ensure virtual environment is activated
# Reinstall requirements
pip install -r requirements.txt
```

### Error: "mysql.connector.Error: Can't connect to MySQL server"
```bash
# Check MySQL is running
# Windows: services.msc → find MySQL
# macOS: brew services list
# Linux: sudo systemctl status mysql

# Verify credentials in .env
# Test connection:
mysql -u recruit_user -p -h localhost resume_shortlisting
```

### Error: "ImportError: No module named 'spacy'"
```bash
# Download the model
python -m spacy download en_core_web_sm
```

### Error: "CSRF token missing"
```bash
# Clear browser cookies for localhost
# Restart the application
```

## Development Commands

### Create Database Tables
```bash
python
>>> from app import db, create_app
>>> app = create_app()
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

### Add Sample Data
```bash
# Create Python script to add sample jobs and candidates
python -c "
from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    # Add users here
    pass
"
```

### Reset Database
```bash
# WARNING: This will delete all data
python
>>> from app import db, create_app
>>> app = create_app()
>>> with app.app_context():
>>>     db.drop_all()
>>>     db.create_all()
>>> exit()
```

### Run with Debug Mode
```bash
export FLASK_DEBUG=1
export FLASK_ENV=development
python run.py
```

## File Upload Configuration

### Supported Formats
- PDF (.pdf)
- Word Document (.docx, .doc)

### Size Limit
- Maximum file size: 50MB (configured in config.py)

### Upload Location
```
app/uploads/
```

## Port Configuration

Default port is 5000. To use different port:

```bash
# Set PORT environment variable
export PORT=8000
python run.py

# Or specify in code:
app.run(host='0.0.0.0', port=8000)
```

## Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn --workers 4 --bind 0.0.0.0:8000 run:app
```

### Using Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
COPY . .
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "run:app"]
```

Build and run:
```bash
docker build -t recruitai .
docker run -p 8000:8000 recruitai
```

## Performance Optimization

### Enable Caching
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

### Database Optimization
- Create indexes on frequently searched fields
- Use connection pooling

### Frontend Optimization
- Enable gzip compression
- Minimize CSS and JavaScript
- Use CDN for static assets

## Security Checklist

- [ ] Change SECRET_KEY in production
- [ ] Use HTTPS certificate
- [ ] Set SESSION_COOKIE_SECURE=True
- [ ] Use strong database password
- [ ] Keep dependencies updated
- [ ] Enable CSRF protection
- [ ] Implement rate limiting
- [ ] Add user input validation
- [ ] Use environment variables for secrets
- [ ] Regular database backups

## Next Steps

1. Explore the application features
2. Customize styling and colors in `app/static/css/style.css`
3. Add more skill synonyms in `app/utils/skill_matcher.py`
4. Implement email notifications
5. Add analytics and reporting
6. Deploy to production server

## Support & Resources

- **Documentation**: See README.md
- **Flask**: https://flask.palletsprojects.com/
- **SQLAlchemy**: https://www.sqlalchemy.org/
- **Bootstrap**: https://getbootstrap.com/
- **MySQL**: https://dev.mysql.com/doc/

## Getting Help

If you encounter issues:
1. Check the troubleshooting section above
2. Review application logs (console output)
3. Check database connection
4. Verify all dependencies are installed
5. Open an issue with error details

---

**Happy recruiting! 🚀**

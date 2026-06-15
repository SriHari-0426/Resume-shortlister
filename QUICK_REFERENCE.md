# Quick Reference Guide

## Application URLs

### Public Pages
- `http://localhost:5000/` - Homepage
- `http://localhost:5000/register` - Registration
- `http://localhost:5000/login` - Login

### Candidate Pages
- `/dashboard/candidate` - Dashboard
- `/dashboard/candidate/upload-resume` - Upload resume
- `/dashboard/candidate/view-resume/<id>` - View resume
- `/dashboard/candidate/jobs` - Browse jobs
- `/dashboard/candidate/job/<id>` - View job details

### Recruiter Pages
- `/dashboard/recruiter` - Dashboard
- `/dashboard/recruiter/create-job` - Post new job
- `/dashboard/recruiter/edit-job/<id>` - Edit job
- `/dashboard/recruiter/job/<id>` - View candidates for job
- `/dashboard/recruiter/shortlisted` - View shortlisted candidates

## Database Commands

### Connect to Database
```bash
mysql -u recruit_user -p resume_shortlisting
```

### View All Users
```sql
SELECT id, username, email, role FROM users;
```

### View All Resumes
```sql
SELECT id, user_id, candidate_name, is_parsed FROM resumes;
```

### View All Jobs
```sql
SELECT id, recruiter_id, title, is_active FROM job_postings;
```

### View Matches
```sql
SELECT m.id, m.job_id, m.resume_id, m.match_score 
FROM candidate_matches m 
ORDER BY m.match_score DESC;
```

### Count Records
```sql
SELECT 
  (SELECT COUNT(*) FROM users) as total_users,
  (SELECT COUNT(*) FROM resumes) as total_resumes,
  (SELECT COUNT(*) FROM job_postings) as total_jobs,
  (SELECT COUNT(*) FROM candidate_matches) as total_matches;
```

### Delete All Test Data
```sql
DELETE FROM candidate_matches;
DELETE FROM shortlists;
DELETE FROM job_postings;
DELETE FROM resumes;
DELETE FROM candidate_profiles;
DELETE FROM users;
```

## Feature Checklist

### Candidate Features
- [x] User registration
- [x] Profile management
- [x] Resume upload (PDF/DOCX)
- [x] Resume view with parsed data
- [x] Browse job opportunities
- [x] View job details
- [x] Match score for jobs
- [x] Resume deletion
- [x] Job search and filter

### Recruiter Features
- [x] User registration
- [x] Create job postings
- [x] Edit job postings
- [x] Delete job postings
- [x] View matched candidates
- [x] Sort candidates by score
- [x] Shortlist candidates
- [x] View shortlisted candidates
- [x] Filter shortlisted by status
- [x] Dashboard statistics

### Technical Features
- [x] Resume parsing (PDF/DOCX)
- [x] Automatic data extraction
- [x] Skill matching algorithm
- [x] Match score calculation
- [x] User authentication
- [x] Role-based access control
- [x] Database persistence
- [x] Responsive design
- [x] Modern UI with animations
- [x] Error handling

## Keyboard Shortcuts

### Global
- `Ctrl+K` - Search (future feature)
- `Ctrl+/` - Show help (future feature)

### Navigation
- `Home` - Go to homepage
- `Alt+D` - Go to dashboard
- `Alt+L` - Logout

## Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| Port 5000 already in use | `export PORT=8000` then `python run.py` |
| Database connection error | Check MySQL is running: `mysql -u root -p` |
| Resume parsing fails | Ensure file is valid PDF/DOCX under 50MB |
| Session expired | Login again |
| File upload error | Check file size and format |
| No candidates showing | Ensure resumes are parsed |
| Match score is 0% | Check if resume has required skills |

## Performance Tips

1. **For Recruiters**
   - Sort candidates by match score (highest first)
   - Use filters to narrow candidate list
   - Batch process shortlisting

2. **For Candidates**
   - Keep resumes under 2 pages for better parsing
   - Use standard section headings (Education, Skills, Experience)
   - Include specific skill names (not just "programming")

3. **For Database**
   - Regular backups: `mysqldump -u user -p database > backup.sql`
   - Archive old jobs: Move closed jobs to archive table
   - Optimize tables: `OPTIMIZE TABLE users, resumes, job_postings;`

## Default Credentials (Development)

These are examples - change in production:

**Candidate**
- Username: john_doe
- Password: SecurePass123

**Recruiter**
- Username: recruiter_jane
- Password: SecurePass123

## File Locations

```
project/
├── app/uploads/          ← Resume files stored here
├── app/templates/        ← HTML templates
├── app/static/           ← CSS and JavaScript
├── app/utils/            ← Business logic modules
├── app/models.py         ← Database models
├── config.py             ← Configuration
└── run.py                ← Application entry point
```

## Important Configuration Values

In `config.py`:

```python
# File upload
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}

# Pagination
ITEMS_PER_PAGE = 10

# Matching
MIN_MATCH_SCORE = 0.3  # 30% minimum

# Session
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
```

## Color Scheme Reference

- Primary Blue: `#4F46E5`
- Cyan/Secondary: `#06B6D4`
- Purple/Accent: `#8B5CF6`
- Dark Background: `#0F172A`
- Dark Text: `#0A0F1A`
- Light Text: `#F0F4F8`
- Muted Text: `#94A3B8`

## API Response Status Codes

- `200 OK` - Success
- `301 Redirect` - Redirect (form submission)
- `400 Bad Request` - Invalid input
- `401 Unauthorized` - Not logged in
- `403 Forbidden` - No permission
- `404 Not Found` - Resource not found
- `500 Server Error` - Server error

## Common SQL Queries

### Find all candidates for a job
```sql
SELECT r.candidate_name, r.email, cm.match_score
FROM candidate_matches cm
JOIN resumes r ON cm.resume_id = r.id
WHERE cm.job_id = 1
ORDER BY cm.match_score DESC;
```

### Find all jobs posted by recruiter
```sql
SELECT id, title, created_at, is_active
FROM job_postings
WHERE recruiter_id = 1
ORDER BY created_at DESC;
```

### Find shortlisted candidates
```sql
SELECT r.candidate_name, r.email, s.status, j.title
FROM shortlists s
JOIN resumes r ON s.resume_id = r.id
JOIN job_postings j ON s.job_id = j.id
WHERE j.recruiter_id = 1;
```

## Development Workflow

1. **Setup**: `python run.py`
2. **Register**: Create test accounts
3. **Upload**: Upload sample resumes
4. **Post**: Create job postings
5. **Match**: Check automatic matching
6. **Shortlist**: Shortlist promising candidates
7. **Export**: Generate reports

## Version Information

- **Application**: v1.0.0
- **Python**: 3.8+
- **Flask**: 2.3+
- **MySQL**: 5.7+
- **Bootstrap**: 5.3

## Support Resources

- **GitHub**: [repository-url]
- **Email**: support@recruitai.com
- **Documentation**: README.md
- **Setup Guide**: SETUP.md
- **API Docs**: API_DOCUMENTATION.md

## Future Enhancements

- Email notifications
- Video interviews
- Advanced analytics
- Mobile app
- Integration APIs
- Machine learning improvements
- Multi-language support
- Dark/Light theme toggle

---

Keep this guide handy for quick reference! 📋

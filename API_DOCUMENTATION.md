# API Documentation

## Overview

Resume Shortlisting Web Application provides a complete REST API for managing candidates, jobs, and recruitment workflows.

## Authentication

All protected endpoints require user authentication via Flask-Login session.

### Login
```
POST /login
Content-Type: application/x-www-form-urlencoded

username=john_doe&password=SecurePass123&remember=true
```

Response: User session created (cookie-based)

### Logout
```
GET /logout
```

## Candidate Endpoints

### Dashboard
```
GET /dashboard/candidate
```
Returns candidate dashboard with resume list and statistics.

**Authentication**: Required (Candidate role)

**Response**: HTML page

---

### Upload Resume
```
POST /dashboard/candidate/upload-resume
Content-Type: multipart/form-data

file: <binary file data>
```

**Parameters**:
- `file`: PDF or DOCX resume file (max 50MB)

**Response**:
```json
{
  "success": true,
  "message": "Resume uploaded successfully!",
  "resume_id": 123
}
```

**Error Response**:
```json
{
  "error": "Only PDF and DOCX files are allowed",
  "success": false
}
```

---

### View Resume
```
GET /dashboard/candidate/view-resume/<resume_id>
```

**Parameters**:
- `resume_id` (path): ID of resume to view

**Response**: HTML page with parsed resume data

**Authentication**: Required (Resume owner or Recruiter)

---

### Delete Resume
```
POST /dashboard/candidate/delete-resume/<resume_id>
```

**Parameters**:
- `resume_id` (path): ID of resume to delete

**Response**:
```json
{
  "success": true,
  "message": "Resume deleted"
}
```

**Error Response**:
```json
{
  "error": "Unauthorized",
  "status": 403
}
```

---

### Browse Jobs
```
GET /dashboard/candidate/jobs
```

**Query Parameters**:
- `search` (optional): Search keyword in job title/description
- `page` (optional): Page number (default: 1)

**Response**: HTML page with job listings and pagination

---

### View Job Details
```
GET /dashboard/candidate/job/<job_id>
```

**Parameters**:
- `job_id` (path): ID of job posting

**Response**: HTML page with job details and candidate's match scores

## Recruiter Endpoints

### Dashboard
```
GET /dashboard/recruiter
```

Returns recruiter dashboard with job postings and statistics.

**Authentication**: Required (Recruiter role)

**Response**: HTML page with:
- Total jobs posted
- Active job postings
- Number of candidates matched
- Shortlisted candidates count

---

### Create Job Posting
```
POST /dashboard/recruiter/create-job
Content-Type: application/x-www-form-urlencoded
```

**Parameters**:
```
title=Senior Developer
description=We are looking for...
required_skills=Python, JavaScript, SQL
nice_to_have_skills=Docker, Kubernetes
required_experience=5
required_education=Bachelor
location=New York, NY
employment_type=Full-time
salary_range=$80k-$120k
```

**Response**: Redirect to recruiter dashboard

---

### Edit Job Posting
```
GET /dashboard/recruiter/edit-job/<job_id>
```

Returns HTML form to edit job posting.

```
POST /dashboard/recruiter/edit-job/<job_id>
Content-Type: application/x-www-form-urlencoded
```

Updates job posting with new details.

**Parameters**: Same as create job

**Response**: Redirect to recruiter dashboard

---

### View Job and Candidates
```
GET /dashboard/recruiter/job/<job_id>
```

**Query Parameters**:
- `sort_by` (optional): 'score', 'name', or 'date' (default: score)
- `page` (optional): Page number

**Response**: HTML page with candidates ranked by match score

---

### Delete Job Posting
```
POST /dashboard/recruiter/delete-job/<job_id>
```

**Response**:
```json
{
  "success": true,
  "message": "Job deleted"
}
```

---

### Shortlist Candidate
```
POST /dashboard/recruiter/job/<job_id>/shortlist/<resume_id>
```

**Parameters**:
- `status` (form): 'shortlisted', 'interviewed', 'hired', or 'rejected'
- `notes` (form): Optional interview notes

**Response**:
```json
{
  "success": true,
  "message": "Candidate shortlisted"
}
```

---

### View Shortlisted Candidates
```
GET /dashboard/recruiter/shortlisted
```

**Query Parameters**:
- `job_id` (optional): Filter by specific job
- `status` (optional): Filter by status
- `page` (optional): Page number

**Response**: HTML page with shortlisted candidates

## API Endpoints (JSON)

### Get Match Score Details
```
GET /api/match-score/<match_id>
```

**Authentication**: Required

**Response**:
```json
{
  "match_score": 0.78,
  "skills_match": 0.85,
  "experience_match": 0.75,
  "education_match": 0.70,
  "matched_skills": [
    "Python (matched with: Python)",
    "JavaScript (matched with: JavaScript)"
  ],
  "missing_skills": [
    "Docker",
    "Kubernetes"
  ],
  "feedback": "Strong match in core skills..."
}
```

---

### Search Candidates
```
GET /api/search-candidates
```

**Authentication**: Required (Recruiter role)

**Query Parameters**:
- `keyword` (optional): Search in name, email, location
- `skill` (optional): Search by skill
- `limit` (optional): Max results (default: 20)

**Response**:
```json
{
  "results": [
    {
      "id": 123,
      "name": "John Doe",
      "email": "john@example.com",
      "skills": ["Python", "JavaScript", "SQL"]
    }
  ]
}
```

## Error Handling

### Common Error Responses

**401 Unauthorized**
```json
{
  "error": "Unauthorized",
  "message": "Please log in to access this page"
}
```

**403 Forbidden**
```json
{
  "error": "Forbidden",
  "message": "You don't have permission to access this resource"
}
```

**404 Not Found**
```json
{
  "error": "Not Found",
  "message": "The requested resource was not found"
}
```

**400 Bad Request**
```json
{
  "error": "Bad Request",
  "message": "Invalid parameters"
}
```

**500 Internal Server Error**
```json
{
  "error": "Server Error",
  "message": "An error occurred while processing your request"
}
```

## Data Models

### User
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "role": "candidate",
  "is_active": true,
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Resume
```json
{
  "id": 1,
  "user_id": 1,
  "filename": "john_doe_resume.pdf",
  "candidate_name": "John Doe",
  "email": "john@example.com",
  "phone": "+1-555-123-4567",
  "location": "New York, NY",
  "skills": ["Python", "JavaScript", "SQL"],
  "experience": [
    {
      "title": "Senior Developer",
      "company": "Tech Corp",
      "duration": "2020-2024"
    }
  ],
  "education": [
    {
      "degree": "Bachelor",
      "field": "Computer Science",
      "year": "2020"
    }
  ],
  "is_parsed": true,
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Job Posting
```json
{
  "id": 1,
  "recruiter_id": 1,
  "title": "Senior Developer",
  "description": "We are looking for...",
  "required_skills": ["Python", "JavaScript", "SQL"],
  "required_experience": 5,
  "required_education": "Bachelor",
  "location": "New York, NY",
  "salary_range": "$80k-$120k",
  "employment_type": "Full-time",
  "is_active": true,
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Candidate Match
```json
{
  "id": 1,
  "job_id": 1,
  "resume_id": 1,
  "match_score": 0.78,
  "skills_match": 0.85,
  "experience_match": 0.75,
  "education_match": 0.70,
  "matched_skills": ["Python", "JavaScript"],
  "missing_skills": ["Docker", "Kubernetes"],
  "created_at": "2024-01-15T10:30:00Z"
}
```

## Rate Limiting

Currently, the API does not implement rate limiting. In production, implement using Flask-Limiter:

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
```

## CORS

CORS is not enabled by default. To enable cross-origin requests:

```python
from flask_cors import CORS
CORS(app, origins=["https://example.com"])
```

## Pagination

API endpoints that return lists support pagination:

**Query Parameters**:
- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 10, max: 100)

**Response Headers**:
```
X-Total-Count: 150
X-Total-Pages: 15
X-Current-Page: 1
```

## Webhooks

Webhooks can be implemented for:
- Resume parsed
- Job created
- Candidate matched
- Interview scheduled

```python
# Example webhook implementation
@app.route('/webhook/match-created', methods=['POST'])
def on_match_created():
    # Handle webhook
    pass
```

## SDK & Client Libraries

### Python Client
```python
from recruitai import RecruitAI

client = RecruitAI(base_url="http://localhost:5000")
client.login(username="john_doe", password="SecurePass123")

# Search candidates
results = client.search_candidates(keyword="Python")

# Get match score
match = client.get_match_score(match_id=123)
```

### JavaScript Client
```javascript
const client = new RecruitAI({
  baseUrl: "http://localhost:5000"
});

await client.login("john_doe", "SecurePass123");
const results = await client.searchCandidates({ keyword: "Python" });
```

## API Versioning

Current API version: v1.0

Future versions will use URL versioning:
- `/api/v1/candidates`
- `/api/v2/candidates`

## Testing

### Using cURL

**Login**:
```bash
curl -X POST http://localhost:5000/login \
  -d "username=john_doe&password=SecurePass123" \
  -c cookies.txt
```

**Upload Resume**:
```bash
curl -X POST http://localhost:5000/dashboard/candidate/upload-resume \
  -F "file=@resume.pdf" \
  -b cookies.txt
```

**Search Candidates**:
```bash
curl -X GET "http://localhost:5000/api/search-candidates?keyword=Python" \
  -b cookies.txt
```

## Support

For API support and issues, contact: api-support@recruitai.com

---

**API Documentation v1.0**
Last updated: 2024-01-15

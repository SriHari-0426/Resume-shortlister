#!/usr/bin/env python
"""
Resume Shortlisting Web Application
Main application entry point
"""

import os
import sys
from app import create_app
from app.models import db, User, Resume, JobPosting, CandidateMatch, Shortlist

# Get configuration
config_name = os.getenv('FLASK_ENV', 'development')

# Create application
app = create_app(config_name)

@app.shell_context_processor
def make_shell_context():
    """Register models for Flask shell"""
    return {
        'db': db,
        'User': User,
        'Resume': Resume,
        'JobPosting': JobPosting,
        'CandidateMatch': CandidateMatch,
        'Shortlist': Shortlist
    }

if __name__ == '__main__':
    # Create app context and initialize database
    with app.app_context():
        db.create_all()
    
    # Run the application
    debug = config_name == 'development'
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000)),
        debug=debug
    )

 def handle_hr(intent, inputs):

    # ── INTENT 1: View Candidate List ──
    if intent == 'view_candidates':
        job_role = inputs.get('job_role', '')
        status_filter = inputs.get('status_filter', 'All')

        if status_filter == 'Shortlisted':
            candidates = [
                {'name': 'Rahul Sharma', 'score': '92%', 'status': 'Shortlisted'},
                {'name': 'Priya Singh', 'score': '88%', 'status': 'Shortlisted'}
            ]
        elif status_filter == 'Pending':
            candidates = [
                {'name': 'Amit Kumar', 'score': '75%', 'status': 'Pending'},
                {'name': 'Sneha Patel', 'score': '71%', 'status': 'Pending'},
                {'name': 'Ravi Verma', 'score': '68%', 'status': 'Pending'}
            ]
        else:
            candidates = [
                {'name': 'Rahul Sharma', 'score': '92%', 'status': 'Shortlisted'},
                {'name': 'Priya Singh', 'score': '88%', 'status': 'Shortlisted'},
                {'name': 'Amit Kumar', 'score': '75%', 'status': 'Pending'},
                {'name': 'Sneha Patel', 'score': '71%', 'status': 'Pending'}
            ]

        return {
            'insight': f'Found {len(candidates)} candidates for {job_role}',
            'status': 'success',
            'candidates': candidates,
            'suggestions': [
                f'{len(candidates)} candidates found for {job_role}',
                'Review top candidates first',
                'Shortlist candidates with score above 80%'
            ],
            'actions': ['Shortlist All', 'Download List', 'Send Invites']
        }

    # ── INTENT 2: Schedule Interview ──
    elif intent == 'schedule_interview':
        candidate_id = inputs.get('candidate_id', '')
        interview_type = inputs.get('interview_type', '')
        date = inputs.get('date', '')

        if not candidate_id:
            return {
                'insight': 'Please enter Candidate ID',
                'status': 'error',
                'suggestions': ['Enter a valid Candidate ID'],
                'actions': ['Try Again']
            }

        if interview_type == 'Online':
            details = 'Zoom meeting link will be sent to candidate email'
        elif interview_type == 'Offline':
            details = 'Venue: Office - Block A, Room 201'
        else:
            details = 'Phone interview - candidate will receive a call'

        return {
            'insight': f'Interview Scheduled for Candidate {candidate_id}',
            'status': 'success',
            'suggestions': [
                f'Interview Type: {interview_type}',
                f'Scheduled: {date}',
                details
            ],
            'actions': ['Send Notification', 'Add to Calendar', 'Download Confirmation']
        }

    # ── INTENT 3: Post Job Opening ──
    elif intent == 'post_job':
        role_title = inputs.get('role_title', 'New Role')
        skills_required = inputs.get('skills_required', '')
        duration = inputs.get('duration', '')

        return {
            'insight': f'Job Opening Ready to Publish: {role_title}',
            'status': 'success',
            'suggestions': [
                f'Role: {role_title}',
                f'Required Skill: {skills_required}',
                f'Duration: {duration}',
                'This job will be visible to all eligible students'
            ],
            'actions': ['Publish Job', 'Save Draft', 'Preview']
        }

    else:
        return {
            'insight': 'Something went wrong',
            'status': 'error',
            'suggestions': ['Please select a valid intent'],
            'actions': ['Go Back']
        }
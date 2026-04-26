def handle_student(intent, inputs):

    # ── INTENT 1: Check Application Status ──
    if intent == 'check_status':
        student_id = inputs.get('student_id', '')
        company = inputs.get('company', '')

        if not student_id:
            return {
                'insight': 'Please enter your Student ID',
                'status': 'error',
                'suggestions': ['Enter a valid Student ID to check status'],
                'actions': ['Try Again']
            }

        if company == 'Google':
            return {
                'insight': f'Your application to {company} is Under Review',
                'status': 'pending',
                'suggestions': [
                    'Complete your profile to 100%',
                    'Prepare for technical interview',
                    'Practice Data Structures and Algorithms'
                ],
                'actions': ['Download Report', 'Share Status']
            }
        elif company == 'Amazon':
            return {
                'insight': f'Congratulations! You are Shortlisted at {company}',
                'status': 'selected',
                'suggestions': [
                    'Check your email for interview details',
                    'Prepare for Leadership Principles questions',
                    'Practice System Design concepts'
                ],
                'actions': ['Download Offer', 'Share Status']
            }
        else:
            return {
                'insight': f'Your application to {company} is Pending Review',
                'status': 'pending',
                'suggestions': [
                    'Keep your profile updated',
                    'Add more relevant skills',
                    'Follow up after 1 week'
                ],
                'actions': ['Download Report', 'Share Status']
            }

    # ── INTENT 2: Find Internship Opportunities ──
    elif intent == 'find_opportunities':
        skill = inputs.get('skill', '')
        domain = inputs.get('domain', '')
        location = inputs.get('location', '')

        if skill == 'Python' or skill == 'Machine Learning':
            jobs = ['Data Science Intern at TCS',
                    'ML Engineer Intern at Wipro',
                    'Python Developer Intern at Infosys']
        elif skill == 'React':
            jobs = ['Frontend Intern at Google',
                    'UI Developer Intern at Amazon',
                    'React Developer Intern at Microsoft']
        elif skill == 'Java':
            jobs = ['Backend Intern at TCS',
                    'Java Developer Intern at Infosys',
                    'Software Intern at Wipro']
        else:
            jobs = ['Software Intern at TCS',
                    'Technology Intern at Wipro',
                    'Developer Intern at Infosys']

        return {
            'insight': f'Found {len(jobs)} opportunities matching your profile',
            'status': 'success',
            'jobs': jobs,
            'suggestions': [
                f'Your skill {skill} is in high demand',
                f'{location} has good opportunities in {domain}',
                'Apply to at least 3 companies for better chances'
            ],
            'actions': ['Apply Now', 'Save List', 'Share']
        }

    # ── INTENT 3: Get Profile Improvement Tips ──
    elif intent == 'profile_tips':
        cgpa = inputs.get('cgpa', '')
        skills_count = inputs.get('skills_count', '')
        target_role = inputs.get('target_role', '')

        if cgpa == 'Above 8':
            readiness = 'Strong'
            score = '85%'
            tips = [
                'Your CGPA is excellent — highlight it in your resume',
                'Focus on building 1-2 strong projects',
                'Apply to top-tier companies like Google and Amazon'
            ]
        elif cgpa == '7 to 8':
            readiness = 'Good'
            score = '70%'
            tips = [
                'Good CGPA — focus on improving your skills',
                'Build at least 2 projects related to your target role',
                'Get 1-2 certifications to strengthen your profile'
            ]
        elif cgpa == '6 to 7':
            readiness = 'Average'
            score = '50%'
            tips = [
                'Focus heavily on building practical skills',
                'Create projects to compensate for CGPA',
                'Apply to mid-tier companies and startups'
            ]
        else:
            readiness = 'Needs Improvement'
            score = '30%'
            tips = [
                'Focus on improving your academics first',
                'Build strong practical projects to compensate',
                'Apply to startups and smaller companies'
            ]

        return {
            'insight': f'Your Profile Readiness: {readiness} ({score})',
            'status': 'success',
            'suggestions': tips,
            'actions': ['Download Tips', 'Share Report']
        }

    # ── Default ──
    else:
        return {
            'insight': 'Something went wrong',
            'status': 'error',
            'suggestions': ['Please select a valid intent'],
            'actions': ['Go Back']
        }

 def handle_college(intent, inputs):

    # ── INTENT 1: View Placement Statistics ──
    if intent == 'placement_stats':
        department = inputs.get('department', 'All')
        batch_year = inputs.get('batch_year', '2025')

        stats = {
            'Computer Science': {'placed': 85, 'total': 100, 'avg_package': '6.5 LPA', 'top_company': 'TCS'},
            'Electronics':      {'placed': 72, 'total': 90,  'avg_package': '5.8 LPA', 'top_company': 'Infosys'},
            'Mechanical':       {'placed': 60, 'total': 85,  'avg_package': '4.5 LPA', 'top_company': 'Wipro'},
            'Civil':            {'placed': 45, 'total': 70,  'avg_package': '4.0 LPA', 'top_company': 'L&T'},
            'All':              {'placed': 262, 'total': 345, 'avg_package': '5.7 LPA', 'top_company': 'TCS'}
        }

        dept_stats = stats.get(department, stats['All'])
        placement_pct = round((dept_stats['placed'] / dept_stats['total']) * 100)

        return {
            'insight': f'{department} Placement: {placement_pct}% ({dept_stats["placed"]}/{dept_stats["total"]} students)',
            'status': 'success',
            'suggestions': [
                f'Batch Year: {batch_year}',
                f'Average Package: {dept_stats["avg_package"]}',
                f'Top Recruiting Company: {dept_stats["top_company"]}',
                f'Total Placed: {dept_stats["placed"]} out of {dept_stats["total"]} students'
            ],
            'actions': ['Download Report', 'Share Stats', 'View Details']
        }

    # ── INTENT 2: Upload Student Data ──
    elif intent == 'upload_students':
        department = inputs.get('department', '')
        batch_year = inputs.get('batch_year', '')
        student_count = inputs.get('student_count', '')

        if not department:
            return {
                'insight': 'Please select a Department',
                'status': 'error',
                'suggestions': ['Select the department to upload students for'],
                'actions': ['Try Again']
            }

        return {
            'insight': f'Ready to Upload {student_count} Students for {department}',
            'status': 'success',
            'suggestions': [
                f'Department: {department}',
                f'Batch Year: {batch_year}',
                f'Student Count: {student_count}',
                'All student profiles will be created automatically'
            ],
            'actions': ['Confirm Upload', 'Cancel', 'Download Template']
        }

    # ── INTENT 3: Contact HR / Company ──
    elif intent == 'contact_hr':
        company_name = inputs.get('company_name', '')
        drive_type = inputs.get('drive_type', '')
        preferred_date = inputs.get('preferred_date', '')

        if drive_type == 'Campus Drive':
            message = f'Dear {company_name} HR Team, We would like to invite you for a Campus Drive at our college.'
        elif drive_type == 'Virtual Drive':
            message = f'Dear {company_name} HR Team, We would like to schedule a Virtual Placement Drive.'
        else:
            message = f'Dear {company_name} HR Team, We would like to invite you for a Pool Campus Drive.'

        return {
            'insight': f'Message Ready to Send to {company_name}',
            'status': 'success',
            'message': message,
            'suggestions': [
                f'Company: {company_name}',
                f'Drive Type: {drive_type}',
                f'Preferred Date: {preferred_date}',
                'Message drafted and ready to send'
            ],
            'actions': ['Send Message', 'Edit Message', 'Download Draft']
        }

    else:
        return {
            'insight': 'Something went wrong',
            'status': 'error',
            'suggestions': ['Please select a valid intent'],
            'actions': ['Go Back']
        }
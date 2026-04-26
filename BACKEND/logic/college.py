def handle_college(intent, inputs):
    try:
        if not inputs:
            return {
                "insight": "No input provided",
                "status": "error",
                "suggestions": ["Provide required inputs"],
                "actions": ["Try Again"]
            }

        # -------- INTENT 1 --------
        if intent == 'placement_stats':
            department = inputs.get('department', 'All')
            batch_year = inputs.get('batch_year', '2025')

            stats = {
                'Computer Science': {'placed': 85, 'total': 100, 'avg_package': '6.5 LPA', 'top_company': 'Amazon'},
                'Electronics': {'placed': 72, 'total': 90, 'avg_package': '5.8 LPA', 'top_company': 'Infosys'},
                'Mechanical': {'placed': 60, 'total': 85, 'avg_package': '4.5 LPA', 'top_company': 'TCS'},
                'Civil': {'placed': 45, 'total': 70, 'avg_package': '4.0 LPA', 'top_company': 'Wipro'},
                'All': {'placed': 262, 'total': 345, 'avg_package': '5.7 LPA', 'top_company': 'Amazon'}
            }

            dept_stats = stats.get(department, stats['All'])
            placement_pct = round((dept_stats['placed'] / dept_stats['total']) * 100)

            return {
                'insight': f'{department} Placement: {placement_pct}%',
                'status': 'success',
                'suggestions': [
                    f'Batch Year: {batch_year}',
                    f'Average Package: {dept_stats["avg_package"]}',
                    f'Top Company: {dept_stats["top_company"]}',
                    f'Total Placed: {dept_stats["placed"]}/{dept_stats["total"]}'
                ],
                'actions': ['Download Report', 'View Details']
            }

        # -------- INTENT 2 --------
        elif intent == 'upload_students':
            department = inputs.get('department')
            batch_year = inputs.get('batch_year')
            student_count = inputs.get('student_count')

            if not department:
                return {
                    'insight': 'Department missing',
                    'status': 'error',
                    'suggestions': ['Select department'],
                    'actions': ['Retry']
                }

            return {
                'insight': f'Ready to upload {student_count} students',
                'status': 'success',
                'suggestions': [
                    f'Department: {department}',
                    f'Batch: {batch_year}'
                ],
                'actions': ['Confirm Upload']
            }

        # -------- INTENT 3 --------
        elif intent == 'contact_hr':
            company_name = inputs.get('company_name')
            drive_type = inputs.get('drive_type')

            if not company_name:
                return {
                    'insight': 'Company name missing',
                    'status': 'error',
                    'suggestions': ['Enter company name'],
                    'actions': ['Retry']
                }

            return {
                'insight': f'Message ready for {company_name}',
                'status': 'success',
                'actions': ['Send Message']
            }

        # -------- INVALID INTENT --------
        else:
            return {
                'insight': 'Invalid intent',
                'status': 'error',
                'suggestions': ['Choose valid option'],
                'actions': ['Go Back']
            }

    except Exception as e:
        return {
            "insight": "Internal Server Error",
            "status": "error",
            "suggestions": [str(e)],
            "actions": ["Retry"]
        }
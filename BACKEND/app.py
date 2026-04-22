from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ── ENDPOINT 1: Get all roles ──
@app.route('/api/roles', methods=['GET'])
def get_roles():
    roles = [
        {'id': 'student', 'label': 'Student', 'icon': 'S'},
        {'id': 'hr', 'label': 'HR', 'icon': 'H'},
        {'id': 'referrer', 'label': 'Referrer', 'icon': 'R'},
        {'id': 'college', 'label': 'College', 'icon': 'C'}
    ]
    return jsonify({'roles': roles})

# ── ENDPOINT 2: Get intents for a role ──
@app.route('/api/intents', methods=['GET'])
def get_intents():
    role = request.args.get('role')

    intents = {
        'student': [
            {'id': 'check_status', 'label': 'Check Application Status',
             'fields': [
                 {'id': 'student_id', 'label': 'Student ID', 'type': 'text'},
                 {'id': 'company', 'label': 'Company Name', 'type': 'select',
                  'options': ['Google', 'Amazon', 'Infosys', 'TCS', 'Wipro']}
             ]},
            {'id': 'find_opportunities', 'label': 'Find Internship Opportunities',
             'fields': [
                 {'id': 'skill', 'label': 'Your Skill', 'type': 'select',
                  'options': ['Python', 'Java', 'React', 'Machine Learning', 'Data Science']},
                 {'id': 'domain', 'label': 'Preferred Domain', 'type': 'select',
                  'options': ['Technology', 'Finance', 'Marketing', 'Design']},
                 {'id': 'location', 'label': 'Location', 'type': 'select',
                  'options': ['Remote', 'Bangalore', 'Mumbai', 'Delhi', 'Hyderabad']}
             ]},
            {'id': 'profile_tips', 'label': 'Get Profile Improvement Tips',
             'fields': [
                 {'id': 'cgpa', 'label': 'Your CGPA', 'type': 'select',
                  'options': ['Below 6', '6 to 7', '7 to 8', 'Above 8']},
                 {'id': 'skills_count', 'label': 'Number of Skills', 'type': 'select',
                  'options': ['1-2 skills', '3-4 skills', '5+ skills']},
                 {'id': 'target_role', 'label': 'Target Role', 'type': 'select',
                  'options': ['Software Engineer', 'Data Analyst', 'Product Manager', 'Designer']}
             ]}
        ],
        'hr': [
            {'id': 'view_candidates', 'label': 'View Candidate List',
             'fields': [
                 {'id': 'job_role', 'label': 'Job Role', 'type': 'select',
                  'options': ['Software Engineer', 'Data Analyst', 'Product Manager']},
                 {'id': 'status_filter', 'label': 'Filter by Status', 'type': 'select',
                  'options': ['All', 'Shortlisted', 'Pending', 'Rejected']}
             ]},
            {'id': 'schedule_interview', 'label': 'Schedule an Interview',
             'fields': [
                 {'id': 'candidate_id', 'label': 'Candidate ID', 'type': 'text'},
                 {'id': 'interview_type', 'label': 'Interview Type', 'type': 'select',
                  'options': ['Online', 'Offline', 'Telephonic']},
                 {'id': 'date', 'label': 'Preferred Date', 'type': 'select',
                  'options': ['This Week', 'Next Week', 'In 2 Weeks']}
             ]},
            {'id': 'post_job', 'label': 'Post a New Job Opening',
             'fields': [
                 {'id': 'role_title', 'label': 'Role Title', 'type': 'text'},
                 {'id': 'skills_required', 'label': 'Skills Required', 'type': 'select',
                  'options': ['Python', 'Java', 'React', 'SQL', 'Machine Learning']},
                 {'id': 'duration', 'label': 'Duration', 'type': 'select',
                  'options': ['1 Month', '2 Months', '3 Months', '6 Months']}
             ]}
        ],
        'referrer': [
            {'id': 'refer_candidate', 'label': 'Refer a Candidate',
             'fields': [
                 {'id': 'candidate_name', 'label': 'Candidate Name', 'type': 'text'},
                 {'id': 'job_role', 'label': 'Job Role', 'type': 'select',
                  'options': ['Software Engineer', 'Data Analyst', 'Product Manager']},
                 {'id': 'relationship', 'label': 'Your Relationship', 'type': 'select',
                  'options': ['Friend', 'Colleague', 'Former Classmate', 'Family']}
             ]},
            {'id': 'track_referral', 'label': 'Track Referral Status',
             'fields': [
                 {'id': 'referral_id', 'label': 'Referral ID', 'type': 'text'},
                 {'id': 'candidate_name', 'label': 'Candidate Name', 'type': 'text'}
             ]},
            {'id': 'referral_history', 'label': 'View Referral History',
             'fields': [
                 {'id': 'time_period', 'label': 'Time Period', 'type': 'select',
                  'options': ['This Month', 'Last 3 Months', 'This Year', 'All Time']},
                 {'id': 'status_filter', 'label': 'Filter by Status', 'type': 'select',
                  'options': ['All', 'Successful', 'Pending', 'Rejected']}
             ]}
        ],
        'college': [
            {'id': 'placement_stats', 'label': 'View Placement Statistics',
             'fields': [
                 {'id': 'department', 'label': 'Department', 'type': 'select',
                  'options': ['Computer Science', 'Electronics', 'Mechanical', 'Civil', 'All']},
                 {'id': 'batch_year', 'label': 'Batch Year', 'type': 'select',
                  'options': ['2025', '2024', '2023', '2022']}
             ]},
            {'id': 'upload_students', 'label': 'Upload Student Data',
             'fields': [
                 {'id': 'department', 'label': 'Department', 'type': 'select',
                  'options': ['Computer Science', 'Electronics', 'Mechanical', 'Civil']},
                 {'id': 'batch_year', 'label': 'Batch Year', 'type': 'select',
                  'options': ['2025', '2024', '2023']},
                 {'id': 'student_count', 'label': 'Number of Students', 'type': 'select',
                  'options': ['1-50', '51-100', '101-200', '200+']}
             ]},
            {'id': 'contact_hr', 'label': 'Contact HR / Company',
             'fields': [
                 {'id': 'company_name', 'label': 'Company Name', 'type': 'select',
                  'options': ['Google', 'Amazon', 'Infosys', 'TCS', 'Wipro', 'Microsoft']},
                 {'id': 'drive_type', 'label': 'Drive Type', 'type': 'select',
                  'options': ['Campus Drive', 'Virtual Drive', 'Pool Campus']},
                 {'id': 'preferred_date', 'label': 'Preferred Date', 'type': 'select',
                  'options': ['This Month', 'Next Month', 'In 3 Months']}
             ]}
        ]
    }

    if role not in intents:
        return jsonify({'error': 'Invalid role'}), 400

    return jsonify({'intents': intents[role]})

# ── ENDPOINT 3: Process input and return output ──
@app.route('/api/process', methods=['POST'])
def process():
    data = request.get_json()
    role = data.get('role')
    intent = data.get('intent')
    inputs = data.get('inputs', {})

    # Import role logic
    if role == 'student':
        from logic.student import handle_student
        result = handle_student(intent, inputs)
    elif role == 'hr':
        from logic.hr import handle_hr
        result = handle_hr(intent, inputs)
    elif role == 'referrer':
        from logic.referrer import handle_referrer
        result = handle_referrer(intent, inputs)
    elif role == 'college':
        from logic.college import handle_college
        result = handle_college(intent, inputs)
    else:
        return jsonify({'error': 'Invalid role'}), 400

    return jsonify(result)

# ── Run server ──
if __name__ == '__main__':
    app.run(debug=True, port=5000)
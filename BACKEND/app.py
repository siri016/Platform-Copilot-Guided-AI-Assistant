from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return "Backend Running ✅"

# ---------------- ROLES ----------------
@app.route('/api/roles', methods=['GET'])
def get_roles():
    return jsonify({
        "roles": [
            {"id": "student", "label": "Student"},
            {"id": "hr", "label": "HR"},
            {"id": "referrer", "label": "Referrer"},
            {"id": "college", "label": "College"}
        ]
    })

# ---------------- INTENTS ----------------
@app.route('/api/intents', methods=['GET'])
def get_intents():
    role = request.args.get('role')

    intents = {
        "student": [
            {
                "id": "check_status",
                "label": "Check Application Status",
                "fields": [
                    {"id": "student_id", "label": "Student ID", "type": "text"},
                    {
                        "id": "company",
                        "label": "Company Name",
                        "type": "select",
                        "options": ["Google", "Amazon", "Infosys", "TCS", "Wipro"]
                    }
                ]
            },
            {
                "id": "find_opportunities",
                "label": "Find Internship Opportunities",
                "fields": [
                    {
                        "id": "skill",
                        "label": "Your Skill",
                        "type": "select",
                        "options": ["Python", "Java", "React", "Machine Learning", "Data Science"]
                    },
                    {
                        "id": "domain",
                        "label": "Preferred Domain",
                        "type": "select",
                        "options": ["Technology", "Finance", "Marketing", "Design"]
                    },
                    {
                        "id": "location",
                        "label": "Location",
                        "type": "select",
                        "options": ["Remote", "Bangalore", "Mumbai", "Delhi", "Hyderabad"]
                    }
                ]
            },
            {
                "id": "profile_tips",
                "label": "Get Profile Improvement Tips",
                "fields": [
                    {
                        "id": "cgpa",
                        "label": "Your CGPA",
                        "type": "select",
                        "options": ["Below 6", "6 to 7", "7 to 8", "Above 8"]
                    },
                    {
                        "id": "skills_count",
                        "label": "Number of Skills",
                        "type": "select",
                        "options": ["1-2 skills", "3-4 skills", "5+ skills"]
                    },
                    {
                        "id": "target_role",
                        "label": "Target Role",
                        "type": "select",
                        "options": ["Software Engineer", "Data Analyst", "Product Manager", "Designer"]
                    }
                ]
            }
        ],
        "hr": [
            {
                "id": "post_job",
                "label": "Post Job",
                "fields": [
                    {"id": "role", "label": "Job Role", "type": "text"}
                ]
            }
        ],
        "referrer": [
            {
                "id": "track",
                "label": "Track Referral",
                "fields": [
                    {"id": "ref_id", "label": "Referral ID", "type": "text"}
                ]
            }
        ],
        "college": [
            {
                "id": "stats",
                "label": "Placement Stats",
                "fields": [
                    {"id": "dept", "label": "Department", "type": "text"}
                ]
            }
        ]
    }

    if role not in intents:
        return jsonify({"error": "Invalid role"}), 400

    return jsonify({"intents": intents[role]})

# ---------------- PROCESS ----------------
@app.route('/api/process', methods=['POST'])
def process():
    data = request.get_json()

    role = data.get("role")
    intent = data.get("intent")
    inputs = data.get("inputs", {})

    if role == "student":

        if intent == "check_status":
            if not inputs.get("student_id") or not inputs.get("company"):
                return jsonify({"error": "Missing required fields"}), 400

            return jsonify({
                "message": f"Status for {inputs.get('student_id')} at {inputs.get('company')} is PROCESSING"
            })

        elif intent == "find_opportunities":
            return jsonify({
                "message": f"Opportunities for {inputs.get('skill')} in {inputs.get('location')}"
            })

        elif intent == "profile_tips":
            return jsonify({
                "message": f"Improve profile for {inputs.get('target_role')} with {inputs.get('skills_count')}"
            })

        else:
            return jsonify({"error": "Invalid intent"}), 400

    elif role == "hr":
        return jsonify({"message": "Job posted"})

    elif role == "referrer":
        return jsonify({"message": "Referral tracked"})

    elif role == "college":
        return jsonify({"message": "Stats shown"})

    else:
        return jsonify({"error": "Invalid role"}), 400


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)

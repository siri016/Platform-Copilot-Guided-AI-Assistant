import sys
import os

# Allow importing from parent folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, request
from flask_cors import CORS

from logic.student import handle_student
from logic.hr import handle_hr
from logic.referrer import handle_referrer
from logic.college import handle_college
from data_engine.logger import log

app = Flask(__name__)
CORS(app)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return "Backend Running ✅"

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
                        "label": "Company",
                        "type": "select",
                        "options": ["Google", "Amazon", "Infosys", "TCS", "Wipro"]
                    }
                ]
            },
            {
                "id": "find_opportunities",
                "label": "Find Opportunities",
                "fields": [
                    {
                        "id": "skill",
                        "label": "Skill",
                        "type": "select",
                        "options": ["Python", "Java", "React"]
                    },
                    {
                        "id": "domain",
                        "label": "Domain",
                        "type": "select",
                        "options": ["Technology", "Finance"]
                    },
                    {
                        "id": "location",
                        "label": "Location",
                        "type": "select",
                        "options": ["Bangalore", "Remote"]
                    }
                ]
            }
        ],

        "hr": [
            {
                "id": "view_candidates",
                "label": "View Candidates",
                "fields": [
                    {"id": "job_role", "label": "Job Role", "type": "text"},
                    {
                        "id": "status_filter",
                        "label": "Status",
                        "type": "select",
                        "options": ["All", "Shortlisted", "Pending"]
                    }
                ]
            }
        ],

        "referrer": [
            {
                "id": "track_referral",
                "label": "Track Referral",
                "fields": [
                    {"id": "referral_id", "label": "Referral ID", "type": "text"},
                    {"id": "candidate_name", "label": "Candidate Name", "type": "text"}
                ]
            }
        ],

        "college": [
            {
                "id": "placement_stats",
                "label": "Placement Stats",
                "fields": [
                    {"id": "department", "label": "Department", "type": "text"},
                    {"id": "batch_year", "label": "Batch Year", "type": "text"}
                ]
            }
        ]
    }

    return jsonify({"intents": intents.get(role, [])})

# ---------------- PROCESS ----------------
@app.route('/api/process', methods=['POST'])
def process():
    data = request.get_json()

    # 🔍 DEBUG PRINTS (VERY IMPORTANT)
    print("\n=== NEW REQUEST ===")
    print("RAW DATA:", data)

    role = data.get("role")
    intent = data.get("intent")
    inputs = data.get("inputs", {})

    print("ROLE:", role)
    print("INTENT:", intent)
    print("INPUTS:", inputs)

    try:
        # Logging
        log(role, intent)

        if role == "student":
            result = handle_student(intent, inputs)

        elif role == "hr":
            result = handle_hr(intent, inputs)

        elif role == "referrer":
            result = handle_referrer(intent, inputs)

        elif role == "college":
            result = handle_college(intent, inputs)

        else:
            return jsonify({
                "insight": "Invalid role",
                "status": "error",
                "suggestions": ["Choose a valid role"],
                "actions": ["Retry"]
            }), 400

        print("RESULT:", result)  # 🔍 DEBUG

        return jsonify(result)

    except Exception as e:
        print("🔥 ERROR OCCURRED:", str(e))  # 🔥 CRITICAL DEBUG

        return jsonify({
            "insight": "Server Error",
            "status": "error",
            "suggestions": [str(e)],
            "actions": ["Retry"]
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
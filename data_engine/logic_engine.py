from db import get_db
from logger import log

# --------------------------------------
# COMMON QUERY FUNCTION
# --------------------------------------
def query(q, args=()):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(q, args)
    res = [r[0] for r in cur.fetchall()]
    conn.close()
    return res


# --------------------------------------
# STUDENT FUNCTIONS
# --------------------------------------

def skill_gap(target_role, user_skills):
    required = query("SELECT skill_name FROM skills WHERE role_name=?", (target_role,))

    if not required:
        return error("Invalid role")

    missing = [s for s in required if s not in user_skills]
    score = int(((len(required) - len(missing)) / len(required)) * 100)

    suggestions = []
    for m in missing:
        courses = query("SELECT course_name FROM courses WHERE skill_name=?", (m,))
        suggestions += [f"{m}: {c}" for c in courses]

    return {
        "insights": [
            f"Target Role: {target_role}",
            f"Match Score: {score}%"
        ],
        "suggestions": suggestions if suggestions else ["No skill gap — you're ready!"],
        "actions": ["View Courses", "Start Learning"]
    }


def career(interest):
    roles = query("SELECT role FROM career_map WHERE interest=?", (interest,))

    return {
        "insights": [f"Career options for {interest}"],
        "suggestions": roles if roles else ["No matching roles found"],
        "actions": ["Explore Roles"]
    }


def internship(role):
    jobs = query("SELECT internship FROM internships WHERE role=?", (role,))

    return {
        "insights": [f"Internships for {role}"],
        "suggestions": jobs if jobs else ["No internships found"],
        "actions": ["Apply Now"]
    }


def resume():
    tips = query("SELECT tip FROM resume_tips")

    return {
        "insights": ["Resume Improvement Tips"],
        "suggestions": tips if tips else ["Add projects", "Highlight skills"],
        "actions": ["Improve Resume"]
    }


# --------------------------------------
# HR FUNCTIONS
# --------------------------------------

def role_match(role, skills):
    required = query("SELECT skill_name FROM skills WHERE role_name=?", (role,))

    if not required:
        return error("Invalid role")

    matched = list(set(required) & set(skills))
    score = int((len(matched) / len(required)) * 100)

    return {
        "insights": [f"Match Score: {score}%"],
        "suggestions": matched if matched else ["No matching skills"],
        "actions": ["Shortlist", "Reject"]
    }


def skill_requirement(role):
    skills = query("SELECT skill_name FROM skills WHERE role_name=?", (role,))

    return {
        "insights": [f"Required skills for {role}"],
        "suggestions": skills if skills else ["No data available"],
        "actions": ["Download JD"]
    }


def screening(exp):
    status = "Qualified" if exp > 2 else "Needs Training"

    return {
        "insights": [f"Candidate Status: {status}"],
        "suggestions": [],
        "actions": ["Proceed", "Hold"]
    }


# --------------------------------------
# COLLEGE FUNCTIONS
# --------------------------------------

def performance(score):
    if score > 75:
        level = "Excellent"
    elif score > 50:
        level = "Average"
    else:
        level = "Needs Improvement"

    return {
        "insights": [f"Performance Level: {level}"],
        "suggestions": ["Practice more", "Take mock tests"],
        "actions": ["View Report"]
    }


def placement(branch):
    return {
        "insights": [f"Placement trends for {branch}"],
        "suggestions": ["High demand roles", "Skill upgrades required"],
        "actions": ["Download Report"]
    }


def training(domain):
    return {
        "insights": [f"Recommended training for {domain}"],
        "suggestions": ["AI Training", "Cloud Bootcamp"],
        "actions": ["Enroll Now"]
    }


# --------------------------------------
# REFERRER FUNCTIONS
# --------------------------------------

def candidate():
    return {
        "insights": ["Candidate profile analyzed"],
        "suggestions": ["Strong in Python", "Needs Machine Learning"],
        "actions": ["Refer Candidate"]
    }


def match():
    return {
        "insights": ["Matching job roles"],
        "suggestions": ["Data Analyst", "ML Engineer"],
        "actions": ["Refer Now"]
    }


# --------------------------------------
# PROCESS ROUTER
# --------------------------------------

def process(role, intent, payload):
    log(role, intent)

    try:
        # STUDENT
        if role == "Student":
            if intent == "skill_gap":
                return skill_gap(payload.get("target_role"), payload.get("skills", []))
            if intent == "career":
                return career(payload.get("interest"))
            if intent == "internship":
                return internship(payload.get("target_role"))
            if intent == "resume":
                return resume()

        # HR
        elif role == "HR":
            if intent == "role_match":
                return role_match(payload.get("role"), payload.get("skills", []))
            if intent == "skill_requirement":
                return skill_requirement(payload.get("role"))
            if intent == "screening":
                return screening(payload.get("experience", 0))

        # COLLEGE
        elif role == "College":
            if intent == "performance":
                return performance(payload.get("score", 0))
            if intent == "placement":
                return placement(payload.get("branch"))
            if intent == "training":
                return training(payload.get("domain"))

        # REFERRER
        elif role == "Referrer":
            if intent == "candidate":
                return candidate()
            if intent == "match":
                return match()
            if intent == "resume":
                return resume()

    except Exception as e:
        return error(f"Error: {str(e)}")

    return error("Invalid role or intent")


# --------------------------------------
# ERROR HANDLER
# --------------------------------------

def error(msg):
    return {
        "insights": [msg],
        "suggestions": [],
        "actions": []
    }

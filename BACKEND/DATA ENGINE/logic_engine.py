from db import get_db
from logger import log

def query(q, args=()):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(q, args)
    res = [r[0] for r in cur.fetchall()]
    conn.close()
    return res


def skill_gap(target_role, user_skills):
    required = query("SELECT skill_name FROM skills WHERE role_name=?", (target_role,))
    missing = [s for s in required if s not in user_skills]
    score = int(((len(required)-len(missing))/len(required))*100)

    suggestions = []
    for m in missing:
        courses = query("SELECT course_name FROM courses WHERE skill_name=?", (m,))
        suggestions += [f"{m}: {c}" for c in courses]

    return {"insights":[f"Match Score: {score}%"], "suggestions":suggestions, "actions":["View Courses"]}


def career(interest):
    roles = query("SELECT role FROM career_map WHERE interest=?", (interest,))
    return {"insights":roles, "suggestions":["Explore roles"], "actions":["View Path"]}


def internship(role):
    jobs = query("SELECT internship FROM internships WHERE role=?", (role,))
    return {"insights":jobs, "suggestions":["Apply now"], "actions":["View Jobs"]}


def resume():
    tips = query("SELECT tip FROM resume_tips")
    return {"insights":["Resume Tips"], "suggestions":tips, "actions":["Improve Resume"]}


def process(role, intent, payload):
    log(role, intent)

    if intent == "skill_gap":
        return skill_gap(payload["target_role"], payload["skills"])
    if intent == "career":
        return career(payload["interest"])
    if intent == "internship":
        return internship(payload["target_role"])
    if intent == "resume":
        return resume()

    return {"insights":["Handled"], "suggestions":["General output"], "actions":["Proceed"]}
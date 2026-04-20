from db import get_db

conn = get_db()
cur = conn.cursor()

cur.executescript("""
CREATE TABLE IF NOT EXISTS roles(name TEXT);
CREATE TABLE IF NOT EXISTS intents(name TEXT);
CREATE TABLE IF NOT EXISTS role_intents(role TEXT, intent TEXT);

CREATE TABLE IF NOT EXISTS skills(role_name TEXT, skill_name TEXT);
CREATE TABLE IF NOT EXISTS courses(skill_name TEXT, course_name TEXT);

CREATE TABLE IF NOT EXISTS career_map(interest TEXT, role TEXT);
CREATE TABLE IF NOT EXISTS internships(role TEXT, internship TEXT);
CREATE TABLE IF NOT EXISTS resume_tips(category TEXT, tip TEXT);

CREATE TABLE IF NOT EXISTS logs(role TEXT, intent TEXT, timestamp TEXT);
""")

conn.commit()
conn.close()
print("DB ready")
from db import get_db

def usage():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT role, COUNT(*) FROM logs GROUP BY role")
    return cur.fetchall()
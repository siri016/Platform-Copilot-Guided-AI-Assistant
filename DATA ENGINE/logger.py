from db import get_db
from datetime import datetime

def log(role, intent):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO logs VALUES (?,?,?)",
                (role, intent, datetime.now().isoformat()))
    conn.commit()
    conn.close()
import csv
from db import get_db

FILES = {
    "roles": "roles.csv",
    "intents": "intents.csv",
    "role_intents": "role_intents.csv",
    "skills": "skills.csv",
    "courses": "courses.csv",
    "career_map": "career_map.csv",
    "internships": "internships.csv",
    "resume_tips": "resume_tips.csv"
}

conn = get_db()
cur = conn.cursor()

for table, file in FILES.items():
    with open(f"data/{file}") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        for row in reader:
            values = [row[c] for c in cols]
            placeholders = ",".join(["?"] * len(cols))
            cur.execute(f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})", values)

conn.commit()
conn.close()
print("All data loaded")
import sqlite3
import os

def get_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "copilot.db")
    print("USING DB:", db_path)   # debug
    return sqlite3.connect(db_path)
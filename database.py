import sqlite3
import pandas as pd
import os

def setup_db():
    if not os.path.exists("assistant.db"):
        with sqlite3.connect("assistant.db") as conn:
            conn.execute('''CREATE TABLE history (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            command TEXT,
                            response TEXT,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

def log_to_db(command, response):
    with sqlite3.connect("assistant.db") as conn:
        conn.execute("INSERT INTO history (command, response) VALUES (?, ?)", (command, response))
        conn.commit()

def export_history():
    with sqlite3.connect("assistant.db") as conn:
        df = pd.read_sql_query("SELECT * FROM history", conn)
        df.to_csv("history.csv", index=False)
        return df

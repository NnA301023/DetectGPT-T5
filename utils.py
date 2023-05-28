import sqlite3
import pandas as pd
from datetime import datetime

def create_table(filename: str = "database/temp.db"):
    conn = sqlite3.connect(filename)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS LOGS 
        (
            timestamp datetime default current_timestamp, 
            text_input TEXT NOT NULL, 
            score INT NOT NULL
        );
        """
    )
    conn.close()

def read_logs(filename: str = "database/temp.db"):
    conn = sqlite3.connect(filename)
    query = "SELECT * FROM LOGS"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def logs(text: str, score: int, filename: str = "database/temp.db"):
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect(filename)
    conn.execute(
        "INSERT INTO LOGS (timestamp, text_input, score) VALUES (?, ?, ?);",
        (current_timestamp, text, score)
    )
    conn.commit()
    conn.close()
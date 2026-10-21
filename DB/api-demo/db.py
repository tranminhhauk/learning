import psycopg2
import os
from psycopg2.extras import RealDictCursor


def get_connection():
    conn = psycopg2.connect(

        host=os.getenv("DB_HOST", "localhost"),
        port=5432,
        dbname=os.getenv("DB_NAME", "test"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "tranminhhau"),
        cursor_factory=RealDictCursor
    )
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    


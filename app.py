from flask import Flask
import os
import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Alex in 3308'


@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()

@app.route("/db_create")
def db_create():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # SQL work goes here

        cur.execute("CREATE TABLE IF NOT EXISTS Basketball( \
            First varchar(255), \
            Last varchar(255), \
            City varchar(255), \
            Name varchar(255), \
            Number int \
            )")

        conn.commit()
        return "Successful database creation"
    except Exception as e:
        if conn is not None:
            conn.rollback()
        return f"Database error: {e}"
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
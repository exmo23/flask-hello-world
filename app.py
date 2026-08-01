from flask import Flask
import os
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Alex in 3308'


@app.route("/db_test")
def db_test():
    conn = None
    try:
        DATABASE_URL = os.environ.get("DATABASE_URL")
        conn = psycopg2.connect(DATABASE_URL)
    except Exception as e:
        return "database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()
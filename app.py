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

@app.route("/db_insert")
def db_insert():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # SQL work goes here

        cur.execute("INSERT INTO Basketball (First, Last, City, Name, Number) \
            VALUES \
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0), \
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30), \
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15), \
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2), \
            ('YOUR_FIRST_NAME', 'YOUR_LAST_NAME', 'CU Boulder', 'YOUR_TEAM_OR_LABEL', 3308);")

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

@app.route("/db_select")
def db_select():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # SQL work goes here

        cur.execute("SELECT * FROM Basketball")
        conn.commit()
        records = cur.fetchall()

        html = "<table border='1'>"
        html += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"

        for row in records:
            html += "<tr>"
            for value in row:
                html += f"<td>{value}</td>"
            html += "</tr>"

        html += "</table>"
        return html

    except Exception as e:
        if conn is not None:
            conn.rollback()
        return f"Database error: {e}"
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
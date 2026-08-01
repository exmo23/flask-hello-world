from flask import Flask
import psycog2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Alex in 3308'


@app.route("/db_test")
def db_test():
    conn = None
    try:
        DATABASE_URL = os.environ.get("DATABASE_URL")
        conn = psycog2.connect(DATABASE_URL)

    finally:
        if conn is not None:
            conn.close()
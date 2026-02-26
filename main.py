from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "todo.db"


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER DEFAULT 0
            )
        """)


@app.route("/")
def index():
    with sqlite3.connect(DATABASE) as conn:
        tasks = conn.execute("SELECT * FROM tasks").fetchall()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete(task_id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8000, debug=True)
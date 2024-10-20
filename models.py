import sqlite3
from config import BASE_URL

#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     description TEXT,
#     done BOOLEAN


class Task:
    def __init__(self):
        self.db = sqlite3.connect("task.db", check_same_thread=False)
        self.sql = self.db.cursor()

    def create(self, fields):
        command = f"CREATE TABLE IF NOT EXISTS tasks {fields}"

        self.sql.execute(command)
        self.db.commit()

        return True

    def all(self):
        command = "SELECT * FROM tasks"

        self.sql.execute(command)

        return self.sql.fetchall()

    def filter(self, task_id):
        command = f"SELECT * FROM tasks WHERE id == {task_id}"

        self.sql.execute(command)

        return self.sql.fetchone()

    def add(self, title, description, done):

        command = f"INSERT INTO tasks (title, description, done) VALUES ('{title}', '{description}', {bool(done)})"

        self.sql.execute(command)
        self.db.commit()
        return self.sql.lastrowid

    def update(self, task_id, title, description, done):

        command = f"UPDATE tasks SET title = '{title}', " \
                  f"description = '{description}', done = {done} WHERE id = {task_id}"

        self.sql.execute(command)
        self.db.commit()

        return self.sql.lastrowid

    def delete(self, task_id):
        command = f"""DELETE FROM tasks WHERE id == {task_id}"""

        self.sql.execute(command)
        self.db.commit()

        return True

    @staticmethod
    def get_public_url(task_id):
        return "http://localhost:5000" + BASE_URL + f"/task/{task_id}"

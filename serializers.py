from flask import jsonify
from models import Task


class TaskSerializer:
    def __init__(self):
        self.manager = Task()

    def get_tasks_list(self):
        try:
            tasks_list = []
            for task in self.manager.all():
                tasks_list.append({
                    'id': task[0],
                    'title': task[1],
                    'description': task[2],
                    'done': task[3]
                })

            return jsonify(tasks_list)
        except Exception as e:
            print(str(e))
            return jsonify([
                {
                    "error": "true"
                }
            ])

    def get_task(self, task_id):
        try:
            task = self.manager.filter(task_id)
            task_json_obj = jsonify(
                [{
                    "id": task[0],
                    "title": task[1],
                    "description": task[2],
                    "done": task[3]
                }]
            )
            return task_json_obj
        except Exception as e:
            print(str(e))
            return jsonify([
                {
                    "error": "true"
                }
            ])

    @staticmethod
    def add_task(task_parameters):
        try:
            task = Task()
            task_id = task.add(task_parameters["title"], task_parameters["description"], task_parameters["done"])

            task_parameters["public_url"] = task.get_public_url(task_id)

            return jsonify([task_parameters])
        except Exception as e:
            print(str(e))
            return jsonify([
                {
                    "error": "true"
                }
            ])

    @staticmethod
    def update_task(task_id, task_parameters):
        try:
            task = Task()
            task.update(
                task_id,
                task_parameters["title"],
                task_parameters["description"],
                task_parameters["done"]
            )

            task_parameters["public_url"] = task.get_public_url(task_id)

            return jsonify(
                [
                    task_parameters
                ]
            )
        except Exception as e:
            print(str(e))
            return jsonify([
                {
                    "error": "true"
                }
            ])

    @staticmethod
    def delete_task(task_id):
        try:
            task = Task()
            task.delete(task_id)

            return jsonify(
                [
                    {
                        "deleted": "true",
                        "error": "false",
                    }
                ]
            )
        except Exception as e:
            print(str(e))
            return jsonify([
                {
                    "error": "true"
                }
            ])

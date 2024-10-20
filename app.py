from flask import Flask, request
from config import *
from serializers import TaskSerializer

app = Flask(__name__)


@app.route(f'{BASE_URL}/tasks', methods=["GET"])
def get_tasks_list():
    serializer = TaskSerializer()
    return serializer.get_tasks_list()


@app.route(f'{BASE_URL}/task/<task_id>', methods=["GET"])
def get_task(task_id):
    serializer = TaskSerializer()
    return serializer.get_task(task_id)


@app.route(f'{BASE_URL}/task_add', methods=['POST'])
def add_task():
    serializer = TaskSerializer()
    return serializer.add_task(request.json)


@app.route(f'{BASE_URL}/task_update/<task_id>', methods=['POST'])
def update_task(task_id):
    serializer = TaskSerializer()
    return serializer.update_task(task_id, request.json)


@app.route(f'{BASE_URL}/task_delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    serializer = TaskSerializer()
    return serializer.delete_task(task_id)


if __name__ == "__main__":
    app.run(debug=DEBUG)

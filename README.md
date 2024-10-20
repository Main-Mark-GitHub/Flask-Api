# Task Management API

This is a simple Flask-based API for managing tasks. It provides endpoints to create, read, update, and delete tasks. The API is designed to be easy to use and integrate with other applications.

## Requirements

- Python 3.x
- Flask
- Any other dependencies specified in `config.py` and `serializers.py`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your configuration in `config.py`. Make sure to define `BASE_URL` and `DEBUG` variables.

## API Endpoints

### 1. Get List of Tasks

- **URL:** `/tasks`
- **Method:** `GET`
- **Description:** Retrieves a list of all tasks.
- **Response:** JSON array of tasks.

### 2. Get a Specific Task

- **URL:** `/task/<task_id>`
- **Method:** `GET`
- **Description:** Retrieves a specific task by its ID.
- **Response:** JSON object of the task.

### 3. Add a New Task

- **URL:** `/task_add`
- **Method:** `POST`
- **Description:** Adds a new task.
- **Request Body:** JSON object containing task details.
- **Response:** JSON object of the created task.

### 4. Update an Existing Task

- **URL:** `/task_update/<task_id>`
- **Method:** `POST`
- **Description:** Updates an existing task by its ID.
- **Request Body:** JSON object containing updated task details.
- **Response:** JSON object of the updated task.

### 5. Delete a Task

- **URL:** `/task_delete/<task_id>`
- **Method:** `POST`
- **Description:** Deletes a task by its ID.
- **Response:** JSON object confirming deletion.

## Running the Application

To run the application, execute the following command:

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000` by default. You can change the host and port in the `app.run()` method if needed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.


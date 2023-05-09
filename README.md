# Microservice: Task Management API

This repository contains a Flask-based microservice for managing tasks. The API allows users to request and update task details.

## Getting Started

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/juj-star/M5.git 
cd M5
pip install flask requests flask_pymongo pymongo
```

Run the Flask application:

```bash
python api.py
```

The microservice will be available at http://127.0.0.1:5001/.

## Requesting Data

To request data from the microservice, you can use a GET request to the /edit-task2/{task_id} endpoint. Replace {task_id} with the actual task ID you want to request. You can use tools like curl, Postman (https://www.postman.com/), or create a Python script using the requests library.

Example request using curl:

```bash
curl -X GET http://127.0.0.1:5001/edit-task2/your_task_id_here
```

## Receiving Data

The response from the GET request will be a JSON object containing the task details.

Sample response:

```json
{
    "_id": "your_task_id_here",
    "task_title": "Task Title",
    "task_description": "Task Description",
    "assignee": "assignee@example.com",
    "due_date": "2023-05-30",
    "assigned_by": "assigned_by@example.com"
}
```

## Updating Data

To update a task, send a PUT request to the /edit-task2/{task_id} endpoint with the updated data in JSON format as the request body. Replace {task_id} with the actual task ID you want to update.

Example request using curl:

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"task_title":"Updated Task Title", "task_description":"Updated Task Description", "assignee":"updated.assignee@example.com", "due_date":"2023-06-01", "assigned_by":"updated.assigned_by@example.com"}' http://127.0.0.1:5001/edit-task2/your_task_id_here
```

Receiving Updated Data

The response from the PUT request will be a JSON object containing the updated task details.

Sample response:

```json
{
    "_id": "your_task_id_here",
    "task_title": "Updated Task Title",
    "task_description": "Updated Task Description",
    "assignee": "updated.assignee@example.com",
    "due_date": "2023-06-01",
    "assigned_by": "updated.assigned_by@example.com"
}
```

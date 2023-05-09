import requests
import json

# Replace with the task_id of the task you want to request and update
task_id = '644731e3d7cd47e231a27521'

# Request the task
api_url = f'http://127.0.0.1:5001/edit-task2/{task_id}'
response = requests.get(api_url)

if response.status_code == 200:
    task = response.json()
    print("Current Task Details:")
    print(json.dumps(task, indent=4))

    # Update the task
    updated_data = {
        "task_title": "Updated Task Title",
        "task_description": "Updated Task Description",
        "assignee": "updated.assignee@example.com",
        "due_date": "2023-06-01",
        "assigned_by": "updated.assigned_by@example.com",
    }

    response = requests.put(api_url, json=updated_data)

    if response.status_code == 200:
        print("Task updated successfully.")
        updated_task = response.json()
        print("Updated Task Details:")
        print(json.dumps(updated_task, indent=4))
    else:
        print("Error updating task.")
else:
    print("Error retrieving task.")

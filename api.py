from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://juj:<PW>@cluster0.beidr0t.mongodb.net/stuff?retryWrites=true&w=majority"
mongo = PyMongo(app)
db = mongo.db

@app.route('/edit-task2/<task_id>', methods=['GET', 'PUT'])
def edit_task2(task_id):
    if request.method == 'GET':
        task = db.tasks.find_one({"_id": ObjectId(task_id)})
        if task:
            task_data = {
                "_id": str(task["_id"]),
                "task_title": task["task_title"],
                "task_description": task["task_description"],
                "assignee": task["assignee"],
                "due_date": task["due_date"],
                "assigned_by": task["assigned_by"],
            }
            return jsonify(task_data), 200
        else:
            return jsonify({"error": "Task not found"}), 404

    elif request.method == 'PUT':
        data = request.json
        update_result = db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {
                "task_title": data["task_title"],
                "task_description": data["task_description"],
                "assignee": data["assignee"],
                "due_date": data["due_date"],
                "assigned_by": data["assigned_by"],
            }}
        )
        if update_result.modified_count == 1:
            return jsonify({"result": "Task updated successfully"}), 200
        else:
            return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)

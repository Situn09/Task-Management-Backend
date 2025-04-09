from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Task, db
from app.utils import validate_fields

tasks_bp = Blueprint("tasks", __name__)

# Create Task
@tasks_bp.route("/", methods=["POST"])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()

    is_valid, error = validate_fields(data, ["title"])
    if not is_valid:
        return jsonify({"msg": error}), 400

    title = data.get("title")
    description = data.get("description")
    status = data.get("status", "pending")

    if not title:
        return jsonify({"msg": "Title is required"}), 400

    task = Task(title=title, description=description, status=status, user_id=user_id)
    db.session.add(task)
    db.session.commit()

    return jsonify({"msg": "Task created", "task": task_to_dict(task)}), 201


# Get All Tasks
@tasks_bp.route("/", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task_to_dict(t) for t in tasks]), 200


# Update Task
@tasks_bp.route("/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({"msg": "Task not found"}), 404

    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)

    db.session.commit()
    return jsonify({"msg": "Task updated", "task": task_to_dict(task)}), 200


# Delete Task
@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({"msg": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"}), 200


# Utility: Convert task to dict
def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "user_id": task.user_id
    }

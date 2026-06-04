from datetime import datetime
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

tasks = []


def add_task(title, description, due_date):
    task = {
        "id": len(tasks) + 1,
        "title": validate_task_title(title),
        "description": validate_task_description(description),
        "due_date": validate_due_date(due_date),
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    return task


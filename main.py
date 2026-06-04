from datetime import datetime

# Simple in-memory task list for the application.
tasks = []

def validate_task_title(title):
    if not isinstance(title, str):
        raise TypeError("Title must be a string.")

    title = title.strip()
    if len(title) == 0:
        raise ValueError("Title cannot be empty.")
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long.")

    return title

def validate_task_description(description):
    if not isinstance(description, str):
        raise TypeError("Description must be a string.")

    description = description.strip()
    if len(description) == 0:
        raise ValueError("Description cannot be empty.")
    if len(description) < 5:
        raise ValueError("Description must be at least 5 characters long.")

    return description

def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise TypeError("Due date must be a string.")

    due_date = due_date.strip()
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty.")

    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Due date must be in the format YYYY-MM-DD.")

    if parsed_date <= datetime.now().date():
        raise ValueError("Due date must be a future date.")

    return due_date

def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    return task



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


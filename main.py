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



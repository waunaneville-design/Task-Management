from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title must be a non-empty string.")

    title = title.strip()
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long.")

    return title


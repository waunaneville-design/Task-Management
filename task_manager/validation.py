from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Title must be a non-empty string.")

    title = title.strip()
    if len(title) == 0:
        raise ValueError("Title must be a non-empty string.")
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long.")

    return title

def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Description must be a non-empty string.")

    description = description.strip()
    if len(description) == 0:
        raise ValueError("Description must be a non-empty string.")
    if len(description) < 5:
        raise ValueError("Description must be at least 5 characters long.")

    return description


def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a non-empty string.")

    due_date = due_date.strip()
    if len(due_date) == 0:
        raise ValueError("Due date must be a non-empty string.")

    try:
        datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Due date must use YYYY-MM-DD format.")

    return due_date


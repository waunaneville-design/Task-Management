from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title must be a non-empty string.")

    title = title.strip()
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long.")

    return title

def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Description must be a non-empty string.")

    description = description.strip()
    if len(description) < 5:
        raise ValueError("Description must be at least 5 characters long.")

    return description


def validate_due_date(due_date):
    if not isinstance(due_date, str) or not due_date.strip():
        raise ValueError("Due date must be a non-empty string.")

    due_date = due_date.strip()
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Due date must use YYYY-MM-DD format.")

    if parsed_date <= datetime.now().date():
        raise ValueError("Due date must be in the future.")

    return due_date


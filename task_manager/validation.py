from datetime import datetime

def validate_task_title(title):
    """
    Validate the task title.
    Title must be a non-empty string with at least 3 characters.
    """
    if not isinstance(title, str):
        raise TypeError("Title must be a string.")
    
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    
    if len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    
    return title.strip()


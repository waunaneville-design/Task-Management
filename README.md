# Task Management System

A Python-based task management application that allows users to manage tasks, track progress, and maintain productivity.

## Project Structure

```
Task1/
├── main.py                          # Main menu-based interface
├── test_system.py                   # Test script demonstrating functionality
└── task_manager/                    # Package directory
    ├── __init__.py                  # Package initialization
    ├── task_utils.py                # Task management functions
    └── validation.py                # Input validation functions
```

## Features

### Core Functionality

1. **Add Tasks** - Create new tasks with title, description, and due date
2. **Mark Tasks Complete** - Mark tasks as completed by task ID
3. **View Pending Tasks** - Display all incomplete tasks
4. **View All Tasks** - Display both completed and pending tasks
5. **Track Progress** - View completion statistics and percentage

### Input Validation

The system includes comprehensive validation for all user inputs:
- **Task Title**: Must be at least 3 characters long and non-empty
- **Description**: Must be at least 5 characters long and non-empty
- **Due Date**: Must be in YYYY-MM-DD format and be a future date

## Task Dictionary Structure

Each task is stored as a dictionary with the following structure:

```python
{
    "id": int,                      # Unique task identifier
    "title": str,                   # Task title (3+ chars)
    "description": str,             # Task description (5+ chars)
    "due_date": str,               # Due date in YYYY-MM-DD format
    "completed": bool,             # Completion status
    "created_at": str              # Timestamp of creation
}
```

## Module Documentation

### task_manager/validation.py

Contains input validation functions:

- **`validate_task_title(title)`** - Validates task title
  - Returns: Trimmed title string
  - Raises: TypeError or ValueError if invalid

- **`validate_task_description(description)`** - Validates task description
  - Returns: Trimmed description string
  - Raises: TypeError or ValueError if invalid

- **`validate_due_date(due_date)`** - Validates due date
  - Returns: Date string in YYYY-MM-DD format
  - Raises: TypeError or ValueError if invalid

### task_manager/task_utils.py

Contains task management functions:

- **`add_task(title, description, due_date)`** - Adds a new task
  - Parameters: Title, description, and due date strings
  - Returns: Task dictionary
  - Raises: Exception if validation fails

- **`mark_task_as_complete(task_id)`** - Marks a task as complete
  - Parameters: Task ID (integer or string)
  - Returns: Tuple (success: bool, message: str)

- **`view_pending_tasks()`** - Returns all pending tasks
  - Returns: List of incomplete task dictionaries

- **`view_all_tasks()`** - Returns all tasks
  - Returns: List of all task dictionaries

- **`calculate_progress()`** - Calculates task statistics
  - Returns: Dictionary with:
    - `total_tasks`: Total number of tasks
    - `completed_tasks`: Number of completed tasks
    - `pending_tasks`: Number of pending tasks
    - `completion_percentage`: Percentage of completed tasks

## Running the Application

### Interactive Mode

To run the interactive menu-based interface:

```bash
python main.py
```

This will launch an interactive menu where you can:
1. Add new tasks
2. Mark tasks as complete
3. View pending tasks
4. View all tasks
5. Check progress statistics
6. Exit the program

### Test Mode

To run the automated test suite:

```bash
python test_system.py
```

This demonstrates all functionality including:
- Adding multiple tasks
- Viewing tasks
- Marking tasks as complete
- Calculating progress
- Testing validation with invalid inputs

## Example Usage

### Adding a Task

```
Title: Complete Python Project
Description: Finish implementing the task management system
Due Date: 2026-12-31
```

### Viewing Progress

```
Total Tasks: 5
Completed Tasks: 2
Pending Tasks: 3
Completion Percentage: 40.0%
```

## Error Handling

The system provides user-friendly error messages for:
- Invalid task titles (too short)
- Invalid descriptions (too short)
- Invalid date formats
- Past due dates
- Non-existent task IDs

## Technical Implementation

- **Language**: Python 3
- **Date/Time**: Uses Python's `datetime` module
- **Data Storage**: In-memory list of task dictionaries
- **Validation**: Built-in validation functions with custom error messages
- **Code Organization**: Modular structure with separate packages for validation and task management

## Key Design Decisions

1. **Task ID Auto-Increment**: Task IDs are automatically assigned based on the number of existing tasks
2. **Timestamp Recording**: Tasks record their creation timestamp automatically
3. **Future Date Validation**: Due dates must be in the future to prevent scheduling past tasks
4. **String Normalization**: All text inputs are trimmed to remove leading/trailing whitespace
5. **In-Memory Storage**: Tasks are stored in a global list (no file persistence)

## Future Enhancements

Possible improvements for future versions:
- File persistence (save/load tasks from disk)
- Task categories or tags
- Priority levels
- Recurring tasks
- Due date reminders
- Task filtering and sorting
- Data export functionality (CSV, JSON)
- User authentication and multi-user support

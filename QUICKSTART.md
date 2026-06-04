# Quick Start Guide - Task Management System

## How to Run

### Interactive Menu (Recommended)
```bash
python main.py
```

### Automated Tests
```bash
python test_system.py
```

## File Structure

```
Task1/
├── main.py                    # Run this to use the system
├── test_system.py            # Run this to test the system
├── README.md                 # Full documentation
├── IMPLEMENTATION.md         # Implementation details
└── task_manager/             # Package folder
    ├── __init__.py          # Makes it a package
    ├── validation.py        # Validation functions
    └── task_utils.py        # Task management functions
```

## Menu Options Explained

### 1. Add Task
- Enter task title (minimum 3 characters)
- Enter description (minimum 5 characters)
- Enter due date (YYYY-MM-DD format, must be future)
- Example: 2026-12-31

### 2. Mark Task as Complete
- View pending tasks
- Enter task ID
- Task marked as complete

### 3. View Pending Tasks
- Shows all incomplete tasks
- Displays: ID, Title, Description, Due Date, Created Date

### 4. View All Tasks
- Shows both completed and pending tasks
- Status indicator: ✓ Completed or ○ Pending

### 5. View Progress
- Total tasks count
- Completed tasks count
- Pending tasks count
- Completion percentage

### 6. Exit
- Closes the program

## Example Session

```
Task Management System
==================================================
1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. View All Tasks
5. View Progress
6. Exit
==================================================
Enter your choice (1-6): 1

--- Add New Task ---
Enter task title: Complete Project
Enter task description: Finish the Python implementation
Enter due date (YYYY-MM-DD): 2026-12-31

✓ Task added successfully!
  Task ID: 1
  Title: Complete Project
  Description: Finish the Python implementation
  Due Date: 2026-12-31
```

## Function Reference

### Adding Tasks
```python
from task_manager import add_task

task = add_task("Learn Python", "Study Python fundamentals", "2026-06-30")
```

### Viewing Tasks
```python
from task_manager import view_pending_tasks, view_all_tasks

pending = view_pending_tasks()  # Get incomplete tasks
all_tasks = view_all_tasks()    # Get all tasks
```

### Marking Complete
```python
from task_manager import mark_task_as_complete

success, message = mark_task_as_complete(1)  # Mark task ID 1 as complete
```

### Progress Tracking
```python
from task_manager import calculate_progress

progress = calculate_progress()
print(f"Completed: {progress['completed_tasks']}/{progress['total_tasks']}")
```

## Input Requirements

### Task Title
- Minimum 3 characters
- Cannot be empty
- Will be trimmed of whitespace

### Task Description
- Minimum 5 characters
- Cannot be empty
- Will be trimmed of whitespace

### Due Date
- Format: YYYY-MM-DD
- Must be a future date
- Examples: 2026-06-30, 2027-01-15, 2026-12-25

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Title must be at least 3 characters long." | Title too short | Enter at least 3 characters |
| "Description must be at least 5 characters long." | Description too short | Enter at least 5 characters |
| "Due date must be in the format YYYY-MM-DD." | Wrong date format | Use YYYY-MM-DD format |
| "Due date must be a future date." | Past date | Enter a date in the future |
| "Task with ID X not found." | Invalid task ID | Check available tasks and use correct ID |

## Tips & Tricks

1. **View Pending Tasks First** - Before marking complete, view pending tasks to see available IDs
2. **Check Progress Often** - Monitor your completion percentage as you work
3. **Use Clear Titles** - Make task titles descriptive for easy identification
4. **Plan Ahead** - Set reasonable due dates for your tasks
5. **Mark Complete** - Mark tasks as done to track progress accurately

## Technical Details

- **Language**: Python 3.14+
- **No External Dependencies**: Uses only Python standard library
- **Data Storage**: In-memory (no file persistence)
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Support

For detailed documentation, see:
- `README.md` - Full user guide
- `IMPLEMENTATION.md` - Technical details
- `test_system.py` - Code examples

## Next Steps

1. Run `python main.py` to start using the system
2. Try all menu options
3. Add several tasks and practice
4. Run `python test_system.py` to see the system in action
5. Review the code in `task_manager/` to understand the implementation

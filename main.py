from task_manager import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    view_all_tasks,
    calculate_progress
)

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("Task Management System")
    print("="*50)
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View All Tasks")
    print("5. View Progress")
    print("6. Exit")
    print("="*50)


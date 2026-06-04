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

def mark_task_as_complete(task_id):
    try:
        task_id = int(task_id)
    except (TypeError, ValueError):
        return False, "Task ID must be a number."

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                return False, f"Task '{task['title']}' is already completed."
            task["completed"] = True
            return True, f"Task '{task['title']}' has been marked as complete."

    return False, f"Task with ID {task_id} not found."

def view_pending_tasks():
    return [task for task in tasks if not task["completed"]]


def view_all_tasks():
    return list(tasks)


def calculate_progress():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    completion_percentage = round((completed_tasks / total_tasks * 100), 2) if total_tasks else 0.0

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_percentage": completion_percentage,
    }

def prompt_input(prompt_text):
    return input(prompt_text).strip()

def print_task(task, show_status=False):
    status = "✓ Completed" if task["completed"] else "○ Pending"
    print(f"ID: {task['id']}")
    print(f"Title: {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Created At: {task['created_at']}")
    if show_status:
        print(f"Status: {status}")
    print("--------------------------------------------------")


def display_menu():
    print("\nTask Management System")
    print("==================================================")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View All Tasks")
    print("5. View Progress")
    print("6. Exit")
    print("==================================================")

def main():
    while True:
        display_menu()
        choice = prompt_input("Enter your choice (1-6): ")

        if choice == "1":
            print("\n--- Add New Task ---")
            title = prompt_input("Enter task title: ")
            description = prompt_input("Enter task description: ")
            due_date = prompt_input("Enter due date (YYYY-MM-DD): ")

            try:
                task = add_task(title, description, due_date)
                print("\n✓ Task added successfully!")
                print_task(task, show_status=True)
            except Exception as error:
                print(f"✗ Error: {error}")

        elif choice == "2":
            print("\n--- Mark Task as Complete ---")
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks available.")
                continue




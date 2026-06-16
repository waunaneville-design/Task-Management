from task_manager import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    view_all_tasks,
    calculate_progress,
)


def prompt_input(prompt_text):
    try:
        return input(prompt_text).strip()
    except EOFError:
        return None


def print_task(task, show_status=False):
    status = "Completed" if task["completed"] else "Pending"
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
        if choice is None:
            break

        if choice == "1":
            print("\n--- Add New Task ---")
            title = prompt_input("Enter task title: ")
            if title is None:
                break
            description = prompt_input("Enter task description: ")
            if description is None:
                break
            due_date = prompt_input("Enter due date (YYYY-MM-DD): ")
            if due_date is None:
                break

            try:
                task = add_task(title, description, due_date)
                print("\nTask added successfully!")
                print_task(task, show_status=True)
            except Exception as error:
                print(f"Error: {error}")

        elif choice == "2":
            print("\n--- Mark Task as Complete ---")
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks available.")
                continue

            for task in pending:
                print(f"ID: {task['id']} - {task['title']} (Due: {task['due_date']})")

            task_id = prompt_input("Enter the task ID to mark as complete: ")
            if task_id is None:
                break
            success, message = mark_task_as_complete(task_id)
            if success:
                print("Task marked as complete!")
            else:
                print(message)

        elif choice == "3":
            print("\n--- Pending Tasks ---")
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks found.")
                continue

            for task in pending:
                print_task(task)

        elif choice == "4":
            print("\n--- All Tasks ---")
            all_tasks = view_all_tasks()
            if not all_tasks:
                print("No tasks have been added yet.")
                continue

            for task in all_tasks:
                print_task(task, show_status=True)

        elif choice == "5":
            print("\n--- Progress Summary ---")
            progress = calculate_progress()
            print(f"Total Tasks: {progress['total_tasks']}")
            print(f"Completed Tasks: {progress['completed_tasks']}")
            print(f"Pending Tasks: {progress['pending_tasks']}")
            print(f"Completion Percentage: {progress['completion_percentage']}%")

        elif choice == "6":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



# Import validation functions
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


# Define tasks list
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    # Validate the title
    valid, message = validate_task_title(title)

    if not valid:
        print(message)
        return

    # Validate the description
    valid, message = validate_task_description(description)

    if not valid:
        print(message)
        return

    # Validate the due date
    valid, message = validate_due_date(due_date)

    if not valid:
        print(message)
        return

    # Create the task dictionary
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }

    # Add the task to the tasks list
    tasks.append(task)

    print("Task added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if len(tasks) == 0:
        print("There are no tasks to complete.")
        return

    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index - 1]

    if task["completed"]:
        print("Task is already completed.")
        return

    task["completed"] = True

    print("Task marked as complete!")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("There are no pending tasks.")
        return

    print("\nPending Tasks:")

    for index, task in enumerate(pending_tasks, start=1):
        print(f"\nTask {index}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed_tasks = 0

        for task in tasks:
            if task["completed"]:
                completed_tasks += 1

        progress = (completed_tasks / len(tasks)) * 100

    print(f"Task progress: {progress:.2f}%")

    return progress
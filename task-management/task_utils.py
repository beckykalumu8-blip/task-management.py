
from datetime import datetime

from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if not tasks:
        print("There are no tasks.")
        return

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    if tasks[index]["completed"]:
        print("Task is already marked as complete.")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending_tasks = [
        task for task in tasks
        if not task["completed"]
    ]

    if not pending_tasks:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")

    for index, task in enumerate(pending_tasks, start=1):
        print(f"{index}. {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print()


def calculate_progress(tasks=tasks):
    if not tasks:
        progress = 0
    else:
        completed_tasks = sum(
            1 for task in tasks
            if task["completed"]
        )

        progress = (completed_tasks / len(tasks)) * 100

    return progress


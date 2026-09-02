
from datetime import datetime


def validate_task_title(title):
    """Validate the task title."""
    if not title or not title.strip():
        print("Error: Task title cannot be empty.")
        return False

    if len(title.strip()) > 100:
        print("Error: Task title cannot exceed 100 characters.")
        return False

    return True


def validate_task_description(description):
    """Validate the task description."""
    if not description or not description.strip():
        print("Error: Task description cannot be empty.")
        return False

    if len(description.strip()) > 500:
        print("Error: Task description cannot exceed 500 characters.")
        return False

    return True


def validate_due_date(due_date):
    """Validate the due date format."""
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
        return False


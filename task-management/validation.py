from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        return False, "Title must be a string."

    if title.strip() == "":
        return False, "Title cannot be empty."

    if len(title.strip()) < 3:
        return False, "Title must be at least 3 characters long."

    return True, "Valid title."


def validate_task_description(description):
    if not isinstance(description, str):
        return False, "Description must be a string."

    if description.strip() == "":
        return False, "Description cannot be empty."

    return True, "Valid description."


def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False, "Due date must be a string."

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, "Valid due date."

    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format."
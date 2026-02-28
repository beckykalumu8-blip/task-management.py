from student_data import students


def format_student_data(student: tuple) -> str:
    """Format student data as a string."""
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"


def display_students():
    """Display all students in a formatted manner."""
    for student in students:
        print(format_student_data(student))
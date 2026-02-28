from student_data import students


def filter_students_by_major(major: str):
    """Filter students by major using list comprehension."""
    return [student for student in students if student[2] == major]
from student_data import students


def student_generator(major: str = None):
    """Return a generator expression for students by major."""
    return (student for student in students if major is None or student[2] == major)
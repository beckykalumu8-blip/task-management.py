from student_data import students


def unique_majors(student_list: list) -> set:
    """Return unique majors using set comprehension."""
    return {student[2] for student in student_list}
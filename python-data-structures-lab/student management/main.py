from student_data import students
from filter import filter_students_by_major
from data_processing import format_student_data, display_students
from set_operations import unique_majors
from data_generator import student_generator


def main():
    print("=" * 50)
    print("ALL STUDENTS")
    print("=" * 50)
    display_students()

    print("\n" + "=" * 50)
    print("FILTERED BY MAJOR: Computer Science")
    print("=" * 50)
    cs_students = filter_students_by_major("Computer Science")
    for student in cs_students:
        print(format_student_data(student))

    print("\n" + "=" * 50)
    print("UNIQUE MAJORS")
    print("=" * 50)
    print(unique_majors(students))

    print("\n" + "=" * 50)
    print("GENERATOR (Physics Students)")
    print("=" * 50)
    physics_gen = student_generator("Physics")
    for student in physics_gen:
        print(format_student_data(student))


if __name__ == "__main__":
    main()
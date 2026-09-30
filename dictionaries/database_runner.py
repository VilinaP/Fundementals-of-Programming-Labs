from student_database import add_student, create_student, display_all_students, display_student, find_student_by_id, get_math_majors


def student_manager() -> None:
    """
    Interactive console-based system for managing student data.
    
    Allows users to:
        - Add new students
        - Look up students by ID
        - List all Math majors
        - Display all student entries
        - Exit the program
    """
    db: dict[str, dict[str, str | int | float]] = {}

    while True:
        print("\nOptions: add, find, list_math, show_all, quit")
        command = input("Enter command: ").strip()

        if command == "add":
            sid = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            major = input("Major: ")
            gpa = float(input("GPA: "))
            student = create_student(name, age, major, gpa)
            add_student(db, sid, student)

        elif command == "find":
            sid = input("Enter Student ID: ")
            student = find_student_by_id(db, sid)
            if student:
                display_student(student)
            else:
                print("Student not found.")

        elif command == "list_math":
            math_majors = get_math_majors(db)
            print("Math Majors:", math_majors)

        elif command == "show_all":
            display_all_students(db)

        elif command == "quit":
            break

        else:
            print("Invalid command.")

student_manager()
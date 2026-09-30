def create_student(name: str, age: int, major: str, gpa: float) -> dict[str, str | int | float]:
    """
    Create a new student dictionary with provided attributes.
    Parameters:
        name (str): Student's full name.
        age (int): Student's age in years.
        major (str): Student's major field of study.
        gpa (float): Student's GPA (Grade Point Average).
    Returns:
        dict: A dictionary representing the student.
    """
    student = {
        'name' : name,
        'major' : major,
        'age' : age,
        'gpa' : gpa,
    }
    return student


def update_gpa(student: dict[str, str | int | float], new_gpa: float) -> None:
    """
    Updates the GPA of the given student in-place.
    Parameters:
        student (dict): A dictionary representing a student.
        new_gpa (float): The new GPA to assign.
    Returns:
        None
    """
    student['gpa'] = new_gpa
    return None


def display_student(student: dict[str, str | int | float]) -> None:
    """
    Prints all key-value pairs from the student dictionary in a readable format.
    Parameters:
        student (dict): A dictionary representing a student.
    Returns:
        None
    """
    print(f" name = {student['name']} \n age = {student['age']} \n major = {student['major']} \n gpa = {student['gpa']}")
    return None


def add_student(db: dict[str, dict[str, str | int | float]], student_id: str, student: dict[str, str | int | float]) -> None:
    """
    Adds a new student entry to the database under the given student ID.
    Parameters:
        db (dict): The student database (student_id -> student info).
        student_id (str): Unique identifier for the student.
        student (dict): Dictionary containing student info.
    Returns:
        None
    """

    db.update({student_id:student})

    return None


def find_student_by_id(db: dict[str, dict[str, str | int | float]], student_id: str) -> dict[str, str | int | float] | None:
    """
    Searches for a student in the database using their ID.
    Parameters:
        db (dict): The student database.
        student_id (str): The ID to look up.
    Returns:
        dict or None: The student dictionary if found, otherwise None.
    """
    if student_id in db :
        return db[student_id]
    else:
        return None


def get_math_majors(db: dict[str, dict[str, str | int | float]]) -> list[str]:
    """
    Returns a list of names of all students who are majoring in Mathematics.
    Parameters:
        db (dict): The student database.
    Returns:
        list[str]: List of names of math majors.
    """
    list = []
    for key in db:
        if db[key]['major'] == 'Mathematics':
            list.append(db[key]['name'])
    return list


def display_all_students(db: dict[str, dict[str, str | int | float]]) -> None:
    """
    Prints a list of all student IDs and their names in the database.
    Parameters:
        db (dict): The student database.
    Returns:
        None
    """
    for key in db:
        print(key, db[key]['name'])
    return None

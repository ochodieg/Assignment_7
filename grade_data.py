
def get_first_name() -> str:
    """Prompts user for students first name"""
    first_name = input("What is the students first name? ")
    return first_name

# print(get_first_name())

def get_last_name() -> str:
    """Prompts user for students last name"""
    last_name = input("What is the students last name? ")
    return last_name
# print(get_last_name())


def get_grade(students_first_name: str) -> float:
    """Accepts and validates user input for student grade"""
    validated = True

    while validated:

        students_grade = input("Enter the grade for " + students_first_name + " ")
        students_grade_as_float = float(students_grade)

        if students_grade_as_float < 0 or students_grade_as_float > 100:

            print("The entered grade is not valid."
                " The grade must be between 0 and 100.")
        else:
            # print("good grade")
            # another_grade(input("do u want to enter another grade? (y or n)"))
            validated = False

    return students_grade_as_float

# print(get_grade("john"))


def get_letter_grade(grade: float) -> str:
    """Returns a letter grade from float grade"""
    if 90.0 <= grade <= 100.0:
        grade = "A"

    elif 80.0 <= grade <= 89.9:
        grade = "B"

    elif 70.0 <= grade <= 79.9:
        grade = "C"

    elif 60.0 <= grade <= 69.9:
        grade = "D"

    elif 0.0 <= grade <= 60.0:
        grade = "F"

    elif grade > 100.0 or grade < 0:
        grade = "Error. Grade is out of range."

    return grade
# print(get_letter_grade(100.1))


def get_continue_choice() -> bool:
    """Asks user if they would like to enter another grade."""
    validated = True

    while validated:
        question = input("\n" + "Would you like to enter another grade? (y or n).\n")

        if question == "y" or question == "Y":
            choice = True
            validated = False

        elif question == "n" or question == "N":
            choice = False
            validated = False

        else:
            print("I did not understand your choice. Please enter a y or n")

    return choice

# print(get_continue_choice())


def format_output_row(student_number: int, first_name: str, last_name: str, grade: float) -> str:
    """Returns formatted string with student info"""
    letter_grade = get_letter_grade(grade)
    grade_as_string = str(grade)
    student_as_string = str(student_number)

    #validated = True

    return "\t" + student_as_string\
           + format(first_name, "^23")\
           + format(last_name, "^11")\
           + format(grade_as_string, "^16")\
           + "\t" + format(letter_grade, "^10")

# students_first_name = get_first_name()
# print(format_output_row(1, students_first_name, get_last_name(), get_grade(students_first_name)))


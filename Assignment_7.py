import grade_data

# REMEMBER, DONT USE GLOBAL VARIABLES!!!! KEEP ALL WHILE-LOOP VARIABLES WITHIN ONLY THE WHILE LOOP UNLESS THEY ARE INITIALIZING!!!

# formatted_result = grade_data.format_output_row(1, first_name, last_name, student_grade)
# print(formatted_result)


# -------------------------------------------------------------------------------------------


validated = True
count = 1
grade = 0
formatted_result = ""

while validated:

    first_name = grade_data.get_first_name()
    last_name = grade_data.get_last_name()
    student_grade = grade_data.get_grade(first_name)

    formatted_result += grade_data.format_output_row(count, first_name, last_name, student_grade) + "\n"
    # choice = grade_data.get_continue_choice()
    validated = grade_data.get_continue_choice()
    count += 1
    grade += student_grade

    # if choice == True:
    #     formatted_result = grade_data.format_output_row(count, first_name, last_name, student_grade) +\
    #     "\n" + grade_data.format_output_row(count, first_name, last_name, student_grade)
    # else:
print("\nStudent#\tFirst name\t\tLast name\t\tGrade%\t\tLetter grade\n"\
    + "------------------------------------------------------------------------\n"\
    + formatted_result)


# --------------------------------------------------------------------------------------

    # # print(formatted_result)
    # if choice == False:
    #     validated = False
    # elif choice == True:
    #     count += 1
    #     formatted_result_final = formatted_result + "\n" + formatted_result
    # validated = choice

# for number in (count):
#     print(grade_data.format_output_row(count, first_name, last_name, student_grade))

# choice = grade_data.get_continue_choice

# validated = False
#
# while grade_data.get_continue_choice == True:
#     choice = grade_data.get_continue_choice
#
#     while choice:
#         count += 1
#         formatted_result = ""
#         formatted_result = formatted_result + grade_data.format_output_row(count, first_name, last_name, student_grade)
#
#         print(formatted_result)
#         choice = grade_data.get_continue_choice
#
#     else:
#         # grade_data.get_continue_choice() == False
#         validated == False
#         print(formatted_result)

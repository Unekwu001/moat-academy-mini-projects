from student_modules import check_result as student_chek
from admin_modules import check_result as admin_chek

user_type = input("Admin or student ? : ")
user_type = user_type.lower()

if user_type == "admin":
    admin_chek()
elif user_type == "student":
    provided_name = input("Provide your name: ")
    provided_name = provided_name.capitalize()

    student_chek(provided_name)
else:
    print("You have entered a wrong input")





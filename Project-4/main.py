# Kayla Jones
# Project 4

# sets the class list dictionary and the
# student schedule as a global variable so that
# all classes can access it
class_list = {}
class_roster = {}


# creates a new class from admin mode
def create_class(class_name, max_size):
    if class_name not in class_list:
        class_list[class_name] = max_size
        print("Class created successfully.")
    else:
        print("Class already exists.")

    return class_list


# deletes a class from admin mode
def delete_class(class_name):
    if class_name in class_list:
        print(class_name + " has been deleted.")
        class_list.pop(class_name)
    else:
        print("That class does not exist.")


# updates a class and its associated max size
# from admin mode
def update_class(class_name):
    if class_name in class_list:
        updated_class_name = input("What would you like to update " + class_name + " to?\n")
        class_list[updated_class_name] = class_list[class_name]
        del class_list[class_name]
        print("Class updated. Refer to the class roster for updates.")
    else:
        print("That class does not exist.")


# prints out the class roster from admin mode
def print_roster():
    for course_name, max_size in class_list.items():
        print(course_name + ": " + str(max_size))


# enrolls student in the class as long as
# there are enough open seats and then class exists
def enroll_student(class_name, student_name):
    if class_name in class_list:
        max_size = class_list[class_name]
        if len(class_roster.get(class_name, [])) < max_size:
            class_roster.setdefault(class_name, []).append(student_name)
            print("Enrollment successful.")
        else:
            print("Class is full, enrollment failed.")
    else:
        print("Class not found.")


# prints student class roster
def print_schedule(student_name):
    enrolled_classes = []
    for class_name, roster in class_roster.items():
        if student_name in roster:
            enrolled_classes.append(class_name)
    if enrolled_classes:
        print("Your enrolled classes:")
        for class_name in enrolled_classes:
            print(class_name)
    else:
        print("You are not enrolled in any classes.")


# un-enrolls student from class as long
# as they are enrolled in the class
def unenroll_student(class_name, student_name):
    if class_name in class_list:
        if student_name in class_roster[class_name]:
            class_roster[class_name].remove(student_name)
            print("Unenrollment successful.")
        else:
            print("Student is not enrolled in the class.")
    else:
        print("Class not found.")


# allows the user to switch between student and
# admin mode to delete/update/display classes and
# enroll/un-enroll/display class schedule
def main():
    mode_selection = int(input("Please select a mode, or select 'exit':\n"
                               "1 - Admin\n2 - Student\n3 - Exit\n"))

    while mode_selection != 3:
        if mode_selection == 1:
            print("You have selected admin mode. What would you like to do?")
            admin_mode_selection = int(input("1 - Create a class\n2 - Delete a class\n3 - Print class roster\n"
                                             "4 - Update a class\n"))

            if admin_mode_selection == 1:
                class_name = input("Class name: ")
                max_size = int(input("Max size for " + class_name + " (whole numbers only, please): "))
                create_class(class_name, max_size)
            elif admin_mode_selection == 2:
                print_roster()
                class_name = input("Which class would you like to delete?")
                delete_class(class_name)
            elif admin_mode_selection == 3:
                print_roster()
            elif admin_mode_selection == 4:
                print_roster()
                class_name = input("Which class would you like to update?")
                update_class(class_name)
            else:
                print("That isn't an option.\n")
        elif mode_selection == 2:
            print("You have selected student mode. What would you like to do?")
            student_mode_selection = int(input("1 - Enroll in a class\n2 - Print class schedule\n"
                                           "3 - Un-enroll from a class\n"))

            if student_mode_selection == 1:
                print_roster()
                class_name = input("Select the class you'd like to enroll in.")
                student_name = input("Enter your name: ")
                enroll_student(class_name, student_name)
            elif student_mode_selection == 2:
                student_name = input("Enter your name: ")
                print_schedule(student_name)
            elif student_mode_selection == 3:
                class_name = input("Select the class you'd like to un-enroll from.")
                student_name = input("Enter your name: ")
                unenroll_student(class_name, student_name)
            else:
                print("That isn't an option.\n")

        mode_selection = int(input("Please select a mode, or select 'exit':\n"
                                   "1 - Admin\n2 - Student\n3 - Exit\n"))


main()

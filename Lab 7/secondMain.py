#Christine Mier
#5 November 2024

from people import Faculty, Student
import sys

def main():
    '''Main function of the program which aims to implement and loop through a main menu'''
    faculty_list = []
    student_list = []

    while True:
        print("*** TUFFY TITAN STUDENT/FACULTY MAIN MENU")
        print("1. Add faculty")
        print("2. Print faculty")
        print("3. Add student")
        print("4. Print student")
        print("5. Exit the program")
        choice = input("Enter menu choice: ")

        if choice == '1':
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            department = input("Enter department: ")
            faculty = Faculty(firstname, lastname, department)
            faculty_list.append(faculty)

        elif choice == '2':
            print("======================= FACULTY =======================")
            print("Record     Name                  Department")
            print("======   ====================   =========================")
            for index, faculty in enumerate(faculty_list):
                print(f"{index:<10} {faculty.firstname} {faculty.lastname:<15} {faculty.department}")

        elif choice == '3':
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            classyear = input("Enter class year: ")
            major = input("Enter major: ")
            advisor_index = int(input("Enter faculty advisor: "))
            student = Student(firstname, lastname)
            student.set_class(classyear)
            student.set_major(major)
            student.set_advisor(faculty_list[advisor_index])
            student_list.append(student)

        elif choice == '4':
            print("================================== STUDENTS =====================================")
            print("Name                 Class    Major                     Advisor")
            print("==================== ======== ========================= =========================")
            for student in student_list:
                advisor_name = student.advisor.firstname + "    " + student.advisor.lastname if student.advisor else "N/A"
                print(f"{student.firstname} {student.lastname:<15} {student.class_year:<15} {student.major:<20} {advisor_name}")

        elif choice == '5':
            sys.exit()

if __name__ == "__main__":
    main()

import random

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)  # Generate a unique course ID
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_students = 0
    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(1000, 9999)  # Generate a unique student ID
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []  # Initialize an empty list of courses
        Student.total_students += 1

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    def get_student_details(self):
        return {
            "Student ID": self.student_id,
            "Name": self.student_name,
            "Age": self.student_age,
            "Student Number": self.student_number
        }

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        if len(self.courses_list) == 0:
            return 0  # Return 0 if there are no courses
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)

students_list = []

while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit\n"))

        if selection == 1:
            student_number = input("Enter Student Number: ")
            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid Value")

            student = Student(student_name, student_age, student_number)
            students_list.append(student)
            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    students_list.remove(student)
                    print("Student Deleted Successfully")
                    break
            else:
                print("Student Not Exist")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    details = student.get_student_details()
                    for key, value in details.items():
                        print(f"{key}: {value}")
                    student.get_student_courses()
                    break
            else:
                print("Student Not Exist")

        elif selection == 4:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    average = student.get_student_average()
                    print(f"Student Average: {average}")
                    break
            else:
                print("Student Not Exist")

        elif selection == 5:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    while True:
                        try:
                            course_mark = float(input("Enter Course Mark: "))
                            break
                        except ValueError:
                            print("Invalid Value")
                    student.enroll_course(course_name, course_mark)
                    print(f"Course '{course_name}' Added Successfully")
                    break
            else:
                print("Student Not Exist")

        elif selection == 6:
            break  # Exit the program

    except ValueError:
        print("Invalid Selection. Please enter a valid number.")

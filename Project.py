#Project

# project : student managment system
#problem statement
# create a student management system using python and oops

# the system allows the user to:
# add a new student
# view all students.
# search for a student using student id
# update a student's marks
# delete a student record
# display the student with the highest marks
# exit the application
# student details

# each student should have :
# student id
# age

# Project: Student Management System
# Problem Statement: Create a student management system using Python and OOPs

class Student:
    def __init__(self, name, age, id, marks):
        self.name = name
        self.id = id
        self.marks = marks
        self.age = age

    def details(self):
        print("name =", self.name)
        print("id =", self.id)
        print("marks =", self.marks)
        print("age =", self.age)

    def display(self):
        self.details()


class ManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_students(self):
        n = int(input("How many students do you want to add? : "))
        for i in range(n):
            print(f"\nEnter details of student {i+1}")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            id = int(input("Enter student ID: "))
            marks = float(input("Enter student marks: "))

            student = Student(name, age, id, marks)
            self.students.append(student)
        print(f"\n{n} students added successfully")

    # View students
    def view_students(self):
        if len(self.students) == 0:
            print("No students found!")
        else:
            print("\n---- Students Details ----")
            for student in self.students:
                student.display()

    # Search student
    def search(self):
        id = int(input("Enter student ID to search: "))
        for student in self.students:
            if student.id == id:
                print("\nStudent found!")
                student.display()
                return
        print("Student not found!")

    # Update marks
    def update_marks(self):
        id = int(input("Enter student ID: "))
        for student in self.students:
            if student.id == id:
                new_marks = float(input("Enter new marks: "))
                student.marks = new_marks
                print("Marks updated successfully")
                return
        print("Student not found!")

    def delete(self):
        id = int(input("Enter student ID: "))
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found")

    # Display topper
    def topper(self):
        if len(self.students) == 0:
            print("No student available!")
        else:
            topper = self.students[0]
            for student in self.students:
                if student.marks > topper.marks:
                    topper = student
            print("\n---- Topper Details ----")
            topper.display()


# Main program
sms = ManagementSystem()
while True:
    print("====STUDENT MANAGEMENT SYSTEM====")
    print("1. Add students")
    print("2. View students")
    print("3. Search students")
    print("4. Update marks")
    print("5. Delete students")
    print("6. Display topper (highest marks)")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sms.add_students()
    elif choice == 2:
        sms.view_students()
    elif choice == 3:
        sms.search()
    elif choice == 4:
        sms.update_marks()
    elif choice == 5:
        sms.delete()
    elif choice == 6:
        sms.topper()
    elif choice == 7:
        print("Thank You!")
        break
    else:
        print("Invalid choice")

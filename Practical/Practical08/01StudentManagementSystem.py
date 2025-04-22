class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grades):
        if student_id in self.students:
            print("Student ID already exists!")
        else:
            self.students[student_id] = {"Name": name, "Age": age, "Grades": grades}
            print("Student added successfully.")

    def update_student(self, student_id, name=None, age=None, grades=None):
        if student_id in self.students:
            if name:
                self.students[student_id]["Name"] = name
            if age:
                self.students[student_id]["Age"] = age
            if grades:
                self.students[student_id]["Grades"] = grades
            print("Student details updated successfully.")
        else:
            print("Student ID not found!")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed successfully.")
        else:
            print("Student ID not found!")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student_id, details in self.students.items():
                print(f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grades: {details['Grades']}")

    def calculate_average_grade(self, student_id):
        if student_id in self.students:
            grades = self.students[student_id]["Grades"]
            if grades:
                avg_grade = sum(grades) / len(grades)
                print(f"Average Grade of {self.students[student_id]['Name']}: {avg_grade:.2f}")
            else:
                print("No grades available for this student.")
        else:
            print("Student ID not found!")


# Main Program Loop
sms = StudentManagementSystem()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Remove Student")
    print("4. View All Students")
    print("5. Calculate Average Grade")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grades_input = input("Enter grades separated by commas (e.g., 85,90,78): ")
        grades = list(map(int, grades_input.split(',')))
        sms.add_student(student_id, name, age, grades)

    elif choice == '2':
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new name (leave blank to skip): ")
        age_input = input("Enter new age (leave blank to skip): ")
        grades_input = input("Enter new grades (comma-separated, leave blank to skip): ")

        name = name if name else None
        age = int(age_input) if age_input else None
        grades = list(map(int, grades_input.split(','))) if grades_input else None

        sms.update_student(student_id, name, age, grades)

    elif choice == '3':
        student_id = int(input("Enter student ID to remove: "))
        sms.remove_student(student_id)

    elif choice == '4':
        sms.view_students()

    elif choice == '5':
        student_id = int(input("Enter student ID to calculate average grade: "))
        sms.calculate_average_grade(student_id)

    elif choice == '6':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

 
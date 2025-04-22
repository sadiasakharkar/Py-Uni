def register_students(class_name, *students, **details):
    print(f"\nClass Name: {class_name}")

    if students:
        print("Students:", ", ".join(students))
    else:
        print("No students registered.")

    if details:
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")

# Taking user input in a simple way
class_name = input("Enter class name: ")
students = input("Enter student names (comma-separated): ").split(",")

teacher = input("Enter teacher's name (optional): ")
room_number = input("Enter room number (optional): ")

# Clean student names
students = [s.strip() for s in students if s.strip()]

# Collect optional details
details = {}
if teacher:
    details["teacher"] = teacher
if room_number:
    details["room_number"] = room_number

# Call the function
register_students(class_name, *students, **details)

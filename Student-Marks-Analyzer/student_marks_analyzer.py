students = []

def menu():
    print("1. Add student")
    print("2. View students")
    print("3. Show statistics")
    print("4. Exit")


def add_student(students):
    name = input("Enter student name: ")
    n = int(input("Enter number of subjects: "))

    marks = []
    for i in range(n):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully")


def view_students(students):
    if len(students) == 0:
        print("No students found")
        return

    for i, student in enumerate(students, start=1):
        name = student["name"]
        marks = student["marks"]
        avg = sum(marks) / len(marks)
        print(f"{i}. {name} | Marks: {marks} | Avg: {avg:.2f}")


def show_statistics(students):
    if len(students) == 0:
        print("No students found")
        return

    total_avg = 0
    topper = None
    lowest = None
    highest_avg = -1
    lowest_avg = 101

    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        total_avg += avg

        if avg > highest_avg:
            highest_avg = avg
            topper = student["name"]

        if avg < lowest_avg:
            lowest_avg = avg
            lowest = student["name"]

    class_avg = total_avg / len(students)

    print(f"Class Average: {class_avg:.2f}")
    print(f"Topper: {topper} ({highest_avg:.2f})")
    print(f"Lowest Scorer: {lowest} ({lowest_avg:.2f})")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        show_statistics(students)
    elif choice == "4":
        print(".....exiting.....")
        break
    else:
        print("Invalid input")

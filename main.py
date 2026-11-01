import json
import csv
import os
from datetime import datetime

FILE = "students.json"6
def load_data():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error: JSON file is damaged.")
            return {}
    return {}
students = load_data()

def save_data():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def log_activity(message):
    with open("activity_log.txt", "a") as f:
        time = datetime.now()
        f.write(str(time) + " - " + message + "\n")

def add_student():
    sid = input("Enter Student ID: ")
    if sid in students:
        print("Student ID already exists!")
        return
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    marks = {}
    for subject in ["Python", "Maths", "DBMS"]:
        while True:
            try:
                mark = float(input(subject + " Marks: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Enter marks between 0 and 100")
            except ValueError:
                print("Please enter a number")
    students[sid] = {
        "name": name,
        "department": department,
        "marks": marks
    }
    save_data()
    log_activity("Student added: " + sid)
    print("Student record saved successfully!")
def view_students():
    if not students:
        print("No student records found.")
        return
    for sid, data in students.items():
        print("\nStudent ID:", sid)
        print("Name:", data["name"])
        print("Department:", data["department"])
        print("Marks:", data["marks"])
def search_student():
    sid = input("Enter Student ID: ")
    if sid in students:
        data = students[sid]
        print("Name:", data["name"])
        print("Department:", data["department"])
        print("Marks:", data["marks"])
    else:
        print("Student not found.")

def update_student():
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found.")
        return

    data = students[sid]
    data["name"] = input("Enter new name: ")
    data["department"] = input("Enter new department: ")
    for subject in ["Python", "Maths", "DBMS"]:
        while True:
            try:
                mark = float(input(subject + " Marks: "))
                if 0 <= mark <= 100:
                    data["marks"][subject] = mark
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Enter a valid number.")
    save_data()
    log_activity("Student updated: " + sid)
    print("Record updated successfully!")
def export_csv():
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Student ID", "Name", "Department",
            "Python", "Maths", "DBMS"
        ])
        for sid, data in students.items():
            writer.writerow([
                sid,
                data["name"],
                data["department"],
                data["marks"]["Python"],
                data["marks"]["Maths"],
                data["marks"]["DBMS"]
            ])
    log_activity("Student records exported to CSV")
    print("CSV file created successfully")
def show_file_methods():
    log_activity("File reading demonstration")
    with open("activity_log.txt", "r") as f:
        print("\nUsing read():")
        print(f.read())

    with open("activity_log.txt", "r") as f:
        print("\nUsing readline():")
        print(f.readline())

    with open("activity_log.txt", "r") as f:
        print("\nUsing readlines():")
        print(f.readlines())

def json_demo():
    sid = input("Enter Student ID: ")

    if sid in students:
        text = json.dumps(students[sid])
        print("JSON String:", text)

        data = json.loads(text)
        print("Python Object:", data)
    else:
        print("Student not found.")


# Main menu
while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Export CSV")
    print("6. Show File Reading Methods")
    print("7. JSON String Operations")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        export_csv()
    elif choice == "6":
        show_file_methods()
    elif choice == "7":
        json_demo()
    elif choice == "8":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
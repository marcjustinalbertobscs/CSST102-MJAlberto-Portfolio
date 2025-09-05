import csv
from datetime import datetime

# Rules

def attendance_rule(attendance):
    return "Attendance Rule, Satisfied" if attendance >= 75 else "Attendance Rule, Not satisfied"

def grading_rule(grade):
    if grade >= 75:
        return "Grading Rule, Satisfied"
    else:
        return "Grading Rule, Not satisfied"

def login_system_rule(login_status):
    return "Login Rule, Access granted" if login_status else "Login Rule, Access denied"

def bonus_points_rule(extra_work):
    return "Bonus Points Rule, +5" if extra_work else "Bonus Points Rule, None"

# NEW RULE: Library Borrowing
def library_borrowing_rule(valid_id):
    return "Library Rule, Allowed" if valid_id else "Library Rule, Not allowed"

# Save results to CSV with timestamp
def log_results(student_name, results):
    with open("logic_results.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), student_name] + results)

# Main Program
def run_expert_system():
    # Clear file at start
    with open("logic_results.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Student", "Attendance", "Grade", "Login", "Bonus", "Library"])

    # Ask user input for students
    students = []
    num_students = int(input("How many students do you want to test? "))

    for i in range(num_students):
        print(f"\nEnter details for Student {i+1}:")
        name = input("Name: ")
        attendance = int(input("Attendance (%): "))
        grade = int(input("Grade: "))
        login = input("Login success? (yes/no): ").strip().lower() == "yes"
        extra_work = input("Did extra work? (yes/no): ").strip().lower() == "yes"
        valid_id = input("Valid ID? (yes/no): ").strip().lower() == "yes"

        students.append({
            "name": name,
            "attendance": attendance,
            "grade": grade,
            "login": login,
            "extra_work": extra_work,
            "valid_id": valid_id
        })

    for student in students:
        results = [
            attendance_rule(student["attendance"]),
            grading_rule(student["grade"]),
            login_system_rule(student["login"]),
            bonus_points_rule(student["extra_work"]),
            library_borrowing_rule(student["valid_id"])
        ]
        log_results(student["name"], results)
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ",", student["name"], ",", ", ".join(results))

if __name__ == "__main__":
    run_expert_system()
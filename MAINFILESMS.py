print("MADE BY : SNEH TIWARI   26BCE10069")
student_database = {}

def add_student():
    print("\n--- Add New Student ---")
    student_id = input("Enter Roll Number / Student ID: ").strip()
    

    if student_id in student_database:
        print("❌ Student ID already exists!")
        return

    name = input("Enter Name: ").strip()
   
    age = int(input("Enter Age: "))
   
        
    course = input("Enter Class / Course: ").strip()

    # Store data as a list inside the dictionary
    student_database[student_id] = [name, age, course]
    print(f"✅ Student '{name}' added successfully!")


def view_all_students():
    print("\n--- Student Records List ---")
    if not student_database:
        print("No student records found in the system.")
        return
    
  
    for s_id, details in student_database.items():
      
        print(f"Roll No: {s_id} | Name: {details[0]} | Age: {details[1]} | Course: {details[2]}")


def search_student():
    print("\n--- Search Student ---")
    student_id = input("Enter Roll Number to search: ").strip()
    
    if student_id in student_database:
        details = student_database[student_id]
        print("🔍 Record Found:")
     
        print(f"Roll No: {student_id} | Name: {details[0]} | Age: {details[1]} | Course: {details[2]}")
    else:
        print("❌ Student Roll Number not found.")


def update_student():
    print("\n--- Update Student Details ---")
    student_id = input("Enter Roll Number to update: ").strip()
    
    if student_id not in student_database:
        print("❌ Student Roll Number not found.")
        return

  
    current_details = student_database[student_id]
  
    print(f"Current Record -> Name: {current_details[0]}, Age: {current_details[1]}, Course: {current_details[2]}")
    print("Leave blank and press Enter to keep current values.")

    new_name = input("Enter new Name: ").strip()
    new_age_input = input("Enter new Age: ").strip()
    new_course = input("Enter new Course: ").strip()

    # If user provided a new value, update it; otherwise keep original
    if new_name != "":
        current_details[0] = new_name
    if new_age_input != "":
        try:
            current_details[1] = int(new_age_input)
        except ValueError:
            print("❌ Invalid age format. Age update skipped.")
    if new_course != "":
        current_details[2] = new_course
        
    print("✅ Student profile updated successfully!")


def delete_student():
    print("\n--- Delete Student Record ---")
    student_id = input("Enter Roll Number to delete: ").strip()
    
    if student_id in student_database:
        # Remove entry from dictionary
        del student_database[student_id]
        print("🗑️ Student record deleted successfully.")
    else:
        print("❌ Student Roll Number not found.")



while True:
    print("\n===============================")
    print("   STUDENT MANAGEMENT SYSTEM   ")
    print("===============================")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Update Student Details")
    print("5. Delete Student Record")
    print("6. Exit Menu")
    
    choice = input("Select an option (1-6): ").strip()

    if choice == '1':
        add_student()
    elif choice == '2':
        view_all_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Thank you for using the system. Goodbye!")
        break
    else:
        print("❌ Invalid selection. Please choose a valid number from 1 to 6.")



        
# Student Record Management System

students = {}


# Function to add a student
def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input("Enter marks of Subject " + str(i) + ": "))
        marks.append(mark)

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


# Function to search a student
def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        student = students[roll_no]

        print("\nStudent Found!")
        print("Roll Number:", roll_no)
        print("Name:", student["name"])
        print("Marks:", student["marks"])
    else:
        print("Student not found!")


# Function to update marks
def update_marks():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Enter new marks:")

        marks = []

        for i in range(1, 6):
            mark = float(input("Enter marks of Subject " + str(i) + ": "))
            marks.append(mark)

        students[roll_no]["marks"] = marks

        print("Marks updated successfully!")
    else:
        print("Student not found!")


# Function to calculate total
def calculate_total(marks):
    return sum(marks)


# Function to calculate percentage
def calculate_percentage(marks):
    total = calculate_total(marks)
    percentage = total / len(marks)
    return percentage


# Function to display result
def display_result():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        student = students[roll_no]

        name = student["name"]
        marks = student["marks"]

        total = calculate_total(marks)
        percentage = calculate_percentage(marks)

        print("\n---------- STUDENT RESULT ----------")
        print("Roll Number:", roll_no)
        print("Name:", name)

        print("Marks:")
        for i in range(len(marks)):
            print("Subject", i + 1, ":", marks[i])

        print("Total Marks:", total)
        print("Percentage:", percentage, "%")

        if percentage >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")

        print("------------------------------------")

    else:
        print("Student not found!")


# Main menu
while True:

    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Display Result")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_marks()

    elif choice == "4":
        display_result()

    elif choice == "5":
        print("Thank you for using Student Record Management System!")
        break

    else:
        print("Invalid choice! Please try again.")

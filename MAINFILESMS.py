print("MADE BY : SNEH TIWARI   26BCE10069")
student_d = {}

def add_s():
    print("\n Add New Student ")
    student_id = input("Enter Roll Number / Id: ").strip()
    

    if student_id in student_d:
        print(" Student ID already exists")
        return

    name = input("Enter Name: ").strip()
   
    age = int(input("Enter Age: "))
   
        
    course = input("Enter Class / Course: ").strip()

    
    student_d[student_id] = [name, age, course]
    print(f" Student '{name}' added successfully!")


def view_a():
    print("\n Student Records List ")
    if not student_d:
        print("No student records found in the system.")
        return
    
  
    for s_id, details in student_d.items():
      
        print(f"Roll No: {s_id} | Name: {details[0]} | Age: {details[1]} | Course: {details[2]}")


def search_s():
    print("\n Search Student ")
    student_id = input("Enter Roll Number to search: ").strip()
    
    if student_id in student_d:
        details = student_d[student_id]
        print("Record Found:")
     
        print(f"Roll No: {student_id} | Name: {details[0]} | Age: {details[1]} | Course: {details[2]}")
    else:
        print(" Student Roll Number not found.")


def update_s():
    print("\n--- Update Student Details ---")
    student_id = input("Enter Roll Number to update: ").strip()
    
    if student_id not in student_d:
        print(" Student Roll Number not found.")
        return

  
    current_details = student_d[student_id]
  
    print(f"Current Record  Name: {current_details[0]}, Age: {current_details[1]}, Course: {current_details[2]}")
    print("Leave blank and press Enter to keep current values.")

    new_name = input("Enter new Name: ").strip()
    new_age_input = input("Enter new Age: ").strip()
    new_course = input("Enter new Course: ").strip()

    
    if new_name != "":
        current_details[0] = new_name
    if new_age_input != "":
        try:
            current_details[1] = int(new_age_input)
        except ValueError:
            print("Invalid age format. Age update skipped.")
    if new_course != "":
        current_details[2] = new_course
        
    print("Student profile updated successfully!")


def delete_s():
    print("\n--- Delete Student Record ---")
    student_id = input("Enter Roll Number to delete: ").strip()
    
    if student_id in student_d:
        
        del student_d[student_id]
        print(" Student record deleted successfully.")
    else:
        print(" Student Roll Number not found.")



while True:
    print("   STUDENT MANAGEMENT SYSTEM   ")
    
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Update Student Details")
    print("5. Delete Student Record")
    print("6. Exit Menu")
    
    choice = input("Select an option (1-6): ").strip()

    if choice == '1':
        add_s()
    elif choice == '2':
        view_a()
    elif choice == '3':
        search_s()
    elif choice == '4':
        update_s()
    elif choice == '5':
        delete_s()
    elif choice == '6':
        print("Thank you Goodbye")
        break
    else:
        print(" Invalid selection of no.")

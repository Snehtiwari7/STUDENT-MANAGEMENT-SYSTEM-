PROJECT README

NAME SNEH TIWARI
RNO. 26BCE10069

Student Record Management
System
# Project Overview
The Student Record Management System is a menu-driven Python application developed to manage student
academic records through the command line.
The system allows the user to:
• Add a student
• Search for a student
• Update student marks
• Calculate total marks and percentage
• Display the student result
• Exit the application
The project demonstrates Python functions, dictionaries, lists, loops, conditional statements, and user input.

# Features
Add Student: Enter Roll Number, Student Name, and marks of five subjects.
Search Student: Search using the roll number and display stored information.
Update Marks: Update marks of an existing student.
Calculate Total: Calculate total marks of five subjects.
Calculate Percentage: Calculate percentage from subject marks.
Display Result: Display roll number, name, marks, total, percentage, and PASS/FAIL result.
Exit: Close the application.

# Technologies Used
• Python 3
• Python Functions
• Dictionary
• List
• For Loop
• While Loop
• If-Else Statements
• Command Line Interface
No external Python libraries are required.

# Project Structure
Student-Record-Management-System/

NAME SNEH TIWARI
RNO. 26BCE10069
■
■■■ student_management.py
■■■ README.md

student_management.py: Complete Python source code.
README.md: Project information, setup, and usage instructions.

# Requirements
• Python 3.x
• Command Prompt / PowerShell / Terminal
No GUI application or external Python packages are required.

# Check Python Installation
Open a terminal or command prompt and run:
python --version

If needed, try:
python3 --version

# Download or Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd Student-Record-Management-System

Replace YOUR_GITHUB_REPOSITORY_URL with the actual GitHub repository URL.

# Environment Setup
No virtual environment or external dependencies are required. The project uses only Python's built-in features.

# Dependency Installation
There are no external dependencies. You do not need to run pip install commands.

# Configuration
No configuration file or environment variables are required.

# Run the Project
python student_management.py

If your system uses python3:
python3 student_management.py
===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. Search Student
3. Update Marks
4. Display Result
5. Exit
Enter your choice:

# How to Use the Program
Step 1: Add a Student — Select 1 and enter roll number, name, and five subject marks.
Enter Roll Number: 101
Enter Student Name: Rahul
Enter marks of Subject 1: 80

NAME SNEH TIWARI
RNO. 26BCE10069
Enter marks of Subject 2: 75
Enter marks of Subject 3: 90
Enter marks of Subject 4: 85
Enter marks of Subject 5: 70
Student added successfully!

Step 2: Search Student — Select 2 and enter the roll number.
Step 3: Update Marks — Select 3, enter an existing roll number, and enter new marks.
Step 4: Display Result — Select 4 and enter the roll number.
---------- STUDENT RESULT ---------Roll Number: 101
Name: Rahul
Subject 1 : 80.0
Subject 2 : 75.0
Subject 3 : 90.0
Subject 4 : 85.0
Subject 5 : 70.0
Total Marks: 400.0
Percentage: 80.0 %
Result: PASS
------------------------------------

Step 5: Exit — Select 5 to terminate the program.

# Result Calculation
total = sum(marks)
percentage = total / len(marks)

Five subjects are assumed, with each subject out of 100, so the average is the percentage.
Percentage >= 40
Percentage < 40

→ PASS
→ FAIL

# Error Handling
Student already exists!
Student not found!
Invalid choice! Please try again.

# Data Storage
students = {}
students = {
"101": {
"name": "Rahul",
"marks": [80, 75, 90, 85, 70]
}
}

Each roll number is used as the dictionary key.

# Important Note About Data
This version uses in-memory storage. Student records are lost when the program is closed. No database or
external file is required for the current version.

# Future Improvements
• Permanent file storage
• Database integration
• Delete student functionality
• Input validation for marks

NAME SNEH TIWARI
RNO. 26BCE10069
• Grade calculation
• Display all students
• Student login system
• Graphical User Interface
• Attendance management
• Subject-wise performance analysis

# Troubleshooting
Python command not found:
python3 --version

Install Python 3 and ensure it is added to PATH.
File not found:
cd Student-Record-Management-System
python student_management.py

Make sure the source file is named student_management.py.

# Project Execution
The complete project can be executed directly from a command-line environment. No GUI, IDE-specific
configuration, external libraries, or additional software is required apart from Python 3.

# MADE BY
Name: Sneh Tiwari
Roll Number: 26BCE10069
Course: Python Essentials
Project: Student Record Management System



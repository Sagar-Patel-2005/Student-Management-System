import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",         
    password="*******",         
    database="student_db"
)

cursor = conn.cursor()

# Add new student
def add_student():
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    query = "INSERT INTO students (name, roll_no, course, marks) VALUES (%s, %s, %s, %s)"
    data = (name, roll_no, course, marks)
    cursor.execute(query, data)
    conn.commit()
    print("Student added successfully!\n")

# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Roll No: {row[2]}, Course: {row[3]}, Marks: {row[4]}")
    print()

# Update student
def update_student():
    id = input("Enter Student ID to update: ")
    name = input("Enter new name: ")
    roll_no = input("Enter new roll number: ")
    course = input("Enter new course: ")
    marks = int(input("Enter new marks: "))

    query = "UPDATE students SET name=%s, roll_no=%s, course=%s, marks=%s WHERE id=%s"
    data = (name, roll_no, course, marks, id)
    cursor.execute(query, data)
    conn.commit()
    print("Student record updated.\n")

# Delete student
def delete_student():
    id = input("Enter Student ID to delete: ")
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    print("Student deleted.\n")

# Menu-driven program
def menu():
    while True:
        print("----- Student Management System -----")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()
conn.close()

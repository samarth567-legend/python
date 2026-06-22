student = {}

while True:
    print("Welcome to Student Management System")
    print("1. Add Student")
    print("2. View All Records")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")

        student[roll_no] = {
            "roll_no": roll_no,
            "name": name
        }

        print("Student added successfully")

    elif choice == 2:
        for roll_no, details in student.items():
            print("Roll No:", roll_no)
            print("Name:", details["name"])

    elif choice == 3:
        roll_no = input("Enter Roll Number to Search: ")

        if roll_no in student:
            print("Name:", student[roll_no]["name"])
        else:
            print("Student not found")

    elif choice == 4:
        roll_no = input("Enter Roll Number to Delete: ")

        if roll_no in student:
            del student[roll_no]
            print("Student deleted successfully")
        else:
            print("Student not found")

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Wrong choice")

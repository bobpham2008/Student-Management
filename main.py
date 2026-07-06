def add_student():
  student_name = input("Enter student name: ")
  print("Student:", student_name)

while True:
  print("\n===== STUDENT MANAGEMENT =====")
  print("1. Add Student")
  print("0. Exit")
  
  choice = input("Choose:")
  if choice == "1":
    add_student()
  elif choice == "0":
    print("Goodbye!")
    break
    
  else:
    print("Invalid choice. Please try again.")
  

def add_student():
  student_name = input("Enter student name: ")
  student_name = student_name.strip().title()
  students_list.append(student_name)
  print("Student added successfully!")

def show_students():
  print("\n===== STUDENT LIST =====")
  
  if len(students_list) == 0:
    print("No students found.")
    return
    
    for student in students_list:
      print(Student)
      
while True:
  print("\n===== STUDENT MANAGEMENT =====")
  print("1. Add Student")
  print("2. Show Students")
  print("0. Exit")
  
  choice = input("Choose:")
  if choice == "1":
    add_student()
  elif choice == "2":
    show_students()
  elif choice == "0":
    print("Goodbye!")
    break
    
  else:
    print("Invalid choice.")
  

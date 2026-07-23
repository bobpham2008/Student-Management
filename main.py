def add_student():
  student_id = input("Enter student ID: ").strip().upper()
  student_name = input("Enter student name:").strip().title()
  student_score = float(input("Enter student score:"))
  student = [
    student_id,
    student_name,
    student_score
  ]
  students_list.append(student)
  print("Student added successfully!")

def view_students():
  print("\n===== STUDENT LIST =====")
  
  if len(students_list) == 0:
    print("No students found.")
    return
    
    for student in students_list:
      print(
        f"ID: {student[0]} | "
        f"Name: {student[1]} | "
        f"Score: {student[2]}"
      )
      
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
  

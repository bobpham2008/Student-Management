def add_student():
  student_name = input("Enter student name: ")
  print("Student:", student_name)

while True:
  add_student()
  choice = input("Continue? (y/n):")
  
  if choice.lower() == "n":
    print("Goodbye!")
    break
    

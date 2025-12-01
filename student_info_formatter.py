# Create a student Info card

Student_Name = input("hey, there please enter your name here ")
Student_Age = int(input("Please enter your age "))
Student_Course = input("enter your course name ")
Student_percentage = float(input("enter your percentage "))  
initials = Student_Name.find(" ")

print(f'''
Student Profile Created successfully
------------------------------------
Name : {Student_Name}
Initials: {Student_Name[0],Student_Name[initials+1]}
Age: {Student_Age}
Course: {Student_Course}
Percentage: {Student_percentage}
''')
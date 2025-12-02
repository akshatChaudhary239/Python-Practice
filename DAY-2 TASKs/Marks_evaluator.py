# Marks evaluator
Subject_1 = int(input("enter your number"))
Subject_2 = int(input("enter your number"))
Subject_3 = int(input("enter your number"))
Subject_4 = int(input("enter your number"))
Subject_5 = int(input("enter your number"))

total_marks = Subject_1+Subject_2+Subject_3+Subject_4+Subject_5
percentage = (total_marks/500)*100
print(total_marks)
if(percentage>=80):
    print("Grade A")
if(percentage>=60 and percentage<80):
    print("Grade B")
if(percentage>=40 and percentage<60):
    print("Grade C")
if(percentage<40):
    print("Grade F")

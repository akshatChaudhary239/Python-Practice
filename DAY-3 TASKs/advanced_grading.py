# Grade evaluator with grading system
Marks_1 = float(input("enter your marks "))
Marks_2 = float(input("enter your marks "))
Marks_3 = float(input("enter your marks "))
Marks_4 = float(input("enter your marks "))
Marks_5 = float(input("enter your marks "))
total_marks = Marks_1+Marks_2+Marks_3+Marks_4+Marks_5
percentage = (total_marks/500)*100
print(percentage)
if percentage >100:
    print("Who do you think you are? AKKU?😏")   
elif percentage>=90:
    print("A+")
elif percentage>=70:
    print("B+")    
elif percentage>=60:
    print("C+")    
elif percentage>=50:
    print("D+")
 
else:
    print("you are fail")        
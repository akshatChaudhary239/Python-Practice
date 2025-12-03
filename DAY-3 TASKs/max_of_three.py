# find the maximum number among three numbers

Number_1 = float(input("enter your number"))
Number_2 = float(input("enter your number"))
Number_3 = float(input("enter your number"))

if Number_1>Number_2 and Number_1>Number_3:
    print("Number1 is the greatest number",Number_1)
elif Number_2>Number_1 and Number_2>Number_3:
    print("Number2 is the greatest",Number_2)    
elif Number_1==Number_2 and Number_2==Number_3 and Number_3==Number_1:
    print("All the numbers are equal")
elif Number_1==Number_2 :
    print("Number1 and Number2 are equal")    
elif Number_2==Number_3 :
    print("Number2 and Number3 are equal")    
elif Number_1==Number_3 :
    print("Number1 and Number3 are equal")    
else:
    print("Number3 is the greatest",Number_3)        
# Print the Largest number out of 3 inputs using only comparision operators

Num1 = int(input("enter the first number "))
Num2 = int(input("enter the second number "))
Num3 = int(input("enter the third number "))
Largest_Number = (Num1>Num2 and Num1>Num3)*Num1 + (Num2>Num1 and Num2>Num3)*Num2 + (Num3>Num1 and Num3>Num2)*Num3
print(Largest_Number)

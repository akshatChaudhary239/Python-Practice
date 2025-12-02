# Take two input and perform every calculation on it

num1= int(input("enter your first number"))
num2 = int(input("enter your second number"))
print(f'''
Sum: {num1+num2}
Sub: {num1-num2}
Multiplication: {num1*num2}
Division: {num1/num2}
Floor Division: {num1//num2}
To the power of: {num1**num2}
Remiander: {num1%num2}
''')
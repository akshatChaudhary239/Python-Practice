# ask user name and age and prinbt a friendly message

Name = input("what is your name")
Age = int(input("what is your age"))
print(f'hi {Name} how are you i am glad to hear that to turned {Age}')

# calculator
# sum
a = 12
b = 14
print(a+b)  

# sub
num1 = 23
num2 = 21
print(num1-num2)

# even or odd
Enter =int(input("enter a number"))
if (Enter%2==0):
    print("even")
else:
    print("odd")    

# celius to fahrenhiet
celsius = int(input("enter the digit"))
fahrenhiet = (celsius*9/5)+32
print(fahrenhiet)

# Ask a sentence and print length and uppercase

sentence = input("enter a sentence ")
print(len(sentence))
print(sentence.upper())
# sum of digits of any number

number = int(input("enter a number "))
sum = 0
for i in str(number):
    sum = sum+int(i)

print(sum)
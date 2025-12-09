# check if the input number is a prime number or not
number = int(input("enter a number "))

if number<=1:
    print("it is not a prime number")
else:
    for i in range(2,number):
        if i%number==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")    

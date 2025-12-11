# Prime number checker

def prime(num):

    if num<=1:
        print("it is not a prime number")
    else:    
        for i in (2,int(num**0.5)+1):
            if num%i==0:
                print("it is not a prime number")
            else:
                print("it is a prime number")    


num = int(input("enter a number "))  
prime(num)             
# find the maximum out of three number

def maximum(a,b,c):
    if a>b and a>c:
        print("A is greatest")
    elif b>c and b>a:
        print ("B is greatest")
    elif a==b and a==c:
        print ("All are equal" )
    elif a==c and a!=b:
        print("A and C are equal" )          
    elif b==c and b!=a:
        print ("B and C are equal" )

a = int(input("Enter a Number "))                  
b = int(input("Enter a Number "))                  
c = int(input("Enter a Number "))   

maximum(a,b,c)


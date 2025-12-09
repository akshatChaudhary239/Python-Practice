# count the number of vowels in a string

string = input("enter a string ")
count = 0
for i in string:
    if i == "A" or i=="a":
        count+=1
    elif i =="E" or i=="e":
        count+=1    
    elif i =="I" or i=="i":
        count+=1    
    elif i =="O" or i=="o":
        count+=1    
    elif i =="U" or i=="u":
        count+=1    

print("number of vowels in your character-",count )        
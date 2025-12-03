# Check if a character is vowel or consonant
Character = input("enter the character")
if Character=="a" or Character=="e"or Character=="i" or Character=="o"or Character=="u":
    print("it is a vowel")
elif Character=="A" or Character=="E"or Character=="I" or Character=="O"or Character=="U":
    print("it is a vowel")
else:
    print("it is a consonant")

# Second method
if Character in "aeiouAEIOU":
    print("it is a vowel")
else:
    print("it is a consonant")    
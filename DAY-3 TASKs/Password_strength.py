# Password strength checker
Password = input("enter a strong password")
if len(Password)>=8 :
    if ("0" in Password or "1"in Password or "2" in Password or "3" in Password or "4" in Password or "5"in Password or"6"in Password or"7"in Password or "8"in Password or "9"in Password):
        print("your password is strong")

else:
    print("password is weak")    
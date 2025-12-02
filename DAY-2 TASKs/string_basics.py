# String basic recaller

Name= input("enter your name ")
no_space = Name.replace(" ","")
char_count = len(no_space)
first_initial = Name[0]
second_initial = Name[-1]
middle_name = Name[1:-1]
resversed_name= Name[::-1]
print(f'''
Your full name: {Name}
Actual Length of the Name : {char_count} 
First Initial: {first_initial}
Last Initial: {second_initial}
Middle Name: {middle_name}
Reversed Name: {resversed_name}
  ''')
# String basic recaller

Name= input("enter your name ")
first_initial = Name[0]
second_initial = Name[-1]
middle_name = Name[1:-2:1]
resversed_name= Name[::-1]
print(f'''
Your full name: {len(Name)}
First Initial: {first_initial}
Last Initial: {second_initial}
Middle Name: {middle_name}
Reversed Name: {resversed_name}
  ''')
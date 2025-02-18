# Assignment-2 

#1 Write a program to input student name & marks of 3 subs
#  print name & percentage in output.

# print("Percentsge Calculator (out of 100 marks)")

# stu_name = input("Enter your name:")
# mar_marks = int(input("Enter marathi marks:"))
# hin_marks = int(input("Enter hindi marks:"))
# eng_marks = int(input("Enter english marks:"))  
# sci_marks = int(input("Enter science marks:")) 
# geo_marks = int(input("Enter history & geography marks:"))
# math_marks = int(input("Enter Mathematics marks:"))

# per = ((mar_marks+eng_marks+sci_marks+geo_marks+math_marks+hin_marks)/6)
# print(f"{stu_name} your final percentage is {per}%") 




'''#2 write a program that collects multiple types of data 
   (e.g., name, age, height & student status) from user input,
   stores them in a dictionary, & then prints out the collected data'''

# initializing dictionary
user_data = {}     # this is for store details in dictionary

# user input
user_data['name'] = input("Enter your name:")
user_data['age'] = int(input("Enter your age:"))
user_data['height'] = float(input("Enter your height in feet:"))
user_data['std_status'] = input("Are you a student (yes/no):")

print(user_data) 
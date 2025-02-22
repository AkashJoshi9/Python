# 1. write a program for leap year checking by using user input 
# user Input
year = int(input("Enter the Year e.g(2025):"))
# checking leap year
if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print(f"{year} is a leap year")
else:
        print(f"{year} is a not leap number")

# 2. Program for username and password (Login incorrect Password, incorrect username)
# predefined User And Pass
predef_user = "Akash"
predef_pas = "Aka123"
# User input
user = input("Username  :")
pas = input("Password  :")
# Checking Creditionals
if user == predef_user:            
    if pas == predef_pas:         
       print("Login Successfull!")
    else: 
       print("incorrect Password!")
else:
   print("Username incorrect")

# 3. Admission Eligiblity : for following criteria
# Marks in Maths >= 50
# Marks in Physics >=50
# Marks in Chemistry >=50
# Total Marks in all three subs >= 160 or Total marks in Mathematics & physics >= 120
print("Enter PCM Marks ('Student Should be passed in all subjects')")
math = int(input("Enter Marks of Mathematics : "))  
phy = int(input("Enter Marks of Physics : "))
chem = int(input("Enter Marks of Chemistry : "))

if (math >= 50 and phy >= 50 and chem >= 50) and (math + phy + chem >= 160) or (math + phy >= 120):
        print("Congrats You are eligible!") 
else:
        print("Unfortunatlly You are not eligible!")
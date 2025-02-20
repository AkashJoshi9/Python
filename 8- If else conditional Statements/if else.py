# If else conditional statements

# 1. if statement
age = int(input("Enter Your age:"))
if age >= 18:
    print("You are an Adult!")

a = 20
b = 30
if a<b:
    print("Yes it is.")

# 2. if-else statement ( for for false statements)
age = int(input("Enter Your age:"))
if age >= 18:   
    print("You are an Adult!")
else:
    print("You are an Minor!")

temp = int(input("Enter to check weather condition:"))
if temp <= 0:
    print("Weather is too cold!")     
else:
    print("Weather is Good!")

# 3. if-elif-else statement ( for multiple condition)

temp = int(input("Enter to check weather condition:"))
if temp <= 0:
    print("Weather is too cold!") 
elif temp <= 15:    
    print("Weather is cold!")
elif temp > 35:    
    print("Weather is too hot!")
elif temp >= 30:    
    print("Weather is hot!")  
else:
    print("Weather is Good!")

# 4. Nested 'if-else' statement (if else inside if-else statement)
#    multiple condition depend on each other

''' Print positive, Nagative & zero. Positive - Even/odd'''

num = int(input("Enter the number:"))

if num > 0: # Checking positive number
    if num % 2 == 0:
        print("This is a even number")
    else:
        print("This is a odd number")
else:
    if num == 0:
        print("This is Zero")
    else:
        print("This is a Nagative number")     

# 5. Conditional Expression (terenary operator)
age = int(input("Enter your age:")) 
a = "You are eligible for Voting!" if age >= 18 else "You are not eligible!"
print(a)                   
# input funtion for python 

# input reads as a string and returns it. 

# name = input("Enter your name:")
# print(f"Welcome {name} to python.")

# age = input("Enter your age:")
# print(f"Great! So 10 years after you will be a {int(age)+10}!")

# input from user to add two numbers and print result
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
print(f"The Answer is {a+b}")

# input from user to basic calculator and print result
print("Choose Option - 'add, mul, div, subs, avg, exit'")

while True:
    user = input("Choose the operation:")
    if user == 'exit':
      print("You are exit!")
      break

    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    if user == 'add':
      result = a + b 
      print(f"Answer: {result}")
    elif user == 'mul':
      result = a * b 
      print(f"Answer: {result}")
    elif user == 'subs':
      result = a - b
      print(f"Answer: {result}")
    elif user == 'div':
     if b != 0:
        result = a / b
        print(f"The result is: {result}")
     else:
        print("Error! Cannot divide by zero.")
    elif user == 'avg':
      result = (a + b)/2
      print(f"Answer: {result}")
    else:
      print("error!")

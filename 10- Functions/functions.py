# Functions in python 

# create function without parameters
def greet():
    print("Thank You!")
# we can use greet() anyware we need multiple times
greet()


# create a function add two numbers using parameters
def add(a, b):    # Parameters (a, b)
    result = a + b
    print("The sum is:", result)
# call function
add(35, 25)       # Arguments (35, 5)


# return statement
def s(y,n,m):
    return y + n * m 
# after return statement funtion ends

r = s(15, 16, 17)
print(r)   


# function to convert celcius to fahrenheit
def c_to_f(cel):
    f = (cel * 9/5) + 32
    return f
# calling fun
tempf = c_to_f(23)
print(tempf)

# always use return statement for numeric operation

# The Pass Statement
def my_f():
    pass       # Code to be updated later
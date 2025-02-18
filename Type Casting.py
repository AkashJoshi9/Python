# casting in python

a = "1"
c = int(a)
b = 3
print(b+c)

# all numerical type can be cast into str
# explicit type casting (manually)
num = 25.45
num1 = str(num)
print(type(num1))

# implicit or coercion type casting (automatically)
var1 = 10
var2 = 15.5
var3 = var1+var2
print(var3)
print(type(var3))

# boolean 
a1 = bool(0)
a2 = bool(1)
print(a1, a2)
print(type(a1))
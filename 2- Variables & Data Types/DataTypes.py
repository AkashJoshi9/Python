# data types in python

a = 1    # this will consider as a 'integer' value
b = 1
print(a+b)
# for checking datatype 
print(type(a))

c = "1"  # this will consider as a 'string' value
d = "1"
print(c+d)
# for checking datatype 
print(type(c))

# basic data types in python
# 1. Numeric
a1 = 1            # integer
b1 = 1.14         # float
c3 = complex(1,3) # complex (1+3j)
print(type(b1))
print(type(c3))

# 2. sequence 
a2 = "Akash"                               # string
b2 = [1,2,3,4,5,"JAJ"]                     # list
c3 = (1,2,3,4,5,"JAJ") or 1,2,3,4,5,"JAJ"  # tuple
print(type(a2))
print(type(b2))
print(type(c3))

# 3. dictionary ('Key': 'Value')
my_dictionary = {"name": "Akash", "age": 23, "city": "Thane"}
print(type(my_dictionary))   

# 4. sets
my_sets = {1,2,3,4,5,"JAJ"}
print(type(my_sets)) 

# 5. boolean
bool1 = True
bool2 = False
print(type(bool1))

# 6. Binary
     # bytes, bytearray, memoryview
byte1 = b"Akash"
print(type(byte1)) 
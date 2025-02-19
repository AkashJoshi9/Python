# operators

# 1. Arithmatic Operators 
a = 9
b = 4
print(a+b) # add operator
print(a-b) # subs operator
print(a*b) # multi operator
print(a/b) # div operator
print(a//b) # floor div (div in integer)
print(a%b) # modulus (returns remainder)
print(a**b) # Exponentiation

# 2. Comparison Operators (boolean: True or false)
print(a==b) # equal
print(a!=b) # not equal
print(a>b)  # greater than
print(a<b)  # less than
print(a>=b) # greater than equal to
print(a<=b) # less than equal to

# 3. Assingnment operators
a1 = 25              # it assigns the value or variable
a2 = a1 + 25
a3 = a2 - 25
print(a1+a2+a3)
# etc 

# 4. Logical Operators
''' Rule : AND OPERATOR
1. True + True = True
2. True + False = False
3. False + False = False'''
x = 11
y = 2
print(x>10 and y<1) 


''' Rule : OR OPERATOR
1. True + True = True
2. True + False = True
3. False + False = False'''

# Not operator
print(not(x==11 and y==2))

# 5. Identity Operator - is, is not
x = [1,2,3]
x = y
z = [1,2,3]
print(x is y)
print(x is z)
print(x is not z)

# 6. Membership Operators - in, not in
my_list = ['Apple', 'Mango', 'Grapes']
print('Apple' in my_list)
print('Mango' not in my_list)

# 7. Bitwise Operator - AND, OR, XOR, NOT etc.,
q = 5         # 5 in binary is 0101
r = 3         # 3 in binary is 0011
print(q & r)
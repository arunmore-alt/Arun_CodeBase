a = 34
b = 45.45
print(f"The Sum {a} + {b} = {a+b}")
c = "bbds"
print(type(a))
print(type(b))
print(type(c))
print(id(a))
print(id(b)) 
print(id(c))
print(a is b)
print(a is not b)
print(a == b)
print(a != b)
d = True
print(type(d))
print(id(d))
print(d is True)
e = complex(3,4)
print(e)
print(type(e))
print(id(e))
f = None
print(f)
print(type(f)) 
print(id(f))
g = b'ahello'
print(g)
print(type(g))
print(id(g))

# List mutable with various data types
h = [1,2,"hjdc",None,5]
print(h)
print(type(h))
print(id(h))

# Tupple immutable with various data types
i = (1,2,3,3,4,5)
print(i)
print(type(i))
print(id(i))   

# Dictionary mutable with various data types
j = {1:"hello",2:34.5,3:None,4:True}
print(j)    
print(type(j))
print(id(j))

# Set mutable with various data types
k = {1,"jshdbh",3,4,5,5,4,3}
print(k)
print(type(k))
print(id(k))

# -------------->>>>>The Everything is Object in Python

# Python is Dynamically Typed Language
x = 34
print(x)
x = "hello" 
print(x)
x = 45.67
print(x)
x = [1,2,3,4]
print(x)
x = (1,2,3,4)
print(x)
print(type(x))

# Operaters in Python
a = 6
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor Division if 2.5 ka only 2 return karega
print(a ** b) # Exponentiation
print(a % b)  # Modulus 
print(-a)      # Negation
print(+b)      # Positive
print(a > b)   # Greater Than
print(a < b)   # Less Than
print(a >= b)  # Greater Than or Equal To
print(a <= b)  # Less Than or Equal To
print(a == b)  # Equal To
print(a != b)  # Not Equal To
print(a is b)  # Identity Operator
print(a is not b) # Identity Operator
print(a & b)   # Bitwise AND
print(a | b)   # Bitwise OR 
print(a ^ b)   # Bitwise XOR
print(~a)      # Bitwise NOT
print(a << 2) # Left Shift
print(a >> 2) # Right Shift
print(a and b) # Logical AND



#Type Casting in Python
x = 34
y = 45.67
print(type(x))
print(type(y))
x = float(x)
y = int(y)
print(type(x))
print(type(y))
print(x)
print(y)

# Conversions to String
a = 34  
b = 45.67
c = True
d = None
print(str(a))
print(str(b))   
print(str(c))
print(str(d))
print(type(str(a)))
print(type(str(b))) 
print(type(str(c)))
print(type(str(d))) 

# Conversions to Integer
a = 34.56       
b = "78"
c = True            
d = None
print(int(a))
print(int(b))
print(int(c))
# print(int(d))  # Error
print(type(int(a)))
print(type(int(b))) 
print(type(int(c))) 

# Conversions to Float
a = 34      
b = "78.56"
c = True

d = None
print(float(a)) 
print(float(b))
print(float(c))
# print(float(d))  # Error
print(type(float(a)))   
print(type(float(b)))
print(type(float(c)))



# Conversions to Boolean
a = 34
b = "78.56"
c = True
d = None
print(bool(a))
print(bool(b))
print(bool(c))
# print(bool(d))  # Error
print(type(bool(a)))
print(type(bool(b)))
print(type(bool(c)))

# Conversions to Complex
a = 34
b = 45.67   
c = True
d = None
print(complex(a))
print(complex(b))
print(complex(c))
# print(complex(d))  # Error
print(type(complex(a)))
print(type(complex(b)))
print(type(complex(c)))

# Conversions to List
a = (1,2,3,4)
b = "78.56" 
c = {1,2,3,4}
d = None
print(list(a))
print(list(b))
print(list(c))
# print(list(d))  # Error   
print(type(list(a)))
print(type(list(b)))    
print(type(list(c)))


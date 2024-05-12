# <================ Python Strings ===============>

# ===================================================================================
# A string is sequence of characters
# Strings can be created by enclosing characters inside a single quote or double quotes.
# Even triple quotes can be used in Python but generally used to 
# represent multiline strings and docstrings.
# Strings are immutable. This means that elements of a string cannot be changed once it has been declared.
# We can simply re-assign different strings to the same name.
# ===================================================================================

# name = "Paras"
# p = '''This is a Demo Paragraph.
# We can write Multiline strings 
# in this Triple Quotes
# '''
# print(name)
# print(p)

# ===================================================================================

# ----------------------
# Python String indexing
# ----------------------

# fruit = "Apple"
# print(fruit[0])
# print(fruit[-5])
# print(fruit[4])
# print(fruit[-1])


# ===================================================================================

# ------------------------------------------
# Accessing Characters in a String (Slicing) 
# ------------------------------------------

# car = "Ferrari"
# print(car[2:5]) # First index is Inclusive but last index is Exclusive
# print(car[:5]) 
# print(car[2:]) 
# print(car[0:7:2])
# print(car) # Strings are immutable 
# print(car[::-1])
# print(car[-1:0:-1])
# print(car[0:5:-1])
# print(car[-1:0:1])


# ===================================================================================

# -----------------------
# for loops with strings
# -----------------------

# for letter in "Hello":
#     print(letter*2, end=" ")

# ===================================================================================

# ---------------
# String Methods
# ---------------

p = "ABCD$%"
print('p.isalpha', p.isalpha())
print('p.isdigit', p.isdigit())
print('p.islower', p.islower())
print('p.isupper', p.isupper())
print('p.lower', p.lower())
print('p.upper', p.upper())

x = "  xyz  "
newXvar = x.rstrip()
print(newXvar)
newXvar = x.lstrip()
print(newXvar)

print(x)















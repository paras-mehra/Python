# <================ Conditional Statements in Python ===============>

# If
# if test expression:
#     statement(s)

# In Python, the body of the if Statement is indicated by the indentation. Body starts with an indentation and the first unindented line marks the end.
# The body of if is executed only if test expression evaluates to True


age = 18

if age >= 18:
    print("You can Vote")
elif age < 18 and age > 3:
    print("You can't Vote")    
else:
    print("You are a Kid")

print("This will Print always")




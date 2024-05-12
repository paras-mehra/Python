# <================ Loops in Python ===============>

# ===================================================================================
# The loops in python is used to iterate over a sequence(list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
# ===================================================================================

for i in range(10):
    print(i*2, end=", ")

# students = ["Karan","Paras","Bharat","Gourav","Rishab","Mukul"]

# for student in students:
#     print(student)

# ===================================================================================

# -----------
# While Loop
# -----------

# The while Loop in Python is used to iterate over a block of code as long as the test expression (condition) is true. 
# We generally use this loop when we don't know beforehand, the number of times to iterate.
# while test_expression:
#     Body of While

# n = 5
# while n >= 0:
#     print(n)
#     n -=1

# ===================================================================================

# -----------------
# break & continue
# -----------------

# The ( break ) statement terminates the loop containing it.
# The ( continue ) statement is used to skip to rest of the code inside a loop for the current iteration only.
# Loops does not terminates but continues on with the next iteration.

# for i in range(10):
#     if i > 6:
#         break
#     print(i)

# for x in range(11):
#     if x == 5:
#         continue
#     print(x)
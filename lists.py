# <================ Lists in Python ===============>

# In Python, a List is created by Placing all the items (elements) inside a square bracket[], 
# separated by commas.
# It can have any number of items and they may be of different types (integer, float, string etc.)
# ================================================================================================

name = [10, "Hello", 20.5, {"age":"20"}, ["Paras","Karan"], ("Doctor","Actor","Painter")]
print(type(name[0]))

fruits = ["Apple","Mango","Watermelon","Orange"] 
print(fruits[1])
print(fruits[-1])

# print(fruits[0:3])
# print(fruits[:2])
# print(fruits[1:])
# print(fruits[-1:0:-2])

# fruits[2] = "Cherry"
# print(fruits) # Lists are Mutable means we can updated Lists
# del fruits[3]
# print(fruits)
# del fruits
# print(fruits)

# ================================================================================================

# -------------------
# List Comprehension
# -------------------

# a = [0,1,2,3,4,5,6,7,8,9,10]

# a = [x for x in range(21)]
# print(a)

# a = [x for x in range(21) if x%2 == 0]
# print(a)

# b = [ 2**i for i in range(10)]
# print(b)


# ================================================================================================

# --------------
# Lists Methods
# --------------

# a = [ 1,2,3]
# print(a)

# a.append(4)
# print(a)

# a.insert(0,0.5)
# a.insert(0,"Paras")
# print(a)

# a.pop(5)
# print(a)

# fruits = ["Mango","Banana","Apple","Watermelon","Orange","Apple","Mango","Apple"] 

# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)

# print(fruits.index("Orange"))
# print(fruits.count("Mango"))
# fruits.clear()
# print(fruits)

# ================================================================================================

# ---------------
# Lists Functions
# ---------------

# num = [1,4,2,5,3,21,64]
# print(max(num))
# print(min(num))
# print(len(num))
# print(sum(num))

# name = "Paras"
# print(list(name))

# ================================================================================================

# ------------------
# for loop with List
# ------------------

# days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

# for day in days:
#     print(day)
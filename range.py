# <================ Range in Python ===============>

# we can generate a sequence of Numbers using range() function.range(10) will generate numbers from 0 to 9 (10numbers). -> [0,1,2,3,4,5,6,7,8,9]
# we can also define the start, stop and step size as range(start, stop, size). Step size defaults to 1 if not provided

a = range(10)
print(a)

a = list(range(10))
print(a)

a = list(range(5, 11)) # first number is inclusive but last number is exclusive
print(a)

a = list(range(4, 12, 2))
print(a)


# <================ Python File Handling ===============>
# How to Open a File?
# Python has a built-in function open() to open a file. This function returns a file Object.
# We can specify the mode while opening a file. In mode , we specify whether we want to read 'r', write 'w' or append 'a' to the file. We also specify if we want to open the file in text mode or binary mode.
# ==================================================================================

f = open("data.txt", 'r')

# print(f.readline())
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)
f.close()

# ==================================================================================

# --------------------------
# Read mode in File Handling
# --------------------------

# with open('data.txt') as f:
#     # for lines in f:
#     #     print(lines)

#     f.seek(23)
#     print(f.read())

# ==================================================================================

# ----------------------------
# Write Mode in File Handling
# ----------------------------

# data = ["Karan\n", "Bishu"]
# with open('write.txt','w') as f:
#     f.write("Paras\n")
#     f.writelines(data)

# ==================================================================================

# ----------------------------
# Append Mode in File Handling
# ----------------------------

# data = ["Karan\n", "Bishu"]
# with open('append.txt','a') as f:
#     f.write("\nParas\n")
#     f.writelines(data)



    
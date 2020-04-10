# open file
f = open("file.txt")
print(f.read())
f.close()

# read first 3 character of file
f = open("file.txt")
print(f.read(3))
f.close()

# read by line
f = open("file.txt")
print(f.readline())
f.close()

# append file
f = open("file.txt", "a")
f.write("append text")
f.close()

# override content
f = open("file.txt", "w")
f.write("new text")
f.close()

# create new file
# f = open("file.txt", "x") => raise error
f = open("new_file.txt", "x")

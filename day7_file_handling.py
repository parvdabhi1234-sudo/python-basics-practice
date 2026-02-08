# Day 7 - File Handling

# 1. Write to a file

file = open("sample.txt", "w")
file.write("Hello, this is my first file handling program.\n")
file.write("Learning Python step by step.")
file.close()

# 2. Read file

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# 3. Append data

file = open("sample.txt", "a")
file.write("\nAppending new line.")
file.close()

print("Data written and appended successfully.")

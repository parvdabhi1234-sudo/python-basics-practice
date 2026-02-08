# Q1 Write numbers 1 to 10 into a file

file = open("numbers.txt", "w")

for i in range(1, 11):
    file.write(str(i) + "\n")

file.close()

# Q2 Read and print file content

file = open("numbers.txt", "r")
print(file.read())
file.close()

# Q3 Count lines in a file

file = open("numbers.txt", "r")
lines = file.readlines()
print("Total lines:", len(lines))
file.close()

# Q4 Sum of numbers from file

file = open("numbers.txt", "r")
nums = file.readlines()

total = 0
for n in nums:
    total += int(n.strip())

print("Sum:", total)

# Q5 Count words in file

file = open("sample.txt", "r")
text = file.read()

words = text.split()
print("Total words:", len(words))

file.close()
file.close()

# Day 3 Practice Questions

# Q1: Multiplication table of 5

for i in range(1, 11):
    print("5 x", i, "=", 5*i)

print()

# Q2: Countdown 10 to 1

for i in range(10, 0, -1):
    print(i)

print()

# Q3: Factorial of 5

num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)

print()

# Q4: Sum of even numbers 1 to 20

total = 0
for i in range(1, 21):
    if i % 2 == 0:
        total += i
print("Sum:", total)

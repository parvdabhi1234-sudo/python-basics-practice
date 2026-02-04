# Day 3 Learning — Loops

print("For loop 1 to 5")
for i in range(1, 6):
    print(i)

print("\nEven numbers from 1 to 10")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("\nSum of numbers 1 to 10")
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

print("\nWhile loop example")
num = 1
while num <= 5:
    print(num)
    num += 1

print("\nBreak example")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nContinue example")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

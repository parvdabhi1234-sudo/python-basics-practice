# Day 5 Practice - List & Tuple

# Q1 Second largest number in list

lst = [10, 25, 5, 40, 15]
lst.sort()
print("Second largest:", lst[-2])

# Q2 Count even and odd numbers

numbers = [1,2,3,4,5,6,7,8]
even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

# Q3 List comprehension divisible by 3

div3 = [x for x in range(1,31) if x%3==0]
print("Divisible by 3:", div3)

# Q4 Tuple min and max

t = (5, 15, 2, 30, 9)
print("Min:", min(t))
print("Max:", max(t))

# Q5 Convert list to tuple

my_list = [1,2,3,4]
converted = tuple(my_list)
print("Tuple:", converted)

# Question 1

# Count frequency of elements

nums = [1,2,2,3,3,3,4]
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)

# Question 2

# Remove duplicates using set

data = [1,2,2,3,4,4,5]
unique = list(set(data))
print(unique)

# Question 3

# Common elements in 2 lists

a = [1,2,3,4]
b = [3,4,5,6]

print(set(a) & set(b))

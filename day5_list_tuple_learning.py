# Day 7 Learning - List & Tuple

# LIST

nums = [10,20,30,40]
print("List:", nums)

# Indexing

print("First:", nums[0])
print("Last:", nums[-1])

# Append

nums.append(50)
print("After append:", nums)

# Slicing

print("Slice:", nums[1:4])

# List comprehension

squares = [x*x for x in nums]
print("Squares:", squares)


# TUPLE

t = (1,2,3,4)
print("Tuple:", t)

print("First element:", t[0])

# Tuple unpacking

a,b,c,d = t
print(a,b,c,d)

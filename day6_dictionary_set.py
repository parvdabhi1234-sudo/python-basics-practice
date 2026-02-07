# Dictionary basics

student = {
    "name": "Parv",
    "age": 20,
    "course": "AI/ML"
}

print("Name:", student["name"])

# Add & update

student["age"] = 21
student["city"] = "Ahmedabad"

print(student)

# Loop in dictionary

for key, value in student.items():
    print(key, ":", value)

# Set basics

nums = {1, 2, 3, 4}

nums.add(5)
nums.remove(2)

print("Set:", nums)

# Set operations

A = {1,2,3}
B = {3,4,5}

print("Union:", A | B)
print("Intersection:", A & B)

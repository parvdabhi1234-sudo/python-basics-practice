# Day 8 - JSON Learning

import json

# Python dictionary

student = {
    "name": "Parv",
    "age": 20,
    "skills": ["Python", "ML"]
}

# Convert dict to JSON & store in file

with open("student.json", "w") as file:
    json.dump(student, file)

print("JSON file created")

# Read JSON file

with open("student.json", "r") as file:
    data = json.load(file)

print("Read from JSON:", data)
print("Name:", data["name"])

# -------- Questions --------

# Q1 Create JSON of product

product = {"item": "Phone", "price": 20000}
with open("product.json", "w") as f:
    json.dump(product, f)

# Q2 Read and print price

with open("product.json", "r") as f:
    p = json.load(f)
print("Price:", p["price"])

# Q3 Store numbers list

nums = [1,2,3,4]
with open("nums.json", "w") as f:
    json.dump(nums, f)

# Q4 Read and sum

with open("nums.json", "r") as f:
    n = json.load(f)
print("Sum:", sum(n))

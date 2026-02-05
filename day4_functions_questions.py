# Day 4 Practice 

# Q1 Prime number check

def is_prime(num):
    if num < 2:
        return "Not Prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

print(is_prime(7))

# Q2 Factorial using function

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print("Factorial:", factorial(5))

# Q3 Count vowels in string

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print("Vowels:", count_vowels("Artificial Intelligence"))

# Q4 Largest number in list

def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print("Largest:", find_max([3, 7, 2, 9, 5]))

# Q5 Lambda — even or odd

check = lambda x: "Even" if x%2==0 else "Odd"
print(check(11))

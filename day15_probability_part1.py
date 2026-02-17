# ===== PROBABILITY PART 1 =====
# Topics covered:
# 1 Basics
# 2 Sample Space & Events
# 3 Rules
# 4 Conditional Probability

print("=== BASICS ===")

# 1) Basic Probability

# Coin head
print("P(Head):", 1/2)

# Dice getting 3
print("P(Getting 3):", 1/6)

print("\n=== SAMPLE SPACE ===")

# Sample space size

dice_space = {1,2,3,4,5,6}
print("Dice Sample Space:", dice_space)

# Event: even numbers

even_event = {2,4,6}
print("Even Event:", even_event)
print("P(Even):", len(even_event)/len(dice_space))

print("\n=== RULES ===")

# Range rule example

p = 0.4
print("Probability in range:", 0 <= p <= 1)

# Complement rule

print("Complement:", 1 - 0.4)


print("\n=== CONDITIONAL PROBABILITY ===")

# Example:
# King given face card
# Kings=4, Face cards=12
print("P(King|Face card):", 4/12)

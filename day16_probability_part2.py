# ===== PROBABILITY PART 2 =====
# Topics:
# 1 Bayes Theorem
# 2 Random Variables
# 3 Mean (Expected Value)
# 4 Variance & Std Dev

print("=== BAYES THEOREM ===")

# Example:

# Disease test
# P(D)=0.01
# P(Pos|D)=0.99
# P(Pos|NoD)=0.05

P_D = 0.01
P_Pos_D = 0.99
P_Pos_NoD = 0.05
P_NoD = 1 - P_D

bayes = (P_Pos_D * P_D) / ((P_Pos_D * P_D) + (P_Pos_NoD * P_NoD))
print("Bayes result:", bayes)

print("\n=== RANDOM VARIABLE ===")

# Dice random variable

outcomes = [1,2,3,4,5,6]
print("Random variable values:", outcomes)

print("\n=== MEAN (Expected Value) ===")

# Mean of dice

mean = sum(outcomes)/len(outcomes)
print("Mean:", mean)

print("\n=== VARIANCE ===")

var = sum((x-mean)**2 for x in outcomes)/len(outcomes)
print("Variance:", var)

std = var**0.5
print("Standard Deviation:", std)

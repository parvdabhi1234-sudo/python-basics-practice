print("\n=== PRACTICE QUESTIONS ===")

# Q1 Mean of [2,4,6]

data = [2,4,6]
print("Q1 Mean:", sum(data)/len(data))

# Q2 Variance of [1,2,3]

d=[1,2,3]
m=sum(d)/len(d)
print("Q2 Variance:", sum((x-m)**2 for x in d)/len(d))

# Q3 Std Dev

print("Q3 Std Dev:", (sum((x-m)**2 for x in d)/len(d))**0.5)

# Q4 Random variable example (coin)

print("Q4 Random Variable:", ["H","T"])

# Q5 Bayes simple example

# P(A)=0.5 P(B|A)=0.8 P(B)=0.6
print("Q5 Bayes:", (0.8*0.5)/0.6)

print("\n--- Day 16 Probability Part 2 Complete ---")

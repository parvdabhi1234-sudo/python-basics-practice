import numpy as np

# Q1 Even numbers from 1–20

arr = np.arange(1,21)
even = arr[arr%2==0]
print("Q1 Even:", even)

# Q2 Diagonal sum

mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print("Q2 Diagonal Sum:", np.trace(mat))

# Q3 Random mean

r = np.random.randint(1,100,10)
print("Q3 Random:", r)
print("Mean:", np.mean(r))

# Q4 Element-wise multiply

a = np.array([1,2,3])
b = np.array([4,5,6])
print("Q4 Multiply:", a*b)

# Q5 Max index in 5x5 matrix

m = np.random.randint(1,50,(5,5))
print("Matrix:\n", m)
print("Max index:", np.unravel_index(np.argmax(m), m.shape))

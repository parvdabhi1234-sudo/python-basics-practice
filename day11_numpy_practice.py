import numpy as np

# Create arrays

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# Shape

print("Shape:", arr2.shape)

# Mathematical operations

print("Mean:", np.mean(arr1))
print("Sum:", np.sum(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))

# Indexing & slicing

print("First element:", arr1[0])
print("Slice:", arr1[1:4])

# Random numbers

rand = np.random.randint(1, 100, 5)
print("Random Array:", rand)

# Reshape

reshaped = np.reshape(arr1, (5,1))
print("Reshaped:\n", reshaped)

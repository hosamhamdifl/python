import numpy as np

# Read the shape of the array from the first line of input
shape = tuple(map(int, input().split()))

# Create an array of zeros with the given shape
zeros_array = np.zeros(shape, dtype=int)

# Create an array of ones with the given shape
ones_array = np.ones(shape, dtype=int)

# Print the resulting arrays
print(zeros_array)
print(ones_array)

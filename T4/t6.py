import numpy as np

def read_matrix(name):
    rows = int(input(f"How many rows in matrix {name}? "))
    cols = int(input(f"How many columns in matrix {name}? "))
    print(f"Enter the elements of matrix {name}:")
    elements = []

    # value setter
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Value for [{i}, {j}]: "))
            row.append(val)
        elements.append(row)

    return np.array(elements)

def merge_and_sort_matrices(mat1, mat2):
    # convert matrix to list , [[1,2],[3,4]] -> [1,2,3,4]
    flat1 = mat1.flatten() 
    flat2 = mat2.flatten()

    # Concatenate and sort
    merged = np.concatenate((flat1, flat2)) # merge to list
    merged.sort()

    return merged

# Get two matrices
mat1 = read_matrix("A")
mat2 = read_matrix("B")

# Merge and sort
result = merge_and_sort_matrices(mat1, mat2)

print("Final sorted array:")
print(result)

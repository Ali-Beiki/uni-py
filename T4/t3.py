row = int(input(f" Enter Count Row :"))
column = int(input(f" Enter Count Column :"))

matrix =[]

# data seter
for row_index in range(row):
    row_data =[]
    for column_index in range(column):
        value = int(input(f"Entet Number [{row_index}][{column_index}]"))
        row_data.append(value)
    matrix.append(row_data)

print("matrix :",matrix)

# transposed matrix
transposed_matrix =[]

for column_index in range(column):
    row_data =[]
    for row_index in range(row):
        row_data.append(matrix[row_index][column_index])
    transposed_matrix.append(row_data)


print("transposed matrix :",transposed_matrix)
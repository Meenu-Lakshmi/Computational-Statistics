matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat_list_by_row = [elem for row in matrix for elem in row]
print("Flatten by row:", flat_list_by_row)

flat_list_by_column = [matrix[row][col] for col in range(len(matrix[0])) for row in range(len(matrix))]
print("Flatten by column:", flat_list_by_column)

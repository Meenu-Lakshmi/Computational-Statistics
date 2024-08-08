def read_sparse_matrix():
    matrix = {}
    rows = int(raw_input("Enter row count: "))
    cols = int(raw_input("Enter column count: "))
    print("Enter matrix elements: ")
    for i in range(rows):
        for j in range(cols):
            value = int(raw_input("Value at (" + str(i) + "," + str(j) + "): "))
            if value != 0:
                matrix[(i, j)] = value
    print("sparse matrix dictionary : ",matrix)
    return matrix, rows, cols

def display_sparse_matrix(matrix, rows, cols):
    print("Sparse matrix:")
    for i in range(rows):
        row = ""
        for j in range(cols):
            if (i, j) in matrix:
                row+=str(matrix[(i, j)]) + " "
            else:
                row+=" 0 "
        print(row)

sparse_matrix, rows, cols = read_sparse_matrix()

display_sparse_matrix(sparse_matrix, rows, cols)


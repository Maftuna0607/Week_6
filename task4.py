def transpose_matrix(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
    list_2=[]
    for i in range(columns):
        row_list=[]
        for j in range(rows):
            row_list.append(matrix[j][i])
        list_2.append(row_list)
    return list_2



matrix_3x2 = [
	[1, 2],
	[3, 4],
	[5, 6]
]
# Expected Output (a 2x3 matrix):
# [
#   [1, 3, 5],
#   [2, 4, 6]
# ]
print(transpose_matrix(matrix_3x2))
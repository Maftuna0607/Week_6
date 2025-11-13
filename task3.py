def sum_diagonals(matrix):
    n=len(matrix)
    d_1_sum=0
    d_2_sum=0
    mid_elem=0
    for i in range(n):
        d_1_sum += matrix[i][i]
        d_2_sum += matrix[i][-i-1]
        if n % 2 == 1:
            mid_index= n//2 
            mid_elem= matrix[mid_index][mid_index]
        return d_1_sum + d_2_sum - mid_elem 
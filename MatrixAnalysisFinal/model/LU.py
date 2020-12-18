# -*- coding:UTF-8 -*-
import numpy as np
import os
from utils.matrixFromFile import load_array
from utils import auxiliary

path = os.getcwd()

def LU_factorization(mat):
    # A = PLU 分解
    m, n = mat.shape
    mat_B = mat.copy()
    for row in range(m-1):# LU分解加了一列标记行变换
        curr_col = np.abs(mat[row:,row])
        max_item = np.max(curr_col)
        if curr_col[0] != max_item:
            max_row_idx = np.where(curr_col == max_item)[0][0] + row
            mat[row] = mat_B[max_row_idx]
            mat[max_row_idx] = mat_B[row]

        for i in range(row+1, m):
            factor = mat[i,row] / mat[row,row]
            mat[i, row] = factor
            value = (-1 * factor * mat[row, row+1:-1])
            mat[i, row+1:-1] += value

        mat_B = mat.copy()

    # 输出上三角阵和下三角阵
    U = np.triu(mat[:, :-1], 0)
    for k in range(m):
        mat_B[k, k] =1
    L = np.tril(mat_B[:,:-1], 0)
    P = np.zeros(shape=(m,n-1))
    for idx in range(m):
        row_idx = int(mat[idx, -1])
        P[idx, row_idx-1] = 1
    return L, U, P

if __name__ == "__main__":
    input_file = "../data/LU.txt"
    matrix = load_array(input_file, "LU")
    m, n = matrix.shape
    # matrix.size == m*n
    print("The input Matrix：")
    auxiliary.print_array(matrix)

    L, U, P = LU_factorization(matrix)
    print("The factorization Results：")
    print("Matrix L:")
    auxiliary.print_array(L)
    print("Matrix U:")
    auxiliary.print_array(U)
    print("Matrix P:")
    auxiliary.print_array(P)
    print("Matrix PLU:")  # 验证结果是否正确
    print(P.dot(L).dot(U))


# -*- coding:UTF8 -*-
import numpy as np

# 打印矩阵
np.set_printoptions(precision=4, suppress=True)
def print_array(mat):
    m, n = mat.shape
    for i in range(m):
        for j in range(n):
            print("%8.4f" % mat[i, j], end=',')
        print()

# 计算矩阵的秩，主元高斯消去法
def rank_of_matrix(mat):
    m, n = mat.shape
    mat = mat.copy()
    row = col = 0
    while row < m - 1 and col < n:
        curr_col = np.abs(mat[row:, col])
        max_item = np.max(curr_col)
        if np.all(curr_col == 0):
            col += 1
            continue
        if curr_col[0] != max_item:  # 行交换
            max_row_idx = np.where(curr_col == max_item)[0][0] + row
            helper = mat[max_row_idx].copy()
            mat[max_row_idx] = mat[row]
            mat[row] = helper

        for i in range(row + 1, m):
            if np.all(mat[i] == 0):
                break
            factor = mat[i, col] / mat[row, col]
            value = (-1 * factor * mat[row, col:])
            mat[i, col:] += value
            for j in range(0, n):  # 为了保证数值稳定性
                if abs(mat[i, j]) < 1e-12:
                    mat[i, j] = 0.

        col += 1
        row += 1

    zero_rows = 0
    for x in mat[::-1]:  # 最后一行开始逐行检查0行
        # print(x)
        if np.all(abs(x) < 1e-12):
            # print("True")
            zero_rows += 1
            continue
        # break
    mat_rank = min(n, m - zero_rows)
    return mat_rank

def rankOfMatrix(mat):
    return np.linalg.matrix_rank(mat)
if __name__ == "__main__":
    M = np.array([
        [1., 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 13],
        [9, 10, 11., 12]
    ])
    M2 = np.array([
        [1., 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ])
    m, n = M.shape
    print(rank_of_matrix(M), np.linalg.matrix_rank(M))

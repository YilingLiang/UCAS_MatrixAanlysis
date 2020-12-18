
import numpy as np
import sys,os
import math

from utils.matrixFromFile import load_array
from utils import auxiliary

path = os.getcwd()

def givens_rotation(A):
    """Givens变换"""
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    (rows, cols) = np.tril_indices(r, -1, c)
    for (row, col) in zip(rows, cols):
        if R[row, col] != 0:  # R[row, col]=0 则 c=1,s=0,R、Q不变
            r_ = np.hypot(R[col, col], R[row, col])  # d
            c = R[col, col]/r_
            s = -R[row, col]/r_
            # 每次构造旋转矩阵 G
            G = np.identity(r)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s
            R = np.dot(G, R)  # R=G(n-1,n)*...*G(2n)*...*G(23,1n)*...*G(12)*A
            Q = np.dot(Q, G.T)  # Q=G(n-1,n).T*...*G(2n).T*...*G(23,1n).T*...*G(12).T
    return Q, R

if __name__ == "__main__":
    input_file = "../data/Givens.txt"
    matrix= load_array(input_file, "Givens")

    print("The input Matrix：")
    auxiliary.print_array(matrix)

    Q, R = givens_rotation(matrix)
    print("The factorization Results：")
    print("Matrix Q:")
    auxiliary.print_array(Q)
    print("Matrix R:")
    auxiliary.print_array(R)

    print("Matrix QR:")# 验证结果是否正确
    print(np.dot(Q, R), "\n")
    # print(Q.dot(R))
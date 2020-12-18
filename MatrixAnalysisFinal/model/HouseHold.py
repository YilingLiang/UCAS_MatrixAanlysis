import numpy as np
import sys, os
import math

from utils.matrixFromFile import load_array
from utils import auxiliary

path = os.getcwd()


def householder_reflection(A):
    """Householder镜面对称变换"""
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    for cnt in range(r - 1):
        x = R[cnt:, cnt]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        v = u / np.linalg.norm(u)
        Q_cnt = np.identity(r)
        Q_cnt[cnt:, cnt:] -= 2.0 * np.outer(v, v)
        R = np.dot(Q_cnt, R)  # R=H(n-1)*...*H(2)*H(1)*A
        Q = np.dot(Q, Q_cnt)  # Q=H(n-1)*...*H(2)*H(1)  H为自逆矩阵
    return Q, R


if __name__ == "__main__":
    input_file = "../data/Household.txt"
    matrix = load_array(input_file, "HH")

    m, n = matrix.shape
    # matrix.size == m*n
    print("The input Matrix：")
    auxiliary.print_array(matrix)

    Q, R = householder_reflection(matrix)
    print("The factorization Results：")
    print("Matrix Q:")
    auxiliary.print_array(Q)
    print("Matrix R:")
    auxiliary.print_array(R)

    print("Matrix QR:")  # 验证结果是否正确
    print(np.dot(Q, R), "\n")
    # print(Q.dot(R))
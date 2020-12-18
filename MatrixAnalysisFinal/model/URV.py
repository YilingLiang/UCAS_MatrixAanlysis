# -*- coding:UTF-8 -*-
import numpy as np
import sys,os
from model.Gram_Schmidt import gram_schmidt
from utils.matrixFromFile import load_array
from utils import auxiliary
from scipy.linalg import null_space, orth

path = os.getcwd()

def URV_factorization(A):
    m, n = A.shape
    r = auxiliary.rankOfMatrix(A)
    
    NAT = null_space(A.T) #求矩阵A转置的零空间
    NA = null_space(A) #求矩阵A的零空间

    Q1 = orth(A) # R(A) 的标准正交基
    NAT,_ = gram_schmidt(NAT)
    # NAT = orth(NAT)
    U = np.column_stack((Q1[:,:r], NAT[:,:]))#构成 U
    # print(Q1.shape, NAT.shape, U.shape)

    Q2 = orth(A.T)#矩阵A转置的标准正交基
    # NA, _ = gram_schmidt(NA)
    NA = orth(NA)
    V = np.column_stack((Q2[:,:r], NA[:,:]))#构成 V
    # print(Q2.shape, NA.shape, V.shape)

    R1 = np.dot(U.T, A)
    R = np.dot(R1, V)# R=U^T*A*V
    return U, R, V
if __name__ == "__main__":
    input_file="../data/URV.txt"
    # output_file=''
    matrix = load_array(input_file,"URV")
    print("Matrix A:")
    auxiliary.print_array(matrix)
    if matrix.size ==0:
        print("input Error!")
        sys.exit()
    r = auxiliary.rank_of_matrix(matrix)

    U,R,V = URV_factorization(matrix)
    print("Factoriaztion results:")
    print("Matrix U:")
    auxiliary.print_array(U)
    print("Matrix R:")
    auxiliary.print_array(R)
    print("Matrix V:")
    auxiliary.print_array(V)
    print("Matrix URV:")
    auxiliary.print_array(U.dot(R).dot(V.T))
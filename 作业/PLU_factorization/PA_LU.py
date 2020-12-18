import numpy
from scipy import linalg

A = [[1,2,4,17],
     [3,6,-12,3],
     [2,3,-3,2],
     [0,2,-2,6]]

# PA=LU
p_inv, L, U = linalg.lu(A)
print(L)
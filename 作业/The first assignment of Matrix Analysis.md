### The first assignment of Matrix Analysis 

#### Slide2 Exercises 6

**Solution：** **(a)** 3-digit arithmetic without pivoting:
$$
\left(\begin{array}{cc|c}
10^{-3} & -1 &   1 \\
1 & 1 & 0
\end{array}\right)_{R_{2}-10^{3} R_{1}} \longrightarrow
\left(\begin{array}{cc|c}
10^{-3} & -1 & 1 \\
0 & \boxed{10^{3}} & -10^{3}
\end{array}\right)
$$
Cause when keeping three significant figures:
$$
float(1+10^3)=float(0.1001\times 10^4)\mathop{\longrightarrow}^{3-digit} 0.100 \times 10^4=10^3
$$
Back substitution, then we get the answer:
$$
x=0,y=-1
$$
**(b)** 3-digit arithmetic with pivoting:
$$
\left(\begin{array}{cc|c}
10^{-3} & -1 &   1 \\
1 & 1 & 0
\end{array}\right)_{swap\ rows} \mathop{\longrightarrow}
\left(\begin{array}{cc|c}
1 & 1 & 0 \\
10^{-3} & -1 &   1 
\end{array}\right)_{R_{2}-10^{-3} R_{1}} \longrightarrow
\left(\begin{array}{cc|c}
1 & 1 & 0 \\
0 & \boxed{-1} &   1 
\end{array}\right)
$$
Cause when keeping three significant figures:
$$
float(-1-10^{-3})=float(-0.1001\times 10^1)\mathop{\longrightarrow}^{3-digit}-0.100\times 10^1=-1
$$
Back substitution, then we get the answer:
$$
x=1,y=-1
$$


#### Slide3 Exercises 4 

**Solution:** **(a)** Transform the augmented matrix $[\mathbf{A}|b]$ as follows:
$$
[\mathbf{A}|b]=\left(\begin{array}{cccc|c}
1 & 2 & 1 & 2 & 3 \\
2 & 4 & 1 & 3 & 4 \\
3 & 6 & 1 & 4 & 5 
\end{array}\right) \rightarrow
\left(\begin{array}{cccc|c}
1 & 2 & 1 & 2 & 3 \\
0 & 0 & -1 & -1 & -2 \\
0 & 0 & -2 & -2 & -4 
\end{array}\right) \\ \rightarrow
\left(\begin{array}{cccc|c}
1 & 2 & 1 & 2 & 3 \\
0 & 0 & -1 & -1 & -2 \\
0 & 0 & 0 & 0 & 0 
\end{array}\right) \rightarrow
\left(\begin{array}{cccc|c}
1 & 2 & 0 & 1 & 1 \\
0 & 0 & 1 & 1 & 2 \\
0 & 0 & 0 & 0 & 0 
\end{array}\right)
$$
Obviously, the rank of $\mathbf{A}$ is equal to the rank of $[\mathbf{A}|b]$, so this system is consistent.

The fundamental set of solutions for the corresponding homogeneous system ($\mathbf{A}x=0$) is:
$$
\xi_1=(1,-1,-1,1)^T,\xi_2=(2,-1,0,0)^T
$$
A particular solution for the nonhomogeneous system is:
$$
\eta=(0,0,1,1)^T
$$
So the general solution for the nonhomogeneous system is:
$$
x=\eta + k_1\xi_1+ k_2\xi_2,k_i \in R,i=1,2
$$



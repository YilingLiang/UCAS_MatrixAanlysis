### The second assignment of Matrix Analysis

#### Slide4 Exercises11

**Solution：(a) **Suppose $PA=LU$，$P$ is the row permutation matrix.
$$
[A|p]=\left(
\begin{array}{rrrr|r}
1 & 2 & 4 & 17 & 1\\
3 & 6 & -12 & 3 & 2\\
2 & 3 & -3 & 2 & 3\\
0 & 2 & -2 & 6 & 4
\end{array}
\right)\rightarrow
\left(
\begin{array}{rrrr|r}
3 & 6 & -12 & 3 & 2\\
1 & 2 & 4 & 17 & 1\\
2 & 3 & -3 & 2 & 3\\
0 & 2 & -2 & 6 & 4
\end{array}
\right)\rightarrow \\
\left(
\begin{array}{rrrr|r}
3 & 6 & -12 & 3 & 2\\
\mathbf{1/3} & 0 & 8 & 16 & 1\\
\mathbf{2/3} & -1 & 5 & 0 & 3\\
\mathbf{0} & 2 & -2 & 6 & 4
\end{array}
\right)\rightarrow
\left(
\begin{array}{rrrr|r}
3 & 6 & -12 & 3 & 2\\
\mathbf{0} & 2 & -2 & 6 & 4 \\
\mathbf{2/3} & -1 & 5 & 0 & 3\\
\mathbf{1/3} & 0 & 8 & 16 & 1\\
\end{array}
\right)\rightarrow \\
\left(
\begin{array}{rrrr|r}
3 & 6 & -12 & 3 & 2\\
\mathbf{0} & 2 & -2 & 6 & 4 \\
\mathbf{2/3} & \mathbf{-1/2} & 4 & 3 & 3\\
\mathbf{1/3} & \mathbf{0} & 8 & 16 & 1\\
\end{array}
\right)\rightarrow
\left(
\begin{array}{rrrr|r}
3 & 6 & -12 & 3 & 2\\
\mathbf{0} & 2 & -2 & 6 & 4 \\
\mathbf{1/3} & \mathbf{0} & 8 & 16 & 1\\
\mathbf{2/3} & \mathbf{-1/2} & 4 & 3 & 3\\
\end{array}
\right)\rightarrow \\
\left(
\begin{array}{rrrr|r}
3 & 6 & -12 & 3 & 2\\
\mathbf{0} & 2 & -2 & 6 & 4 \\
\mathbf{1/3} & \mathbf{0} & 8 & 16 & 1\\
\mathbf{2/3} & \mathbf{-1/2} & \mathbf{1/2} & -5 & 3\\
\end{array}
\right)
$$
Therefore，
$$
P=\left(
\begin{array}{rrrr}
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0\\
0 & 0 & 1 & 0\\
\end{array}
\right),
L=\left(
\begin{array}{rrrr}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
1/3 & 0 & 1 & 0\\
2/3 & -1/2 & 1/2 & 1\\
\end{array}
\right),
U=\left(
\begin{array}{rrrr}
3 & 6 & -12 & 3 \\
0 & 2 & -2 & 6 \\
0 & 0 & 8 & 16\\
0 & 0 & 0 & -5\\
\end{array}
\right),
$$
**(b)** The system $Ax = b$ is equivalent to  $PAx=Pb$ . In **(a)** we have already performed the factorization $PA = LU$ , then we can solve $Ly = Pb$ for $y$ by forward substitution：
$$
\left(
\begin{array}{rrrr}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
1/3 & 0 & 1 & 0\\
2/3 & -1/2 & 1/2 & 1\\
\end{array}
\right)
\left(
\begin{array}{c}
y_1 \\ y_2 \\ y_3 \\ y_4 \\
\end{array}
\right) = 
\left(
\begin{array}{c}
3 \\ 4 \\ 17 \\ 3 \\
\end{array}
\right)\Longrightarrow
y=\left(
\begin{array}{c}
y_1 \\ y_2 \\ y_3 \\ y_4 \\
\end{array}
\right)=\left(
\begin{array}{c}
3 \\ 4 \\ 16 \\ -5 \\
\end{array}
\right)
$$
and then solve $Ux = y$ by back substitution：
$$
\left(
\begin{array}{rrrr}
3 & 6 & -12 & 3 \\
0 & 2 & -2 & 6 \\
0 & 0 & 8 & 16\\
0 & 0 & 0 & -5\\
\end{array}
\right)\left(
\begin{array}{c}
x_1 \\ x_2 \\ x_3 \\ x_4 \\
\end{array}
\right) = \left(
\begin{array}{c}
3 \\ 4 \\ 16 \\ -5 \\
\end{array}
\right) \Longrightarrow
x=\left(
\begin{array}{c}
x_1 \\ x_2 \\ x_3 \\ x_4 \\
\end{array}
\right)=\left(
\begin{array}{c}
2 \\ -1 \\ 0 \\ 1 \\
\end{array}
\right)
$$



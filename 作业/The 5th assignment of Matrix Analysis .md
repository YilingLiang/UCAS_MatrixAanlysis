### 矩阵分析第五次作业

#### 课件7 Exercises 3

**解： ** 

$A^TA=4A$ 的特征值为 $0,10$，故：
$$
\begin{align}
||A||_F&=1^2+(-2)^2+(-1)^2+2^2=10\\
||A||_1&=max\{1+1,2+2\}=4\\
||A||_2&=max\{\sqrt{10},0\}=\sqrt{10}\\
||A||_{\infty}&=max\{1+2,1+2\}=3\\
\end{align}
$$

$B^TB=I$ 的特征值为 $1,1,1$，故：
$$
\begin{align}
||B||_F&=1^2+1^2+1^2=3\\
||B||_1&=max\{1+0+0,0+1+0,0+0+1\}=1\\
||B||_2&=max\{1,1,1\}=1\\
||B||_{\infty}&=max\{1+0+0,0+1+0,0+0+1\}=1\\
\end{align}
$$

$C^TC=9C$ 的特征值为 $0,0,81$，故：
$$
\begin{align}
||C||_F&=2\cdot (4^2+(-2)^2+4^2)+(-2)^2+1^2+(-2)^2=81\\
||C||_1&=max\{4+2+4,2+1+2,4+2+4\}=10\\
||C||_2&=max\{0,0,9\}=9\\
||C||_{\infty}&=max\{4+2+4,2+1+2,4+2+4\}=10\\
\end{align}
$$

#### 课件7 Exercises 12

**解： (a)** 设 $A=(\alpha_1,\alpha_2,\alpha_3)=QR =(q_1,q_2,q_3)\cdot R$，对 $A$ 列向量进行 Schmidt 正交化为 $q_1,q_2,q_3$ 
$$
\begin{align}
q_1&=\frac{\alpha_1}{||\alpha_1||}=(\frac{1}{\sqrt{3}},\frac{1}{\sqrt{3}},\frac{1}{\sqrt{3}},0)^T\\
q_2&=\frac{\alpha_2-( q_1\alpha_2)q_1}{||\alpha_2-(q_1\alpha_2)q_1||}=
(\frac{-1}{\sqrt{3}},\frac{1}{\sqrt{3}},0,\frac{1}{\sqrt{3}})^T\\
q_3&=\frac{\alpha_3-(q_1\alpha_3 )q_1-(q_2\alpha_3 )q_2}{||\alpha_3-(q_1\alpha_3 )q_1-(q_2\alpha_3 )q_2||}=(\frac{1}{\sqrt{6}},\frac{1}{\sqrt{6}},\frac{-2}{\sqrt{6}},0)^T
\end{align}
$$
所以
$$
(\alpha_1,\alpha_2,\alpha_3)=QR=(q_1,q_2,q_3)\cdot\left(
\begin{array}{rrr}
\sqrt{3} & \sqrt{3} & -\sqrt{3}\\
0 & \sqrt{3} & \sqrt{3}\\
0 & 0 & \sqrt{6}
\end{array}
\right)
$$
其中
$$
Q=\left(
\begin{array}{rrr}
\frac{1}{\sqrt{3}} & \frac{-1}{\sqrt{3}} & \frac{1}{\sqrt{6}}\\
\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}}\\
\frac{1}{\sqrt{3}} & 0 & \frac{-2}{\sqrt{6}}\\
0 & \frac{1}{\sqrt{3}} & 0\\
\end{array}
\right)
$$
**(b)** 方程 $Ax=x$ 即 $ QRx=b$ ，将方程两边乘 $Q^T$ ，则最小二乘方程化为 $Rx=Q^Tb$
$$
\begin{align}
\left(
\begin{array}{rrr}
\sqrt{3} & \sqrt{3} & -\sqrt{3}\\
0 & \sqrt{3} & \sqrt{3}\\
0 & 0 & \sqrt{6}
\end{array}
\right)\left(
\begin{array}{r}
x_1\\
x_2\\
x_3
\end{array}
\right)=\left(\begin{array}{r}
\sqrt{3}\\
\frac{1}{\sqrt{3}}\\
0
\end{array}
\right)
\end{align}
$$
解得
$$
\begin{align}
\left(
\begin{array}{r}
x_1\\
x_2\\
x_3
\end{array}
\right)=\left(\begin{array}{r}
\frac{2}{3}\\
\frac{1}{3}\\
0
\end{array}
\right)
\end{align}
$$

#### 课件7 Exercises 16

**解：** 

**(a)**  $\frac{vv^T}{v^Tv}u=(\frac{1}{6},\frac{2}{3},0,\frac{-1}{6})^T$ 

**(b)**  $\frac{uu^T}{u^Tu}v=(\frac{-2}{5},\frac{1}{5},\frac{3}{5},\frac{-1}{5})^T$

**(c)**  $(I-\frac{vv^T}{v^Tv})u=(\frac{-13}{6},\frac{1}{3},3,\frac{-5}{6})^T$ 

**(d)**  $(I-\frac{uu^T}{u^Tu})v=(\frac{7}{5},\frac{19}{5},\frac{-3}{5},\frac{-4}{5})^T$  
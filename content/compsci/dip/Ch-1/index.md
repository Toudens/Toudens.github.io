---
title: Ch-1 图像的基本属性
weight: "1"
type: docs
date: 2026-04-10
---
像素

$$
\begin{align}
&
\begin{bmatrix}Y\\U\\V\end{bmatrix}=
\begin{bmatrix}
0.299 & 0.587 & 0.114\\
-0.147&-0.289 & 0.435\\
0.615 &-0.515 & -0.100
\end{bmatrix}\cdot
\begin{bmatrix}
R\\G\\B
\end{bmatrix}\\
&
\begin{bmatrix}R\\G\\B\end{bmatrix}=
\begin{bmatrix}
1 & 0 & 1.4075\\
1 & -0.3455 & -0.7169\\
1 & 1.779 & 0
\end{bmatrix}
\cdot
\begin{bmatrix}
Y\\U\\V
\end{bmatrix}
\end{align}
$$


```C
struct TIFF_img{
	unsigned char **mono;
	unsigned char **cmap;
	unsigned char ***color;
	char TIFF_type;
	char compress_type;
	int  height;
	int  width;
} 
```

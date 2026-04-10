---
title: Ch-1 图像的基本属性
weight: "1"
type: docs
date: 2026-04-10
---
$$
\begin{bmatrix}
Y\\U\\V
\end{bmatrix}
=
\begin{bmatrix}
0.299 & 0.587 & 0.114\\
-0.147&-0.289 & 0.435\\
0.615 &-0.515 & -0.100
\end{bmatrix}
\begin{bmatrix}
R\\G\\B
\end{bmatrix}
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
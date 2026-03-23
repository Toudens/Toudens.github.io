$$
\begin{align}
&\text{Average memory access time}\\
=&\text{Hit time}_\text{L1}+\text{Miss rate}_\text{L1}\times\text{Miss penalty}_\text{L1}\\
=&\text{Hit time}_\text{L1}+\text{Miss rate}_\text{L1}\times(\text{Hit time}_\text{L2}+\text{Miss rate}_\text{L2}\times\text{Miss penalty}_\text{L2})
\end{align}
$$
$$
\begin{align}
&\text{Average mem stalls per instruction}\\
=&\text{Misses per instruction}_\text{L1}\times\text{Hit time}_\text{L2}+\text{Misses per instruction}_\text{L2}\times\text{Miss penalty}_\text{L2}
\end{align}
$$

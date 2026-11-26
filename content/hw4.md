3240102910 朱航逸 2026.11.21
___
(1) Pure ALOHA has a maximum normalized throughput of $1/2e$ . Therefore, the maximum useful data rate is:
$$
56000/2e\approx10300.62\text{ bit/s}
$$
Each station generates $1000/100=10\text{ bit/s}$ . Thus:
$$
N_\text{max}=\left\lfloor\frac{10300.64}{10}\right\rfloor=1030
$$
___
(2)

|  0  |  0  |  0  |  1  |  1  |  1  |  0  |  1  |  0  |  1  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| LH  | LH  | LH  | HL  | HL  | HL  | LH  | HL  | LH  | HL  |
```
__|‾‾|__|‾‾|__|‾‾‾‾|__|‾‾|__|‾‾|____|‾‾‾‾|____|‾‾‾‾|__
```
___
(3) For collision detection, the sender must still be transmitting when a collision signal from the farthest end returns. Thus, the frame transmission time must be at least the round-trip propagation delay:
$$
2T_p=2\times\frac{1}{200000}=10\mu s
$$
The minimum frame size is:
$$
L_\text{min}=10^9\times10^{-5}=10000\text{ bits}=1250\text{ bytes}
$$
___
(4) Standard 10-Mbps Ethernet uses Manchester encoding, which represents each data bit using two half-bit signal elements. Therefore:
$$
\text{Baud rate}=2\times10^7=20\text{ Mbaud}
$$
___
(5) C
As collisions accumulate, the algorithm increases the random backoff range, reducing the probability of repeated collisions. Under light load, the range remains small. Therefore, it adapts to the network load.
___
(6) B
$$
\max_n\{2^{\min\{n,10\}}-1\}=1023
$$
___
(7) B
Hubs operate at the physical layer by repeating and regenerating signals. Ordinary Layer 2 switches forward frames based on MAC addresses and operate at the data link layer.
___
(8) C


Each switch port provides an independent 10-Mbps link, so each computer has a link rate of 10 Mbps. Actual application throughput also depends on the destination and other network bottlenecks.
___
(9) D
Bridges separate collision domains, connect network segments, and can improve effective network throughput by reducing unnecessary traffic and collisions.
___
(10) C
The F in the question denotes fiber optics. 
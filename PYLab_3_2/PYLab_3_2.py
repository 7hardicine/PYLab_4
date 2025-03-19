import numpy as np
import matplotlib.pyplot as plt
import math as m

xn = float(input("Input the value of xn: "))
xk = float(input("Input the value of xk: "))
dx = float(input("Input the value of dx: "))

X1 = np.arange(xn, xk, dx)
size = len(X1)
Y1 = np.zeros(size)

for i in range(size):
    Y1[i] = 50 * np.cos((X1[i])**2 + 2*X1[i] + 2)

xn = float(input("Input the value of xn: "))
xk = float(input("Input the value of xk: "))
N = int(input("Input the value of N: "))
while N < 20:
    N = int(input("Something went wrong, N must be bigger than 30, try again: "))

X2 = np.linspace(xn, xk, N)
Y2 = np.zeros(N)
for i in range (N):
    Y2[i] = m.exp(X2[i]) * m.sin(X2[i]) * m.cos(X2[i])

plt.figure(1)
plt.grid(True)
plt.title("Cool graphics :)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["f1","f2"])
plt.plot(X1,Y1, color="blue")
plt.plot(X2, Y2, linestyle = '--')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

xn = float(input("Input the value of xn: "))
xk = float(input("Input the value of xk: "))
dx = float(input("Input the value of dx: "))

X1 = np.arange(xn, xk, dx)
Y1 = 50 * np.cos((X1)**2 + 2*X1 + 2)

xn = float(input("Input the value of xn: "))
xk = float(input("Input the value of xk: "))
N = int(input("Input the value of N: "))
while N < 20:
    N = int(input("Something went wrong, N must be bigger than 30, try again: "))

X2 = np.linspace(xn, xk, N)
Y2 = np.exp(X2) * np.sin(X2) * np.cos(X2)

plt.figure(1)
plt.grid(True)
plt.title("Cool graphics :)")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X1,Y1, "--*b")
plt.plot(X2, Y2, "--sr")
plt.legend(["y1","y2"])
plt.show()
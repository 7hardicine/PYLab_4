import numpy as np
import matplotlib.pyplot as plt

xn = float(input("Input the value of xn: "))
xk = float(input("Input the value of xk: "))
dx = float(input("Input the value of dx: "))

x = np.arange(xn,xk,dx)
size = len(x)
y = np.zeros(size)

for i in range(size):
    if x[i] > 5: 
        y[i] = 1 - 3*x[i]
    elif x[i] <= 5 and x[i] >= -5:
        y[i] = x[i] - 5 * np.sin(x[i])
    else: 
        y[i] = x[i]**2

plt.figure(1)
plt.grid(True)
plt.title("Less cool graphic :(")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
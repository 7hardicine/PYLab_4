from ast import Delete
import numpy as np
import matplotlib.pyplot as plt

tn = float(input("Input the value of tn: "))
tk = float(input("Input the value of tk: "))
dt = float(input("Input the value of dt: "))  
Yp = float(input("Input the value of Yp: "))

t = np.arange(tn,tk,dt)

x = 11 * np.cos(2*t)*(1 + np.cos(2*t))
y = 11 * np.sin(2*t)*(1 + np.cos(2*t))
size = len(y)

stop = 0
for i in range(size):
    if y[i] <= Yp:
        stop = i

plt.figure(1)
plt.grid(True)
plt.title("Good graphic :|")
plt.plot(x,y, "r")
plt.axhline(Yp, color="blue", linestyle="--")
plt.plot(x[stop], y[stop], "--sb")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
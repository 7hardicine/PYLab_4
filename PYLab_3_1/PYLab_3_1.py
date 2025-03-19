import numpy as np
import matplotlib.pyplot as plt
import math as m

a = float(input("Input the value of a: "))
b = float(input("Input the value of b: "))
N = int(input("Input the value of N: "))
while N < 30:
    N = int(input("Something went wrong, N must be bigger than 30, try again: "))

x = np.linspace(a, b, N)
y = np.zeros(N)

for i in range (N):
    y[i] = 1 - m.cos(2*x[i]) - m.log(x[i])

plt.figure(1)
plt.plot(x,y)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

a = float(input("Input the value of a: "))
b = float(input("Input the value of b: "))
N = int(input("Input the value of N: "))
while N < 30:
    N = int(input("Something went wrong, N must be arrays can be bigger than 30, try again: "))

x = np.linspace(a, b, N)
y = 1 - np.cos(2*x) - np.log(x)

plt.figure(1)
plt.plot(x,y)
plt.show()
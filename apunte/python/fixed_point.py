import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

xs = np.linspace(-1, 2.5, 200)
fs = np.cos(xs)

x_0 = 0
N = 100
ptos = [(x_0, f(x_0))]

for i in range(0, N):
    if i == 0:
        result = x_0
    result = f(result)
    ptos.append((result, f(result)))

xz, yz = zip(*ptos)
indices = np.arange(len(ptos))
plt.plot(xs, fs, color="#72e3bb", label='$f(x)=\cos(x)$')
plt.scatter(xz, yz, c=indices, cmap='plasma')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Iteración de punto fijo $x_{n+1}=\cos(x_n)$')
plt.grid(True)
plt.plot(xs, xs, '--', color='gray', label='$y=x$')
plt.legend()
plt.show()
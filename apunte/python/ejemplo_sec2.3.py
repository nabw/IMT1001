import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(0.00001,1,1000)
gofs = np.log(np.sin(np.sqrt(xs)))


plt.plot(xs,gofs, color="#946ccd",lw=3 )
plt.grid(True)
plt.title('Grafo de la composición g o f')
plt.xlabel("x")
plt.ylabel("(g(f(x))")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Definimos el array de puntos para x entre -1 y 1
x = np.linspace(-1,1,1000)

# Definimos la función f aunque no la usaremos directamente
def f(x):
    if -1/2 < x < 1/2:
        return 1
    else:
        return 0

#Definimos el coeficiente b_n que depende de n 
def b(n):
    result = 2*np.sin((n*np.pi)/2)/(n*np.pi)
    return result

#Definimos la serie de Fourier Truncada
def f_N(x, N):
    s = np.full_like(x, 0.5) #El array parte con 0.5's ya que consideramos el coeficiente a_0 = 1/2
    for n in range(1, N+1):
        coeff = b(n)
        s += coeff * np.cos(n*np.pi*x)
    return s #Retornamos el array de puntos que corresponden a f_N

N = [1, 5, 10, 50, 100] #Definimos la lista de valores de N que graficaremos
colors = ['#4887cf', '#3d60db','#262cc9',"#4533a0", '#5d26c9'] #Defino una lista de colores para los gráficos

fig, axs = plt.subplots(1, 5, figsize=(20, 4)) #Definmos el tamaño de la figura y la malla de subplots

for i in range(len(N)): #Ploteamos cada gráfico con cada color, título y valor de N correspondiente
    axs[i].plot(x, f_N(x,N[i]), color=colors[i])
    axs[i].set_title(f"N={N[i]}")

plt.show()
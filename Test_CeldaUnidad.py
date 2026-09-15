import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Importar módulo 3D
import numpy as np # Para manejar datos numéricos


##### ESTE CÓDIGO ES UNA PRUEBA MUY SIMPLE PARA VER EL FUNCIONAMIENTO BÁSICO #####

# Creamos los ejes con Matplotlib

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Lista de puntos

L = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]


# El código que lo plotea todo

x = [i[0] for i in L]
y = [i[1] for i in L]
z = [i[2] for i in L]
ax.scatter(x, y, z, color="black", s=100)

ax.set_axis_off()
plt.show()


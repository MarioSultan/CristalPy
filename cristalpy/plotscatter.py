import matplotlib.pyplot as plt
import numpy as np

def plotscatter(ax, points, color="#888888", radius=0.15, steps=15):

    # Parámetros de las esferas

    u = np.linspace(0, 2*np.pi, steps*2)
    v = np.linspace(0, np.pi, steps)

    U, V = np.meshgrid(u, v)


    # Dibujamos una esfera en cada punto

    for x0, y0, z0 in points:

        x = x0 + radius * np.cos(U) * np.sin(V)
        y = y0 + radius * np.sin(U) * np.sin(V)
        z = z0 + radius * np.cos(V)

        ax.plot_surface(x, y, z, color=color)

    ax.set_axis_off()
    ax.set_aspect('equal')

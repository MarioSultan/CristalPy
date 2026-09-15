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
    

V = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]
F = [(.5,.5,0), (.5,.5,1), (0,.5,.5), (.5,0,.5), (1,.5,.5), (.5,1,.5)]
B = [(.5,.5,.5)]

FCC = V + F
BCC = V + B

DIAMOND = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1),
    (0,.5,.5), (1,.5,.5), (.5,0,.5), (.5,1,.5), (.5,.5,0), (.5,.5,1),
    (.25,.25,.25), (.25,.75,.75), (.75,.25,.75), (.75,.75,.25)
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plotscatter(ax, DIAMOND, radius=np.sqrt(3)/8, color="#0066ff")
plt.show()


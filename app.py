import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.integrate import dblquad


def update(val):
    ax.cla()
    bx.cla()
    cx.cla()

    nx_val = int(nx_slider.val)
    ny_val = int(ny_slider.val)

    z = psy(L, x, y, nx_val, ny_val, A)
    ax.plot_surface(x, y, z, cmap='prism')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$\Psi$')
    ax.set_title(('$|\Psi|$ dla nx = %i i ny = %i' % (nx_val, ny_val)))

    q = prob(L, x, y, nx_val, ny_val, A)
    bx.plot_surface(x, y, q, cmap='prism')
    bx.set_xlabel('$x$')
    bx.set_ylabel('$y$')
    bx.set_zlabel('$|\Psi|^2$')
    bx.set_title(('$|\Psi|^2$ dla nx = %i i ny = %i' % (nx_val, ny_val)))

    w = dblquad(rte, 0, L, 0, L)
    cx.plot_surface(x, y, w[0] * np.ones_like(x), cmap='prism')
    cx.set_xlabel('$x$')
    cx.set_ylabel('$y$')
    cx.set_zlabel('$|\Psi|^2$')
    cx.set_title(('∫∫$|\Psi|^2dxdy$ dla nx = %i i ny = %i' % (nx_val, ny_val)))

    plt.draw()


def psy(L, x, y, nx, ny, A):
    psy = (A * (np.sin((np.pi * nx * x) / L))) * (A * (np.sin((np.pi * ny * y) / L)))
    return psy


def prob(L, x, y, nx, ny, A):
    prob = abs((A * (np.sin((np.pi * nx * x) / L))) * (A * (np.sin((np.pi * ny * y) / L)))) ** 2
    return prob


L = 10 ** -9
A = np.sqrt(2 / L)

x = np.linspace(0, L, 100)
y = np.linspace(0, L, 100)
x, y = np.meshgrid(x, y)

n = 1
nx_init = 1
ny_init = 1


def rte(x, y):
    return prob(L, x, y, nx_init, ny_init, A)


fig, (ax, bx, cx) = plt.subplots(1, 3, figsize=(19, 9.5), subplot_kw={'projection': '3d'})

axcolor = 'lightgoldenrodyellow'
ax_nx = plt.axes((0.2, 0.1, 0.65, 0.03), facecolor=axcolor)
ax_ny = plt.axes((0.2, 0.05, 0.65, 0.03), facecolor=axcolor)

nx_slider = Slider(ax_nx, 'nx', 1, 5, valinit=nx_init, valstep=1)
ny_slider = Slider(ax_ny, 'ny', 1, 5, valinit=ny_init, valstep=1)

nx_slider.on_changed(update)
ny_slider.on_changed(update)

z = psy(L, x, y, nx_init, ny_init, A)
ax.plot_surface(x, y, z, cmap='prism')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$\Psi$')
ax.set_title('$|\Psi|$ dla nx = %i i ny = %i' % (nx_init, ny_init))

q = prob(L, x, y, nx_init, ny_init, A)
bx.plot_surface(x, y, q, cmap='prism')
bx.set_xlabel('$x$')
bx.set_ylabel('$y$')
bx.set_zlabel('$|\Psi|^2$')
bx.set_title('$|\Psi|^2$ dla nx = %i i ny = %i' % (nx_init, ny_init))

w = dblquad(rte, 0, L, 0, L)
cx.plot_surface(x, y, w[0] * np.ones_like(x), cmap='prism')
cx.set_xlabel('$x$')
cx.set_ylabel('$y$')
cx.set_zlabel('$|\Psi|^2$')
cx.set_title('∫∫$|\Psi|^2dxdy$ dla nx = %i i ny = %i' % (nx_init, ny_init))

plt.show()

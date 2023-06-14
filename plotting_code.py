import numpy as np
import matplotlib.pyplot as plt

def plot_level_curves():
    x = np.linspace(-1, 1)
    y = np.linspace(-1, 1)
    X, Y = np.meshgrid(x, y)
    Z = (X * Y) / np.exp(2 * (X**2) + (Y**4))

    fig, ax = plt.subplots()
    ax.contour(X, Y, Z)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_title("Level curves of f")
    plt.show()
    fig.savefig('outputimage.png')

def plot_surface():
    x = np.linspace(-1, 1)
    y = np.linspace(-1, 1)
    X, Y = np.meshgrid(x, y)
    Z = (X * Y) / np.exp(2 * (X**2) + (Y**4))

    fig = plt.figure(figsize=(15, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.contour(X, Y, Z)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_zlabel("z axis")
    ax.set_title("3D surface plot")
    fig.savefig('outputimage.png')

def draw_plot(a, tmax, n):
    t = np.linspace(0, tmax, n)
    x = np.cos(a * t)
    y = np.cos(t) * (4 + np.sin(a * t))
    z = np.sin(t) * (4 + np.sin(a * t))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, 'black', lw=1.25)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_zlabel("z axis")
    ax.set_title("Parametric plot of f")

    return fig

plot_level_curves()
plot_surface()
figoutput = draw_plot(2 * np.pi, 20 * np.pi, 1000)
figoutput.savefig('outputimage.png')

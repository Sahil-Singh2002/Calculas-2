# Plotting Code

This file demonstrates the use of the matplotlib package to plot the level curves and surface of a function, as well as generate a parametric 3D plot of another function.

$$\textbf{Level Curves of f(x,y)}$$

The function ${ f(x,y) = \frac{xy}{e^(2x^2 + y^4)} }$ is defined on the domain ${ \mathbf{D} ⊆ \mathbb{R}^2 }$, where ${ \mathbf{D} }$ is given by ${ \mathbf{D} }$ = { ${(x, y) : -1 \leq x,y \leq 1 \}$ }.

To plot the level curves of the function, execute the following code:

```
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1)
y = np.linspace(-1, 1)
X, Y = np.meshgrid(x, y)
Z = (X * Y) / np.exp(2 * (X ** 2) + (Y ** 4))

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.contour(X, Y, Z)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Level curves of f")

plt.savefig('outputimage.png')
plt.show()
```

This code will generate a plot with the level curves of the function $f(x,y)$. The resulting figure will be saved in a file named `outputimage.png`.

$$\textbf{Surface Plot of f(x,y)}$$

To plot the surface of the function ${ f(x,y) = \frac{xy}{e^(2x^2 + y^4)} }$, execute the following code:

```
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1)
y = np.linspace(-1, 1)
X, Y = np.meshgrid(x, y)
Z = (X * Y) / np.exp(2 * (X ** 2) + (Y ** 4))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.contour(X, Y, Z)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Surface plot of f")

plt.savefig('outputimage.png')
plt.show()
```

This code will generate a $\mathbb{R}^3$ surface plot of the function $f(x,y)$, with appropriate labels for the $x, y$ and $z$ axes. The resulting figure will be saved in a file named `outputimage.png`.

$$\textbf{Parametric 3D Plot of f(t)}$$

To generate a parametric $\mathbb{R}^3$ plot of the function $f(t) = (x(t), y(t), z(t))$, where

```
x(t) = cos(at)
y(t) = (4 + sin(at)) * cos(t)
z(t) = (4 + sin(at)) * sin(t)
```

and ${ 0 \leq t \leq t_{max} }$, with $n$ points on the curve, use the following code:

```
import numpy as np
import matplotlib.pyplot as plt

def draw_plot(a, tmax, n):
    t = np.linspace(0, tmax, n)
    x = np.cos(a * t)
    y = np.cos(t) * (4 + np.sin(a * t))
    z = np.sin(t) * (4 + np.sin(a * t))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, 'black', lw='1.25')
```


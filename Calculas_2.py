import numpy as np
import matplotlib.pyplot as plt
#The code for the Function f(x,y)
x = np.linspace(-1,1)
y = np.linspace(-1,1)
X,Y = np.meshgrid(x,y)
Z = (X*Y)/np.exp(2*(X**2)+(Y**4))
fig = plt.figure()
#the Labeling code:
ax = fig.add_subplot(111,aspect='equal') 
ax.contour(X,Y,Z)
ax.set_xlabel("The X axies")
ax.set_ylabel("The y axies")
ax.set_title("Level curve of f")
plt.show()
#FILE
fig.savefig('outputimage.png')
#_________________________________________________________
x = np.linspace(-1,1)
y = np.linspace(-1,1)
X,Y = np.meshgrid(x,y)
Z = (X*Y)/np.exp(2*(X**2)+(Y**4))
fig = plt.figure(figsize=(15,5))
#code for ploting the graph and labels:
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_title("3D surface plot")
ax.contour(X,Y,Z)
ax.set_xlabel("x axies")
ax.set_ylabel("y axies")
ax.set_zlabel("z axies")
#FILE
fig.savefig('outputimage.png')
#________________________________________________________
def draw_plot(a,tmax,n):
    t = np.linspace(0,tmax,n)
    x= np.cos(a*t)    
    y= np.cos(t)*(4+np.sin(a*t))    
    z= np.sin(t)*(4+np.sin(a*t))
    #plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z,'black',lw='1.25')
    ax.set_xlabel("x axies")
    ax.set_ylabel("y axies")
    ax.set_zlabel("z axies")
    ax.set_title("Parametric plot of f")
    return fig
figoutput=draw_plot(2*np.pi,20*np.pi,1000)
#FILE
figoutput.savefig('outputimage.png')

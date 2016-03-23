import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm  
from matplotlib.colors import LightSource 
from mpl_toolkits.mplot3d import Axes3D 
 
def plot_implicit(fn): 
    xmin, xmax, ymin, ymax, zmin, zmax = [-1.1,1.1]*3 
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d') 
    A = np.linspace(xmin, xmax, 100) # resolution of the contour 
    B = np.linspace(xmin, xmax, 20) # number of slices 
    A1,A2 = np.meshgrid(A,A) # grid on which the contour is plotted 
 
    for z in B: # plot contours in the XY plane 
        X,Y = A1,A2 
        Z = fn(X,Y,z) 
        cset = ax.contour(X, Y, Z+z, [z], zdir='z') 
        # [z] defines the only level to plot for this contour for this value of z 
 
    for y in B: # plot contours in the XZ plane 
        X,Z = A1,A2 
        Y = fn(X,y,Z) 
        cset = ax.contour(X, Y+y, Z, [y], zdir='y') 
 
    for x in B: # plot contours in the YZ plane 
        Y,Z = A1,A2 
        X = fn(x,Y,Z) 
        cset = ax.contour(X+x, Y, Z, [x], zdir='x') 
 
    # must set plot limits because the contour will likely extend 
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits 
    # to encompass all values in the contour. 
    ax.set_zlim3d(zmin,zmax) 
    ax.set_xlim3d(xmin,xmax) 
    ax.set_ylim3d(ymin,ymax) 
 
    plt.show() 
def op(a,b): 
    return a+b-np.sqrt(a**2+b**2) 
def func(x,y,z): 
    return op(op(1-x**2,1-y**2),1-z**2) 
 
x=np.arange(-10,10.01,0.01) 
plt.fill_between(x,np.cos(x)*np.sin(x), facecolor='None',hatch='/') 
plt.fill_between(x, 3*np.cos(x+np.e**2),facecolor='None',linestyle=':',hatch='\\') 
plt.grid(True) 
plt.show() 
 
t=np.arange(-10,10.01,0.01) 
x=np.cosh(t) 
y=np.sin(t) 
plt.fill_between(x,y, facecolor='y',linestyle='--') 
plt.show() 
 
x=np.arange(0.1,10.1,0.1) 
y=np.arange(0.1,10.1,0.1) 
X, Y = np.meshgrid(x, y)  
Z=np.cos(X)*np.sin(Y)-np.log(X**2+Y**2) 
plt.contour(X,Y,Z) 
plt.show() 
ls = LightSource(azdeg=0, altdeg=0) 
plt.imshow(ls.hillshade(Z), cmap='gray') 
plt.show() 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False) 
plt.show() 
 
x=np.arange(-10,11,1) 
y=np.arange(-10,11,1) 
X, Y = np.meshgrid(x, y) 
plt.streamplot(x, y, -1+np.cos(X)+Y**2, np.sin(Y)-X**2) 
plt.show() 
 
u=np.arange(-10,10.1,0.1) 
v=np.arange(-10,10.1,0.1) 
U, V = np.meshgrid(u, v) 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
ax.plot_surface(np.cos(U)*np.sin(V), U+V, np.sin(U)-np.cos(V),rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False) 
plt.show()
plot_implicit(func)    
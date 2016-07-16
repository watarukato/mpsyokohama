# coding: utf-8
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def z(x,y):
    return np.power(x,2) + np.power(y,2)

def dz(x,y,x0,y0):
    return 2*x0*(x-x0) + 2*y0*(y-y0) #点(x0,y0,f(x0,y0))で接する傾きだけあっている点

if __name__ =='__main__':
    x0 =0.5
    y0 =0.5
    
    xs = np.linspace(-3,3,100)
    ys = np.linspace(-3,3,100)
    XS,YS = np.meshgrid(xs,ys)
    Z = z(XS,YS)
    DZ = dz(XS,YS,x0,y0)  #点(x0,y0,f(x0,y0))で接する傾きだけあっている平面
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(XS,YS,Z)
    ax.plot_wireframe(XS,YS,DZ+z(x0,y0))
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    
    def z(x,y):
    return np.power(x,2)+np.power(y,2)

def dz(x,y,x0,y0):
    return 2*x0*(x-x0)+2*y0*(y-y0)

if __name__=='__main__':
    x0 = 0.5
    y0 = 0.5
    
    xs = np.linspace(-3,3,100)
    ys = np.linspace(-3,3,100)
    XS,YS = np.meshgrid(xs,ys)
    ZS = np.vectorize(z)
    DZ = np.vectorize(dz)
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(XS,YS,ZS(XS,YS))
    ax.plot_wireframe(XS,YS,DZ(XS,YS,x0,y0)+z(x0,y0))
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

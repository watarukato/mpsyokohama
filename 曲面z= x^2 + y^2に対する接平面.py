
# coding: utf-8

# In[4]:

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[5]:

def z(x,y):
    return np.power(x,2)+np.power(y,2)


# In[11]:

def dz(x,y,x0,y0): ##全微分して曲面zに接する傾きを出す
    return (2 * x0)*(x - x0) + (2 * y0)*(y - y0)


# In[13]:

if __name__ =='__main__':
    xs = np.linspace(-2,2,100)
    ys = np.linspace(-2,2,100)
    
    x0=0.5
    y0=0.5
    
    XS,YS = np.meshgrid(xs,ys)
    Z = z(XS,YS)
    DZ = dz(XS,YS,x0,y0) ##全微分＝接平面の傾きの集まり
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(XS,YS,Z) ##元の曲面z= x^2 + y^2
    ax.plot_wireframe(XS,YS,z(x0,y0)+DZ)
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()


# In[ ]:




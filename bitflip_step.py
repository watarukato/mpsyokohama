
# coding: utf-8

# In[1]:


import numpy as np


# In[23]:

class Neuron:
    def __init__(self,w,b,f,a):
        self.w = np.concatenate((w,b), axis=1)
        self.f = f
        self.a = a  ##aはアルファずつ動かす
        
    def output(self,x):
        x = np.concatenate([x,[[1,],]], axis=0)
        return self.f(self.w.dot(x))
    
    def learn(self,x,y):
        d = y - self.output(x)  # yはxのときの正解データ dはエラーの距離
        if d < 0 :
            self.w[0][0] -= self.a
        elif d > 0 :
            self.w[0][0] +=self.a
        print(self.w, np.abs(d))
        return np.abs(d)
    
def f(u):  #stepfunction
    u[u >0] =1
    u[u <= 0] =0
    return u

if __name__ =='__main__':
    w =[[0.3,],]
    b =[[0.1,],]
    a =0.01
    
    n = Neuron(w,b,f,a)
    for i in range(100):
        n.learn([[0.0,],],[[1.0,],])
        n.learn([[1.0,],],[[0.0,],])


# In[22]:




# In[ ]:




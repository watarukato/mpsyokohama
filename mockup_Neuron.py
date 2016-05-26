
# coding: utf-8

# In[13]:

#y(vector)=W(matrix)*x(vector)+b(vector)を表現する

import numpy as np

class Neuron:
    def __init__(self,w,b):
        self.w=w
        self.b=b
        
    def output(self,x):
        arr_x = np.array(x)
        arr_w = np.array(w)
        arr_b = np.array(b)
        print(arr_x)
        print(arr_w)
        print(arr_b)
        return np.dot(arr_w,arr_x) + arr_b

x =[2.0,3.0]
w =[[1.0,2.0],]
b =[-1.0]
n = Neuron(w,b)

answer=n.output(x)

print(answer)


# In[ ]:




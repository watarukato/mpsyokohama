
# coding: utf-8

# In[19]:

import numpy as np

class Neuron:
    def __init__(self, w, b, f, epsilon, acceptable_error):
        self.w = np.concatenate((w,b), axis =1)
        self.f = f
        self.epsilon = epsilon
        self. acceptable_error = acceptable_error
        
    def output(self, x):
        return self.f(self.w.dot(x))
    
    def learn(self, teaching_datum):
        while True:
            x = teaching_datum[:-1]
            yt = teaching_datum[-1]
            y  = self.output(x)
            se = np.power((yt-y) ,2)
            
            if se < self.acceptable_error:
                return self.w
            else:
                self.w -= self.epsilon * 2*(yt-y)*y*(y-1.0)*x
                
def f(x):
    return 1 / (1+np.exp(-1*x))


# In[24]:

if __name__ =='__main__':
    w =[[0.4,],]
    b =[[0.5,],]
    epsilon = 0.5
    data = [[0,1,1],[1,1,0]]
    a= 0.1
    
    n = Neuron(w,b,f,epsilon,a)
    
    for teaching_datum in data:
        
        print(n.learn(teaching_datum))


# In[ ]:




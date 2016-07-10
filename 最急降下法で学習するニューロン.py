
# coding: utf-8

# In[1]:

import numpy as np


# In[15]:

class Neuron:
    def __init__(self,w,beta,epsilon=0.5):
        self.w = np.concatenate((w,beta),axis=1)
        self.epsilon = epsilon
    
    def sigmoid(self,x):
        ##x = np.concatenate([x,[[1,],]], axis=0) teaching_datumに１あるからいらない？
        return 1/(1+np.exp(-1*self.w.dot(x)))
    
    def get_otuput(self,x):
        x = np.concatenate([x,[[1,],]], axis=0)
        return sigmoid(self.w.dot(x))
    
    def learn(self,teaching_datum):
        """"
        :param teaching_datum:[[0,1,1],[1,1,0]]
        """"
        x = teaching_datum[:-1]
        y = teaching_datum[-1]
        val = self.get_output(x)
        self.w -= self.epsilon * 2.0*(val-y)*val*(1.0-val)*x
        
        


# In[ ]:

##ここにy-ytの差分のアクセプタブルエラーでwを変更する回数ないのかな。でニューロン実体化して、
if __name__ =='__main__':
    n = Neuron(w,beta,epsilon)
    
    for teaching_datum in data:
        neuron.learn(teaching_datum)
        


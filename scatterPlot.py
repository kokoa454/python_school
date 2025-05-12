# -*- coding: utf-8 -*-
"""
Created on Fri May  9 14:36:04 2025

@author: qqnq7
"""

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import MultipleLocator

 

#class1 data 

mu1=np.array([2,2]) 

V1=np.array([[1,0.01],[0.01,1]]) 

class1=np.random.multivariate_normal(mu1,V1,size=30) 

 

#class2 data 

mu2=np.array([4,3]) 

V2=np.array([[1,0.01],[0.01,1]]) 

class2=np.random.multivariate_normal(mu2,V2,size=30) 

#scatter plot coontrol
plt.scatter(class1[:, 0], class1[:, 1], label='Class1', c='red', marker="*", alpha=0.4, s=150)
plt.scatter(class2[:, 0], class2[:, 1], label='Class2', c='blue', marker="o", alpha=0.4, s=150)
ax = plt.gca()
ax.yaxis.set_major_locator(MultipleLocator(0.5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.show()

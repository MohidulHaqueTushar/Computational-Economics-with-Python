# -*- coding: utf-8 -*-
"""
@author: Md Mohidul Haque
"""

"""Import Modules"""
import scipy.stats 
import matplotlib.pyplot as plt
import numpy as np 

"""Defining Functions"""
def kestren_process(x_0,t=1,a_min=0.8,a_max=1.2,b_min=0,b_max=10000):
    """
    Function that will calculate the growth of firms by using Kestren 
    process.
    
    Parameters
    ----------
    x_0 : initial size of the firm
    
    t : int
     time steps
     
    a_min : Lower bound of alpha
     0.8 by default
    
    a_max : Upper bound of alpha
     1.2 by default
     
    b_min = Lower bound of beta
     0 by default
    
    b_max = Upper bound of beta
     10000 by default
     
    Returns
    -------
    firm’s size in terms of capital stock in Euro at time t
    
    """
    if t<0:
        raise ValueError('Time can not be negative!')
    elif t==0:
        v = np.ones(n)
        return v*x_0
    else:
        for i in range(1,t+1):
            alpha = scipy.stats.uniform(a_min, a_max).rvs()
            beta = scipy.stats.uniform(b_min,b_max).rvs()
            x = alpha*x_0+beta
            x_0 = x
        return x 

def growts_of_firms(n,x_0,t):
    """
    Function that will calculate the growths of n firms by using
    the function kestren_process.
    
    Parameters
    ----------
    n = int
     Number of firms
     
    x_0 : initial size of the firm
    
    t : int
     time steps
    
    Returns
    -------
    array of the growth of n firms
    
    """
    count = 0
    growths = []
    while count < n:
        growths.append(kestren_process(x_0,t))
        count = count+1
    growths = np.array(growths)
    return growths

"""Main script"""
"""kestren_process on 10000 firms, where initial size of all firms are 10000, and timesteps are 5"""
growth_process = growts_of_firms(n=10000,x_0=10000,t=5)
print("The minimum growth is: {}\nand maximun growth is: {}".format(growth_process.min(),growth_process.max()))

"""Plot the Distribution"""
fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
ax[0][0].hist(growth_process, bins=100, color='b', alpha=0.6, rwidth=0.85)
ax[0][0].set_title("kestren process on 10000 firms")
ax[0][0].set_xlabel("x_t: Firm’s size in terms of capital stock in Euro at time t")
ax[0][0].set_ylabel("Frequency")

"Save figure as image"
plt.savefig("Kesten process on 10000 firms.png", dpi=300)
plt.show()


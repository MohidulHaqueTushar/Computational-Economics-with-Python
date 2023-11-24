# -*- coding: utf-8 -*-
"""
Created on Wed Dec 8 

@author: Md Mohidul Haque

"""
"Import Module"
import numpy as np
import matplotlib.pyplot as plt

"""Functions"""

"""Function that will seperate the total asset into n equal pieces"""
def equal_pieces_of(total_capital,n=20):
    
    """
    Function that will seperate the given first argument (total_asset) into 
    n equal pieces.
    
    Parameters
    ----------
    total_capital : int
      Number
    
    n : int
     Number of pieces, by default n = 20
     
    Returns
    -------
    n equal pieces of first argument : list
      list length will be equal to n
    
    """
    
    pieces = []
    each_piece = total_capital / n
    for i in range(n):
        pieces.append(each_piece)
    return pieces

""" Function that will create a random walk for the given length"""
def create_random_walk(length, decrement = -1, increment = 1):
    """
    Function that will give the random walk for the given length 
    with given decrement and increment.
    
    Parameters
    ----------
    length : int
      Number
    
    decrement : int
     by default decrement is -1
    
    increment : int
     by default increment is 1
     
     
    Returns
    -------
    random walk : array
      array length will be equal to given length
    
    """
    
    """ Check input values"""
    assert length > 0
    
    """ Create increment/decrement time series"""
    sample = np.random.choice([decrement, increment], size=length)
    
    """ Compute sum over time series"""
    random_walk = np.cumsum(sample)
    
    """ Return random walk"""
    return random_walk

"main script"

"""Input values"""
total_capital = 20000
pieces = 20

"""Using the function equal_pieces_of(total_asset,n)"""

"""calculate pieces and convert to numpy array """
total_pieces_of_capital = np.array(equal_pieces_of(total_capital, pieces))
print("{} equal pieces of the total capital {} is: \n{}".format(pieces,total_capital,total_pieces_of_capital),"\n")

"""Initial value of each pieces of the total capital"""
initial_value = total_pieces_of_capital[0]
print("Initial value for each {} different investment is: {}\n".format(pieces,initial_value))

"""Create price development data"""

"""Create a 'numpy.ndarray for storing random walk as developing_price'"""
developing_price = np.arange(2000).reshape(len(total_pieces_of_capital), 100)
shape = developing_price.shape

print("The initial array is:\n{} \n \n With the shape: {} ".format(developing_price,shape))

"""Use the function create_random_walk() with decrement -1 and increment 1, and calculate the difference of initial_value 
   from each 20 random walk, and store the result in developing_price array """

for i in range(shape[0]):
    random_walk = create_random_walk(shape[1])
    developing_price[i,:] = random_walk + initial_value
    print("Random walk {} is:\n {}\n".format(i,random_walk),"\n")
    print("Developing price for random walk {} is:\n {}\n".format(i, developing_price[i,:]))

""" Calculating the shape of price development """
shape = developing_price.shape

print("All developing price:\n {}\n \n With the shape: {}".format(developing_price,shape))

"""Calculating the average time series"""
"""assign initial counting value for while loop"""
time_series_sum= developing_price[0, :]

for n in range(1,20):
    time_series_sum = time_series_sum + developing_price[n,:]

time_series_avg = time_series_sum/20

print("Average time series is:\n {}\n".format(time_series_avg))
print("The length of the average time series is: ",len(time_series_avg))

""" Create a figure and a set of axes """

fig, ax = plt.subplots(nrows = 4, ncols = 5, squeeze = False)

"""Plot the price development in red and average time series in black"""
k = 0
while k<20:
    for i in range(4):
        for j in range(5):
            ax[i][j].plot(np.arange(shape[1]),developing_price[k,:],c="r")
            ax[i][j].plot(np.arange(shape[1]),time_series_avg, c="k")
            k = k+1
        
"""Ensure that figure is arranged nicely""" 
plt.tight_layout()
"save figure as pdf"
plt.savefig("20 time series and their average.pdf")
"save figure as image"
plt.savefig("20 time series and their average.png", dpi=300)
plt.show()



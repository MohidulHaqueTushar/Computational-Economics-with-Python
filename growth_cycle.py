# -*- coding: utf-8 -*-
"""
@author: Md Mohidul Haque

"""

"""Input Modules"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Defining Function"""
"""The Function will calculate the total number of Rabbits and Cats and their change in number 
   by using the given values"""

def populations(r_0,c_0,t,growth_rate=0.1,car_death_rate = 0.05,dying = 0.0005):
    
    """
    Function that will calculate the number of Rabbit's and Cat's, and their change for specific time t.
    
    Parameters
    ----------
    r_0 : int or float
      initial number of Rabbit's in the environment
    
    c_0 : int or float
      initial number of Cat's in the environment
          
    t : int
      time steps
    
    growth_rate : int or float
      Growth of rabbit population with time, default value is 0.1
          
    car_death_rate : int or float
      Death rate of Both polulations (Rabbit and Cat) by Car, default value is 0.05
          
    dying : int or float
      Death rate of Rabbit population by Cat population, default value is 0.0005
     
    Returns
    -------
    df : pandas.core.frame.DataFrame
      DataFrame will have four columns, and rows equal to number of time steps.
      This Dataframe will store both Cat and Rabbit populations and their changes with time.
    
    """
    rabbit = [r_0]
    cat = [c_0]
    rabbit_growth_list = [None]
    cat_growth_list = [None]
    
    if t<0:
        raise ValueError('Time can not be negative!')
    elif t==0:
        print("No Change for time equal to Zero!")
    else:
        for i in range(1,t+1):
            new_rabbit = rabbit[-1] + growth_rate * rabbit[-1] - dying * rabbit[-1] * cat[-1] - car_death_rate * rabbit[-1]
            new_cat = cat[-1] + growth_rate * dying * rabbit[-1] * cat[-1] - car_death_rate * cat[-1]
            rabbit_growth = growth_rate * rabbit[-1] - dying * rabbit[-1] * cat[-1] - car_death_rate * rabbit[-1]
            cat_growth = growth_rate * dying * rabbit[-1] * cat[-1] - car_death_rate * cat[-1]
            rabbit.append(new_rabbit)
            cat.append(new_cat)
            rabbit_growth_list.append(rabbit_growth)
            cat_growth_list.append(cat_growth)
        
    df=pd.DataFrame({"Rabbit's":rabbit,"Cat's":cat,"Rabbit Changes":rabbit_growth_list,"Cat Changes":cat_growth_list })
    return df


"""Main Script"""
"""We will use the function populations(), where initial value of rabbits and cats 
   are 400 and 50 respectively, and run the function for the time t = 1000"""
df = populations(400,50,1000)

"""Print the calculated data (just 10 rows)"""
shape = df.shape
print("The calculated dataFrame:\n\n{},\n\nAnd the shape is: {}".format(df.head(10),shape))

"""More details"""
print("\nMore details about the data:\n\n{}".format(df.describe(include = "all")))

"""Correlatins between the columns"""
print("\nThe correlations between the columns:\n\n{}".format(df.corr()))

"""Plot the data"""
"""Plot the Rabbit and Cat populations"""
fig1, ax = plt.subplots(nrows = 2, ncols = 1, squeeze = False)
ax[0][0].plot(np.arange(shape[0]),df["Rabbit's"],c="r", label = "Rabbit's population")
ax[1][0].plot(np.arange(shape[0]),df["Cat's"], c="k", label = "Cat's population")
ax[0][0].legend()
ax[1][0].legend()
plt.tight_layout()
plt.savefig("Rabbit and Cat population.png", dpi=300)

"""Plot the Changes of Rabbit and Cat population"""
fig2, ax = plt.subplots(nrows = 2, ncols = 1, squeeze = False)
ax[0][0].plot(np.arange(shape[0]),df["Rabbit Changes"],c="b", label = "Rabbit's population Changes")
ax[1][0].plot(np.arange(shape[0]),df["Cat Changes"], c="g", label = "Cat's population Changes")
ax[0][0].legend()
ax[1][0].legend()
plt.tight_layout()
plt.savefig("Changes of Rabbit and Cat population.png", dpi=300)

"""Plot the Rabbit population against the Cat polulation"""
fig3, ax = plt.subplots(nrows = 1, ncols = 1, squeeze = False)
ax[0][0].plot(df["Cat's"],df["Rabbit's"],c="m")
ax[0][0].set_title("Predator Prey Relation!")
ax[0][0].set_xlabel("Cat's")
ax[0][0].set_ylabel("Rabbit's")
plt.tight_layout()
plt.savefig("Rabbit population against cat population.png", dpi=300)
plt.show()

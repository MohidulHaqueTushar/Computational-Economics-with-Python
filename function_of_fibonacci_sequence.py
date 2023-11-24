# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:04:18 2021

@author: Md Mohidul Haque

"""

"""Functions"""

def  arbitrary_element_of(n):
    """
    Computes arbitrary elements of the parameter n of the Fibonacci sequence.
    
    Parameters
    ----------
    n : 'int' type
      Numbers  
    
    Returns
    -------
    number : 'int' type
    
    """
    
    """
    Checking the input(n) is equal to zero or one, otherwise using the 
    formula.
    
    """
    if n in {0,1}:
        return n
    else:
        return arbitrary_element_of(n-1) + arbitrary_element_of(n-2)
    

"""Main Script"""

"""
   We will write a function by using the function arbitrary_element_of(n) to find the  
   Fibonacci sequence. 

"""

""" 
  Write a  function which returns the Fibonacci sequence starts from one.
  
"""

def fibonacci_sequence_of(n):
    
    """
    Compute Fibonacci sequence of the parameter n.
    
    Parameters
    ----------
    n : 'int' type
      Numbers  
    
    Returns
    -------
    Series of numbers : 'list' type
    
    """
    
    """
    Using for loop to acces every value from 1 to n.
    
    """
    return [arbitrary_element_of(i) for i in range(1,n+1)]

"""Print the sequences"""

print("Fibonacci Sequence when n is 5,\nF5 is: ",fibonacci_sequence_of(5))
print("\nFibonacci Sequence when n is 6,\nF6 is: ",fibonacci_sequence_of(6))
print("\nFibonacci Sequence when n is 7,\nF7 is: ",fibonacci_sequence_of(7))
print("\nFibonacci Sequence when n is 25,\nF25 is: ",fibonacci_sequence_of(25))
print("\nFibonacci Sequence when n is 40,\nF40 is: ",fibonacci_sequence_of(40))




        
        
    



    
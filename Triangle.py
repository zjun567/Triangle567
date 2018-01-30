# -*- coding: utf-8 -*-
"""
Updated Jan 28, 2018
Assignment 2a -- Testing - Classify Triangle
@author: Zhe Jun
"""

def classifyTriangle(a,b,c):
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,(float,int)) and isinstance(b,(float,int)) and isinstance(c,(float,int))):
        return 'InvalidInput';
    
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    x,y,z = sorted([a,b,c])
        
    # now we know that we have a valid triangle 
    if a == b ==c:
        return 'Equilateral'
    elif round(((x ** 2) + (y ** 2)), 2) == round((z ** 2), 2):
        if x == y:
            return 'IsoscelesRight'
        else:
            return 'ScaleneRight'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'

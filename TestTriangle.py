# -*- coding: utf-8 -*-
"""
Updated Jan 28, 2018
Assignment 2a -- Testing - Classify Triangle
@author: Zhe Jun
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(-1,0,1), 'InvalidInput', '-1,0,1 is invalidinput')
        self.assertEqual(classifyTriangle('A',0,1), 'InvalidInput', 'A,0,1 is invalidinput')
        self.assertEqual(classifyTriangle(1,1,2), 'NotATriangle', '1,1,2 is not a triangle')
        
    def testScaleneRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5), 'ScaleneRight','3,4,5 is a ScaleneRight triangle')
        self.assertEqual(classifyTriangle(10,8,6), 'ScaleneRight', '6,8,10 is ScaleneRight triangle')
        
    def testIsoscelesRightTriangle(self):
        self.assertEqual(classifyTriangle(2,2,8**0.5), 'IsoscelesRight', '2,2,8**0.5 is a IsoscelesRight triangle')
        
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3,3,4), 'Isosceles', '3,3,4 is a Isosceles triangle')
        self.assertEqual(classifyTriangle(4,3,4), 'Isosceles', '4,3,4 is a Isosceles triangle')
    
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3,4,6), 'Scalene', '3,4,6 is a Scalene triangle')

        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


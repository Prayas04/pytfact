# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:29:43 2023

@author: praya
"""

class factorial1:
    def __init__(self,number):
        self.number=number
    def factorial(self):
        if self.number == 0:
            return 1 
        else:
            n1 = self.number
            self.number-= 1
            return n1 * self.factorial()
   # def getnum(self):
    #    return self.number
number=int(input("Enter number whose factorial is to be found: "))
a=factorial1(number)
print(a.factorial())
        
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:27:12 2019

@author: raghed
"""

def FactIterative(num):
    fact=1;
    for i in range(num,1,-1):
        fact=fact*i
    return fact


def FactRecursion(num):
    
    if num == 1:
           return 1
    return num * FactRecursion(num-1)
 


num = int(input("Enter a number to calculte factoriel\n"))

factoriel = FactIterative(num)
factoriel_rec = FactRecursion(num)

print ("Factorielle (iterative) de " + str(num) + " est: "+ str(factoriel))
print("Factorielle (recursive) de  "+ str(num) + "  est: "+str(factoriel_rec))



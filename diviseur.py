# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 08:29:57 2019

@author: raghed
"""

def petitDiv(n):

    for i in range(2,n+1):
        if(n%i==0):
            #a.append(i)
            print("PLus petit Diviseur est:",i)
            break
    #a.sort() 
   # print("PLus petit Diviseur est:",a[0])

    
 
n=int(input("Donner un nombre positif:"))
if n>0:
    petitDiv(n)
else:
    print("Nombre est negatif ou 0")
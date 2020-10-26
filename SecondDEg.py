# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:53:49 2019

@author: raghed
"""

# R0: résoudre équation du second degré ax^2 +bx +c =0

## R01: Lire donnée a et b et c
## R02: Claculer la solution
## R03: Afficher la solution
import math

# premDegre calcul -b/a a condition d'être sure que a!=0
def premDegre(a,b):
    # assert permet de faire de la programation deffensive
    assert a!=0 ,"A ne doit pas être nul"
    return -b/a

def controleEntreeEtSol(a,b,c):
    if a == 0:
        if b==0:
            if c==0:
                return "Infinité de solutions"
            else:
                return "Impossible pas de solutions"
        else:
            premDegre(a,b)
    else:
        D=pow(b,2) - 4*a*c
        if D<0:
            return " pas de solutions dans l'ensemble R"
        if D==0:
            return str(-b/2*a)
        if D>0:
           return " deux solutions : "+ str((-b-math.sqrt(D))/2*a) + " et " + str((-b+math.sqrt(D))/2*a )
    
            
    
    



def pgmSecondDegre():
    print("saisir a et b pour calculer ax+b=0")
    x=int(input("Donner a "))
    y=int(input("Donner b "))
    z=int(input("Donner b "))
    rep=controleEntreeEtSol(x,y,z)
    print("la solution de",x,"x^2 +",y,"x + ",z,"= 0 est ",rep)

pgmSecondDegre()



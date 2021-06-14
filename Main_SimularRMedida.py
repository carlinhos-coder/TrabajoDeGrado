#RMedida rx1 rx2 rx3 rx4 rx5
from funciones import crearMatriz
from CalcularMa2 import *
from CalcularMa1 import *
from RCalculada import *
import numpy as geek


def Main_SimularRMedida():
# L�mite superior e inferior de la variable Fblood

    xu1 = 0.07;                 # L�mite superior de la variable Fblood
    xl1 = 0.002;                # L�mite inferior de la variable Fblood
    res1 = (xu1 - xl1)/150
    rx1 = 0.02
# L�mite superior e inferior de la variable que representa la melanina
    xu2 = 0.45;                 # L�mite superior de la variable melanina
    xl2 = 0.013;                # L�mite inferior de la variable melanina
    res2 = (xu2 - xl2)/150
    rx2 = 0.013

    #Oxygen saturation
    #Originial Can vary from 0% to 100%
    xu5 = 0;                # L�mite superior del di�metro de las part�culas de col�geno
    xl5 = 1;                # L�mite inferior del di�metro de las part�culas de col�geno
    res5 = (xu5 - xl5)/150
    rx5 = 0.9

    Ua1=crearMatriz(1,31)
    Ua2=crearMatriz(1,31)
    Ua1[1,:] = CalcularMa1(rx2)
    Ua2[1,:] = CalcularMa2(rx1, rx5)
    #load Us1
    #Us1 = open ('Us1.txt','r')
    Us1=[37.4301,   35.0355,  32.8091 ,  30.7394 ,  28.8157 , 27.0276 ,  25.3653 ,  23.8196  , 22.3820 ,  21.0443 ,  19.7992,   18.6397 ,  17.5594, 16.5523 ,  15.6131 ,  14.7365 ,  13.9181 ,  13.1533  , 12.4384 ,  11.7697  , 11.1437  , 10.5574 ,  10.0079  , 9.4926  ,  9.0091 ,   8.5552 ,8.1287 ,   7.7277,    7.3506,    6.9956,    6.6613]
    Ua1[1,:] = Ua1[1,:]+ Ua2[1,:]

    L=0.02
    RMedida=crearMatriz(1,31)
    RMedida[1,:] = RCalculada[Ua1,Us1]

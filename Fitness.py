from typing import Sized
import numpy as geek
def Fitness(rx1,rx2):
##Calculo de la funcion con operacion matricial y division punto de la Fn
##para retornarlas
#(rx1.^2 + rx2 -11).^2 + (rx1 + rx2.^2 -7).^2
    lista=[]
    efes=[]
    fits=[]
    v=len(rx1)
    for j in range(0,v):
        f = (rx1[j]**2 + rx2[j] -11)**2 + (rx1[j] + rx2[j]**2 -7)**2 ## evaluar en la funcion F(x1,x2)=la funcion evaluada en los 20 valores
        fitt = 1/(1+f) ## paso Para sacar el minimo de la funcion
        efes.append(f)
        fits.append(fitt)
    minim=geek.min(efes)
    return (efes,fits,minim)

    
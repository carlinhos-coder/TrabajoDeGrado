from funciones import crearMatriz
import numpy as geek
def RCalculada(Ua1,Us1):
    k2 = 50
    k1 = 0.0255
    Rr=crearMatriz(1,31)
    for i in range(1,31):
        Rr[i] = Us1(i)/(k1+k2*Ua1(i))
    return Rr


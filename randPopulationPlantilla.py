import random
import numpy as geek
from pprint import pprint
from dec2bin import dec2bin

def zeros(size):
    return [[0 for x in range(size)]]

def randPopulationPlantilla(xu,xl,tamanoPobla,q):

    #binPop: poblaci�n de n�meros binarios
    #decodedV: n�meros binarios en decimal
    #r: valores en decimal de las variables x1 y x2;
    #x1=(geek.random.rand(1,tamanoPobla))
    tam=zeros(tamanoPobla)
    pos=tam[0]
    decodedV = geek.random.randint(1023, size=(1, 20))#numero de bits a utilizar %% valores aleatorios a d(dise�o)
    binPop=[]
    for i in range(len(pos)):
        aux=decodedV[0,i]
        #numbinPop = int(geek.binary_repr(aux,1))
        numbinPop=format(aux, "010b")
        digits = [int(x) for x in str(numbinPop)]
        digits
        binPop.append(digits)
        r= xl + (xu-xl)/(2**q-1) *decodedV   
    return (binPop,decodedV,r)
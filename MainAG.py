
import math
from numpy.random import randint
import rand
import numpy as geek
from pprint import pprint
from randPopulationPlantilla import *
from Fitness import *
from funciones import *
"""La funci�n a minimizar es: f = (x1^2 + x2 -11)^2 + (x1 + x2^2 -7)^2;
% Rango de variables: 0<=x1,x2<=6;
% N�mero de puntos iniciales: 20
% resoluci�n = 0.006;"""

#DEFINIMOS LAS VARIABLES XU Y XL
xu=6.0
xl=0.0

res = 0.006 #toma los valores entre 0 y 6 cada intervalo de 0.006
tamanoPobla = 20#inicializamos x1 x2 con 20 valores
#Selecci�n del n�mero de bits (q) a utilizar para representar cada variable,
#con una resoluci�n de 0.006 en el intervalo (0,6):

q = round(math.log2((xu-xl)/res)) #numero de bits de x1 redondedado
#cambiamnos el nuevo valor
binPopx1, decodedVx1, rx1 = randPopulationPlantilla(xu,xl,tamanoPobla,q)
binPopx2, decodedVx2, rx2 = randPopulationPlantilla(xu,xl,tamanoPobla,q)
z = crearMatriz(tamanoPobla,tamanoPobla)

z=geek.concatenate((binPopx1,binPopx2),1)

VectTemp=[]
rx1=rx1[0]
rx2=rx2[0]
for k in range(150):
################################################################
##################################     Fitness        #####################
    
    f, fitt, minim = Fitness(rx1,rx2)## devuelve f ya evaluada en la funcion y fitt ya minimizado
    #mini=geek.min(f)
    VectTemp.append(minim)
################################# Reproduccion ###############################

    prob_individuo = crearMatriz(tamanoPobla,1)
    prob_acumuladas= crearMatriz(tamanoPobla,2)

    #prob_acumuladas = prob_individuo

    fit=fitt


    for i in range(0,tamanoPobla):
        prob=fit[i]/sum(fit)
        prob_individuo[i]=prob
        if i==0: #solo ingresa una vez por que debe de empezar en 0 
            prob_acumuladas[i][0] = 0;  
            prob_acumuladas[i][1] = prob_individuo[i]
        else:
            prob_acumuladas[i][0] = prob_acumuladas[i-1][1]
            n=prob_individuo[i]
            m=prob_acumuladas[i-1][1]
            prob_acumuladas[i][1] = m+n
##########################       Ruleta  #########################################
    x = crearMatriz(tamanoPobla,tamanoPobla)
    
    j=0
    RepeticionJ = crearMatriz(tamanoPobla,1)
    for i in range (0,tamanoPobla):
        R=geek.random.random() ###valor aleatorio 
        for l in range (0,tamanoPobla):
            if R >= prob_acumuladas[l][0] and R < prob_acumuladas[l][1]:####estamos verificando que R pertenesca a un rango en la matriz
                j=l
                break
        x[i][:]=z[j][:]### asigna a la matriz X los valores de la fila que corresponden a J 
        RepeticionJ[i][0]=j ##control en # decimal para las repeticiones

###################################### Crossover ##################################
    cross=x
    ke=geek.random.randint(1,20)
    for t in range(0,12,2):
        cross[t][ke+1:20]= x[t+1][ke+1:20]
        cross[t+1][ke+1:20]= x[t][ke+1:20]
####################################### Mutacion  #############################
    xMutacion = cross
    for u in range (0,tamanoPobla):
        k1=geek.random.randint(1,20)
        k2=geek.random.rand() 
        if k2 <= 0.6: 
            if xMutacion[u][k1]==0:
                xMutacion[u][k1]=1
            else: xMutacion[u][k1]=0


######################################################################################
####################### Actualizacion   ##############################################
    binPopx1=crearMatriz(20,10)
    binPopx2=crearMatriz(20,10)
    ##tm=geek.zeros((20,10))
    ##tm=xMutacion[:][0]
    
    for l in range (0,tamanoPobla):
        for k in range(0,tamanoPobla):
            if k<=9:
                binPopx1[l][k] = xMutacion[l][k]
    
    for f in range(0,tamanoPobla):
        i=10
        for t in range(0,10):
            binPopx2[f][t] = xMutacion[f][i]
            i=i+1

    z=geek.concatenate((binPopx1,binPopx2),1)

    ## actualizar rx1 y rx2
    for n in range (0,tamanoPobla):
        tem=xMutacion[n][0:10]
        temp1=int(''.join(map(str,xMutacion[n][0:10])),2)
        rx1[n] = xl + ((xu-xl)/((2**q) -1))*temp1
        temp2=int(''.join(map(str,xMutacion[n][10:20])),2)
        rx2[n] = xl + ((xu-xl)/((2**q) -1))*temp2
pprint(rx1)
pprint(rx2)


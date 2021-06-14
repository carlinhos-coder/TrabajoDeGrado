import numpy as geek
def CalcularMa1(Fmel):
    #'Lambda' Longitud de onda
    Lambda_min = 450;                                                    #Units: cm
    Lambda_max = 750;                                                    #Units: cm

    # Vectores de Lambda
    Vect_Lambda = geek.linspace(Lambda_min,Lambda_max,31)

    #Propiedades �pticas de la Epidermis
    UaMelanosome = (6.6 * 10**11) * (Vect_Lambda ** -3.33);  
    
    UaBaseline = 7.84*(10**8)*(Vect_Lambda**-3.255);   
    
    #Ua1 Epidermis
    Ua1 = Fmel * UaMelanosome + (1 - Fmel) * UaBaseline;                  #Units: cm^-1
    return Ua1

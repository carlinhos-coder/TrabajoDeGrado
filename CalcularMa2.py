import numpy as geek
def CalcularMa2(Fblood,OS):
    #Vector 'Oxi' - Hemoglobina Espectro Te�rico de 450:10:750
    Vect_Oxy = [62816, 44480, 33209.2, 26629.2, 23684.4, 20932.8, 20035.2, 24202.4, 39956.8 ,53236, 43016, 32613.2 ,44496, 50104, 14400.8, 3200 ,1506, 942 ,610, 442, 368, 319.6,294 ,277.6, 276, 290, 314, 348,390, 446, 518]

    #Vector 'Deoxi' - Hemoglobina Espectro Te�rico de 450:10:750
    Vect_Deoxy = [103292, 23388.8, 16156.4,14550, 16684, 20862, 25773.6 ,31589.6, 39036.4 ,46592 ,53412, 53788 ,45072 ,37020, 28324.4, 14677.2 ,9443.6, 6509.6, 5148.8, 4345.2 ,3750.12 ,3226.56, 2795.12, 2407.92, 2051.96, 1794.28, 1540.48, 1325.88, 1102.2, 1115.88 ,1405.24]
    #'Lambda' Longitud de onda
    Lambda_min = 450;                                                    #Units: cm
    Lambda_max = 750;                                                    #Units: cm

    #Vectores de Lambda
    Vect_Lambda = geek.linspace(Lambda_min,Lambda_max,31)

    #Propiedades �pticas de la Epidermis
    UaBaseline = 7.84*(10**8)*(Vect_Lambda**-3.255);                             #Units: cm^-1

    #Using model from Dmitry Yudovsky and Laurent Pilon AO2009 (Simple and accurate expressions for diffuse
    #reflectance of semi-infinite and two-layer
    #absorbing and scattering media)
    uoxy = 150*OS*Vect_Oxy/66500
    udoxy = 150*(1-OS)*Vect_Deoxy/66500
    ublood = uoxy + udoxy
    Ua2 = Fblood *(ublood) + (1 - Fblood) * UaBaseline
    return Ua2
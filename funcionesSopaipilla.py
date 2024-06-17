import os
import random
import numpy as np
def validarMenu():
    while(True):
        try:
            op=int(input("  Ingrese su opcion: "))
            if(op>=1 and op<=7):
                break
        except ValueError:
            print("Debe ser un número entero")
    return op
def llenarMatriz(mm):
    for i in range(5):
        for j in range(7):
            mm[i][j]=random.randint(3000,50000)


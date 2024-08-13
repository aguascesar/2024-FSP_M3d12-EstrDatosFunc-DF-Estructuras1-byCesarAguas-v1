# * my_wordCount v1 (https://github.com/aguascesar/2024-FSP_M3d12-EstrDatosFunc-DF-Estructuras1-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d12-EstrDatosFunc-DF-Estructuras1-byCesarAguas-v1/LICENSE)
#  
#   Conversion de pesos chilenos otras monedas
#
#Crear un archivo conversiones.py y una estructura de datos apropiada que permita
#ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar
#mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.

import sys

# A lo menos necesitamos una funcion para recibir los datos como argumentos ingresados por el usuario.
# la taza de conversion para
# Sol peruano: 0.0046
# Peso Argentino: 0.093
# Dólar Americano: 0.00013


# Creando funciones necesarias para las conversiones
def shift_pe(pe, cl):
    clPe = cl * pe
    return clPe

def shift_ar(ar, cl):
    clAr = cl * ar
    return clAr

def shift_us(us, cl):
    clUs = cl * us
    return clUs
# Con la siguente funcion se espera que se ingresen en orden los argumentos
# taza sol peruano, taza peso argentino, taza dolar americano, por ultimo a cifra a convertir (pesos chilenos)
def shift_all(pe, ar, us, cl):
    clPe = cl * pe
    clAr = cl * ar
    clUs = cl * us
    return clPe, clAr, clUs


# Comenzando las rutinas

# Se necesita chequear el ingreso de argumentos
if len(sys.argv) != 5:
    print("Por favor ingrese las 3 tazas en el orden que se espera, y 1 valor a convertir.")
    sys.exit(1)

# Se espera poder extraer los valores esperados y en el orden correcto.
try:
    pe = float(sys.argv[1])
    ar = float(sys.argv[2])
    us = float(sys.argv[3])
    cl = float(sys.argv[4])
except ValueError:
    print("Por favor ingrese solo numeros")
    sys.exit(1)
#   Aunque sea mas economico en escritura de lineas de codigo 
#   no se recomienda hacer todo esto en una linea,
#   sobretodo cuando son muchos variables y datos.
#
#   Ejecutando funciones de conversion.
#clPe, clAr, clUs = shift_all(pe, ar, us, cl)
clPe = shift_pe(pe, cl)
clAr = shift_ar(ar, cl)
clUs = shift_us(us, cl)

#   Mostrando los resultados
print(f"{cl:.0f} pesos chilenos convertidos a:")
print(f"{clPe} Soles Peruanos")
print(f"{clAr} Pesos Argentinos")
print(f"{clUs} Dólares Americanos")
# * my_wordCount v1 (https://github.com/aguascesar/2024-FSP_M3d12-EstrDatosFunc-DF-Estructuras1-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d12-EstrDatosFunc-DF-Estructuras1-byCesarAguas-v1/LICENSE)
#   
#   Contando caracteres y palabras distintas
#El texto lorem ipsum es un texto de prueba que se utiliza para demostrar distintas
#tipografías además de usarse para rellenar espacios que requieran largos textos.
#¿Cuántas palabras componen este texto?

import sys

#   Definiendo funciones necesarias
#
#   Funcion para contar caracteres diferentes.
def find_chars(texto_txt):
    # Buscando caracteres distintos, repetidos no se admiten y guardandolos en una lista
    chars = set(texto_txt)
    #print(chars)
    return len(chars)

#   Funcion para contar palabras distintas.
def count_words(texto_txt):
    # Separando palabras por espacios en blanco y guardandolos en una lista
    diff_words = texto_txt.split(" ")
    #print(diff_words)
    # Separando palabras distintas y guardandolas en otra lista
    words = set(diff_words)
    return len(words)

# Comenzando las rutinas

# Se necesita chequear el ingreso de argumentos
if len(sys.argv) != 2:
    print("Por favor ingresar el archivo a procesar.")
    sys.exit(1)

# Se utiliza la funcion open, con el metodo read para guardar el contenido en la variable.
#with open(sys.argv[1], "r") as file:
with open("lorem_ipsum.txt", "r") as file:
    texto_txt = file.read()

#Ejecutando funciones
chars = find_chars(texto_txt)
words = count_words(texto_txt)

#Mostrando resultados.
print(f"El número de caracteres distintos es: {chars}")
print(f"El número de palabras distintas es: {words}")
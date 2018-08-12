#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo:
Generar un archivo de texto (pass.txt) con al menos 10 mil de contraseñas
que cumpla con los los siguientes requerimientos:
1. Al menos un caracter entre [a-z]
2. Al menos un numero entre [0-9]
3. Al menos una letra mayuscula entre [A-Z]
4. Al menos un caracter de los siguientes simbolos [$#@]
5. Longitud mínima de 8 caracteres
6. Longitud máxima de 20 caracteres

El archivo no debe de contener ninguna contraseña repetida
"""
# librerías
import random

# función main
def main():
    # palabras claves
    palabras_claves = ["juan", "lopez", "metallica", "2000"]

    # generar passwords
    passwords = generar_pass(palabras_claves)

    # print
    #print(passwords)

    # guardar las contraseñas al archivo pass.txt
    text_file = open("data/pass.txt", "w")
    text_file.write("\n".join(passwords))
    text_file.close()


def generar_pass(array_de_palabras_claves):
    """
    """
    # numero de palabras
    no_palabras = len(array_de_palabras_claves)

    # longitud de cada palabra
    no_longitudes = [len(x) for x in array_de_palabras_claves]

    # declarar el arreglo para guardar los passwords
    array_passwords_generados = []

    # número mínimo de passwords
    no_passwords = 1
    for element in array_de_palabras_claves:
        no_passwords*=len(element)

    # ciclo para genear los passwords
    counter = 0
    while counter < no_passwords:
        for palabra in array_de_palabras_claves:
            # declarar la variable para guardar el pwd
            pwd = ""

            # ciclo
            for letra in palabra:
                pwd+= array_de_palabras_claves[random.randint(0,len(array_de_palabras_claves)-1)][:random.randint(0,len(palabra)-1)]

            # evitar que los passwords sean repetidos
            if pwd in array_passwords_generados:
                pass
            else:
                # agregar passord a array_passwords_generados
                array_passwords_generados.append(pwd)
                print("\n",pwd)
                counter += 1

    # regresar el arrreglo de passwords
    return array_passwords_generados

if __name__ == '__main__':
    main()

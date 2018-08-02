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
    # cadena de carácteres
    caracteres = "abcdefghijklmnospqrstuvwxyzABCDEFGHIJKLMNOSPQRSTUVWXYZ1234567890$#@"

    # solicitar al usuario el número de contraseñas y la longitud de las mismas
    numero, longitud = input("Número Longitud ").split()

    # convertir a enteros los valores del usuario
    numero = int(numero)
    longitud = int(longitud)

    # declarar el arreglo que va a guardar las contraseñas
    arreglo_password = []

    # ciclo para generar las contraseñas
    counter = 0
    while counter < numero:
        # generar pwd
        password = "".join(random.sample(caracteres, longitud))

        # validación del pwd
        if validacion(password):

            # verificar si el pwd ya fue generado
            if password in arreglo_password:
                pass
            else:
                arreglo_password.append(password)
                counter += 1
                print("{} : {}".format(counter, password))

    # guardar las contraseñas al archivo pass.txt
    text_file = open("pass.txt", "w")
    text_file.write("\n".join(arreglo_password))
    text_file.close()

# función para verificar los requerimientos de las contraseñas
def validacion(pwd):
    """
    Validación de cada una de las contraseñas que se generan
    param: pwd: contraseña que se desea validar
    """
    # constantes
    isMayuscula = False
    isNumero = False
    isSimbolo = False
    isMinuscula = False
    long_min = 8
    long_max = 20

    # ciclo de validación
    if len(pwd) >= long_min and len(pwd) <= long_max:
        for letra in pwd:
            if letra in "abcdefghijklmnospqrstuvwxyz":
                isMinuscula = True
            if letra in "ABCDEFGHIJKLMNOSPQRSTUVWXYZ":
                isMayuscula = True
            if letra in "1234567890":
                isNumero = True
            if letra in "$#@":
                isSimbolo = True
            if isMinuscula and isMayuscula and isNumero and isSimbolo:
                return True
    else:
        return False

if __name__ == '__main__':
    main()

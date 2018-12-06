#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Info:
Script que permite la codificación y decoficación de una frase
por medio del método de Caeser Cipher https://cryptii.com/caesar-cipher

La transformación se puede representar mediante la alineación de dos secuencias
del alfabeto, el alfabeto de cifrado es el alfabeto simple firado hacia la
izquierda o hacia la derecha por un número determinado de posiciones.

Ejmplo:
cigrado Caeser Cipher usando una rotación de tres posiciones a izquierda, lo
cual equivale a un desplazamiento de 23 posiciones a la derecha, el parámetro
de cambio se utiliza como clave:

Normal:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cifrado:   XYZABCDEFGHIJKLMNOPQRSTUVW

Al encriptar, una persona busca cada letra del mensaje en la línea "normal"
y anota la letra correspondiente en la línea de "Cifrado".


Texto Normal:  TALLER DE PROGRAMACION EN PYTHON
Texto Cifrado: QXIIBO AB MOLDOXJXZFLK BK MVQELK
"""

# librerías
import string
import os

def main():
    # variable de control
    isRunning = True

    # ciclo while
    while isRunning:
        # limpiar pantalla
        os.system("clear")

        # imprimir el menú
        imprimir_menu()

        # opción del usuario
        accion_usuario = int(input("Opción: "))

        # validar input del usuario
        if accion_usuario > 0 and accion_usuario < 5:
            # validación codificar
            if accion_usuario == 1:
                frase_usuario = input("Ingresa tu frase a codificar: ")
                clave_usuario = int(input("Número de codificación: "))
                print("*** FR4S3 C0D1F1C4D4: ***\n\n",codificar(frase_usuario, clave_usuario))
                u = input("\nPresiona enter para continuar...")
            elif accion_usuario == 2:
                frase_usuario = input("Ingresa tu frase a decodificar: ")
                clave_usuario = int(input("Número de decodificación: "))
                print("*** FR4S3 D3C0D1F1C4D4: ***\n\n",decodificar(frase_usuario, clave_usuario))
                u = input("\nPresiona enter para continuar...")
            elif accion_usuario == 3:
                frase_usuario = input("Ingresa tu frase para usar fuerza bruta: ")
                print("*** FU3RZ4 BRUT4: ***\n", fuerza_bruta(frase_usuario))
                u = input("\nPresiona enter para continuar...")
            elif accion_usuario == 4:
                os.system("clear")
                isRunning = False
            else:
                pass
        else:
            print("Acción invalida")


def imprimir_menu():
    print("* * * * * * * * * * * * * * * * * * * * * * * *")
    print("*                                             *")
    print("*     Script para codificar y decodificar     *")
    print("*     mensajes utilizando el método de        *")
    print("*     Caeser Cipher                           *")
    print("*     1. Codificar                            *")
    print("*     2. Decodificar                          *")
    print("*     3. Fuerza bruta                         *")
    print("*     4. Salir                                *")
    print("*                                             *")
    print("* * * * * * * * * * * * * * * * * * * * * * * *")
    print("\n")

def codificar(frase, clave):
    """
    param: frase: texto que se desea convertir
    param: clave: número de posiciones para realizar la codificación
    """

    # Create a placeholder list
    encrypted_text = list(range(len(frase)))

    alphabet = string.ascii_lowercase

    # Create shifted alphabet
    first_half = alphabet[:clave]
    second_half = alphabet[clave:]
    shifted_alphabet = second_half+first_half

    for i,letter in enumerate(frase.lower()):

        # Check for spaces or punctuation
        if letter in alphabet:
            # Find the original index position
            original_index = alphabet.index(letter)

            # Shifted letter
            new_letter = shifted_alphabet[original_index]

            encrypted_text[i] = new_letter

        # Punctuation or space
        else:
            encrypted_text[i] = letter

    return ''.join(encrypted_text)

def decodificar(frase, clave):
    """
    param: frase: texto que se desea convertir
    param: clave: número de posiciones para realizar la decodificación
    """

    # Create a placeholder list
    decrypted_text = list(range(len(frase)))

    alphabet = string.ascii_lowercase

    # eCreate shifted alphabet
    first_half = alphabet[:clave]
    second_half = alphabet[clave:]
    shifted_alphabet = second_half+first_half

    for i,letter in enumerate(frase.lower()):

        # Check for spaces or punctuation
        if letter in alphabet:
            # Find the original index position
            index = shifted_alphabet.index(letter)

            # Shifted letter
            original_letter = alphabet[index]

            decrypted_text[i] = original_letter

        # Punctuation or space
        else:
            decrypted_text[i] = letter

    return ''.join(decrypted_text)

def fuerza_bruta(frase):
    """
    param: texto que se desea convertir
    """
    # ciclo de fuerza bruta
    for n in range(26):
        print('Valor: {} Frase: {}'.format(n, decodificar(frase,n)))
        print('\n')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

De una serie de datos del 1 al 100, realizar
las siguientes acciones:

1. Imprimir la sumatoria de los numeros pares.
2. Imprimir la sumatoria de los numeros divisibles entre 5
3. Imprimir el promedio de los numeros divisibles entre 7
4. Imprimir el promedio de los numeros que sean divisibles entre 2, 5, y 7.
"""

# variables
sumatoria_pares              = []
sumatoria_divisibles_5       = []
sumatoria_divisibles_7       = []
sumatoria_divisibles_2_5_7   = []

# ciclo for
for i in range(1,101):
    if i % 2 == 0:
        sumatoria_pares.append(i)
    if i % 5 == 0:
        sumatoria_divisibles_5.append(i)
    if i % 7 == 0:
        sumatoria_divisibles_7.append(i)
    if i % 2 == 0 and i % 5 == 0 and i % 7 == 0:
        sumatoria_divisibles_2_5_7.append(i)

print("Sumatoria de los numeros pares: ", sum(sumatoria_pares))
print("Sumatoria de los numeros divisibles entre 5: ", sum(sumatoria_divisibles_5))
print("Promedio de los numeros divisibles entre 7: ", sum(sumatoria_divisibles_7) / len(sumatoria_divisibles_7))
print("Promedio de los numeros divisibles entre 2, 5 y 7: ", sum(sumatoria_divisibles_2_5_7) / len(sumatoria_divisibles_2_5_7))

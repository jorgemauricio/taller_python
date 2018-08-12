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
Generar un script el cual pueda tenerminar cuantos correos a recibido
tu instructor desde el 2013-01-02 hasta el 2018-06-23 por parte
de 3 destinatarios:

- Masha de Coding Blonde
- Natalie Franke
- No One Corp

Los emails estan almacenados en la carpeta data/folders.zip,
"""
# librerías
import os


# def main():
#
#     # declarar la fecha inicial
#     fecha_inicial    = "2013-01-01"
#
#     anio, mes, dia   = fecha_inicial.split("-")
#
#     anio             = int(anio)
#     mes              = int(mes)
#     dia              = int(dia)
#
#     dia_del_mes      = 0
#
#     count_masha      = 0
#     count_natalie    = 0
#     count_corp       = 0
#
#     fecha            = 0
#
#     for i in range(1999):
#         if mes in [1,3,5,7,8,10,12]:
#             dia_del_mes = 31
#         elif mes in [4,6,9,11]:
#             dia_del_mes = 30
#         elif mes == 2:
#             if anio % 4 == 0:
#                 dia_del_mes = 29
#             else:
#                 dia_del_mes = 28
#         dia += 1
#         if dia > dia_del_mes:
#             dia = 1
#             mes += 1
#             if mes > 12:
#                 mes = 1
#                 anio += 1
#             fecha = "{:04d}-{:02d}-{:02d}".format(anio, mes, dia)
#         else:
#             fecha = "{:04d}-{:02d}-{:02d}".format(anio, mes, dia)
#
#         # checar contenido del email.txt
#         with open("data/folders/{}/email.txt".format(fecha), "r") as f:
#             file = f.read()
#             if "Masha" in file:
#                 count_masha += 1
#             elif "Natalie" in file:
#                 count_natalie += 1
#             elif "Corp" in file:
#                 count_corp += 1
#             else:
#                 pass
#             f.close()
#
#     print("Masha: {}".format(count_masha))
#     print("Natalie: {}".format(count_natalie))
#     print("Corp: {}".format(count_corp))

def main():

    count_masha      = 0
    count_natalie    = 0
    count_corp       = 0

    arr_folders = [x for x in os.listdir("data/folders") if x.endswith("")]
    for fecha in arr_folders:
        # checar contenido del email.txt
        with open("data/folders/{}/email.txt".format(fecha), "r") as f:
            file = f.read()
            if "Masha" in file:
                count_masha += 1
            elif "Natalie" in file:
                count_natalie += 1
            elif "Corp" in file:
                count_corp += 1
            else:
                pass
            f.close()

    print("Masha: {}".format(count_masha))
    print("Natalie: {}".format(count_natalie))
    print("Corp: {}".format(count_corp))


if __name__ == '__main__':
    main()

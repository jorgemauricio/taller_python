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
Escribe un programa que calcule el valor neto de una cuenta de banco basado
en las transacciones que se ingresan en la consola de comandos.

Ej:
	D 200
	D 250
	P 300
	D 100
	P 200
	Donde:
	D = Deposito
	P = Pago

Resultado:
	50
"""

#librerías
import os

def main():

	# constantes
	status          = True
	cuenta_banco    = 0
	arr_log         = []

	# ciclo while
	while status:
		# limpiar pantalla
		os.system("clear")

		# imprimir menú
		imprimir_menu()

		# instrucción del usuario
		transaccion, dinero = input("Transacción: ").split()

		if transaccion.upper() == "EXIT" and dinero.upper() == "BANK":
			print("Cuenta de banco con: {}".format(cuenta_banco))
			break
		elif transaccion.upper() == "D":
			cuenta_banco += int(dinero)
			arr_log.append("{} {}".format(transaccion, dinero))
		elif transaccion.upper() == "P":
			if cuenta_banco - int(dinero) < 0:
				print("Fondos insuficientes")
				arr_log.append("{} {}".format(transaccion, dinero))
			else:
				cuenta_banco -= int(dinero)
				arr_log.append("{} {}".format(transaccion, dinero))
		elif transaccion.upper() == "LOG" and dinero.upper() == "BANK":
			print("\n".join(arr_log))
			u = input("Presiona Enter para continuar...")
		else:
			print("Error")

def imprimir_menu():
    print("* * * * * * * * * * * * * * * * * * * * * * * *")
    print("*                                             *")
    print("*     Script para depositar y retirar dinero  *")
    print("*     de tu cuenta bancaria                   *")
    print("*     Para depositar incluye D y el           *")
    print("*     Para pagar incluye P y el monto         *")
    print("*     Para ver tu historia LOG BANK           *")
    print("*     Para salir teclea EXIT BANK             *")
    print("*     Ejem. Deposito de 200 pesos             *")
    print("*     D 200                                   *")
    print("*     Ejem. Pagar 100 pesos                   *")
    print("*     P 100                                   *")
    print("*                                             *")
    print("* * * * * * * * * * * * * * * * * * * * * * * *")
    print("\n")

if __name__ == '__main__':
	main()

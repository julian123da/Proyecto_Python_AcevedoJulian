# ################################
# ### Proyecto Python ##########
# ################################

import json
from Gestion_Datos import *
from Mis_funciones import *
from tabulate import tabulate
import datetime

listaGastos = abrirJSON()

booleano = True
while (booleano == True):
    menuPrincipal()
    opcionNumeria = int(input("Selecciona tu opcion: "))
    if opcionNumerica == 1:
        primerMenu()
        monto = float(input("Ingresa el monto del gasto: "))
        categoria = input('Ingresa el apellido del usuario: ')
        descripcion = input("(opcional) Añade la descripcion de tu gasto: ")
        dic1 = {
            "id":1, "monto": monto, "categoria": categoria, "descripcion": descripcion
        }
        listaGastos['gastos'].append(dic1)
        guardarJSON(listaGastos)
        table = listaGastos
        print(tabulate(table))
    # table = lista
    # print (tabulate(lista))

    #Desrrollado por Julian David Acevedo Gomez TI 1.097.100.290
# ################################
# ### Proyecto Python ##########
# ################################

import json
from Gestion_Datos import *
from Mis_funciones import *
from tabulate import tabulate
import datetime

listaGastos = abrir(JSON)


booleano = True
while (booleano == True):
    menuPrincipal()
    opcionNumerica = int(input("Selecciona tu opcion: "))
    if opcionNumerica == 1:
        primerMenu()
        monto = input("INgresa el nombre del usuario: ")
        categoria = input('Ingresa el apellido del usuario: ')
        descripcion = input("(opcional Añade la descripcion de tu gusto:)")
        dic1 = {
            "id":1, "monto": monto, "categoria": categoria, "descripcion": descripcion
        }
        listaGastos['gastos']. append(dic1)
        guardarJSON(listaGastos)
        print (tabulate(listaGastos))
        # table = lista
        # print (tabulate(lista))

        #Desrrollado por Julian David Acevedo Gomez TI 1.097.100.290
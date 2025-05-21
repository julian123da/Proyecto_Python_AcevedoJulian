# ################################
# ### Proyecto Python ##########
# ################################

# Se importa la informacion al archivo principal
import json
from Gestion_Datos import *
from Mis_funciones import *
from tabulate import tabulate
import datetime

listaGastos = abrirJSON()

booleano = True 
while (boolano == True):
    menuPrincipal()
    opcionNumerica = int(input("Selecciona tu opcion: "))
    if (opcionNumerica == 1):
        primerMenu()
        monto = float(input("Ingrese el monto de gasto: "))
        categoria = input('Ingresa el tipo de gasto (ejem: trasnporte, comida, ): ')
        descripcion = input("(opconal) Añade la descripcion de tu gasto: ")
        fecha = input("Ingresa la fecha del gasto realizado")
        dic1 = {
            "id":1, "monto": monto, "categoria": categoria, "descripcion": descripcion
        }
        listaGastos['gastos'].append(dic1)
        guardarJSON(listaGastos)
        table = mostrarGastos(listaGastos)
        print(tabulate(table))
    if (opcionNumerica == 2):
        segundoMenu()

    if (opcionNumerica == 3):
        tercerMenu()    

    if (opcionNumerica == 4):
        cuartoMenu

    if (opcionNumerica == 8):
        booleano = False

    # table = lista
    # print (tabulate(lista))

    # Desarrollado por Julian David Acevedo Gomez T.I 1.097.100.290
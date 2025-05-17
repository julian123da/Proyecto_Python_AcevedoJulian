# ################################
# ### Proyecto Python ##########
# ################################

import json
from Gestion_Datos import *
from Mis_funciones import *

print("=========================================")
print("       Simulador de Gasto Diario         ")
print("=========================================")
print("Seleccione una opcion: ")
print("")
print("1.Registrar nuevo gasto")
print("2.Lsta de gastos")
print("3.Calcular total de gastos")
print("4.Generar reporte de gastos")
print("5.Salir")
print("=========================================")
opcionUsuario=int(input())

if (opcionUsuario==1):
    print("=====================================")
    print("      Registar Gastos Nuevos         ")
    print("=====================================")
    print("")
    print("Ingrese la informacion del gasto")

    montoNuevo=input("Monto del gasto: ")
    categoriaNueva=input("Categoria: ")
    descripcionNueva=input("Descripcion (opcional):")
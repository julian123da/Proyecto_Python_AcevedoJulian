from Gestion_Datos import *

# Funciones por medio de menús
def menuPrincipal():
    print('''==================================
        Simulador de Gasto Diario
=====================================
        Seleccione una opcion:
        1. Registrar nuevo gasto
        2. Consultar gasto
        3. Actualizar gasto
        4. Eliminar gasto
        5. Listar gasto
        6. Calcular total de gastos
        7. Generar reporte de gastos
        8. Salir
======================================''')

def primerMenu():
    print('''
========================================
        Registrar Nuevo Gasto
=======================================
        Ingrese la informacion del gasto
        
        - Monto del gasto
        - Categoria (ej. Comida, Transporte, Entretenimiento, otros):
        - Descripcion (opcional):

        Ingrese 's' para guardar o 'c' para cancelar.
===============================================''')

def segundoMenu():
    print('''
==================================
        Listar de Gastos
=================================
        Seleccione una opcion para filtrar los gastos:
        
        1. Ver todos los gastos
        2. Filtrar por categoria
        3. Filtrar por rango de fechas
        4. Regresar al menu principal
        
=================================''')

def tercerMenu():
    print('''
=====================================
        Calcular Total de gastos
=====================================
        Seleccione el periodo de calculo:
        
        1. Calcular total diario
        2. Calcular total semanal
        3. Calcular total mensual
        4. Regresar al menu principal
=======================================''')

def cuartoMenu():
    print('''
======================================
        Generar reporte de gastos
======================================
        Seleccione el tipo de reporte:
        
        1. Reporte diario
        2. Reporte semanal
        3. Reporte mensual
        4. Regresar al menu principal
=====================================''')

def salida():
    print("¿Deseas salir del programa? (S/N):")

def resultadosGastos(dict_gastos):
    listaGastos = dict_gastos["gastos"]
    id_buscado = len(listaGastos)  # Asumiendo que buscas por el último ID
    
    for i in range(len(listaGastos)):
        if (id_buscado == listaGastos[i]["id"]):
            resultado = [
                ['id', listaGastos[i]["id"]], 
                ["monto", listaGastos[i]["monto"]], 
                ["categoria", listaGastos[i]["categoria"]]
            ]
            return resultado
    return None  # Si no se encuentra el gasto

def total(listaGastos, id_buscado):
    total_monto = 0
    
    for i in range(len(listaGastos)):
        if (id_buscado == listaGastos[i]["id"]):
            total_monto += listaGastos[i]["monto"]
            
    return total_monto
              
from Gestion_Datos import *
from tabulate import tabulate

# Mostrar lista de gastos en formato tabla
def imprimirGastos(lista):
    print(tabulate(lista, headers="keys", tablefmt="fancy_grid"))

def actualizarRegistro():
    data = abrirJSON()
    registros = data["gastos"]

    id_buscar = int(input("Escribe el ID del gasto que quieres modificar: "))
    for i in range(len(registros)):
        if id_buscar == registros[i]["id"]:
            nuevo_valor = float(input("Nuevo monto del gasto: "))
            nueva_categoria = input("Tipo de gasto (ej. transporte, comida...): ")
            nueva_nota = input("Descripción nueva: ")
            nueva_fecha = input("Nueva fecha (dd-mm-aaaa): ")

            entrada_modificada = {
                "id": id_buscar,
                "monto": nuevo_valor,
                "categoria": nueva_categoria,
                "descripcion": nueva_nota,
                "fecha": nueva_fecha
            }

            registros[i] = entrada_modificada
            data["gastos"] = registros
            guardarJSON(data)
            break

def borrarRegistro():
    data = abrirJSON()
    registros = data["gastos"]

    id_borrar = int(input("Escribe el ID del gasto que quieres eliminar: "))
    for i in range(len(registros)):
        if id_borrar == registros[i]["id"]:
            registros.pop(i)
            break

    data["gastos"] = registros
    guardarJSON(data)
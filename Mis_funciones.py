import json

def menuPrincipal ():
    print('''==================================
        Simulador de Gasto Diario 
        =====================================
        Seleccione un opcion:
        1.Registrar nuevo gasto
        2.Consultar gasto
        3.Actualizar gasto
        4.Eliminar gasto
        5.Listar gasto
        6.Calcular total de gastos
        7.Generar reporte de gastos
        8.Salir
        ======================================''')
    
def primerMenu ():
    print('''
        ========================================
        Registar Nuevo Gasto
        =======================================
        Ingrese la infomacion del gasto
          
        -Monto del gasto
        -Categoria (ej. Comida, Trasnporte, Entretenimiento, otros):
        -Descripcion (opcional):

        Ingrese 's' para guardar o 'c' para cancelar.
        ===============================================''')
    
def segundoMenu ():
        print('''
        ==================================
            istar de Gastos 
            =================================
            Seleccione una opcion para filtrar los gastos:

            1.Ver todos los gastos
            2.Filtrar por categoria
            3.Filtrar por rango de fechas
            4.Regresar al menu principal
              =================================''')
        
def tercerMenu ():
            print('''
                =====================================
                Calcular Total de gastos 
                =====================================
                Seleccione el periodo de calculo:
                  
                1.Calcular total diario
                2.Calcular total semanal
                3.Calcular total mensual
                4.Regresar al menu principal
                =======================================''')
            

def cuartoMenu ():
       print('''
             ======================================
             Generar reporte de gastos 
             ======================================
             Seleccione el tipo de reporte:
             
             1.Reporte diaro
             2.Reporte semanal
             3.Reporte mensaual
             4.Regresar al menu principal
             =====================================''')
       
def salida ():
       print("¿Deseas salir del programa? (S/N):")

def resultadosGastos(dict):
       listaGastos=dict["gastos"]
       id = len(listaGastos)
       for i in range (len(listaGastos)):
              if (id == listaGastos[i]["id"]):
                     dict = [['id', listaGastos[i]["id"]],["monto", listaGastos[i]["monto"], ["categoria", listaGastos]]]
                     return dict
              
def total():
       listaGastos = G
       for i in range (len(listaGastos)):
              if id = (listaGastos[i] ["id"])

    

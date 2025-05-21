from tabulate import tabulate # Instalamos tabulate para visualizar tablas estilizadas
#Esta es la interfaz del programa que verá el usuario

#Se utilizan funciones de operacionesBase para evitar llamarlas repetidamente como operacionesBase.agregar_transaccion()
"""
ESTA ES LA INTERFAZ QUE VE EL USUARIO: LOS MENÚS 

"""

from funciones.operacionesBase import *         
#Agrega una nueva transacción al archivo JSON
#Muestra todas las transacciones guardadas
#Suma las transacciones por día, semana o mes
#Crea un informe de transacciones y lo muestra o guarda                  
#Abre y carga el contenido del archivo JSON
#Verifica si el tipo de transacción ingresado es válido (alimentación, movilidad, etc.)               
#Carga solo los tipos existentes en el JSON   
# Importamos esta función para mostrar tipos reales


# Función que muestra el menú principal del programa
def mostrar_menu_inicial():
    print("""
=============================================
         Administrador Financiero Personal
=============================================
Seleccione una opción:

1. Registrar nueva transacción
2. Visualizar transacciones
3. Calcular totales de transacciones
4. Crear informe financiero
5. Salir
=============================================
""")

# Función para registrar una nueva transacción
def mostrar_menu_agregar_transaccion():   #  1 opción del menú inicial que es registrar la transacción
    print("""
=============================================
            Registrar Nueva Transacción
=============================================
Ingrese la información de la transacción:
""")
    try:#Se utiliza para controlar errores al digitar un número
        # Pedimos el valor al usuario 
        valor = float(input("- Valor de la transacción: $"))
        if valor <= 0:
            print("El valor debe ser mayor a 0\n")  #Se pide al usuario que ingrese un valor que debe ser mayor a 0
            return

        # Obtenemos los tipos disponibles y los mostramos
        tipos = cargar_tipos() 
        print(f"Tipos disponibles: {', '.join(tipos)}") #entra e imprime la lista de tipos disponibles
        
        # Pedimos el tipo
        tipo = input("- Tipo: ").strip().lower() #Limpia espacios y convierte a minúsculas lo que escribe el usuario
     
        # Verificamos que el tipo sea válido
        if not validar_tipo(tipo):
            tipos_str = ", ".join(cargar_tipos()) #accede a los tipos y el usuario debe escoger uno válido
            print(f"Tipo no válido. Tipos disponibles: {tipos_str}\n") #si el usuario no selecciona un tipo correcto mostrará error
            return #volverá a retornar hasta que el usuario ingrese un tipo correcto
    
        # Pedimos un detalle opcional
        detalle = input("- Detalle (opcional): ").strip() # no es obligatorio el detalle

        # Mostramos un resumen de la transacción para confirmar
        print(f"\nResumen de la transacción:")                                        #muestra un breve resumen de lo que el usuario ingresó
        print(f"Valor: ${valor}")                                                     #mostrará el valor, el tipo seleccionado
        print(f"Tipo: {tipo.title()}")                                                #y si dejó un detalle
        print(f"Detalle: {detalle if detalle else 'Sin detalle'}")                    # coloca el detalle si existe, sino muestra "Sin detalle"
    
        # Solicitamos confirmación para guardar
        confirmar = input("\nIngrese 's' para guardar o 'c' para cancelar: ").strip().lower() # se le pide al usuario que ingrese s para guardar y c para cancelar
        if confirmar == "s":
            agregar_transaccion(valor, tipo, detalle)
            print("¡Transacción registrada correctamente!\n")                        #al presionar s se guarda dentro del json
        else:
            print("Registro cancelado.\n")                                           #al presionar c no se guarda nada
    except ValueError:
        # Capturamos error si el usuario no ingresa un número válido
        print("El valor ingresado no es válido. Ingrese un número para el valor.\n") #muestra error si se ingresa un valor no numérico

# Función para mostrar el menú de listado de transacciones
"""
ESTA ES LA 2ª OPCIÓN DEL MENÚ PRINCIPAL
"""

def mostrar_menu_lista_transacciones():    
    print("""
=============================================         
           Visualizar Transacciones
=============================================
Opciones de filtrado:

1. Mostrar todas las transacciones
2. Filtrar por tipo
3. Filtrar por fecha
4. Volver al menú inicial
=============================================
""")

    try:
        opcion = input("Seleccione una opción (1/2/3/4): ").strip()

        if opcion == "1":
            # Mostrar todas las transacciones
            transacciones = listar_transacciones()            
            mostrar_transacciones_tabla(transacciones)
        elif opcion == "2":
            # Filtrar por tipo
            tipos = cargar_tipos()                                                   #muestra los tipos existentes
            print(f"Tipos disponibles: {', '.join(tipos)}")
            tipo = input("Ingrese el tipo a filtrar: ").strip().lower()              #solicita el tipo para filtrar
            if validar_tipo(tipo):                                                   #si ingresa un tipo correcto 
                transacciones = listar_transacciones(tipo=tipo)                      #mostrará las transacciones de ese tipo
                mostrar_transacciones_tabla(transacciones, f"Transacciones - Tipo: {tipo.title()}")    
            else:
                print("Tipo no válido.\n")
        elif opcion == "3": 
            # Filtrar por fecha
            fecha = input("Ingrese la fecha (YYYY-MM-DD) o presione enter para hoy: ").strip()
            transacciones = listar_transacciones(fecha=fecha if fecha else None)
            mostrar_transacciones_tabla(transacciones, f"Transacciones - Fecha: {fecha if fecha else 'hoy'}")
        elif opcion == "4":
            # Volver al menú inicial
            return
        else:
            print("Opción inválida.\n")

    except Exception as e:
        print(f"Error al listar transacciones: {e}\n")

# Función para mostrar una tabla con las transacciones
def mostrar_transacciones_tabla(transacciones, titulo="Todas las transacciones"):
    if not transacciones:
        print("No hay transacciones registradas.\n")
        return

    print(f"\n{titulo}")
    print("=" * 88)

    # Preparar datos para la tabla
    headers = ["Fecha", "Tipo", "Valor", "Detalle"]
    tabla_datos = []

    for transaccion in transacciones:
        tabla_datos.append([
            transaccion['fecha'],
            transaccion['tipo'].title(),
            f"${transaccion['valor']}",
            transaccion['detalle'] if transaccion['detalle'] else 'Sin detalle'
        ])  

    # Mostrar tabla usando tabulate para mejor visualización
    print(tabulate(tabla_datos, headers=headers, tablefmt="grid"))
    print(f"\nTotal de transacciones mostradas: {len(transacciones)}")
    print(f"Suma total: ${sum(transaccion['valor'] for transaccion in transacciones)}\n")

# Función para mostrar el menú de cálculo de totales
def mostrar_menu_calcular_totales():
    print("""
=============================================
      Calcular Totales de Transacciones
=============================================
Opciones de cálculo:

1. Total general
2. Total por tipo
3. Total diario
4. Total semanal
5. Total mensual
6. Volver al menú inicial
=============================================
""")
    try:
        opcion = input("Seleccione una opción (1/2/3/4/5/6): ").strip()

        if opcion == "1":
            # Calcular total general
            total = calcular_totales()
            print(f"\nTotal general de transacciones: ${total}\n")
        elif opcion == "2":
            # Calcular totales por tipo
            totales_tipo = calcular_totales(por_tipo=True)
            mostrar_totales_tipo(totales_tipo)
        elif opcion == "3":
            # Calcular total diario
            fecha = input("Ingrese la fecha (YYYY-MM-DD) o presione enter para hoy: ").strip()
            total = calcular_totales(periodo='diario', fecha=fecha if fecha else None)
            print(f"\nTotal del día: ${total}\n")
        elif opcion == "4":
            # Calcular total semanal
            total = calcular_totales(periodo='semanal')
            print(f"\nTotal de la semana: ${total}\n")
        elif opcion == "5":
            # Calcular total mensual
            total = calcular_totales(periodo='mensual')
            print(f"\nTotal del mes: ${total}\n")
        elif opcion == "6":
            # Volver al menú inicial
            return
        else:
            print("Opción no válida.\n")
    except Exception as e:
        print(f"Error al calcular totales: {e}\n")

# Función para mostrar totales de transacciones por tipo
def mostrar_totales_tipo(totales):
    if not totales:
        print("No hay transacciones registradas.\n")
        return
        
    print("\nTransacciones por tipo")
    print("=" * 50)

    headers = ["Tipo", "Valor", "Porcentaje"]
    tabla_datos = []
    total_general = sum(totales.values())

    for tipo, valor in totales.items():
        porcentaje = (valor / total_general * 100) if total_general > 0 else 0
        tabla_datos.append([
            tipo.title(),
            f"${valor}",
            f"{porcentaje:.2f}%"
        ])
        
    # Mostrar tabla de totales por tipo
    print(tabulate(tabla_datos, headers=headers, tablefmt="grid"))
    print(f"\nTotal general: ${total_general}\n")

# Función para mostrar menú de generación de informes
def mostrar_menu_generar_informes():
    print("""
=============================================
           Crear Informe Financiero
=============================================
Opciones de informe:

1. Informe completo (mostrar en pantalla)
2. Informe por período (mostrar en pantalla)
3. Guardar informe completo en archivo
4. Volver al menú inicial
=============================================
""")
 
    try:
        opcion = input("Seleccione una opción (1/2/3/4): ").strip()

        if opcion == '1':
            # Generar informe completo
            informe = generar_informe()
            print("\n" + informe)
        elif opcion == "2":
            # Generar informe por período
            periodo = input("Ingrese el período (diario/semanal/mensual): ").strip().lower()
            if periodo in ['diario', 'semanal', 'mensual']:
                informe = generar_informe(periodo=periodo)
                print("\n" + informe)
            else:
                print("Período no válido.\n")
        elif opcion == '3':
            # Guardar informe en archivo
            nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ").strip()
            if nombre_archivo:
                generar_informe(guardar_archivo=True, nombre_archivo=nombre_archivo)
                print(f"Informe guardado como '{nombre_archivo}.txt'\n")
            else:
                print("Nombre de archivo no válido.\n")
        elif opcion == "4":
            # Volver al menú inicial
            return
        else:
            print("Opción no válida.\n")
    except Exception as e:
        print(f"Error al generar informe: {e}\n")

# Función principal que ejecuta el programa
def main():
    print("Iniciando Administrador Financiero Personal...")
    cargar_datos()  # Carga de datos al inicio
    print("Datos cargados correctamente.\n")

    # Bucle principal del programa
    while True:
        mostrar_menu_inicial()
        opcion = input("Ingrese su opción (1/2/3/4/5): ").strip()

        if opcion == "1":
            mostrar_menu_agregar_transaccion()
        elif opcion == "2":
            mostrar_menu_lista_transacciones()
        elif opcion == "3":
            mostrar_menu_calcular_totales()
        elif opcion == "4":
            mostrar_menu_generar_informes()
        elif opcion == "5":
            print("¡Gracias por usar el Administrador Financiero Personal!")
            print("Todos los datos fueron guardados.")
            break
        else:
            print("Opción no válida. Por favor seleccione nuevamente.\n")
   
# Este bloque verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
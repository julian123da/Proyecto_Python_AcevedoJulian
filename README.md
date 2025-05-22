Simulador de Gasto Diario

Aplicación en consola para registrar, consultar y gestionar tus gastos personales de forma sencilla y organizada.

Descripción

Este simulador permite registrar gastos diarios junto con su categoría, descripción y fecha. Ofrece opciones para visualizar, filtrar y eliminar gastos, así como calcular el total gastado. Los datos se almacenan de forma persistente en un archivo JSON.

Problemática

Los usuarios necesitan una herramienta que les permita:
	•	Registrar gastos de forma rápida y organizada
	•	Consultar todos los movimientos realizados
	•	Filtrar gastos por categoría o fecha
	•	Calcular el total de dinero gastado en un periodo
	•	Eliminar registros innecesarios o erróneos

Instalación

Requisitos
	•	Python 3.7 o superior
	•	Biblioteca externa: tabulate

Instalación de dependencias.

pip install tabulate

python simulador.py

simulador_gastos/
├── simulador.py         # Archivo principal con toda la lógica del programa
└── datos.json           # Archivo donde se almacenan los gastos (se crea automáticamente)
Funcionalidades

Registro de gastos
	•	Ingreso de categoría, monto, descripción y fecha
	•	Validación de formatos (números, fechas)

Visualización de gastos
	•	Listado completo en formato tabular
	•	Vista clara y ordenada de los datos ingresados

Filtros
	•	Filtrado por categoría
	•	Filtrado por rango de fechas

Cálculos
	•	Suma total de todos los gastos registrados

Eliminación
	•	Eliminación de registros individuales mediante índice
	•	Confirmación tras la eliminación

Persistencia
	•	Todos los datos se guardan automáticamente en un archivo JSON
	•	La información se conserva entre ejecuciones

Uso
	1.	Ejecutar el programa desde la terminal
	2.	Seleccionar una opción del menú (registrar, listar, filtrar, eliminar, etc.)
	3.	Ingresar los datos requeridos según la opción elegida
	4.	Consultar o modificar la información según sea necesario

El programa valida entradas incorrectas e informa al usuario sobre errores como fechas mal formateadas o índices fuera de rango.

Licencia

https://youtu.be/-Kogu3KAEqg

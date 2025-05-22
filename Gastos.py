import json
import os
from datetime import date, datetime, timedelta

# Ruta relativa a un archivo
def ruta_relativa(nombre_archivo):
    return nombre_archivo

# Cargar categorías desde JSON o usar por defecto
def obtener_categorias():
    try:
        ruta = ruta_relativa("categorias.json")
        if os.path.isfile(ruta):
            with open(ruta, 'r') as archivo:
                info = json.load(archivo)
                return info.get("categorias", [])
    except Exception as error:
        print(f"No se pudo cargar categorías: {error}")
    return ["alimentación", "movilidad", "ocio", "varios"]

# Verificar si la categoría ingresada es válida
def es_categoria_valida(nombre_categoria):
    return nombre_categoria in obtener_categorias()

# Leer gastos desde archivo JSON
def leer_gastos():
    ruta = ruta_relativa("gastos.json")
    try:
        if os.path.exists(ruta):
            with open(ruta, 'r') as archivo:
                return json.load(archivo)
    except Exception as error:
        print(f"Error al leer archivo de gastos: {error}")
    return []

# Guardar gastos en archivo
def escribir_gastos(lista_gastos):
    ruta = ruta_relativa("gastos.json")
    try:
        with open(ruta, 'w') as archivo:
            json.dump(lista_gastos, archivo, indent=2)
        print("Información almacenada correctamente.")
    except Exception as error:
        print(f"No se pudo guardar la información: {error}")

# Agregar un nuevo gasto
def agregar_gasto(valor, tipo, nota=""):
    try:
        gastos = leer_gastos()
        nuevo = {
            "fecha": date.today().isoformat(),
            "tipo": tipo,
            "valor": valor,
            "nota": nota
        }
        gastos.append(nuevo)
        escribir_gastos(gastos)
        return nuevo
    except Exception as error:
        print(f"No se pudo agregar gasto: {error}")
        return None

# Filtrar gastos opcionalmente por tipo y fecha
def filtrar_gastos(tipo=None, fecha=None):
    try:
        registros = leer_gastos()
        if tipo:
            registros = [g for g in registros if g["tipo"] == tipo]
        if fecha:
            try:
                fecha_valida = datetime.strptime(fecha, "%Y-%m-%d").date().isoformat()
                registros = [g for g in registros if g["fecha"] == fecha_valida]
            except ValueError:
                hoy = date.today().isoformat()
                registros = [g for g in registros if g["fecha"] == hoy]
        return registros
    except Exception as error:
        print(f"Error al filtrar gastos: {error}")
        return []

# Calcular el total, con posibilidad de agrupar
def resumen_gastos(intervalo=None, fecha=None, dividir_por_tipo=False):
    try:
        registros = leer_gastos()
        hoy = date.today()

        if intervalo:
            if intervalo == "diario":
                fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date() if fecha else hoy
                registros = [g for g in registros if g["fecha"] == fecha_obj.isoformat()]
            elif intervalo == "semanal":
                inicio = hoy - timedelta(days=hoy.weekday())
                fin = inicio + timedelta(days=6)
                registros = [g for g in registros if inicio.isoformat() <= g["fecha"] <= fin.isoformat()]
            elif intervalo == "mensual":
                registros = [g for g in registros if g["fecha"].startswith(hoy.strftime("%Y-%m"))]

        if dividir_por_tipo:
            totales = {}
            for g in registros:
                tipo = g["tipo"]
                totales[tipo] = totales.get(tipo, 0) + g["valor"]
            return totales
        else:
            return sum(g["valor"] for g in registros)
    except Exception as error:
        print(f"No se pudo calcular resumen: {error}")
        return {} if dividir_por_tipo else 0

# Crear reporte con opción de guardarlo
def crear_reporte(intervalo=None, guardar=False, nombre="reporte_financiero"):
    try:
        registros = leer_gastos()
        hoy = date.today()

        if intervalo:
            if intervalo == "diario":
                registros = [g for g in registros if g["fecha"] == hoy.isoformat()]
                subtitulo = f"Fecha: {hoy.isoformat()}"
            elif intervalo == "semanal":
                inicio = hoy - timedelta(days=hoy.weekday())
                fin = inicio + timedelta(days=6)
                registros = [g for g in registros if inicio.isoformat() <= g["fecha"] <= fin.isoformat()]
                subtitulo = f"Semana: {inicio.isoformat()} a {fin.isoformat()}"
            elif intervalo == "mensual":
                registros = [g for g in registros if g["fecha"].startswith(hoy.strftime("%Y-%m"))]
                subtitulo = f"Mes: {hoy.strftime('%Y-%m')}"
        else:
            subtitulo = "Todos los registros"

        reporte = []
        reporte.append("=" * 60)
        reporte.append(f"{'REPORTE FINANCIERO':^60}")
        reporte.append(f"{subtitulo:^60}")
        reporte.append("=" * 60)

        if not registros:
            reporte.append("No se encontraron registros.")
        else:
            total = sum(g["valor"] for g in registros)
            reporte.append(f"\nTotal: ${total:.2f}")
            reporte.append(f"Cantidad de registros: {len(registros)}")

            reporte.append("\nPor categoría:")
            categorias = {}
            for g in registros:
                categorias[g["tipo"]] = categorias.get(g["tipo"], 0) + g["valor"]
            for cat, val in categorias.items():
                porcentaje = (val / total) * 100 if total else 0
                reporte.append(f" - {cat.title()}: ${val:.2f} ({porcentaje:.1f}%)")

            reporte.append("\nDetalle de gastos:")
            reporte.append(f"{'Fecha':<12} {'Tipo':<15} {'Valor':<10} {'Nota':<20}")
            reporte.append("-" * 60)
            for g in sorted(registros, key=lambda x: x["fecha"]):
                reporte.append(f"{g['fecha']:<12} {g['tipo']:<15} ${g['valor']:<9.2f} {g['nota']:<20}")

        reporte.append("=" * 60)
        reporte.append(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        resultado = "\n".join(reporte)

        if guardar:
            try:
                with open(ruta_relativa(f"{nombre}.txt"), 'w', encoding='utf-8') as archivo:
                    archivo.write(resultado)
                print(f"Reporte guardado como {nombre}.txt")
            except Exception as error:
                print(f"No se pudo guardar el reporte: {error}")

        return resultado
    except Exception as error:
        return f"Error al generar reporte: {error}"

import csv
import os

def leer_csv(ruta_archivo):
    datos = []
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta = os.path.join(carpeta_actual, ruta_archivo)
    
    if not os.path.exists(ruta_absoluta):
        ruta_absoluta = os.path.join(os.path.dirname(carpeta_actual), ruta_archivo)

    try:
        with open(ruta_absoluta, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            encabezados = lector.fieldnames
            for fila in lector:
                if 'Attack' in fila: fila['Attack'] = int(fila['Attack'])
                if 'Defense' in fila: fila['Defense'] = int(fila['Defense'])
                datos.append(fila)
        print(f"Archivo CSV leído con éxito desde: {ruta_absoluta}")
        return encabezados, datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en '{ruta_archivo}' ni en '{ruta_absoluta}'.")
        return None, None

def guardar_csv(nombre_archivo, encabezados, datos):
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    
    if "Tarea_Programada#1" in carpeta_actual:
        partes = carpeta_actual.split("Tarea_Programada#1")
        ruta_base = partes[0] + "Tarea_Programada#1"
    else:
        ruta_base = os.path.dirname(carpeta_actual)

    carpeta_salida = os.path.join(ruta_base, "output")
    
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    ruta_completa = os.path.join(carpeta_salida, nombre_archivo)

    with open(ruta_completa, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(datos)
        
    print(f"Guardado con éxito en: {ruta_completa}")
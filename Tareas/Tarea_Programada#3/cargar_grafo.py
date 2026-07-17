import json
import os

def cargar_grafo(ruta_archivo):
    """
    Valida la existencia del archivo y lo carga en un diccionario de Python.
    """
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        return None
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            grafo = json.load(archivo)
            
            # Validación de estructura básica
            if not isinstance(grafo, dict):
                print("Error: El archivo JSON debe contener un diccionario principal.")
                return None
            
            for pais, conexiones in grafo.items():
                if not isinstance(conexiones, dict):
                    print(f"Error: Las conexiones de '{pais}' deben ser un diccionario.")
                    return None
                for vecino, peso in conexiones.items():
                    if not isinstance(peso, (int, float)):
                        print(f"Error: El peso hacia '{vecino}' desde '{pais}' debe ser numérico.")
                        return None
            
            return grafo
    except json.JSONDecodeError:
        print("Error: El archivo no tiene un formato JSON válido.")
        return None
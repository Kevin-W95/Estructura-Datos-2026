import json
import os

def cargar_grafo(ruta_archivo):
    """
    Carga el grafo oficial de Street Fighter y lo convierte en una 
    lista de adyacencia (diccionario de diccionarios) compatible.
    """
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        return None
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            
            if "vertices" not in datos or "aristas" not in datos:
                print("Error: El JSON no contiene las llaves 'vertices' o 'aristas'.")
                return None
            
            grafo_formateado = {vertice: {} for vertice in datos["vertices"]}
            
            for arista in datos["aristas"]:
                origen = arista.get("origen")
                destino = arista.get("destino")
                peso = arista.get("peso")
                
                if origen in grafo_formateado:
                    grafo_formateado[origen][destino] = peso
            
            return grafo_formateado
            
    except json.JSONDecodeError:
        print("Error: El archivo no tiene un formato JSON válido.")
        return None
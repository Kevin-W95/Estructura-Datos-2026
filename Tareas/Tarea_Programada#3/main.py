import os
from cargar_grafo import cargar_grafo
from dijkstra import resolver_dijkstra
from tsp import resolver_tsp

def main():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_grafo = os.path.join(directorio_actual, "grafo.json")
    punto_partida = "Japón"
    
    print("="*55)
    print("SISTEMA DE PLANIFICACIÓN TÁCTICA - SHADALOO")
    print("="*55)
    print("Cargando mapas de inteligencia militar...")
    
    # Cargar y validar
    grafo = cargar_grafo(archivo_grafo)
    
    if grafo:
        print("¡Grafo cargado y verificado con éxito!")
        
        # Resolver Dijkstra (Camino más corto)
        resolver_dijkstra(grafo, inicio=punto_partida)
        
        # Resolver TSP (Ruta óptima)
        resolver_tsp(grafo, inicio=punto_partida)
        
        print("\n" + "="*55)
        print("Misión completada. Información enviada a M. Bison.")
        print("="*55)
    else:
        print("El programa se detuvo debido a errores en el archivo JSON.")

if __name__ == "__main__":
    main()
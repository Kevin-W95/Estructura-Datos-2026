def tsp_backtracking(grafo, inicio):
    """
    Resuelve el TSP de forma exacta visitando todos los nodos una vez y volviendo al inicio.
    """
    todos_paises = list(grafo.keys())
    mejor_ruta = []
    mejor_costo = float('inf')

    def buscar(nodo_actual, visitados, ruta_actual, costo_actual):
        nonlocal mejor_costo, mejor_ruta
        
        # Si ya visitamos todos los países del grafo
        if len(visitados) == len(todos_paises):
            vecinos_actual = grafo.get(nodo_actual, {})
            if inicio in vecinos_actual:
                costo_total = costo_actual + vecinos_actual[inicio]
                if costo_total < mejor_costo:
                    mejor_costo = costo_total
                    mejor_ruta = list(ruta_actual) + [inicio]
            return

        # Búsqueda en profundidad (DFS)
        vecinos_actual = grafo.get(nodo_actual, {})
        for vecino, peso in vecinos_actual.items():
            if vecino not in visitados and vecino in grafo:
                # Poda inteligente: si el costo supera el mejor costo actual, descartamos la rama
                if costo_actual + peso < mejor_costo:
                    visitados.add(vecino)
                    ruta_actual.append(vecino)
                    
                    buscar(vecino, visitados, ruta_actual, costo_actual + peso)
                    
                    # Backtracking
                    ruta_actual.pop()
                    visitados.remove(vecino)

    # Inicializar la búsqueda
    visitados_iniciales = {inicio}
    buscar(inicio, visitados_iniciales, [inicio], 0)
    
    return mejor_ruta, mejor_costo


def resolver_tsp(grafo, inicio="Japón"):
    """
    Imprime la ruta óptima para la gira de Shadaloo.
    """
    print("\n" + "="*55)
    print(f" PROBLEMA 2: GIRA MUNDIAL ÓPTIMA (TSP) DESDE {inicio.upper()}")
    print("="*55)
    
    if inicio not in grafo:
        print(f"Error: El país de inicio '{inicio}' no está en el mapa.")
        return
        
    ruta, costo = tsp_backtracking(grafo, inicio)
    
    if costo == float('inf') or not ruta:
        print("¡Imposible realizar la gira mundial! No existe una ruta cíclica válida para todos los países.")
    else:
        ruta_formateada = " -> ".join(ruta)
        print(f"Ruta óptima calculada:\n   {ruta_formateada}")
        print(f"Costo total de la gira: {costo}")
def dijkstra(grafo, inicio):
    """
    Encuentra los caminos más cortos desde el nodo inicial a todos los demás usando Dijkstra.
    """
    distancias = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    
    if inicio not in distancias:
        print(f"Error: El nodo inicial '{inicio}' no existe en el grafo.")
        return None, None
        
    distancias[inicio] = 0
    
    # Cola de prioridad manual usando una lista estándar 
    nodos_activos = [(0, inicio)]
    
    while nodos_activos:
        # Ordenamos para simular el comportamiento de una cola de prioridad
        nodos_activos.sort()
        distancia_actual, nodo_actual = nodos_activos.pop(0)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        vecinos = grafo.get(nodo_actual, {})
        for vecino, peso in vecinos.items():
            if vecino not in distancias:
                continue
                
            distancia_nueva = distancia_actual + peso
            
            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                predecesores[vecino] = nodo_actual
                nodos_activos.append((distancia_nueva, vecino))
                
    return distancias, predecesores


def reconstruir_camino(predecesores, destino):
    """
    Reconstruye la ruta de nodos seguidos desde el origen al destino.
    """
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual)
        actual = predecesores[actual]
    return camino


def resolver_dijkstra(grafo, inicio="Japón"):
    """
    Imprime los resultados de Dijkstra formateados.
    """
    print("\n" + "="*55)
    print(f" PROBLEMA 1: CAMINOS MÁS CORTOS DESDE {inicio.upper()}")
    print("="*55)
    
    distancias, predecesores = dijkstra(grafo, inicio)
    if not distancias:
        return
        
    for pais in distancias:
        if pais == inicio:
            continue
        
        distancia = distancias[pais]
        if distancia == float('inf'):
            print(f"{pais}: NO ES ALCANZABLE desde {inicio}.")
        else:
            camino = reconstruir_camino(predecesores, pais)
            ruta_formateada = " -> ".join(camino)
            print(f"Hacia {pais}:")
            print(f"   - Distancia/Costo Mínimo: {distancia}")
            print(f"   - Ruta: {ruta_formateada}")
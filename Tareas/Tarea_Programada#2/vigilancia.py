def es_seguro(tablero, fila, col, n):
    """Verifica si es seguro colocar un guardia en la posición (fila, col)"""
    # Verificar la fila hacia la izquierda
    for j in range(col):
        if tablero[fila][j] == 'Q':
            return False

    # Verificar diagonal superior izquierda
    i, j = fila, col
    while i >= 0 and j >= 0:
        if tablero[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Verificar diagonal inferior izquierda
    i, j = fila, col
    while i < n and j >= 0:
        if tablero[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

def resolver_n_reinas_aux(tablero, col, n, soluciones):
    """Algoritmo de Backtracking para N-Reinas"""
    if col >= n:
        # Al encontrar una solución válida, guardamos una copia de la estructura del tablero
        soluciones.append([fila[:] for fila in tablero])
        return

    for fila in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 'Q'  # Decisión: Colocar guardia (Q)
            
            resolver_n_reinas_aux(tablero, col + 1, n, soluciones)
            
            tablero[fila][col] = '.'  # Backtracking: Quitar guardia (.)

def resolver_vigilancia():
    """Manejador principal del Problema 1"""
    print("\n--- PROBLEMA 1: Vigilancia del Castillo ---")
    try:
        n = int(input("Ingrese el tamaño del tablero (N): "))
        if n <= 0:
            print("El tamaño debe ser un entero positivo.")
            return
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    # Inicializar el tablero vacío empleando la nomenclatura (. = Casilla vacía)
    tablero = [['.' for _ in range(n)] for _ in range(n)]
    soluciones = []
    
    resolver_n_reinas_aux(tablero, 0, n, soluciones)
    
    if soluciones:
        print(f"\nUna solución válida encontrada:")
        for fila in soluciones[0]:
            print("".join(fila))
    else:
        print("\nNo se encontraron soluciones para este tamaño de tablero.")
        
    print(f"Total de soluciones encontradas: {len(soluciones)}")
from estructura import PilaListaEnlazada

def buscar_subconjuntos_aux(lista, objetivo, indice, pila_actual, soluciones):
    """Algoritmo de Backtracking utilizando la Pila"""
    
    # Reconstruimos los elementos dentro de la pila para evaluar el estado actual
    elementos_actuales = []
    actual = pila_actual.tope
    while actual:
        elementos_actuales.append(actual.dato)
        actual = actual.siguiente
    
    suma_actual = sum(elementos_actuales)
    
    if suma_actual == objetivo:
        # Invertimos el orden dado el comportamiento LIFO de la pila
        soluciones.append(elementos_actuales[::-1])
        return

    if suma_actual > objetivo or indice >= len(lista):
        return

    for i in range(indice, len(lista)):
        pila_actual.push(lista[i])  # Decisión: Agregar recurso
        
        buscar_subconjuntos_aux(lista, objetivo, i + 1, pila_actual, soluciones)
        
        pila_actual.pop()  # Backtracking: Remover recurso

def resolver_recursos():
    """Manejador principal del Problema 2."""
    print("\n--- PROBLEMA 2: Gestión de Recursos del Reino ---")
    try:
        entrada_lista = input("Ingrese la lista de recursos separados por espacios (ej: 2 3 5 7): ")
        lista = [int(x) for x in entrada_lista.split()]
        objetivo = int(input("Ingrese la cantidad de recursos objetivo: "))
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar solo números enteros.")
        return

    soluciones = []
    pila_rastreo = PilaListaEnlazada()
    
    buscar_subconjuntos_aux(lista, objetivo, 0, pila_rastreo, soluciones)
    
    print("\nSalida:")
    if soluciones:
        for sol in soluciones:
            print(sol)
    else:
        print("No existe ninguna solución.")
        
    print(f"Total de soluciones encontradas: {len(soluciones)}")
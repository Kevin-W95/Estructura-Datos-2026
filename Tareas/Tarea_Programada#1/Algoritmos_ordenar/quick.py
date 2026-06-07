def quick_sort(lista, llave):
    """Algoritmo Quick Sort (versión recursiva) adaptado para listas de diccionarios."""
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        
        izq = [x for x in lista 
            if x[llave] < pivote[llave]]
        centro = [x for x in lista 
            if x[llave] == pivote[llave]]
        der = [x for x in lista 
            if x[llave] > pivote[llave]]
        
        return quick_sort(izq, llave) + centro + quick_sort(der, llave)
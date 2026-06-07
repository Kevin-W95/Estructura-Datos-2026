def merge_sort(lista, llave):
    """Algoritmo Merge Sort adaptado para ordenar una lista de diccionarios por una llave específica."""
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio], llave)
    derecha = merge_sort(lista[medio:], llave)

    return _mezclar(izquierda, derecha, llave)

def _mezclar(izquierda, derecha, llave):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][llave] <= derecha[j][llave]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
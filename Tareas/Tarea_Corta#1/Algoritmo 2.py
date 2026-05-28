import time


# =========================
# Algoritmo 2
# =========================
def algoritmo2(n):

    total = 0 # O(1) -> Constante
    suma_pares = 0 # O(1) -> Constante
    suma_impares = 0 # O(1) -> Constante

    # Operaciones constantes
    a = 10 # O(1) -> Constante
    b = 20 # O(1) -> Constante
    c = a + b # O(1) -> Constante

    for i in range(n): # Único ciclo principal: Se repite N veces

        total += i # O(1) -> Operación simple

        if i % 2 == 0: # O(1) -> Operación simple
            suma_pares += i # O(1) 
        else:
            suma_impares += i # O(1) 
        x = i * 2 # O(1) -> Operación simple
        y = x + 5 # O(1) -> Operación simple
        z = y / 2 # O(1) -> Operación simple
 
    promedio = total / n # O(1) -> Constante

    return promedio + suma_pares + suma_impares # O(1) -> Constante

# Primero, se eliminan las operaciones simples que están afuera (como crear las variables total, suma_pares, suma_impares, a, b, c, calcular el promedio y el return). 
# Se descartan porque son de tiempo constante O(1).
# Hay un solo ciclo for y solo se repite exactamente n veces de forma secuencial. 
# Por dentro tiene varias operaciones rápidas (como sumas, multiplicaciones y un if-else), todas ellas son de tiempo constante O(1) y solo se ejecutan una vez por cada vuelta del ciclo.
# El resultado teórico es O(n) función de crecimiento lineal.

# =========================
# Medición de tiempo
# =========================
def medir_tiempo(funcion, n):

    inicio = time.perf_counter()

    resultado = funcion(n)

    fin = time.perf_counter()

    tiempo = fin - inicio

    print(f"\n{funcion.__name__}")
    print(f"n = {n}")
    print(f"Resultado = {resultado}")
    print(f"Tiempo = {tiempo:.8f} segundos")


# =========================
# Programa principal
# =========================

n = int(input("Ingrese el valor de n: "))

medir_tiempo(algoritmo2, n)
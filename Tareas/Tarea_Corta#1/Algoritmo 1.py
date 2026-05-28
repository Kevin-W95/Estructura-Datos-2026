import time


# =========================
# Algoritmo 1
# =========================
def algoritmo1(n):

    contador = 0 # O(1) -> (Constante)
    suma = 0 # O(1) -> (Constante)

    # Operaciones constantes
    a = 5 # O(1) -> (Constante)
    b = 7 # O(1) -> (Constante)
    c = a * b # O(1) -> (Constante)

    for i in range(n): # Bucle Externo: Se ejecuta N veces
 
        for j in range(n): # Bucle Interno: Se ejecuta N veces por cada 'i'

            contador += 1 # O(1) -> Se ejecuta N * N veces

            suma += i + j # O(1) -> Se ejecuta N * N veces

            x = i * j # O(1) -> Se ejecuta N * N veces
            y = x + 100 # O(1) -> Se ejecuta N * N veces
            z = y / 3 # O(1) -> Se ejecuta N * N veces

            if x % 2 == 0: # O(1) -> Condicional (Constante)
                suma += 1 # O(1)
            else: 
                suma -= 1 # O(1)

    promedio = suma / (n * n) # O(1) -> (Constante)

    return contador + promedio # O(1) -> (Constante)

# Primero, se eliminan las operaciones simples de afuera 
# (como crear las variables contador, suma, a, b, c, calcular el promedio y el return).

# Se descartan porque son de tiempo constante O(1), es decir, tardan lo mismo sin importar el tamaño de n.

# Lo importante: los dos ciclos for anidados (uno dentro de otro). 

# El ciclo de afuera se repite n veces, y por cada una de esas veces, el ciclo de adentro se vuelve a repetir n veces. 

# Aunque las operaciones de adentro (los sumas y el if-else) son rápidas, 
# al estar atrapadas en este doble ciclo se terminan multiplicando y ejecutando n \times n = n^2 veces.  

# Al final, se borran los números constantes y se quedan solo las parte que más crecen. 
# Por eso, el resultado teórico del Algoritmo 1 es O(n^2), que se conoce como una función de crecimiento cuadrática.

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

medir_tiempo(algoritmo1, n)
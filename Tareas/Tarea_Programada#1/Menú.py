from Cargar_archivo import leer_csv, guardar_csv
from Algoritmos_ordenar.merge import merge_sort
from Algoritmos_ordenar.quick import quick_sort

def menu_principal():
    archivo_defecto = "pokemones.csv"
    encabezados, lista_pokemones = leer_csv(archivo_defecto)

    while True:
        print("\n" + "="*40)
        print("POKÉDEX SYSTEM - PROFESOR OAK")
        print("="*40)
        print("1. Cargar archivo CSV")
        print("2. Ordenar por Nombre")
        print("3. Ordenar por Ataque")
        print("4. Ordenar por Defensa")
        print("5. Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            print("Recargando base de datos...")
            resultado_lectura = leer_csv(archivo_defecto)

            if resultado_lectura[1] is not None:
                encabezados, lista_pokemones = resultado_lectura
                print("Datos actualizados correctamente.")
            else:
                print("No se pudo actualizar. Se mantienen los datos anteriores.")

        elif opcion in ["2", "3", "4"]:
            if not lista_pokemones:
                print("Primero debe cargar los datos seleccionando la Opción 1.")
                continue

            criterios = {"2": ("Name", "nombre"), "3": ("Attack", "ataque"), "4": ("Defense", "defensa")}
            llave_columna, nombre_criterio = criterios[opcion]

            print(f"\n--- Ordenar por {nombre_criterio.capitalize()} ---")
            print("a. Utilizar Merge Sort")
            print("b. Utilizar Quick Sort")
            algp_opcion = input("Seleccione el algoritmo (a/b): ").strip().lower()

            if algp_opcion == 'a':
                datos_ordenados = merge_sort(lista_pokemones, llave_columna)
                algo_nombre = "mergesort"
            elif algp_opcion == 'b':
                datos_ordenados = quick_sort(lista_pokemones, llave_columna)
                algo_nombre = "quicksort"
            else:
                print("Opción de algoritmo inválida.")
                continue

            archivo_salida = f"pokemones_{nombre_criterio}_{algo_nombre}.csv"
            print("Procesando ordenamiento...")
            guardar_csv(archivo_salida, encabezados, datos_ordenados)
            print("¡Proceso de ordenamiento exitoso!") 

        elif opcion == "5":
            print("¡Gracias por ayudar al Profesor Oak! Cerrando sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":

    menu_principal() 


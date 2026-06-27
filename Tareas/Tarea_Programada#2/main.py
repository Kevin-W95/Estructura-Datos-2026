from vigilancia import resolver_vigilancia
from recursos import resolver_recursos

def menu_principal():
    """Dibuja el menú interactivo para el usuario"""
    while True:
        print("\n=============================================")
        print("  AGENCIA DE SEGURIDAD DEL REINO DE HYRULE   ")
        print("=============================================")
        print("1. Problema 1: Vigilancia del Castillo (N-Reinas)")
        print("2. Problema 2: Gestión de Recursos (Suma de Subconjuntos)")
        print("3. Salir")
        print("=============================================")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            resolver_vigilancia()
        elif opcion == "2":
            resolver_recursos()
        elif opcion == "3":
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
class Nodo:
    """Clase Nodo Simple"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaListaEnlazada:
    """Clase Pila usando lista enlazada"""
    def __init__(self):
        self.tope = None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def pop(self):
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def esta_vacia(self):
        return self.tope is None
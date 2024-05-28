from typing import Generic, TypeVar

T = TypeVar("T")

'''
Implementar la variante del TAD Grafo (grafo simple) representado con una lista de adyacencia con sus constructores y proyectores básicos. 
Los nodos del grafo simplemente tienen una etiqueta única para identificarlos y pueden asociarse entre ellos mediante aristas o arcos. 
Se puede crear un grafo vacío. Implementar las funciones:
-agregar_nodo
-agregar_arista
-eliminar_nodo
-eliminar_arista
-es_vecino_de
-vecinos_de
'''

class Nodo(Generic[T]):
    def __init__(self, valor: T) -> None:
        self.valor = valor
        self.aristas: set[Grafo_Adyacencia[T]] = set()

    def __str__(self) -> str:
        return f"Nodo({self.valor})"

class Grafo_Adyacencia(Generic[T]):
    def __init__(self) -> None:
        self.nodos: set[Nodo[T]] = set()
    
    @staticmethod
    def crear_grafo(valor: T) -> "Grafo_Adyacencia[T]":
        nuevo = Grafo_Adyacencia()
        nuevo.nodos.add(Nodo(valor))
        return nuevo
    
    def __str__(self) -> str:
        txt = ""
        for nodo in self.nodos:
            txt += str(nodo) + "\n"
        return txt

if __name__ == "__main__":
    g = Grafo_Adyacencia.crear_grafo(1)
    print(g)

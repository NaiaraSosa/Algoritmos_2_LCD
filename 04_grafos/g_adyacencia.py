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

class GrafoAdyacencia(Generic[T]):
    def __init__(self, vertices: set[T]=set(),aristas: dict[T : set[T] ]= {}) -> None:
        self.vertices = vertices
        self.aristas = aristas

    def agregar_nodo(self,nodo:T) -> None:
        self.vertices.add(nodo)
        self.aristas[nodo] = set()

    def agregar_arista(self,arista:tuple[T]) -> None:
        self.aristas[arista[0]].add(arista[1])
        self.aristas[arista[1]].add(arista[0])

    def eliminar_nodo(self,nodo:T) -> None:
        self.vertices.discard(nodo)

    def eliminar_arista(self,arista:tuple[T]) -> None:
        self.aristas[arista[0]].discard(arista[1])
        self.aristas[arista[1]].discard(arista[0])

    def es_vecino_de(self,nodoA:T,nodoB:T) -> bool:
        return nodoB in self.aristas[nodoA]
    
    def vecinos_de(self,nodo:T) -> list[T]:
        return self.aristas[nodo]
    
    def __str__(self) -> str:
        return f"Vertices = {self.vertices} \n Aristas = {self.aristas}"

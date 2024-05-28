from typing import TypeVar
T = TypeVar('T')

'''
Implementar la variante del TAD Grafo (grafo simple) representado con una matriz de adyacencia con sus constructores y proyectores básicos. 
Los nodos del grafo simplemente tienen una etiqueta única para identificarlos y pueden asociarse entre ellos mediante aristas o arcos. 
Se puede crear un grafo vacío. Implementar las funciones:
-agregar_nodo
-agregar_arista
-eliminar_nodo
-eliminar_arista
-es_vecino_de
-vecinos_de
'''

class GrafoMatrizAdyacencia():
    def __init__(self) -> None:
        self.indices = []
        self.matriz = []
        
    def agregar_nodo(self, nodo: int) -> None:
        self.indices.append(nodo)
        for fila in self.matriz:
            fila.append(0)
        self.matriz.append([0 for nodo in self.indices])
        
    def agregar_arista(self, nodoA: int, nodoB: int) -> None:
        indiceA = self.indices.index(nodoA)
        indiceB = self.indices.index(nodoB)
        self.matriz[indiceA][indiceB] = 1
        self.matriz[indiceB][indiceA] = 1
        
    def eliminar_nodo(self, nodo: int) -> None:
        indice = self.indices.index(nodo)
        self.matriz.pop(indice)
        for fila in self.matriz:
            fila.pop(indice)
        self.indices.pop(indice)
        
    def eliminar_arista(self, nodoA: int, nodoB: int) -> None:
        pass
        
    def es_vecino_de(self, nodoA, nodoB):
        indiceA = self.indices.index(nodoA)
        indiceB = self.indices.index(nodoB)
        
    def vecinos_de(self) -> None:
        pass

        
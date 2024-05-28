from typing import Generic, TypeVar

T = TypeVar("T")

'''
Implementar la variante del TAD Grafo (grafo simple) representado con conjunto de nodos y arista con sus constructores y proyectores básicos. 
Los nodos del grafo simplemente tienen una etiqueta única para identificarlos y pueden asociarse entre ellos mediante aristas o arcos. 
Se puede crear un grafo vacío. Implementar las funciones:
-agregar_nodo
-agregar_arista
-eliminar_nodo
-eliminar_arista
-es_vecino_de
-vecinos_de
'''

class Grafo(Generic[T]):
    def __init__(self) -> None:
        self.vertices: set[T] = set()
        self.aristas: set[tuple[T, T]] = set()

    def agregar_nodo(self, valor: T):
        if valor not in self.vertices:
            self.vertices.add(valor)
        else:
            raise ValueError('El nodo ya existe en el grafo')
    

    def agregar_arista(self, arista: tuple[T, T]):
        if arista[0] in self.vertices and arista[1] in self.vertices:
            self.aristas.add(arista)
        elif arista in self.aristas:
            raise ValueError('La arista ya existe en el grafo')
        else:
            raise ValueError("Ambos nodos deben pertenecer al grafo.")


    def eliminar_nodo(self, valor: T):
        if valor in self.vertices:
            self.vertices.remove(valor)
            self.aristas = {arista for arista in self.aristas if valor not in arista} # crea un set() con todas las aristas que no conectan el nodo eliminado
        else:
            raise ValueError("El nodo no está en el grafo.")


    def eliminar_arista(self, arista: tuple[T, T]):
        self.aristas.remove(arista)
        self.aristas.remove((arista[1], arista[0]))


    def es_vecino(self, valor1: T, valor2: T) -> bool:
        return (valor1, valor2) in self.aristas or (valor2, valor1) in self.aristas


    def vecinos_de(self, valor: T) -> list[T]:
        if valor not in self.vertices:
            raise ValueError("El nodo no está en el grafo.")
        else:
            vecinos = [arista[1] for arista in self.aristas if arista[0] == valor]
            vecinos += [arista[0] for arista in self.aristas if arista[1] == valor]
            return vecinos
        
        
    def dfs(self) -> list[T]:
        visitados = []
        recorrido = []

        def dfs_recursivo(nodo: T, visitados: list[T], recorrido: list[T]):
            visitados.append(nodo)
            recorrido.append(nodo)
            for vecino in self.vecinos_de(nodo):
                if vecino not in visitados:
                    dfs_recursivo(vecino, visitados, recorrido)

        for nodo in self.vertices:
            if nodo not in visitados:
                dfs_recursivo(nodo, visitados, recorrido)
        return recorrido

    
    def bfs_cola(self) -> list[T]:

        def bfs_interno(queue, recorrido: list[T]) -> list[T]:
            if not queue:
                return recorrido
            actual = queue.pop(0)
            if actual not in recorrido:
                recorrido.append(actual)
                for vecino in self.vecinos_de(actual):
                    queue.append(vecino)
            return bfs_interno(queue, recorrido)
        
        nodo_inicial = [next(iter(self.vertices))]
        return bfs_interno(nodo_inicial, []) 
    

    def existe_conexion(self, valor1: T, valor2: T) -> bool:  
        if self.es_vecino(valor1, valor2):
            return True


if __name__ == '__main__':
    g = Grafo()
    g.agregar_nodo(1)
    g.agregar_nodo(2)    
    g.agregar_nodo(3)
    g.agregar_nodo(4)
    g.agregar_nodo(5)
    g.agregar_nodo(6)
    g.agregar_nodo(7)
    g.agregar_arista((1,2))
    g.agregar_arista((2,4))
    g.agregar_arista((4,7))
    g.agregar_arista((2,5))
    g.agregar_arista((1,3))
    g.agregar_arista((3,6))
    g.agregar_arista((5,6))
    print(f'DFS: {g.dfs()}')
    print(f'BFS: {g.bfs_cola()}')
    print(f'Existe conexion entre 2 y 7: {g.existe_conexion(2,7)}')

from typing import Generic, TypeVar, List, Set

T = TypeVar("T")

# 1 -> [2]
# 2 -> [1, 3]
# 4 -> [3]

class Grafo(Generic[T]):
    def __init__(self) -> None:
        self.vertices: set[T] = set()
        self.aristas: set[tuple[T, T]] = set()

    def agregar_nodo(self, valor: T):
        self.vertices.add(valor)
    
    def agregar_arista(self, arista: tuple[T, T]):
        if arista[0] in self.vertices and arista[1] in self.vertices:
            self.aristas.add(arista)
        else:
            raise ValueError("Ambos nodos deben pertenecer al grafo.")

    def eliminar_nodo(self, valor: T):
        if valor in self.vertices:
            self.vertices.remove(valor)
            self.aristas = {arista for arista in self.aristas if valor not in arista}
        else:
            raise ValueError("El nodo no está en el grafo.")

    def eliminar_arista(self, arista: tuple[T, T]):
        self.aristas.discard(arista)
        self.aristas.discard((arista[1], arista[0]))

    def es_vecino(self, valor1: T, valor2: T) -> bool:
        return (valor1, valor2) in self.aristas or (valor2, valor1) in self.aristas

    def vecinos_de(self, valor: T) -> list[T]:
        if valor not in self.vertices:
            raise ValueError("El nodo no está en el grafo.")
        else:
            vecinos = [arista[1] for arista in self.aristas if arista[0] == valor]
            vecinos += [arista[0] for arista in self.aristas if arista[1] == valor]
            return vecinos
        
    def dfs(self, inicio: T) -> List[T]:
        visitados = set()
        recorrido = []
        
        def _dfs_recursivo(nodo: T, visitados: Set[T], recorrido: List[T]):
            visitados.add(nodo)
            recorrido.append(nodo)
            for vecino in self.vecinos_de(nodo):
                if vecino not in visitados:
                    _dfs_recursivo(vecino, visitados, recorrido)
                    
        _dfs_recursivo(inicio, visitados, recorrido)    
        return recorrido
    
    def bfs(self) -> List[T]:
        def _bfs_interno(queue, recorrido: List[T]) -> List[T]:
            if not queue:
                return recorrido
            actual = queue.pop(0)
            if actual not in recorrido:
                recorrido.append(actual)
                for vecino in self.vecinos_de(actual):
                    queue.append(vecino)
            return _bfs_interno(queue, recorrido)
        primer_nodo = next(iter(self.vertices))  
        queue = [primer_nodo]
        # queue = [self.vertices[0]]
        return _bfs_interno(queue, [])        
    
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
    print(f'DFS: {g.dfs(1)}')
    print(f'BFS: {g.bfs()}')
    print(f'Existe conexion entre 2 y 7: {g.existe_conexion(2,7)}')

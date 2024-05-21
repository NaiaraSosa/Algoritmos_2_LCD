from collections.abc import Callable
from typing import Any, Generic, Optional, TypeVar
from functools import wraps

T = TypeVar('T')

' ESTRUCTURA DE RECURSIÓN MUTUA (ArbolBinario se compone opcionalmente de NodoAB y NodoAB se compone de dos tipos de ArbolBinario si y sd)'

class NodoAB(Generic[T]):
    def __init__(self, dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None):
        self.dato = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

    def __str__(self):
        return self.dato
    
class ArbolBinario(Generic[T]):

    # El constructor solo permite instanciar árboles vacíos
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None  # Permite anular la raíz de un árbol, se puede modelar el árbol vacío
        
    class _Decoradores:
        @classmethod
        def valida_es_vacio(cls, f: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(f)
            def wrapper(self, *args: Any, **kwargs: Any) -> Any:
                if self.es_vacio():
                    raise TypeError('Arbol Vacio')
                return f(self, *args, **kwargs)
            return wrapper
    
    # Hacemos un método estático para ocultar y encapsular la clase NodoAB 
    @staticmethod
    def crear_nodo(dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None
    
    ' OPERACIONES PROYECTORAS --------------------------------------------------------------------------------------------------------------------------------------------'
    
    # Devuelve subárbol izquierdo
    @_Decoradores.valida_es_vacio
    def si(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.si
    
    # Devuelve subárbol derecho
    @_Decoradores.valida_es_vacio
    def sd(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.sd

    # Devuelve dato del nodo
    @_Decoradores.valida_es_vacio
    def dato(self) -> T:
        assert self.raiz is not None
        return self.raiz.dato
    
    # Indica si el árbol actual es hoja (no es vacío y no tiene descendientes)
    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio and self.sd().es_vacio()
    
    ' OPERACIONES MODIFICADORAS --------------------------------------------------------------------------------------------------------------------------------------------'
    
    # Permite incorporar o reemplazar nuevos subárboles a la raíz actual
    @_Decoradores.valida_es_vacio
    def insertar_si(self, si: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.si = si

    # Permite incorporar o reemplazar nuevos subárboles a la raíz actual
    @_Decoradores.valida_es_vacio
    def insertar_sd(self, sd: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.sd = sd

    def set_raiz(self, nodo: NodoAB[T]):
        self.raiz = nodo
        
    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())
        
    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())
    
    def __str__(self):
        def mostrar(t: ArbolBinario[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            if t.es_vacio():
                return indent + 'AV\n'
            else:
                out = indent + str(t.dato()) + '\n'
                out += mostrar(t.si(), nivel + 1)
                out += mostrar(t.sd(), nivel + 1)
                return out
            
        return mostrar(self, 0)
    
    # Implementar una operación que, dado un valor o etiqueta de un nodo, devuelva cuál es el nivel del mismo dentro del árbol.
    def nivel(self, valor: T) -> int:
        if self.es_vacio():
            return 0
        elif valor == self.dato():
            return 1
        else:
            nivel_izquierdo = self.si().nivel(valor)
            nivel_derecho = self.sd().nivel(valor)
            if nivel_izquierdo != 0:
                return 1 + nivel_izquierdo
            elif nivel_derecho != 0:
                return 1 + nivel_derecho
            else:
                return 0
            
    # Implementar la operación __eq__() para un árbol que permita identificar si dos árboles son iguales.
    def __eq__(self, otro: "ArbolBinario[T]") -> bool:
        return isinstance(otro, ArbolBinario) and self.dato() == otro.dato() and self.sd() == otro.sd() and self.si() == otro.si()
    
    def preorder(self) -> list[T]:
        if self.es_vacio():
            return []
        return [self.dato()] + self.si().preorder() + self.sd().preorder()

    def inorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().inorder() + [self.dato()] + self.sd().inorder()
        
    # Eliminar recursión en DFS - Implementar una versión de recorrido DFS inorder con recursión de cola.

    def postorder(self) -> list[T]:
        if self.es_vacio():
            return []
        return self.si().postorder() + self.sd().postorder() + [self.dato()]
    
    ''' A diferencia del recorrido DFS que se apoya en la pila de ejecución, para implementar este tipo de recorrido 
        utilizaremos una cola explícita para almacenar los subárboles restantes a recorrer en cada visita.

        Es importante notar que eventualmente la recursión termina (llega al caso base de una cola vacía) porque en todas 
        las instancias recursivas se desencola un nodo, pero no necesariamente siempre se enconlan los descendientes.
    '''
    
    def bfs(self) -> list[T]:
        def recorrido(q: list[ArbolBinario[T]], camino: list[T]) -> list[T]:
            if not q:
                return camino
            actual = q.pop(0)  # desencolar árbol visitado
            if not actual.es_vacio():
                camino.append(actual.dato())
                q.append(actual.si())    # encolar subárbol izquierdo
                q.append(actual.sd())    # encolar subárbol derecho
            return recorrido(q, camino)  # encolar raíz
        return recorrido([self], [])
    
    def bfs_invertido(self) -> list[T]: 
        def recorrido(p: list[ArbolBinario[T]], camino: list[T]) -> list[T]:
            if not p:
                return camino
            else:
                actual = p.pop(0)
                if not actual.es_vacio():
                    camino.append(actual.dato())
                    p.append(actual.sd())
                    p.append(actual.si())
                return recorrido(p, camino)
        return recorrido([self], [])
    
    # Ejercicio: Recorrido bottom-up - algoritmo que devuelva el recorrido desde las hojas hasta la raiz de derecha a izquierda

    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario[T]()
        nuevo = ArbolBinario.crear_nodo(self.dato())
        nuevo.insertar_si(self.si().copy())
        nuevo.insertar_sd(self.sd().copy())
        return nuevo

    def espejo(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario[T]()
        nuevo = ArbolBinario.crear_nodo(self.dato())
        nuevo.insertar_si(self.sd().espejo())
        nuevo.insertar_sd(self.si().espejo())
        return nuevo
        
    def hojas(self) -> list[T]:
        if self.es_vacio():
            return []
        elif self.es_hoja():
            return [self.dato()]
        else:
            hojas_si = self.si().hojas()
            hojas_sd = self.sd().hojas()
            return hojas_si + hojas_sd
    
    def sin_hojas(self) -> "ArbolBinario[T]":
        if self.es_vacio() or self.es_hoja():
            return ArbolBinario()
        else:
            nuevo = ArbolBinario.crear_nodo(self.dato())
            nuevo.insertar_si(self.si().sin_hojas())
            nuevo.insertar_sd(self.sd().sin_hojas())
            return nuevo
        
    def podar(self, dato: T) -> "ArbolBinario[T]":
        if self.es_vacio() or self.dato() == dato:
            return ArbolBinario()
        else:
            nuevo = ArbolBinario.crear_nodo(self.dato())
            nuevo.insertar_si(self.si().podar(dato))
            nuevo.insertar_sd(self.sd().podar(dato))
            return nuevo
        
def main():
    t  = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n9 = ArbolBinario.crear_nodo(9)
    n10 = ArbolBinario.crear_nodo(10)
    n11 = ArbolBinario.crear_nodo(11)

    t.insertar_si(n2)
    t.insertar_sd(n3)
    n2.insertar_si(n4)
    n2.insertar_sd(n5)
    n5.insertar_si(n9)
    n5.insertar_sd(n10)
    n4.insertar_si(n8)
    n3.insertar_si(n6)
    n3.insertar_sd(n7)
    n7.insertar_sd(n11)

    print(t)
    print(f'Nivel de A1: {t.nivel(4)}')
    print(f'Preorder de A1: {t.preorder()}')
    print(f'Inorder de A1: {t.inorder()}')
    print(f'Postorder de A1: {t.postorder()}')
    print(f'BFS: {t.bfs()}')
    print(f'BFS invertido: {t.bfs_invertido()}')

    # t2: ArbolBinario[int] = t.sin_hojas()
    # print(t2)

    t3 = t.podar(5)
    print(t3)

    # t4 = t.espejo()
    # print(t4)

if __name__ == '__main__':
    main()
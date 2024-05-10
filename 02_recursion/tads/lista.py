from typing import Generic, TypeVar, Optional, TypeAlias
from copy import copy

T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig= Lista()
        else:
            self.sig = sig

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo] = None

    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.dato

    # En cada caso recursivo estamos generando un nodo por vez y encadenandolo a los generados anteriores
    def copy(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        else:
            parcial = self._head.sig.copy()
            actual = Lista()
            actual._head = Nodo(copy(self._head.dato), parcial)
            return actual
    
    # Por iteración
    def copy_reversa_iter(self) -> ListaGenerica:
        copia = self.copy()
        nueva = Lista()
        while not copia.es_vacia():           
            nueva.insertar(copia.head())
            copia = copia.tail()
        return nueva
    
    # Por recursión de cola
    def copy_reversa_cola(self) -> ListaGenerica:
        def reversa_interna(original: ListaGenerica, reversa: ListaGenerica):
            if not original.es_vacia():
                elemento = original.head()
                reversa.insertar(elemento)
                reversa_interna(original.tail(), reversa)
        reversa = Lista()
        reversa_interna(self, reversa)
        return reversa
    
    # Por recursión de pila
    def copy_reversa_pila(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        else:
            parcial = self.tail().pila()
            parcial.insertar_fin(self.head())  # Hacer método
            return parcial

    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.sig.copy()

    def insertar(self, dato: T):
        if self.es_vacia():
            self._head = Nodo(dato)
        else:
            actual = copy(self)
            self._head = Nodo(dato, actual)

    def eliminar(self, valor: T):
        def _eliminar_interna(actual: ListaGenerica, previo: ListaGenerica, valor: T):
            if not actual.es_vacia():
                if actual.head() == valor:
                    previo._head.sig = actual._head.sig
                else:
                    _eliminar_interna(actual._head.sig, actual, valor)

        if not self.es_vacia():
            if self.head() == valor:
                self._head = self._head.sig._head
            else:
                _eliminar_interna(self._head.sig, self, valor)

    """
    Ejercicio: Extender el TAD Lista
    A partir de la implementación de Lista, completar las operaciones que faltan definir
    """

    def ultimo(self) -> T:
        if self.es_vacia():
            raise IndexError("Lista vacía")
        elif self.tail().es_vacia:
            return self.head()
        else:
            return self._head.ultimo()

    def concat(self, ys: ListaGenerica) -> ListaGenerica:
        pass
        
    def join(self, separador: str = '') -> str:
        if self.es_vacia():
            return ''
        else:
            nodos = []
            actual = self
            while not actual.es_vacia():
                nodos.append(str(actual.head()))
                actual = actual.tail()
            return separador.join(nodos)
        
    def index(self, valor: T) -> int:
        pass
        
    def existe(self, valor: T) -> bool:
        pass

    def __repr__(self) -> str:
        def interna(lista: ListaGenerica):
            if lista.es_vacia():
                return ''
            else:
                return f'{lista.head()} {lista.tail().__repr__()}'
        return f'{interna(self)}'
    
    def __repr__(self):
        return f'[{self.join(",")}]' 
    
    def __getItem__(self, indice):
        pass

    def __len__(self):
        if self.es_vacia():
            return 0
        else:
            return 1 + self.tail().__len__()
        
    def __eq__(self, otra: ListaGenerica) -> bool:
        pass

if __name__ == '__main__':
    xs: Lista[int] = Lista()
    print(xs)    
    xs.insertar(4)
    xs.insertar(10)
    xs.insertar(20)
    print(f'xs: {xs}')                          # [20,10,4]
    ys: Lista[int] = xs.tail()
    ys.insertar(9)
    ys.eliminar(10)
    ys.insertar(8)
    print(f'ys: {ys}')                          # [8,9,4]
    zs: Lista[int] = ys.copy()
    zs.eliminar(8)
    zs.eliminar(9)  
    print(f'zs: {zs}')                          # [4]
    reversa: Lista[int] = xs.copy_reversa_cola()
    print(f'reversa: {reversa}')

   











    #print(f'ultimo(xs): {xs.ultimo()}')		# 4
    #print(f'len(xs): {len(ys)}')			# 3, ver __len__
    #print(f'xs[1]: {xs[1]}')				# 10, ver __getitem__

    # Consumiendo como iterable
    #for x in xs:
       # print(x)	# 20 -> 10 -> 4

    # Otras operaciones
    #print(f'xs.concat(ys): {xs.concat(ys)}')		# [20, 10, 4, 8, 9, 4]
    #print(f'ys.join(" -> "): {ys.join(" -> ")}')	# 8 -> 9 -> 4
    #print(f'xs.index(4): {xs.index(4)}')			# 2
    #print(f'xs.existe(10): {xs.existe(10)}')        # True
    #print(f'xs == zs? {xs == zs}')                  # False
    #zs.insertar(10)
    #zs.insertar(20)
    #print(f'xs == zs? {xs == zs}')                  # True
    
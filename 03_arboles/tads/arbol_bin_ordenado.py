from typing import TypeVar, Optional, Protocol
from arbol_binario import ArbolBinario, NodoAB

class Comparable(Protocol):
    def __lt__(self: 'T', otro: 'T') -> bool: ...
    def __le__(self: 'T', otro: 'T') -> bool: ...
    def __gt__(self: 'T', otro: 'T') -> bool: ...
    def __ge__(self: 'T', otro: 'T') -> bool: ...
    def __eq__(self: 'T', otro: 'T') -> bool: ...
    def __ne__(self: 'T', otro: 'T') -> bool: ...

T = TypeVar('T', bound=Comparable)


class NodoABO(NodoAB[T]):
    def __init__(self, dato: T):
        super().__init__(dato, ArbolBinarioOrdenado(), ArbolBinarioOrdenado())
    
    # En este tipo de árboles es esencial la comparación para mantener una relación de orden
    def __lt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato < otro.dato
    
    def __gt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato > otro.dato

    def __eq__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato == otro.dato
    
    
class ArbolBinarioOrdenado(ArbolBinario[T]):

    # Debemos ocultar este método para que construya su propio objeto Ordenado porque ya lo tenemos en ArbolBinario
    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinarioOrdenado[T]":
        nuevo = ArbolBinarioOrdenado()
        nuevo.set_raiz(NodoABO(dato))
        return nuevo
    
    def es_ordenado(self) -> bool:
        def es_ordenado_interna(
            arbol: "ArbolBinarioOrdenado[T]", 
            minimo: Optional[T] = None, 
            maximo: Optional[T] = None
        ) -> bool:
            if arbol.es_vacio(): # si el árbol es vacío está ordenado
                return True
            
            # si el dato es menor al mínimo permitido no está ordenado o si el dato es mayor al máximo permitido no está ordenado
            if (minimo is not None and arbol.dato() <= minimo) or (maximo is not None and arbol.dato() >= maximo):
                return False
            return es_ordenado_interna(arbol.si(), minimo, arbol.dato()) and es_ordenado_interna(arbol.sd(), arbol.dato(), maximo)
        
        return es_ordenado_interna(self)
    
    # Debemos sobrescribir si() y sd() porque tienen una restricción de orden, a diferencia de ArbolBinario

    # Básicamente insertamos el subárbol, luego chequeamos si está ordenado y si es False, retomamos el árbol ordenado original y lanzamos una excepción
    def insertar_si(self, arbol: "ArbolBinarioOrdenado[T]"):
        si = self.si()
        super().insertar_si(arbol)
        if not self.es_ordenado():
            super().insertar_si(si)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
    
    def insertar_sd(self, arbol: "ArbolBinarioOrdenado[T]"):
        sd = self.sd()
        super().insertar_sd(arbol)
        if not self.es_ordenado():
            super().insertar_sd(sd)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
    
    # Comenzamos desde la raíz y nos movemos a la izquierda si el valor del nodo actual es menor o a la derecha si es mayor
    def insertar(self, valor: T):
        if self.es_vacio():
            self.set_raiz(NodoABO(valor))
        elif valor == self.dato:
            raise ValueError('El valor ya se encuentra en el árbol.')
        elif valor < self.dato():
            self.si().insertar(valor)
        else:
            self.sd().insertar(valor)

    # Implementar la operación de búsqueda en un árbol binario ordenado, donde dado un valor de dato devuelva si existe un nodo en el árbol con ese valor.
    def pertenece(self, valor: T) -> bool:
        if self.es_vacio():
            return False
        elif valor == self.dato:
            return True
        else:
            return self.si().pertenece(valor) or self.sd().pertenece(valor)

    def max(self):
        if self.es_vacio():
            raise ValueError('AV no tiene max.')
        elif not self.sd().es_vacio():
            return self.sd().max()
        return self
    
    def max_con_pred(self) -> tuple['ArbolBinarioOrdenado[T] | None', 'ArbolBinarioOrdenado[T] | None']: # actual y predecesor
        if self.es_vacio():
            return None, None
        elif not self.sd().es_vacio():
            return self, None
        elif self.sd().es_vacio():
            return self.sd(), self
        else:
            return self.sd().max_con_pred()
        
        
    def eliminar(self, valor: T):

        def eliminar_fusion(t: ArbolBinarioOrdenado[T]): 
                    t.si().max().insertar_sd(t.sd()) # inserta sd de t como sd del nodo mayor del si de t
                    t.raiz = t.si().raiz # establece la raiz del si de t eliminando t y fusionando los subarboles

        '''def eliminar_copia(t: ArbolBinarioOrdenado[T]):
            max, pred = t.si().max_con_pred()
            if max is not None and pred is not None:
                t.raiz.dato = max.dato()  # Aquí cambiamos solo el dato de la raíz, no la raíz completa
            if pred.si().raiz == max.raiz:  # Si el predecesor es el padre directo del máximo
                pred.raiz.si = max.si()  # Conectar el subárbol izquierdo del máximo al predecesor
            else:
                pred.raiz.sd = max.si()  # Conectar el subárbol izquierdo del máximo al predecesor'''

        if not self.es_vacio():
            if valor == self.dato():

                # Caso trivial: Eliminamos una hoja y reemplazamos por árbol vacío
                if self.es_hoja():
                    self.raiz = None

                # Eliminasión por fusión
                elif not self.sd().es_vacio() and not self.si().es_vacio():
                    eliminar_fusion(self) # Puede ser eliminar_fusion() o eliminar_copia()
                
                # Caso trivial: Sin descendiente izquierdo
                elif not self.sd().es_vacio():
                    self.raiz = self.sd().raiz

                # Caso trivial: Sin descendiente derecho
                else:
                    self.raiz = self.si().raiz

            elif self.dato() < valor:
                self.sd().eliminar(valor)
            else:
                self.si().eliminar(valor)
        else:
            raise ValueError('No puede eliminarse la hoja porque no existe en árbol.')

    '''Dado un árbol binario clásico, definir una operación que permita convertirlo en un árbol binario ordenado 
        si se cumplen las restricciones de orden. De lo contrario, devolver una excepción. 
        Tener en cuenta que el nuevo árbol debe ser una copia del original y con el tipo de dato adecuado (ArbolBinarioOrdenado).'''
    @staticmethod
    def convertir_ordenado(arbol_binario: ArbolBinario[T]) -> "ArbolBinarioOrdenado[T]":
        arbol_ordenado: ArbolBinarioOrdenado[T] = arbol_binario.copy()


        return arbol_ordenado
        

def main():
    t: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado() # type: ignore
    t.insertar(10)
    t.insertar(5)
    t.insertar(15)
    t.insertar(2)
    t.insertar(7)
    t.insertar(12)
    t.insertar(17)
    t.insertar(20)
    t.insertar(13)
    print(t)

    print(f'El árbol es ordenado: {t.es_ordenado()}')
    print(f'Tiene 12: {t.pertenece(12)}')

    t.eliminar(15)
    print(t)

if __name__ == "__main__":
    main()
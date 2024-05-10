from typing import Generic, TypeVar
from functools import reduce

T = TypeVar('T')

class ArbolN(Generic[T]):

    # Estructura con recursión directa múltiple
    def __init__(self, dato: T):
        self._dato: T = dato
        self._subarboles: list[ArbolN[T]] = []
    
    # Decidimos mantener los atributos privados para convertirlos en propiedades
    @property
    def dato(self) -> T:
        return self._dato

    @dato.setter
    def dato(self, valor: T):
        self._dato = valor

    @property
    def subarboles(self) -> "list[ArbolN[T]]":
        return self._subarboles
    
    @subarboles.setter
    def subarboles(self, subarboles: "list[ArbolN[T]]"):
        self._subarboles = subarboles

    # Extender árboles con nuevos descendientes
    def insertar_subarbol(self, subarbol: "ArbolN[T]"):
        self.subarboles.append(subarbol)

    # Presenta si un nodo no tiene subárboles
    def es_hoja(self) -> bool:
        return self.subarboles == []
    
    def altura(self) -> int:
        def altura_n(bosque: list[ArbolN[T]]) -> int:
            if not bosque:
                return 0
            else:
                return max(bosque[0].altura(), altura_n(bosque[1:]))
        return 1 + altura_n(self.subarboles)
    
    # Acá vemos la lógica más entendible en el caso iterativo
    def altura_iter(self) -> int:
        altura_actual = 0
        for subarbol in self.subarboles:
            altura_actual = max(altura_actual, subarbol.altura())
        return altura_actual + 1
    
    # Cantidad de nodos
    def __len__(self) -> int:
        if self.es_hoja():
            return 1
        else:
            return 1 + sum([len(subarbol) for subarbol in self.subarboles])
        
    # Implementar el método __eq__() que permita identificar si dos árboles n-arios son iguales.
    def __eq__(self, otro: "ArbolN[T]") -> bool:
        return isinstance(otro, ArbolN) and self.dato == otro.dato and self.subarboles == otro.subarboles

    def __str__(self):
        def mostrar(t: ArbolN[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            out = indent + str(t.dato) + '\n'
            for subarbol in t.subarboles:
                out += mostrar(subarbol, nivel + 1)
            return out
            
        return mostrar(self, 0)

    def preorder(self) -> list[T]:
        return reduce(lambda recorrido, subarbol: recorrido + subarbol.preorder(), self.subarboles, [self.dato])

    def preorder2(self) -> list[T]:
        recorrido = [self.dato]
        for subarbol in self.subarboles:
            recorrido += subarbol.preorder2()
        return recorrido
    
    def preorder3(self) -> list[T]:
        def preorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            return [] if not bosque else bosque[0].preorder3() + preorder_n(bosque[1:])
        return [self.dato] + preorder_n(self.subarboles)

    def bfs(self) -> list[T]:
        pass
    
    def posorder(self) -> list[T]:
        pass

    def nivel(self, x: T) -> int:
        def buscar(t: ArbolN[T], x):
            pass
    
    def copy(self) -> "ArbolN[T]":
        pass
        
    def sin_hojas(self) -> "ArbolN[T]":
        if self.es_hoja():
            return None
        nuevo = ArbolN(self.dato)
        for subarbol in self.subarboles:
            a = subarbol.sin_hojas()
            if a is None:
                continue
            nuevo.insertar_subarbol(a)
        return nuevo
    
    # Version 1 -> Saco el dato buscado en el predecesor directo
    def antecesores_pred(self, dato: T) -> list[T]:
        if dato == self.dato:
            return [dato]
        elif self.es_hoja():
            return []
        else:
            i = 0
            resultado = []
            while i < len(self.subarboles) and not resultado:
                resultado = self.subarboles[i].antecesores_pred(dato)
                i += 1
            if resultado:
                if resultado [0] == dato:
                    resultado.pop()
                resultado.insert(0, self.dato)
            return resultado
    
    # Version 2 -> Saco el dato buscado al final
    def antecesores_fin(self, dato: T) -> list[T]:
        def antecesor_interna(t: ArbolN[T]) -> list[T]:
            if dato == t.dato:
                return [dato]
            elif t.es_hoja():
                return []
            else:
                i = 0
                resultado = []
                while i < len(t.subarboles) and not resultado:
                    resultado = antecesor_interna(t.subarboles[i])
                    i += 1
                if resultado:
                    resultado.insert(0, t.dato)
                return resultado
        resultado = antecesor_interna(self)
        if resultado:
            resultado.pop()
        return resultado

    # Version 3 -> Look ahead (con esta metodologia nunca llegamos al nodo buscado, solo en el caso de que sea la raíz)
    def antecesores_look(self, dato: T) -> list[T]:
        if dato == self.dato or self.es_hoja():
            return []
        else:
            i = 0
            resultado = []
            encontrado = False
            while i < len(self.subarboles) and not encontrado:
                if self.subarboles[i].dato == dato:
                    encontrado = True
                else:
                    resultado = self.subarboles[i].antecesores_look(dato)
                    encontrado = bool(resultado) # lo encontre
                i += 1
            if encontrado:
                resultado.insert(0, self.dato)
            return resultado

    # Version 4 -> Top-down, vamos llenando la lista y borrando a medida que encontremo y no encontremos
    def antecesores(self, dato: T) -> list[T]:
        def antecesor_interna(t: ArbolN[T], antecesores: list[T]):
            if dato == t.dato:
                return antecesores
            elif t.es_hoja():
                return []
            else:
                i = 0
                antecesores.append(t.dato)
                resultado = []
                while i < len(t.subarboles) and not resultado:
                    resultado = antecesor_interna(t.subarboles[i], antecesores.copy())
                    i += 1
                return resultado
        return antecesor_interna(self,[])

    def recorrido_guiado(self, direcciones: list[int]) -> T:   # profundidad
        if not direcciones:
            return self.dato
        else:
            i = direcciones.pop(0)
            if i >= len(self.subarboles):
                raise Exception('No existe la dirección ingresada.')
            return self.subarboles[i].recorrido_guiado(direcciones)


def main():
    t = ArbolN(1)
    n2 = ArbolN(2)
    n3 = ArbolN(3)
    n4 = ArbolN(4)
    n5 = ArbolN(5)
    n6 = ArbolN(6)
    n7 = ArbolN(7)
    n8 = ArbolN(8)
    n9 = ArbolN(9)
    t.insertar_subarbol(n2)
    t.insertar_subarbol(n3)
    t.insertar_subarbol(n4)
    n2.insertar_subarbol(n5)
    n2.insertar_subarbol(n6)
    n4.insertar_subarbol(n7)
    n4.insertar_subarbol(n8)
    n7.insertar_subarbol(n9)

    print(t)
  
    print(f'Altura: {t.altura()}')
    print(f'Nodos: {len(t)}')

    print(f'Antecesores: {t.antecesores_pred(9)}')
    print(f'Antecesores: {t.antecesores_fin(9)}')
    print(f'Antecesores: {t.antecesores_look(9)}')
    print(f'Antecesores: {t.antecesores(9)}')

    print(f'Recorrido guiado: {t.recorrido_guiado([2,0,0])}')

    # print(f'BFS: {t.bfs()}')
    # print(f'DFS preorder : {t.preorder()}')
    # print(f'DFS preorder2: {t.preorder2()}')
    # print(f'DFS preorder3: {t.preorder3()}')
    # print(f'DFS posorder: {t.posorder()}')

    # print(f'Nivel de 9: {t.nivel(9)}')
    # print(f'Nivel de 13: {t.nivel(13)}')

    # t2 = t.copy()
    # t3 = t2.sin_hojas()
    # print(t)
    # print(t2)
    # print(t3)
    # print(f't == t2 {t == t2}')

    # print(f'recorrido_guiado [2,0,0]: {t2.recorrido_guiado([2,0,0])}')

if __name__ == '__main__':
    main()

'''
Ejercicio: resta_lista iterativa
Convertir la última función resta_lista que utiliza una pila explícita de forma que no use ningún tipo de recursión y sólo utilice iteración.
'''


# Ejemplo del factorial con iteración

def factorial(n: int) -> int:
    solucion = 1
    while n > 1:
        solucion *= n
        n -= 1
    return solucion


def resta_lista_iterativa(xs: list[int]) -> int:
    solucion_final: int = 0
    while not xs:
        solucion_final 


    return solucion_final


# Recursión de pila 

def resta_lista(xs: list[int]) -> int:
    if xs == []:
        return 0
    else:
        return xs[0] - resta_lista(xs[1:])

resta_lista([10, 2, 5, 9])   # (10 - (2 - (5 - 9)) = 4
print(resta_lista([10, 2, 5, 9]))
# Recursión de cola

def resta_lista(xs: list[int]) -> int:
    def resta_lista_interna(xs: list[int], acumulador: int) -> int:
        if xs == []:
            return acumulador
        else:
            return resta_lista_interna(xs[1:], acumulador - xs[0])
    return 0 if xs == [] else resta_lista_interna(xs[1:], xs[0])

resta_lista([10, 2, 5, 9]) # ((10 - 2) - 5) - 9) = -6
print(resta_lista([10, 2, 5, 9]))

def resta_lista(xs: list[int]) -> int:
    def apilado(xs: list[int], pila: list[int]):
        if xs != []:
            pila.append(xs[0])
            apilado(xs[1:], pila)

    def desapilado(pila: list[int], acumulador: int) -> int:
        if pila == []:
            return acumulador
        else:
            return desapilado(pila, pila.pop() - acumulador)
      
    pila = []
    apilado(xs, pila)
    return desapilado(pila, 0)

resta_lista([10, 2, 5, 9]) # (10 - (2 - (5 - 9)) = 4
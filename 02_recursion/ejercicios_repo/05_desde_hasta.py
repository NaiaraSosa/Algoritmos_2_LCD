"""
Ejercicio: Desde-Hasta
- Definir la función desde_hasta, que dados dos números enteros retorne una lista de números consecutivos donde el 
primer elemento de la lista resultante sea el primer elemento dado, y el último elemento de la lista resultante 
sea el segundo elemento dado.
- Redefinir las funciones sumatoria y factorial utilizando desde_hasta.
"""

from functools import reduce

def desde_hasta(n1: int, n2:int) -> list[int]:
    if n2 < n1:
        raise ValueError("El segundo valor debe ser mayor al primero.")
    if n1 == n2:
        return [n1]
    else:
        return [n1] + desde_hasta(n1 + 1, n2)

def sumatoria(n: int) -> int:
    lista = desde_hasta(0, n)
    return sum(lista)

def factorial(n: int) -> int:
    lista = desde_hasta(0, n)
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, desde_hasta(1, n))

if __name__ == '__main__':
    print(desde_hasta(1, 5))   # [1, 2, 3, 4, 5]
    print(sumatoria(10))       # 55
    print(factorial(5))        # 120


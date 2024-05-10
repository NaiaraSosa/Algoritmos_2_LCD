"""
Ejercicio: Generador de primos
Implementar una función generadora que permita producir todos los números primos uno a uno.
"""

from collections.abc import Iterator

def generador_primos(n: int) -> Iterator[int]:
    numeros_no_primos = set()
    primo: int = 2

    while True:
        if primo not in numeros_no_primos:
            yield primo 

            # Marcar todos los múltiplos del número primo como compuestos
            numeros_no_primos.update(range(primo * primo, primo * primo * 2, primo))
        
        # Pasar al siguiente número para verificar si es primo
        primo += 1

for i in generador_primos(100):
    print(i)


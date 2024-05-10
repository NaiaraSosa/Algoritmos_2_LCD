"""
Ejercicio: Conteo de elementos
Definir utilizando reduce una operación que dada una lista de cadenas devuelva un diccionario 
donde las claves sean cada elemento de la lista y los valores sean la cantidad de apariciones que tiene ese elemento en la lista.
Ejemplo: contar(['a', 'b', 'c', 'a', 'a', 'c', 'b', 'd', 'c', 'a', 'e']) -> {'a': 4, 'b': 2, 'c': 3, 'd': 1, 'e': 1}.
"""

from functools import reduce

# Implementar contar(xs: list[str]) -> dict[str, int]

contar(['a', 'b', 'c', 'a', 'a', 'c', 'b', 'd', 'c', 'a', 'e']) # {'a': 4, 'b': 2, 'c': 3, 'd': 1, 'e': 1}
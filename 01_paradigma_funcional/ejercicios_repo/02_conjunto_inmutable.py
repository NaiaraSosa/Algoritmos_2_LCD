"""
Ejercicio: Conjunto inmutable
Implementar una versión de un conjunto de elementos de cualquier tipo que sea inmutable. 
Podemos apoyarnos en la tuple de Python. El conjunto se crea con una cantidad de elementos variables 
y luego ya no puede modificarse.
"""

from dataclasses import dataclass

@dataclass (frozen=True) # En True este parámetro evita la asignacion de nuevos valores

class ConjuntoInmutable():
    elementos: tuple

contenedor = ConjuntoInmutable(('a', 1, 3, 'b', 5))
print(contenedor)              # ConjuntoInmutable(elementos=('a', 1, 3, 'b', 5))
print(contenedor.elementos)    # ('a', 1, 3, 'b', 5)
contenedor.elementos[2] = 10   # TypeError: 'tuple' object does not support item assignment




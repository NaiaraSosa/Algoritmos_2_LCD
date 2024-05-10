"""
Ejercicio: Contar letras
A través del uso del map, dada una lista de cadenas generar una nueva lista que devuelva 
la cantidad que tiene de cierta letra (pasada como argumento) cada elemento. 
Por ejemplo, si queremos contar la letra 'a' en ['casa', 'hogar', 'espacio', 'cuento'] deberíamos obtener [2, 1, 1, 0].
"""

# Implementar contar_a(texto) o contar(letra, texto)

xs = ['casa', 'hogar', 'espacio', 'cuento']
list(map(contar_a, xs))     # [2, 1, 1, 0]
"""
Ejercicio: Decorando para valores faltantes
En ciertas situaciones veremos que una función no siempre puede devolver un valor como esperamos. 
Dependiendo de los argumentos recibidos, es posible que la función produzca algún error durante su evaluación 
o simplemente no encuentre un valor apropiado a devolver. En la programación funcional se suele utilizar 
la mónada Maybe para resolver este problema, pero nosotros itentearemos una solución más sencilla.

Se pide implementar una función decoradora acepta_no_valor que permita adaptar una función con un 
único parámetro de cualquier tipo no nulo de forma que devuelva la evaluación de esa función 
si el argumento recibido no es None. De lo contrario, debe devolver None.

TIP: Se puede usar el hint de tipo de retorno de la decoradora como: Callable[[T | None], R | None]. Ver Generics.
"""


# Implementar decorador acepta_no_valor

@acepta_no_valor
def incrementar(x: int) -> int:
    return x + 1

incrementar(20)     # 21
incrementar(None)   # None
"""
Ejercicio: Función de orden superior
- Implementar una función llamada wrapper que reciba por parámetro a otra función f sin argumentos, 
la ejecute e imprima en pantalla el mensaje de ejecución: "Ejecutada f()

- Extender la función wrapper de forma que pueda aceptar cualquier función con argumentos variables 
y se puedan pasar también desde la función wrapper para que se invoquen en f. 
Por ejemplo, si f acepta 3 argumentos, éstos deberían también pasarse a wrapper para que
se invoque f(arg1, arg2, arg3) dentro.
"""

from typing import Callable, Any

def wrapper(func: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
    print(f"Ejecutada {func.__name__}()")  
    func(*args, **kwargs)  

# El Callable[..., Any] nos permite aceptar cualquier función con cualquier cantidad de argumentos y tipo de retorno.
# Los argumentos args y kwargs nos permiten aceptar cualquier cantidad de argumentos posicionales y con nombre.

def saludar(nombre: str) -> None:
    print(f"Hola, {nombre}!")

def suma(a: int, b: int) -> None:
    print(f"La suma de {a} y {b} es: {a + b}")

# Uso de la función wrapper con diferentes funciones y argumentos
wrapper(saludar, "Juan")  # Ejecutada saludar()
                          # Hola, Juan!
wrapper(suma, 5, 3)       # Ejecutada suma()
                          # La suma de 5 y 3 es: 8



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# wrapper(test, 1, 'a', a = 3, x = 44, n = 'pepepe')
# Salida esperada:
# Ejecutada test()
# Argumentos posicionales: (1, 'a')
# Argumentos con nombre: {'a': 3, 'x': 44, 'n': 'pepepe'}
"""
Ejercicio: Pares
Definir la operación procedimiento pares, que dado un número entero, muestre todos los pares de números 
enteros positivos que son suma del número entero dado. Por ejemplo, 5 = (1 , 4), (2, 3).
"""

def pares(n: int):
    if n < 2:
        raise ValueError("El número debe ser mayor a 1")
    if n == 2:
        return (n-1, n-1)
    else: 
        return f'{pares (n-1)}, {pares(n+1)}'
    

if __name__ == '__main__':
    print(pares(4))




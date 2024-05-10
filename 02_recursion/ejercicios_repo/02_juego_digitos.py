"""
Ejercicio: Jugando con dígitos
"""

# a. Una función recursiva digitos, que dado un número entero, retorne su cantidad de dígitos.
def digitos(n:int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + digitos(n // 10) # le quita el ultimo numero a n

# b. Una función recursiva reversa_num que, dado un número entero, retorne su imagen especular. Por ejemplo: reversa_num(345) = 543
def reversa_num(n: int) -> int:
    if n < 10:
        return n
    else:
        potencia = 10 **(digitos(n)-1)
        primer_digito = n // potencia
        valor_previo = reversa_num(n - primer_digito * potencia)
        return valor_previo * 10 + primer_digito
    

# c. Una función recursiva suma_digitos que, dado un número entero, retorne la suma de sus dígitos.
def suma_digitos(n: int) -> int:
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n//10) # el % devuelve el ultimo digito del numero
    
# d. Una función recursiva que retorne los dos valores anteriores a la vez como un par, aprovechando la recursión.
def full(n:int) -> tuple[int, int]:
    if n < 10:
        return (n, n)
    else:
        potencia = 10 **(digitos(n)-1)
        ultimo_digito = n % 10
        reverso_previo, suma_previa = full(n//10)   # (reverso, suma)
        reverso = potencia * ultimo_digito + reverso_previo
        suma = ultimo_digito + suma_previa
        return (reverso, suma)
   

if __name__ == '__main__':
    n = 12345
    print(f'Dígitos de {n}: {digitos(n)}')
    print(f'Reversa de {n}: {reversa_num(n)}')
    print(f'Suma de {n}: {suma_digitos(n)}')
    print(f'Conjunto de {n}: {full(n)}')
from typing import Union, TypeAlias

# Especifica los elementos que voy a importar cuando invoque a nat
__all__ = ['Nat', 'cero', 'division', 'es_cero', 'igual', 'mayor', 'mayor_igual', 'menor', 'menor_igual', 'nat_to_int', 'potencia', 'pred', 'producto', 'resta', 'suc', 'suma']

Nat: TypeAlias = Union["Cero", "Suc"]

# Clases constructoras de estructura
class Cero:
    def __repr__(self):
        return 'Cero'

    def __str__(self):
        return '0'
    
    def __eq__(self, otro: "Nat"):      # para sobrecargar el ==
        return isinstance(otro, Cero)
    
    def __hash__(self):
        return 0
    
    def __lt__(self, otro:Nat):
        return False

class Suc:
    def __init__(self, pred: Nat):
        self.pred = pred

    def __repr__(self):
        return f'Suc({self.pred.__repr__()})'

    def __str__(self):
        return str(nat_to_int(self))
    
    def __eq__(self, otro: Nat):    # para sobrecargar el ==
        return isinstance(otro, Suc) and igual(self, otro)
    
    def __hash__(self):
        return hash((self.__repr__()))
    
    def __lt__(self, otro: Nat):
        return isinstance(otro, Suc) and menor(self, otro)
    
    def __sub__(self, otro: Nat):
        if isinstance(otro, Suc):
            return resta(self, otro)
        elif isinstance(otro, Cero):
            return self
        else:
            raise ValueError('pepe')

# Operaciones
def cero() -> Nat:
    return Cero()

def es_cero(n: Nat) -> bool:
    return isinstance(n, Cero)

def suc(n: Nat) -> Nat:
    return Suc(n)

def pred(n: Nat) -> Nat:
    if es_cero(n):
        raise ValueError('Cero no tiene predecesor')
    else:
        return n.pred

def nat_to_int(n: Nat) -> int:
    if es_cero(n):
        return 0
    else:
        return 1 + nat_to_int(pred(n))

# Operaciones de comparación
    
def igual(x: Nat, y: Nat) -> bool:
    if es_cero(x):
        return es_cero(y)
    elif es_cero(y):
        return False
    else:
        return igual(pred(x), pred(y))
    
def menor(x: Nat, y: Nat) -> bool:
    if es_cero(x):
        return not es_cero(y)
    elif es_cero(y):
        return False
    else:
        return menor(pred(x), pred(y))
    
def menor_iter(x: Nat, y: Nat) -> bool:
    while not es_cero(x) and not es_cero(y):
        x = pred(x)
        y = pred(y)
    return es_cero(x) and not es_cero(y)

# Operaciones de cuentas

def suma(x: Nat, y: Nat) -> Nat:
    if es_cero(x):
        return y
    else:
        return suma(pred(x), suc(y))
    
def resta(x: Nat, y: Nat) -> Nat:
    if not es_cero(x) and not es_cero(y):
        return resta(pred(x), pred(y))
    else: 
        return x
    
def producto(x: Nat, y: Nat) -> Nat:
    if isinstance(y, Cero):
        return cero()
    else:
        return suma(x, producto(x, pred(y)))

    
"""
Ejercicio: Extender el TAD Nat
A partir de la implementación de Nat, completar las operaciones que faltan definir.
"""

def mayor(x: Nat, y: Nat) -> bool:
    pass

def mayor_igual(x: Nat, y: Nat) -> bool:
    pass

def menor_igual(x: Nat, y: Nat) -> bool:
    pass

def division(x: Nat, y: Nat) -> Nat:
    pass

def potencia(base: Nat, exponente: Nat) -> Nat:
    pass

if __name__ == '__main__':
    n1: Nat = cero()                # n1 = 0
    n2: Nat = suc(suc(suc(n1)))     # n2 = 3
    n3: Nat = suc(suc(n2))          # n3 = 5
    n4: Nat = suc(suc(suc(n1)))     # n4 = 3

    # Comparaciones
    print(f'Son iguales n2 y n3: {igual(n2, n3)}')              # False
    print(f'Son iguales n2 y n4: {igual(n2, n4)}')              # True
    print(f'n2 < n3: {menor(n2, n3)}')                          # True

    # Cuentas
    print(f'n2 + n3: {suma(n2, n3)}')                           # 8
    print(f'n3 - n2: {resta(n3, n2)}')                           # 8
    print(f'n4 x n3: {producto(n3, n4)}')                       # 15
    
    
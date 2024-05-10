"""
Ejercicio: Par-Impar mejorado
Adaptar la solución propuesta con recursión mutua para determinar si un número es par o impar pero 
permitiendo aceptar también números negativos.
"""

def es_par(n: int) -> bool:
  if n == 0:
    return True
  elif n > 0:
    return es_impar(n - 1)
  else:
    return es_impar(n + 1)

def es_impar(n: int) -> bool:
  if n == 0:
    return False
  elif n > 0: 
    return es_par(n - 1)
  else:
    return es_par (n + 1)


if __name__ == '__main__':
  print(es_par(10))   # True
  print(es_par(9))    # False
  print(es_impar(4))  # False
  print(es_impar(7))  # True
  print(es_par(-8)) # True
  print(es_impar(-3)) # True

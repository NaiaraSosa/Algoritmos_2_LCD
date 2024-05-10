'''
Ejercicio: Permutaciones
Definir una funcion que dada una lista de números enteros, devuelva una lista de listas de todas las posibles permutaciones 
de esa lista original.

Por ejemplo: permutaciones([6,2,3]) = [[6,2,3], [6,3,2], [2,3,6], [2,6,3], [3,2,6], [3,2,6]]
'''

def permutar(xs: list[int]) -> list[list[int]]:
    xss: list[list[int]] = []
    if len(xs) == 1:
        return [xs]
    else:
        for i in range(len(xs)):
            primer_elemento = xs[i]
            resto_elementos = xs[:i] + xs[i+1:] # elementos antes y despues de i
            permutaciones_resto = permutar(resto_elementos)  # aplicamos la recursividad
            for perm in permutaciones_resto:
                xss.append([primer_elemento] + perm)
    return xss
print(permutar([5,2,6]))






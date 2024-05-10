'''
Ejercicio: Recorriendo un laberinto
Pensando una simplificación simplificada de un laberinto, definir una estructura que permita modelar un laberinto cuadrado. 
1. Generar un cuadrado con todas las posiciones (por ejemplo, 5x5, etc) donde cada posición sea un muro. Inicialmente el laberinto 
no tiene recorrido alguno. 
2. Definir como entrada la posición de arriba a la izquierda y la salida sería abajo a la derecha.
3. Construir al menos un camino utilizando el concepto de backtracking donde comenzamos desde la entrada e iremos 'tirando muros'
en un recorrido aleatorio hasta llegar a la salida. Imaginemos este proceso como el de una lombriz que va generando surcos de tierra.
Finalmente, implementar una operación que permita encontrar todos los caminos posibles desde la entrada hasta la salida del laberinto. 
'''


'''
Un estilo de implementación requiere mantener presente en cada instancia de recursión una copia de la solución parcial (camino 
recorrido recorrido hasta el momento), porque estamos probando muchas diferentes opciones y no queremos que se alteren. 
'''

# Algoritmo que encuentre un camino que lleve a la salida.
# camino_previo: precondición, lista solo con la posicion inicial del laberinto (entrada).
# posicion_actual: se determina con el último elemento de ese parámetro, camino de entrada hasta situación actual.

# TODO
# es_salida(): devuelve V la si posicion es una salida del laberinto.
# avanzar(): dada una posición en el laberinto y una dirección, devuelve la nueva posición que surge de ir en esa dirección desde la posición original.
# hay_paso(): valida si la posición actual es válida opara avanzar (si no tiene un muro que lo impida)

# En el caso recursivo: si no podemos avanzar, se descarta esa posición, y si avanzamos copiamos el camino previo como actual y 
# le agregamos la posicion actual final, y continuamos utilizando este como camino actual

class Posicion:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def es_salida(pos: Posicion):
    pass

def avanzar(pos: Posicion, direcciones: list[str]):
    pass

def hay_paso(pos: Posicion):
    pass

def recorrer(camino_previo: list[Posicion]) -> (bool, list[Posicion]): 
    posicion_actual = camino_previo[-1]
    if es_salida(posicion_actual):
        return True, camino_previo
    else:
        salida_encontrada = False
        direcciones = ['N', 'S', 'O', 'E']
        while direcciones and not salida_encontrada:
            nueva_posicion = avanzar(posicion_actual, direcciones.pop())
            if hay_paso(nueva_posicion) and nueva_posicion not in camino_previo:
                camino_actual = camino_previo.copy()
                camino_actual.append(nueva_posicion)
                salida_encontrada, solucion = recorrer(camino_actual)
        return salida_encontrada, solucion
    

def generar_caminos(camino_previo: list[Posicion]) -> tuple[(bool, list[Posicion])]: 
    posicion_actual = camino_previo[-1]
    if es_salida(posicion_actual):
        return True, camino_previo
    else:
        salida_encontrada = False
        direcciones = ['N', 'S', 'O', 'E']
        while direcciones and not salida_encontrada:
            nueva_posicion = avanzar(posicion_actual, direcciones.pop())
            if hay_paso(nueva_posicion) and nueva_posicion not in camino_previo:
                camino_actual = camino_previo.copy()
                camino_actual.append(nueva_posicion)
                salida_encontrada, solucion = recorrer(camino_actual)
        return salida_encontrada, solucion
    

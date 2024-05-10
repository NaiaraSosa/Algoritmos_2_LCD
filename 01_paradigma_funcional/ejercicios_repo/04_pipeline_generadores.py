"""
Ejercicio: Pipeline de datos con generadores
En ciertos casos podemos encontrarnos con archivos CSV muy grandes que no entren en memoria para procesarlos completamente, 
por lo cual veremos una forma de procesar datos a demanda a medida que se leen. Se pide implementar:
- un lector de archivo CSV utilizando 3 generadores:
    uno para producir cada línea leída del archivo.
    otro para producir una lista de campos string a partir de cada línea leída, consumiendo el generador previo.
    otro para producir un diccionario a partir de cada lista de campos obtenida con el generador previo.
- calcular la suma de los sepal_width de todas las especies Iris-setosa del dataset IRIS.csv, 
  utilizando un generador que produzca cada valor de sepal_width de una planta a la vez que sea de esa especie. 
  Valor esperado: 170.9
- similar al punto anterior, pero calculando el promedio del sepal_width de las especies Iris-setosa. 
  Valor esperado: 3.418
"""


import csv

def lector_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.reader(archivo)
        for linea in lector:
            yield linea

def campos_string_generador(lector):
    for linea in lector:
        yield [str(campo) for campo in linea]

def diccionario_generador(campos_generador):
    encabezados = next(campos_generador)
    for campos in campos_generador:
        yield dict(zip(encabezados, campos))

def sepal_width_iris_setosa(archivo):
    lector = lector_csv(archivo)
    campos_generador = campos_string_generador(lector)
    diccionario_generador_iris = diccionario_generador(campos_generador)
    suma_sepal_width = 0
    for planta in diccionario_generador_iris:
        if planta['species'] == 'Iris-setosa':
            suma_sepal_width += float(planta['sepal_width'])
    return suma_sepal_width

def promedio_sepal_width_iris_setosa(archivo):
    lector = lector_csv(archivo)
    campos_generador = campos_string_generador(lector)
    diccionario_generador_iris = diccionario_generador(campos_generador)
    suma_sepal_width = 0
    contador = 0
    for planta in diccionario_generador_iris:
        if planta['species'] == 'Iris-setosa':
            suma_sepal_width += float(planta['sepal_width'])
            contador += 1
    if contador == 0:
        return 0
    return suma_sepal_width / contador

# Ejemplo de uso
archivo = 'IRIS.csv'
suma_sepal_width = sepal_width_iris_setosa(archivo)
print("Suma de sepal_width de especies Iris-setosa:", suma_sepal_width)

promedio_sepal_width = promedio_sepal_width_iris_setosa(archivo)
print("Promedio de sepal_width de especies Iris-setosa:", promedio_sepal_width)

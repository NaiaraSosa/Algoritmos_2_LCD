"""
2. Crea una clase Persona con atributos nombre y edad. Además, hay que crear un método cumpleaños 
que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con Persona.
"""

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1

juan = Persona("Juan", 12)
juan.edad
juan.cumpleaños()
juan.edad
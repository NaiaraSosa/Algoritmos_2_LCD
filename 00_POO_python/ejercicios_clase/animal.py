"""
4. Define una clase base Animal con un método hablar(). Luego define varias clases derivadas 
que sobrescriban el método hablar para devolver el sonido caracteristico del animal
"""

class Animal:
    def hablar(self):
        print ('El animal hace sonido.')

class Perro(Animal):
    def hablar(self):
        print('El perro ladra.')
    
class Gato(Animal):
    def hablar(self):
        print('El gato maúlla')

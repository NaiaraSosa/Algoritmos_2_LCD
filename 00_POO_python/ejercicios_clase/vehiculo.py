"""5. Define una clase llamada Vehiculo con un atributo color y un metodo info() que imprima 
el color del vehiculo. Luego, se define una clase Coche que hereda de Vehiculo y tenga un atributo 
adicional marca. Sobreescriba el metodo info() en la clase Coche para que tambien imprima la marca"""

class Vehiculo:

    def __init__(self, color):
        self.color = color

    def info(self):
        print (f"Color: {self.color}.")

class Coche(Vehiculo):

    def __init__(self, color, marca):
        super().__init__(color)
        self.marca = marca

    def info(self):
        super().info()
        print("Marca:", self.marca, ".")

coche = Coche("Rojo", "Toyota")
coche.info()
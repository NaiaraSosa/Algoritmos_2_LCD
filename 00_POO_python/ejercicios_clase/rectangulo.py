"""
1. Escribe una clase llamada Rectangulo que tenga dos atributos: base y altura, 
y dos métodos para calcular el área y el perímetro del rectángulo
"""

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return f"El área del rectángulo es {self.base*self.altura}."
    
    def calcular_perimetro(self):
        return f"El perímetro del rectángulo es {(self.base*2)+(self.altura*2)}."
    
rectangulo = Rectangulo (5, 4)
rectangulo.base
rectangulo.calcular_area()
rectangulo.calcular_perimetro()

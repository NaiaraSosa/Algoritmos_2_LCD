"""
3. Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el 
método __init__. Calcular despues la suma, resta, multiplicacion y division. 
Utilizar un método para cada una e imprimir los resultados obtenidos
"""

class Calculadora:
    def __init__(self):
        self.valor1 = input ("Ingrese el primer valor.")
        self.valor2 = input ("Ingrese el segundo valor.")

    def suma(self):
        return self.valor1 + self.valor2
    
    def resta(self):
        return self.valor1 - self.valor2
    
    def multiplicacion(self):
        return self.valor1 * self.valor2
    
    def division(self):
        if self.valor2 != 0:
            raise ValueError("No se puede dividir por 0")
        else:
            return self.valor1 / self.valor2
    
calc = Calculadora()
print(calc.suma())
print(calc.resta())
print(calc.multiplicacion())
print(calc.division())

'''
Mochila
'''

from dataclasses import dataclass
from functools import reduce

@dataclass
class ItemMochila:
    peso: float
    valor: float

    def valor_ajutado(self) -> float:
        return self.valor / self.peso
    
    # Hacemos esto para usar el compareTo, sobreescribimos el método 'mayor a'
    def __gt__(self, otro: "ItemMochila"):
        return isinstance(otro, ItemMochila) and self.valor_ajutado() > otro.valor_ajutado()


class Mochila:
    def __init__(self, capacidad: float):
        self.capacidad = capacidad
        self.contenido = []

    def valor(self) -> float:
        return reduce(lambda acc, actual: acc + actual.valor, self.contenido, 0)
    
    def peso_disponible(self) -> float:
        return self.capacidad + reduce(lambda acc, actual: acc + actual.peso, self.contenido, 0)
    
    def entra_item(self, item: ItemMochila) -> bool:
        return self.peso_disponible() >= item.peso
    
    def agregar(self, item: ItemMochila):
        if self.entra_item(item):
            self.contenido.append(item)
        else:
            raise ValueError('Item no entra')
        
    def __str__(self):
        ret = f'Peso disponible: {self.peso_disponible()}/n'
        ret += f'Valor: {self.valor()}/n'
        ret += str(self.contenido)
        return ret

    def optimizar_greedy(self, items: list[ItemMochila]):
        def optimizar(items):
            if items:
                item = items[0]
                if self.entra_item(item):
                    self.agregar(item)
                    optimizar(items[1:])    
        items.sort(reverse=True) # mayor a menor
        optimizar(items)

if __name__ == '__main__':
    items = [
        ItemMochila(2.4, 10),
        ItemMochila(5.9, 20),
        ItemMochila(9.4, 3),
        ItemMochila(6.4, 6),
        ItemMochila(2.8, 8),
        ItemMochila(3.4, 17),
    ]

    mochila = Mochila(10)
    
    mochila.optimizar_greedy(items)
    
    print(mochila)
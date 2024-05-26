class Pagina:
    def __init__(self, nombre: str, contenido: str) -> None:
        self.nombre: str = nombre
        self.contenido: str = contenido
        self.vinculos: dict[str, Vinculo] = {}
    
    def agregar_vinculo(self, label: str, destino: "Pagina"):
        self.vinculos[label] = Vinculo(label, destino)

    def obtener_pagina_vinculo(self, nombre: str) -> "Pagina":
        if nombre not in self.vinculos:
            raise ValueError('Vinculo inexistente')
        else:
            return self.vinculos[nombre].get_destino()

    def __str__(self) -> str:
        return f'Pagina {self.nombre}\n  \
        -----------------------------  \
        {self.contenido} \
        *********  \
        <Vinculos>: {list(self.vinculos.keys())}'
    

class Vinculo:
    def __init__(self, label: str, destino: Pagina) -> None:
        self.label = label
        self.destino = destino

    def get_destino(self) -> Pagina:
        return self.destino
    
    def __str__(self) -> str:
        return self.label
        
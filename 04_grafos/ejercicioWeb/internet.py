from pagina import Pagina

class Internet:
    def __init__(self) -> None:
        self.paginas: dict[str, Pagina] = {}

    def agregar_pagina(self, pagina: Pagina):
        self.paginas[pagina.nombre] = pagina

    def obtener_pagina(self, nombre: str) -> Pagina:
        if nombre not in self.paginas:
            raise ValueError('HTTP CODE 404: Not Found')
        return self.paginas[nombre]
"""
Ejercicio: Modelar las zonas para censo
Implementar las clases necesarias para modelar las diferentes zonas a censar, donde país es la más amplia y se compone de provincias, etc. 
Todas deben tener un atributo de subzonas que representa la lista de zonas que las conforman, excepto la clase de vivienda que 
tiene el atributo habitantes. Finalmente, incorporar la operación recursiva de censar como método en la clase abstracta Zona.
"""

from dataclasses import dataclass
from abc import ABC

@dataclass
class Zona(ABC):
    subzonas: list

    def es_vivienda(self) -> bool:
        pass

@dataclass
class Vivienda():
    cant_habitantes: int

@dataclass
class Partido():
    nombre:str
    partido: list[Vivienda]

@dataclass
class Provincia():
    nombre: str
    provincia: list[Partido]


@dataclass
class Pais():
    nombre: str
    pais: list[Provincia]

def censar(zona: Zona) -> int:
    if zona.esVivienda():
        return zona.habitantes
    else:
        habitantes: int = 0
        for subzona in zona.subzonas:
            habitantes += censar(subzona)
        return habitantes


argentina = Pais()
print(argentina)
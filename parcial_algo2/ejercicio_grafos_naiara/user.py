from genero import Genero
from pelicula import Pelicula

class User:

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.perfil = {}
        for genero in Genero:
            self.perfil[genero] = 0

    def _actualizar_perfil(self, pelicula: Pelicula):
        for genero in pelicula.generos:
            self.perfil[genero] += 1

    def tiene_perfil_similar(self, otro: 'User') -> bool:
        for genero in Genero:
            if abs(self.perfil[genero] - otro.perfil[genero]) > 1:
                return False
        return True

    

    
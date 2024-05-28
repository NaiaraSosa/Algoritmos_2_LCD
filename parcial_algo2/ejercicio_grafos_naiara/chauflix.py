from user import User
from pelicula import Pelicula

class ChauFlix:
    def __init__(self) -> None:
        self.usuarios: dict[str, User] = {}
        self.peliculas: dict[str, Pelicula] = {}
        self.relaciones = {}

    def agregar_usuarix(self, usuario: User):
        if usuario.nombre in self.usuarios:
            raise ValueError('El usuario ya está registrado en la plataforma')
        else:
            self.usuarios[usuario.nombre] = usuario

    def agregar_pelicula(self, pelicula: Pelicula):
        if pelicula.titulo in self.peliculas:
            raise ValueError('La película ya se encuentra en la plataforma')
        else:
            self.peliculas[pelicula.titulo] = pelicula

    def mirar_pelicula(self, usuario: User, pelicula: Pelicula):
        usuario._actualizar_perfil(pelicula)
        self._actualizar_relaciones()

    def _actualizar_relaciones(self):
        self.relaciones = {usuario.nombre: set() for usuario in self.usuarios.values()}
        for usuario1 in self.usuarios.values():
            for usuario2 in self.usuarios.values():
                if usuario1 != usuario2 and usuario1.tiene_perfil_similar(usuario2):
                    self.relaciones[usuario1.nombre].add(usuario2.nombre)

    def tienen_relacion(self, usuario1: User, usuario2: User) -> bool:
        if usuario2.nombre in self.relaciones.get(usuario1.nombre, set()):
            return True
        return False
    
    def tienen_alguna_relacion(self, usuario1: User, usuario2: User) -> bool:
        def _tienen_relacion_recursiva(nombre_user1: str, nombre_user2: str, visitados: set) -> bool:
            if nombre_user1 == nombre_user2:
                return True
            visitados.add(nombre_user1)
            for usuario in self.relaciones.get(nombre_user1, []):
                if usuario not in visitados and _tienen_relacion_recursiva(usuario, nombre_user2, visitados):
                    return True
            return False
        return _tienen_relacion_recursiva(usuario1.nombre, usuario2.nombre, set())




from typing import Optional

class Nodo:
    def __init__(self, dato: int, especial: bool = False, si: "Optional[ArbEsp]" = None, sd: "Optional[ArbEsp]" = None):
        self.dato = dato
        self.especial = especial
        self.si: ArbEsp = ArbEsp() if si is None else si
        self.sd: ArbEsp = ArbEsp() if sd is None else sd

class ArbEsp:

    def __init__(self):
        self.raiz: Optional[Nodo] = None

    @staticmethod
    def crear_nodo(dato: int, especial: bool = False, si: "Optional[ArbEsp]" = None, sd: "Optional[ArbEsp]" = None) -> "ArbEsp":
        arbol = ArbEsp()
        arbol.raiz = Nodo(dato, especial, si, sd)
        return arbol
    
    def es_vacio(self) -> bool:
        return self.raiz is None
    
    def dato(self) -> int:
        assert self.raiz is not None
        return self.raiz.dato
    
    def si(self) -> "ArbEsp":
        assert self.raiz is not None
        return self.raiz.si
    
    def sd(self) -> "ArbEsp":
        assert self.raiz is not None
        return self.raiz.sd
    
    def insertar_si(self, si: "ArbEsp"):
        assert self.raiz is not None
        self.raiz.si = si

    def insertar_sd(self, sd: "ArbEsp"):
        assert self.raiz is not None
        self.raiz.sd = sd

    def preorder(self) -> list[int]:
        if self.es_vacio():
            return []
        return [self.dato()] + self.si().preorder() + self.sd().preorder()

    def preorder_especial(self) -> list[int]:
        def _preorder_especial_recursivo(nodo: Nodo) -> list[int]:
            if nodo is None:
                return []
            if nodo.especial:
                return [nodo.dato]
            return [nodo.dato] + _preorder_especial_recursivo(nodo.si.raiz) + _preorder_especial_recursivo(nodo.sd.raiz) # type: ignore
        return _preorder_especial_recursivo(self.raiz) # type: ignore
    
    def es_especial(self, valor: int) -> bool:
        if self.es_vacio():
            return False
        elif valor == self.dato() and self.raiz.especial: # type: ignore
            return True
        else:
            return self.si().es_especial(valor) or self.sd().es_especial(valor)

    # Se que seguramente no es como se esperaba pero no me dio el tiempo a pensar algo mas :)
    def podados(self) -> int:
        dfs = self.preorder()
        cant_dfs = len(dfs)
        dfs_especiales = self.preorder_especial()
        cant_dfs_especiales = len(dfs_especiales)
        return cant_dfs - cant_dfs_especiales
    






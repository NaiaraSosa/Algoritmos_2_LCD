from internet import Internet
from navegador import Navegador
from pagina import Pagina

def crear_internet():
    internet = Internet()
    google = Pagina('google', 'Esto es google')
    unsam = Pagina('unsam', 'Esto es unsam')
    duck =  Pagina('duck', 'Esto es duck')
    github = Pagina('github', 'Esto es github')
    ubuntu = Pagina('ubuntu', 'Esto es ubuntu')

    google.agregar_vinculo('unsam', unsam)
    google.agregar_vinculo('duck', duck)
    google.agregar_vinculo('github', github)
    google.agregar_vinculo('ubuntu', ubuntu)

    duck.agregar_vinculo('unsam', unsam)
    duck.agregar_vinculo('google', google)
    duck.agregar_vinculo('github', github)
    duck.agregar_vinculo('ubuntu', ubuntu)

    ubuntu.agregar_vinculo('unsam', unsam)
    unsam.agregar_vinculo('github', github)

    internet.agregar_pagina(google)
    internet.agregar_pagina(unsam)
    internet.agregar_pagina(unsam)
    internet.agregar_pagina(unsam)
    internet.agregar_pagina(unsam)
    

def main():
    internet = crear_internet()
    navegador = Navegador(internet)

if __name__ == '__main__':
    main()
from arbol_especial import ArbEsp

def main():
    t  = ArbEsp.crear_nodo(3)
    n2 = ArbEsp.crear_nodo(2, especial = True)
    n1 = ArbEsp.crear_nodo(1)
    n5 = ArbEsp.crear_nodo(5)
    n6 = ArbEsp.crear_nodo(6)
    n7 = ArbEsp.crear_nodo(7, especial = True)
    n0 = ArbEsp.crear_nodo(0)
  
    t.insertar_si(n2)
    t.insertar_sd(n6)
    n2.insertar_si(n1)
    n2.insertar_sd(n5)
    n6.insertar_sd(n7)
    n7.insertar_si(n0)

    print(f'Preorder: {t.preorder()}')
    print(f'Preorder especial: {t.preorder_especial()}')

    print(f'El 2 es especial: {t.es_especial(2)}')
    print(f'El 0 es especial: {t.es_especial(0)}')

    print(f'Cantidad de nodos no recorridos: {t.podados()}')


if __name__ == '__main__':
    main()

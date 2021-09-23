from claseArbolBinarioBusqueda import ArbolBinarioBusqueda
from claseMenu import Menu

if __name__ == '__main__':

    #-------------------------------------------#
    #   CREACIÓN DEL ARBOL BINARIO DE BÚSQUEDA  #
    #-------------------------------------------#
    arbol = ArbolBinarioBusqueda(70)
    raiz = arbol.getRaiz()
    arbol.insertar(raiz,47)
    arbol.insertar(raiz,92)
    arbol.insertar(raiz,35)
    arbol.insertar(raiz,68)
    arbol.insertar(raiz,83)
    arbol.insertar(raiz,100)
    arbol.insertar(raiz,79)
    
    menu = Menu('EJERCICIO 3')
    menu.setOpciones(['Mostrar el nodo padre y el nodo hermano, de un nodo',
                    'Mostrar la cantidad de nodos del árbol en forma recursiva',
                    'Mostrar altura del árbol',
                    'Mostrar los sucesores de un nodo' ])

    op = menu.showMenu()
    while op != 0:
        if op == 1:
            clave = int(input('Ingrese clave de un nodo: '))
            arbol.mostrarPadreHermano(raiz,clave)
        elif op == 2:
            cant = arbol.contarNodos(raiz)
            print("Cantidad de nodos: {}".format(str(cant)))
        elif op == 3:
            altura = arbol.altura(raiz)
            print("Altura del arbol: {}".format(str(altura)))
        elif op == 4:
            clave = int(input('Ingrese clave de un nodo: '))
            nodo = arbol.buscar(raiz,clave)
            print('Sucesores del nodo con clave {}: '.format(str(clave)))
            arbol.mostrarSucesores(nodo,clave)
            
        input("\nPresione una tecla para continuar...")
        op = menu.showMenu()
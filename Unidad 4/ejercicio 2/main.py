from claseArbolBinarioBusqueda import ArbolBinarioBusqueda

if __name__ == '__main__':
    arbol = ArbolBinarioBusqueda(70)
    raiz = arbol.getRaiz()
    arbol.insertar(raiz,47)
    arbol.insertar(raiz,92)
    arbol.insertar(raiz,35)
    arbol.insertar(raiz,68)
    arbol.insertar(raiz,83)
    arbol.insertar(raiz,100)
    arbol.insertar(raiz,79)
    
    input("\nArbol generado, pulse una tecla para continuar...")
    print("Frontera del arbol: {}".format(arbol.frontera(raiz)))    
from claseArbolBinarioBusqueda import ArbolBinarioBusqueda


if __name__ == '__main__':
    #--------------------------------------------#
    #   CREACION DEL ÁRBOL BINARIO DE BÚSQUEDA   #
    #--------------------------------------------#
    arbol = ArbolBinarioBusqueda(70)
    raiz = arbol.getRaiz()
    arbol.insertar(raiz,47)
    arbol.insertar(raiz,92)
    arbol.insertar(raiz,35)
    arbol.insertar(raiz,68)
    arbol.insertar(raiz,83)
    arbol.insertar(raiz,100)
    arbol.insertar(raiz,79)
    print("Intento insertar un nodo con clave existente")
    arbol.insertar(raiz,79)

    print("Busqueda del 68 y del 69")
    arbol.buscar(raiz,68)
    arbol.buscar(raiz,69)

    print("Inserto el 91")
    arbol.insertar(raiz,91)

    #--------------------------------------------#
    #    RECORRER EL ÁRBOL BINARIO DE BÚSQUEDA   #
    #--------------------------------------------#    
    arbol.preorden(raiz)
    print("\n")
    arbol.inorden(raiz)
    print("\n")
    arbol.postorden(raiz)
    print("\n")

    #--------------------------------------------#
    #       TEST DE LOS MÉTODOS RESTANTES        #
    #--------------------------------------------#  

    print("Suprimo la raiz del arbol (test suprimir nodo grado 2)")
    arbol.suprimir(raiz,70)
    arbol.inorden(raiz)
    print("\n")

    print("Suprimo nodo con clave 47 (test suprimir nodo grado 1)")
    arbol.suprimir(raiz,47)
    arbol.inorden(raiz)
    print("\n")

    print("Suprimo nodo con clave 79 (test suprimir nodo grado 0)")
    arbol.suprimir(raiz,79)
    arbol.inorden(raiz)
    print("\n")

    print("Determino el nivel del nodo con clave 100")
    nivel = arbol.nivel(raiz,100)
    print(nivel)

    print("Analizo si un nodo es hoja, hijo o padre")
    if arbol.hoja(raiz,79):
        print("79 es una hoja")

    if arbol.hijo(raiz,83,92):
        print("83 si es hijo de 92")
    else:
        print("No es hijo")

    if arbol.padre(raiz,83,92):
        print("92 es padre de 83")
    else:
        print("No es hijo")
    
    print("Muestro el camino entre distintos nodos")
    print(arbol.camino(raiz,70,91))
    print(arbol.camino(raiz,92,83))
    print(arbol.camino(raiz,990,91))
    print(arbol.camino(raiz,70,150))
    print(arbol.camino(raiz,79,100))

    print("Determino la altura del árbol")
    print(arbol.altura(raiz))

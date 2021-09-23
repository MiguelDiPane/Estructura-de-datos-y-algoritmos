class Nodo:
    __izq = None
    __der = None
    __clave = 0

    def __init__(self,clave=None):
        self.__izq = None
        self.__der = None
        self.__clave = clave
   
    def setIzq(self,izq):
        self.__izq = izq
    def setDer(self,der):
        self.__der = der
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def setClave(self,clave):
        self.__clave = clave
    def getClave(self):
        return self.__clave


class ArbolBinarioBusqueda:
    __raiz = None

    def __init__(self,clave):
        self.__raiz = Nodo(clave)

    #Analizo cada subarbol
    def insertar(self,raiz,clave):
        if clave == raiz.getClave():
            print("Error: Elemento ya existe")
        else:
            if clave < raiz.getClave():
                if raiz.getIzq() is None:
                    raiz.setIzq(Nodo(clave))
                    print("Exito - {} nueva hoja izquierda".format(str(clave)))
                else:
                    print("Se va por izquierda")
                    self.insertar(raiz.getIzq(),clave)
            elif clave > raiz.getClave():
                if raiz.getDer() is None:
                    raiz.setDer(Nodo(clave))
                    print("Exito - {} nueva hoja derecha".format(str(clave)))
                else:
                    print("Se va por derecha")
                    self.insertar(raiz.getDer(),clave)
        
    def getRaiz(self):
        return self.__raiz

    #Retorno el nodo
    def buscar(self,raiz,clave):
        if raiz == None:
            return None
        else:
            if clave == raiz.getClave():
                return raiz
            elif clave < raiz.getClave():
                #Buscar en raiz de subarbol izquierdo
                nodo = self.buscar(raiz.getIzq(),clave)
            elif clave > raiz.getClave():
                #Buscar en raiz de subarbol derecho
                nodo = self.buscar(raiz.getDer(),clave)
        return nodo

    def nivel(self,raiz,clave,nivel=1):
        if raiz == None:
            print("Error: Elemento inexistente")
            return None
        else:
            if clave == raiz.getClave():
                return nivel
            elif clave < raiz.getClave():
                #Buscar en raiz de subarbol izquierdo
                level = self.nivel(raiz.getIzq(),clave,nivel+1)
            elif clave > raiz.getClave():
                #Buscar en raiz de subarbol derecho
                level = self.nivel(raiz.getDer(),clave,nivel+1)        
        return level

    def hoja(self,raiz,clave):
        if raiz == None:
            print("Error: Elemento inexistente")
            return None
        else:
            if clave == raiz.getClave():
                if raiz.getIzq() == None and raiz.getDer() == None:
                    print("Exito: El nodo es una hoja")
                    return True
                else:
                    print("Falla: El nodo no es una hoja")
                    return False
            elif clave < raiz.getClave():
                #Buscar en raiz de subarbol izquierdo
                esHoja = self.hoja(raiz.getIzq(),clave)
            elif clave > raiz.getClave():
                #Buscar en raiz de subarbol derecho
                esHoja = self.hoja(raiz.getDer(),clave)
        return esHoja

    def hijo(self,raiz,claveH,claveP):
        if raiz == None:
            print("Error: Elemento inexistente")
            return None
        else:
            if claveP == raiz.getClave():
                izq = raiz.getIzq()
                der = raiz.getDer()
                if izq.getClave() == claveH or der.getClave() == claveH:
                    #El nodo con claveH si es hijo del nodo con claveP
                    return True
                else:
                    return False
            elif claveP < raiz.getClave():
                #Buscar en raiz de subarbol izquierdo
                esHijo = self.hijo(raiz.getIzq(),claveP,claveH)
            elif claveP > raiz.getClave():
                #Buscar en raiz de subarbol derecho
                esHijo = self.hijo(raiz.getDer(),claveP,claveH)        
            return esHijo

    def padre(self,raiz,claveH,claveP):
        if raiz == None:
            print("Error: Elemento inexistente")
            return None
        else:
            if claveP == raiz.getClave():
                izq = raiz.getIzq()
                der = raiz.getDer()
                if izq.getClave() == claveH or der.getClave() == claveH:
                    #El nodo con claveH si es hijo del nodo con claveP
                    return True
                else:
                    return False
            elif claveP < raiz.getClave():
                #Buscar en raiz de subarbol izquierdo
                esPadre = self.padre(raiz.getIzq(),claveP,claveH)
            elif claveP > raiz.getClave():
                #Buscar en raiz de subarbol derecho
                esPadre = self.padre(raiz.getDer(),claveP,claveH)        
            return esPadre

    def camino(self,raiz,claveX,claveZ,start=True,camino=None):
        if start:
            if raiz == None:
                print("Error: Elemento con clave X inexistente")
                return None
            else:
                if claveX == raiz.getClave():
                    #Se llego al nodo de partida, busco el nodo con clave Z
                    camino = []
                    miCamino = self.camino(raiz,claveX,claveZ,False,camino)
                elif claveX < raiz.getClave():
                    #Buscar en raiz de subarbol izquierdo
                    miCamino = self.camino(raiz.getIzq(),claveX,claveZ)
                elif claveX > raiz.getClave():
                    #Buscar en raiz de subarbol derecho
                    miCamino = self.camino(raiz.getDer(),claveX,claveZ)        
        else:
            if raiz == None:
                print("Error: No hay camino desde {} a {}".format(str(claveX),str(claveZ)))
                return None
            else:
                if claveZ == raiz.getClave():
                    #Se llego al nodo de destino
                    camino.append(claveZ)
                    return camino
                elif claveZ < raiz.getClave():
                    #Buscar en raiz de subarbol izquierdo
                    camino.append(raiz.getClave())
                    miCamino = self.camino(raiz.getIzq(),claveX,claveZ,False,camino)
                elif claveZ > raiz.getClave():
                    #Buscar en raiz de subarbol derecho
                    camino.append(raiz.getClave())
                    miCamino = self.camino(raiz.getDer(),claveX,claveZ,False,camino)
        return miCamino

    def grado(self,raiz):
        grado = 0
        if raiz.getIzq() != None:
            grado += 1
        if raiz.getDer() != None:
            grado += 1
        return grado

    #Busca entre los nodos mas chicos, el mas cercano a la raiz (el mayor de los menores)
    def __encontrarReemplazo(self,raiz,start=True):
        if raiz == None:
            return None
        else:
            if start:
                raiz = raiz.getIzq()
            if raiz.getDer() != None:
                raiz = raiz.getDer()
                self.__encontrarReemplazo(raiz,False)
            return raiz
    #Camino seguido para encontrar el nodo con clave mas cercana al nodo de grado 2 a eliminar
    #               /
    #               \
    #                 \        
        
    def suprimir(self,raiz,clave,ant=None):
        #Si el arbol esta vacio
        if raiz == None:
            return None
        else:
            #Al encontrar el nodo procedo a eliminar segun su grado
            if clave == raiz.getClave():
                #Si el nodo es de grado 0, elimino el nodo
                if raiz.getDer() is None and raiz.getIzq() is None:
                    if ant.getDer() == raiz:
                        ant.setDer(None)
                    else:
                        ant.setIzq(None)
                    del raiz
                #Nodo de grado 1, uno a su padre con su hijo
                elif raiz.getDer() is not None and raiz.getIzq() is None:
                    hijo = raiz.getDer()
                    ant.setDer(hijo)
                    del raiz
                elif raiz.getIzq() is not None and raiz.getDer() is None:
                    hijo = raiz.getIzq()
                    ant.setIzq(hijo)
                    del raiz
                #Nodo de grado 2
                elif raiz.getIzq() is not None and raiz.getDer() is not None:
                    #Obtengo el nodo cuya clave reemplazara a la raiz del subarbol de grado 2
                    nodoReemplazo = self.__encontrarReemplazo(raiz)
                    newClave = nodoReemplazo.getClave()
                    #Suprimo el nodo hoja que ahora sera la nueva raiz del subarbol
                    self.suprimir(self.__raiz,newClave)
                    #Seteo la clave en el subarbol
                    raiz.setClave(newClave)
                    
            #Si aun no lo encuentra se va por derecha o izquierda segun el valor de la clave
            elif clave < raiz.getClave():
                #Buscar en raiz de subarbol izquierdo
                self.suprimir(raiz.getIzq(),clave,raiz)
            elif clave > raiz.getClave():
                #Buscar en raiz de subarbol derecho
                self.suprimir(raiz.getDer(),clave,raiz)            
            
    #----------------------#
    #     RECORRIDOS       #
    #----------------------#
    def preorden(self, raiz):
        if raiz is not None:
            print(raiz.getClave(), end=", ")
            self.preorden(raiz.getIzq())
            self.preorden(raiz.getDer())
    
    def inorden(self, raiz, nivel=0):
        if raiz is not None:
            self.inorden(raiz.getIzq(),  nivel+1)
            print(' ' *7 * nivel + '--> {}'.format(raiz.getClave()))
            self.inorden(raiz.getDer(), nivel+1)

    def postorden(self, raiz):
        if raiz is not None:
            self.postorden(raiz.getIzq())
            self.postorden(raiz.getDer())
            print(raiz.getClave(), end=", ")

    #Sigue la logica de inorden
    def frontera(self,raiz,frontera=[]):
        if raiz is not None:
            self.frontera(raiz.getIzq(),frontera)
            clave = raiz.getClave()
            if self.hoja(raiz,clave):
                frontera.append(clave)
            self.frontera(raiz.getDer(),frontera)
            return frontera
    
    #----------------------------#
    #     METODOS EJERCICIO 3    #
    #----------------------------#

    def mostrarPadreHermano(self,raiz,clave,ant=None):
        if raiz == None:
            print("Error: Nodo inexistente")
        else:
            if clave == raiz.getClave():
                if ant != None:
                    #Busco si tiene hermano
                    if ant.getDer() == raiz:
                        hermano = ant.getIzq()
                    else:
                        hermano = ant.getDer()
                    print('Padre: {}'.format(str(ant.getClave())))
                    if hermano != None:
                        print('Hermano: {}'.format(str(hermano.getClave())))
                    else:
                        print('Hermano: No tiene')
                else:
                    print("La raiz del árbol no tiene padre ni hermanos")
                
            elif clave < raiz.getClave():
                #Buscar en raiz de subarbol izquierdo
                self.mostrarPadreHermano(raiz.getIzq(),clave,raiz)
            elif clave > raiz.getClave():
                #Buscar en raiz de subarbol derecho
                self.mostrarPadreHermano(raiz.getDer(),clave,raiz)
   
    def contarNodos(self,raiz):
        if raiz is None:
            return 0
        return 1 + self.contarNodos(raiz.getIzq()) + self.contarNodos(raiz.getDer())
    
    #Sigue la logica del postorden
    def altura(self,raiz):
        if raiz is None:
            return 0
        else :
            #Calcular la altura de cada subarbol
            HIzq = self.altura(raiz.getIzq())
            HDer = self.altura(raiz.getDer())
            #Retorno la mas grande
            if (HIzq > HDer):
                altura = HIzq + 1
            else:
                altura = HDer + 1
            return altura

    def mostrarSucesores(self, raiz,clave):
        if raiz is not None:
            self.mostrarSucesores(raiz.getIzq(),clave)
            if raiz.getClave() != clave:
                print('- {}'.format(raiz.getClave()))
            self.mostrarSucesores(raiz.getDer(),clave)        
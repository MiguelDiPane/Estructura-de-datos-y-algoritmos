class PilaSecuencial:
    __items = None
    __tope = -1
    __cant = 0

    def __init__(self,xcant=0):
        self.__items = []
        self.__cant = xcant
        self.__tope = -1
    
    def vacia(self):
        vacia = False
        if(self.__tope == -1):
            vacia = True
        return vacia

    def llena(self):
        llena = False
        if(self.__tope == self.__cant-1):
            llena = True
        return llena 

    def insertar(self,x):
        if(not self.llena()):
            self.__items.append(x)
            self.__tope = self.__tope + 1
        else:
            print("Pila llena")
    
    def suprimir(self):
        if(self.vacia()):
            return None
        else:
            x = self.__items.pop()
            self.__tope = self.__tope - 1
            return x

class Nodo:
    __item = None
    __sig = None 

    def __init__(self,xitem=None):
        self.__item = xitem
        self.__sig = None

    def getItem(self):
        return self.__item

    def setSiguiente(self, siguiente):
        self.__sig = siguiente
    
    def getSiguiente(self):
        return self.__sig

#pila dinamica (no coloco la cantidad de elementos al crearla) 
class PilaEncadenada: 
    __comienzo = None
    __cant = 0

    def __init__(self):
        self.__comienzo = None
        self.__cant = 0
    
    def vacia(self):
        vacia = False
        if(self.__cant == 0):
            vacia = True
        return vacia       

    def insertar(self,xitem):
        nodo = Nodo(xitem)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__cant += 1

    def suprimir(self):
        if(self.vacia()):
            print("Pila vacia")
        else:
            x = self.__comienzo.getItem()
            self.__comienzo = self.__comienzo.getSiguiente()
            self.__cant -= 1
            return x

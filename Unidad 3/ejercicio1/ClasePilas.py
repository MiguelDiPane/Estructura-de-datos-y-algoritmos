class PilaSecuencial:
    __items = None
    __tope = -1
    __cant = 0

    def __init__(self,xcant=0):
        self.__items = []
        self.__cant = xcant
        self.__tope = -1
    
    def vacia(self):
        return self.__tope == -1

    def llena(self):
        return self.__tope == self.__cant-1

    def insertar(self,x):
        if(not self.llena()):
            self.__items.append(x)
            self.__tope = self.__tope + 1
        else:
            print("Pila llena")
    
    def suprimir(self):
        result = None
        if not self.vacia():
            result = self.__items.pop()
            self.__tope = self.__tope - 1
        return result 

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
        return self.__cant == 0
    
    #Inserta por cabeza
    def insertar(self,xitem):
        nodo = Nodo(xitem)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__cant += 1

    def suprimir(self):
        result = None
        if not self.vacia():
            result = self.__comienzo.getItem()
            self.__comienzo = self.__comienzo.getSiguiente()
            self.__cant -= 1
        return result

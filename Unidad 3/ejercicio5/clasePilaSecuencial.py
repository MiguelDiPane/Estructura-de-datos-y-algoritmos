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
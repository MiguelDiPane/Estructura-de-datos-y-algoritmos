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

    #Inserta por cabeza
    def insertar(self,x):
        if not self.llena():
            self.__items.append(x)
            self.__tope = self.__tope + 1
    
    def suprimir(self):
        x = None
        if not self.vacia():
            x = self.__items.pop()
            self.__tope = self.__tope - 1
        return x
import numpy as np

class PilaSecuencial():
    __items = None
    __topeInf = 0
    __topeSup = 0
    __cant = 0

    def __init__(self,xcant=0):
        self.__items = np.empty(xcant,dtype=int)
        self.__cant = xcant
        self.__topeInf = -1
        self.__topeSup = xcant
    
    def vacia(self):
        return [self.__topeInf == -1, self.__topeSup == self.__cant] #[pila1, pila2]

    def llena(self):
        return self.__topeInf == self.__topeSup-1

    def insertarInf(self,x):
        if not self.llena():
            self.__topeInf += 1
            self.__items[self.__topeInf] = x    

    def insertarSup(self,x):
        if not self.llena():
            self.__topeSup -= 1
            self.__items[self.__topeSup] = x 

    def suprimirInf(self):
        x = None
        vacia = self.vacia()
        if not vacia[0]:
            x = self.__items[self.__topeInf]
            self.__topeInf -= 1
        return x

    def suprimirSup(self):
        x = None
        vacia = self.vacia()
        if not vacia[1]:
            x = self.__items[self.__topeSup]
            self.__topeSup += 1
        return x
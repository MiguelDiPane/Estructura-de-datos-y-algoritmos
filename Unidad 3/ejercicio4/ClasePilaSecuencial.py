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
        vacia = [False, False] #[pila1, pila2]
        if(self.__topeInf == -1):
            vacia[0] = True
        if (self.__topeSup == self.__cant):
            vacia[1] = True
        return vacia

    def llena(self):
        llena = False
        if(self.__topeInf == self.__topeSup-1):
            llena = True           
        return llena 

    def insertarInf(self,x):
        llena = self.llena()
        if(not llena):
            self.__topeInf += 1
            self.__items[self.__topeInf] = x    
        else:
            print("Pila inferior llena")

    def insertarSup(self,x):
        llena = self.llena()
        if(not llena):
            self.__topeSup -= 1
            self.__items[self.__topeSup] = x 
        else:
            print("Pila superior llena")

    def suprimirInf(self):
        x = None
        vacia = self.vacia()
        if(vacia[0]):
            x = "Pila inferior vacia"
        else:
            x = self.__items[self.__topeInf]
            self.__topeInf -= 1
        return x

    def suprimirSup(self):
        vacia = self.vacia()
        if(vacia[1]):
            x = "Pila superior vacia"
        else:
            x = self.__items[self.__topeSup]
            self.__topeSup += 1
        return x
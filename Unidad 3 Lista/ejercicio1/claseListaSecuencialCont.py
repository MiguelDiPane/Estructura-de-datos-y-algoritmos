class ListaSecuencialCont:
    __items = None
    __tope = 0
    __cant = 0

    def __init__(self,cant):
        self.__items = []
        self.__tope = 0
        self.__cant = cant
             
    def vacia(self):
        return self.__tope == 0
    def llena(self):
        return self.__tope == self.__cant
    
    def insertar(self,item):
        if not self.llena():
            if self.vacia():
                self.__items.append(item)
            else:
                i = 0
                while i < self.__tope and item > self.__items[i]:
                    i+=1
                if i == self.__tope:
                    self.__items.append(item)
                else:
                    #Corro el ultimo elemento para hacer lugar al nuevo
                    self.__items.append(self.__items[self.__tope-1])
                    #Shifteo
                    for j in range(self.__tope,i,-1):
                        self.__items[j] = self.__items[j-1]
                    self.__items[i] = item
            self.__tope +=1 
        else:
            print("Lista llena")

    def suprimir(self,pos):
        if pos >= 0 and pos < self.__tope:
            if self.vacia():
                print("Lista vacia")
            else:
                for i in range(pos,self.__tope-1):
                    self.__items[i] = self.__items[i+1]
                self.__tope -= 1

    def suprimirCont(self,item):
        if self.vacia():
            print("Lista vacia")
        else:
            i = 0
            while i<self.__tope and item != self.__items[i]:
                i+=1
            if i == self.__tope:
                print("Elemento no encontrado")
            else:
                for j in range(i,self.__tope-1):
                    self.__items[j] = self.__items[j+1]
                self.__tope -= 1

    def recuperar(self,pos):
        item = None
        if pos >= 0 and pos < self.__tope:
            item = self.__items[pos]
        return item

    #Localiza el elemento en la lista y retorna su indice o None (si no esta)
    def buscar(self,elemento):
        indice = None
        esta = False
        i = 0
        while i < self.__tope and not esta:
            if self.__items[i] == elemento:
                esta = True
            else:
                i += 1
        if i < self.__tope:
            indice = i
        return indice

    def primer_elemento(self):
        if not self.vacia():
            return self.__items[0]
        else:
            print("La lista esta vacia")

    def ultimo_elemento(self):
        if not self.vacia():
            return self.__items[self.__tope-1]
        else:
            print("La lista esta vacia")

    def siguiente(self,pos):
        result = None
        if pos >= 0 and pos < self.__tope-1:
            result = self.__items[pos+1]
        return result

    def anterior(self,pos):
        result = None
        if pos > 0 and pos < self.__tope:
            result = self.__items[pos-1]
        return result

    def recorrer(self):
        print("[",end="")
        for i in range(self.__tope):
            print(" {0} ".format(self.__items[i]), end="")
        print("]\n")


class ListaSecuencial:
    __elementos = None
    __tope = 0
    __cant = 0

    def __init__(self,cant):
        self.__elementos = []
        self.__tope = 0
        self.__cant = cant
   
    def vacia(self):
        return self.__tope == 0
    def llena(self):
        return self.__tope == self.__cant
    
    #Pos es el indice donde se va a insertar
    def insertar(self,elemento,pos):
        if not self.llena():
            if pos >= 0 and pos <= self.__tope:
                if self.vacia():
                    self.__elementos.append(elemento)
                else:
                    if pos == self.__tope:
                        self.__elementos.append(elemento)
                    else:
                        #Agrego una copia del ultimo elemento al final, para hacer espacio al nuevo elemento
                        self.__elementos.append(self.__elementos[self.__tope-1])
                        #Shifteo desplaza desde el ultimo elemento hasta el elemento ubicado en pos-1 (donde ira el nuevo elemento)
                        for i in range(self.__tope,pos,-1):
                            self.__elementos[i] = self.__elementos[i-1]
                        self.__elementos[pos] = elemento
                self.__tope += 1
        else:
            print("Lista llena")

    def suprimir(self,pos):
        if pos >= 0 and pos < self.__tope:
            if self.vacia():
                print("Lista vacia")
            else:
                for i in range(pos,self.__tope-1):
                    self.__elementos[i] = self.__elementos[i+1]
                self.__tope -= 1
  
    def recuperar(self,pos):
        result = None
        if pos >= 0 and pos < self.__tope:
            result = self.__elementos[pos]
        return result

    #Localiza el elemento en la lista y retorna su indice o None (si no esta)
    def buscar(self,elemento):
        indice = None
        esta = False
        i = 0
        while i < self.__tope and not esta:
            if self.__elementos[i] == elemento:
                esta = True
            else:
                i += 1
        if i < self.__tope:
            indice = i
        return indice

    def primer_elemento(self):
        if not self.vacia():
            return self.__elementos[0]
        else:
            print("La lista esta vacia")

    def ultimo_elemento(self):
        if not self.vacia():
            return self.__elementos[self.__tope-1]
        else:
            print("La lista esta vacia")

    def siguiente(self,pos):
        result = None
        if pos >= 0 and pos < self.__tope-1:
            result = self.__elementos[pos+1]
        return result

    def anterior(self,pos):
        result = None
        if pos > 0 and pos < self.__tope:
            result = self.__elementos[pos-1]
        return result

    def recorrer(self):
        print("[",end="")
        for i in range(self.__tope):
            print(" {0} ".format(self.__elementos[i]), end="")
        print("]\n")

    def len(self):
        return self.__tope

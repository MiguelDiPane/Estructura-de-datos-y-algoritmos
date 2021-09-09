class Nodo:
    __dato = None
    __sig = None

    def __init__(self,dato=None):
        self.__dato = dato
        self.__sig = None
    def setSiguiente(self,siguiente):
        self.__sig = siguiente
    def getSiguiente(self):
        return self.__sig
    def getDato(self):
        return self.__dato
    def setDato(self,dato):
        self.__dato = dato

class ListaEncadenadaCont:
    __comienzo = None
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__tope = 0

    def vacia(self):
        return self.__tope == 0

    #Inserta segun el valor del elemento
    def insertar(self,elemento):
        newNodo = Nodo(elemento)
        if self.vacia():
            self.__comienzo = newNodo
        else:
            aux = self.__comienzo
            ant = self.__comienzo
            while aux != None and aux.getDato() < elemento:
                ant = aux
                aux = aux.getSiguiente()
            
            #Inserta al final
            if aux == None:
                ant.setSiguiente(newNodo)
            #Inserta por cabeza
            elif aux == self.__comienzo:
                newNodo.setSiguiente(aux)
                self.__comienzo = newNodo
            else:
                newNodo.setSiguiente(aux)
                ant.setSiguiente(newNodo)
        self.__tope += 1

    def suprimir(self,pos):
        if pos >=0 and pos < self.__tope: 
            if pos == 0:
                aux = self.__comienzo
                self.__comienzo = aux.getSiguiente()
            else:
                anterior = self.__comienzo
                aux = self.__comienzo
                i = 0
                while i != pos:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i+=1
                anterior.setSiguiente(aux.getSiguiente())
            self.__tope -= 1
    
    #Suprimir segun el elemento
    def suprimirCont(self,elemento):
        if not self.vacia():
            aux = self.__comienzo
            ant = self.__comienzo

            while aux != None and aux.getDato() != elemento:
                ant = aux
                aux = aux.getSiguiente()

            #Elimina la cabeza
            if aux == self.__comienzo:
                self.__comienzo = aux.getSiguiente()
            #No se encontro el elemento
            elif aux == None:
                print("Elemento no encontrado")
            #Encadenamiento entre anterior y siguiente al nodo con el elemento a eliminar
            else:
                ant.setSiguiente(aux.getSiguiente())
            self.__tope -= 1
            del aux
        else:
            print("Lista vacia")

    def recuperar(self,pos):
        result = None
        if pos >= 0 and pos < self.__tope:
            aux = self.__comienzo
            i = 0
            while i < pos:
                aux = aux.getSiguiente()
                i += 1
            result = aux.getDato()
        return result

    def buscar(self,elemento):
        i = 0
        indice = None
        esta = False
        aux = self.__comienzo
        while aux != None and not esta:
            if aux.getDato() == elemento:
                esta = True
            else:
                aux = aux.getSiguiente()
                i+=1
        if aux != None:
            indice = i
        return indice

    def primer_elemento(self):
        return self.__comienzo.getDato()

    def ultimo_elemento(self):
        aux = self.__comienzo
        ant = self.__comienzo
        while aux != None:
            ant = aux
            aux = aux.getSiguiente()
        return ant.getDato()

    def siguiente(self,pos):
        result = None
        if pos >= 0 and pos < self.__tope-1:
            i=0
            aux = self.__comienzo
            while i < pos+1:
                aux = aux.getSiguiente()
                i+=1
            result = aux.getDato()
        return result

    def anterior(self,pos):
        result = None
        if pos > 0 and pos < self.__tope:
            i=0
            aux = self.__comienzo
            while i < pos-1:
                aux = aux.getSiguiente()
                i+=1
            result = aux.getDato()
        return result   

    def recorrer(self):
        aux = self.__comienzo
        print("[",end="")
        while aux != None:
            print(" {0} ".format(aux.getDato()), end="")
            aux = aux.getSiguiente()
        print("]\n")
        
    def len(self):
        return self.__tope
class Nodo:
    __dato = 0
    __sig = 0

    def __init__(self):
        self.__sig = -2 #Equivale a null 
    def setDato(self,dato):
        self.__dato = dato
    def getDato(self):
        return self.__dato
    def setSig(self,sig):
        self.__sig = sig
    def getSig(self):
        return self.__sig

class ListaCursores:
    __items = None
    __max = 0
    __cab = 0
    __cant = 0
    __disponible = 0

    def __init__(self,xmax):
        self.__max = xmax
        self.__cab = 0
        self.__cant = 0
        self.__items = []
        for i in range(xmax):
            newNodo = Nodo()
            self.__items.append(newNodo)
   
    def vacia(self):
        return self.__cant == 0
    def llena(self):
        return self.__cant == self.__max
    
    def getDisponible(self):
        i = 0
        while i < self.__max and self.__items[i].getSig() != -2:
            i+=1
        if i < self.__max:
            disp = i
        else:
            disp = -2
        return disp
    
    def freeDisponible(self,disp):
        liberado = False
        if disp >= 0 and disp < self.__max:
            self.__items[disp].setSig(-2)
            liberado = True
        return liberado
    
    #Insertar por posicion
    def insertarPos(self,item,pos):
        exito = False
        self.__disponible = self.getDisponible()
        if not self.llena():
            if pos >= 0 and pos <= self.__cant and self.__disponible != -2:
                #Fisicamente lo colca en el primer lugar disponible que encuentra
                self.__items[self.__disponible].setDato(item)
                ant = self.__cab
                aux = self.__cab
                i = 0
                while i < pos:
                    i+=1
                    ant = aux
                    aux = self.__items[aux].getSig()
                
                #Enlace a su posicion correcta
                #Inserta al inicio de la lista
                if aux == self.__cab:
                    #Inserta en lista vacia
                    if self.__cant == 0:
                        self.__items[self.__cab].setSig(-1)
                    #Inserta en la lista con elementos
                    else:
                        self.__items[self.__disponible].setSig(self.__cab)
                    self.__cab = self.__disponible
                #Inserta al final de la lista
                elif aux == -1:
                    self.__items[self.__disponible].setSig(-1)
                    self.__items[ant].setSig(self.__disponible)
                else:
                    self.__items[self.__disponible].setSig(aux)
                    self.__items[ant].setSig(self.__disponible)
                self.__cant += 1
                exito = True
            else:
                print("Posición incorrecta o no disponible")
        else:
            print("Lista llena")
        return exito

    #Insertar por contenido
    def insertarCont(self,item):
        self.__disponible = self.getDisponible()
        if not self.llena() and self.__disponible != -2:
            ant = self.__cab
            aux = self.__cab
            i = 0
            #Fisicamente lo coloca al final de los elementos
            self.__items[self.__disponible].setDato(item)
            while i < self.__cant and aux != -1 and self.__items[aux].getDato() < item:
                i += 1
                ant = aux
                aux = self.__items[aux].getSig()
            #Inserta al inicio de la lista
            if aux == self.__cab:
                #Inserta en lista vacia
                if self.__cant == 0:
                    self.__items[self.__cab].setSig(-1)
                #Inserta en la lista con elementos
                else:
                    self.__items[self.__disponible].setSig(self.__cab)
                self.__cab = self.__disponible 
            #Inserta al final de la lista
            elif self.__cab == -1:
                self.__items[self.__disponible].setSig(-1)
                self.__items[ant].setSig(self.__disponible)
            else:
                self.__items[self.__disponible].setSig(aux)
                self.__items[ant].setSig(self.__disponible)
            self.__cant += 1
            exito = True
        else:
            print("Espacio lleno o no disponible")
            exito = False
        return exito

    def suprimir(self,pos):
        dato = None
        if not self.vacia():
            if pos >= 0 and pos < self.__cant:
                ant = self.__cab
                aux = self.__cab
                i = 0
                while i < pos and aux != -1:
                    i+=1
                    ant = aux
                    aux = self.__items[aux].getSig()
                if aux == self.__cab:
                    if self.__cant == 1:
                        self.__cab = 0
                    else:
                        self.__cab = self.__items[ant].getSig()
                else:
                    self.__items[ant].setSig(self.__items[aux].getSig())
                dato = self.__items[aux].getDato()
                self.__disponible = aux
                self.freeDisponible(self.__disponible)
                self.__cant -= 1
            else: 
                print("Posicion incorrecta")
        else:
            print("Lista vacía")
        return dato

    def recuperar(self,pos):
        result = None
        if pos >= 0 and pos < self.__cant:
            aux = self.__cab
            while aux != pos:
                aux = self.__items[aux].getSig()
            
            result = self.__items[aux].getDato()
        return result

    def buscar(self,elemento):
        i = 0
        indice = None
        esta = False
        aux = self.__cab
        ant = self.__cab
        while aux != -1 and not esta:
            if self.__items[aux].getDato() == elemento:
                esta = True
            else:
                ant = aux
                aux = self.__items[aux].getSig()
        if aux != -1:
            indice = ant 
        return indice

    def primer_elemento(self):
        return self.__items[self.__cab].getDato()

    def ultimo_elemento(self):
        aux = self.__cab
        ant = self.__cab
        while aux != -1:
            ant = aux
            aux = self.__items[aux].getSig()
        return self.__items[ant].getDato()

    def siguiente(self,pos):
        result = None
        if pos >= 0 and pos < self.__cant-1:
            aux = self.__cab
            while aux < pos+1:
                aux = self.__items[aux].getSig()
            result = self.__items[aux].getDato()
        return result

    def anterior(self,pos):
        result = None
        if pos > 0 and pos < self.__cant:
            aux = self.__cab
            while aux < pos-1:
                aux = self.__items[aux].getSig()
            result = self.__items[aux].getDato()
        return result   
   
    def recorrer(self):
        header = '+' + '-'*35 + '+'
        print(header)
        print("|{0:^35}|".format("Lista enlazada por cursores"))
        print(header)
        print("|{0:35}|".format(" Cabeza: " + str(self.__cab)))
        print(header)
        print("|{0:^8}|{1:^12}|{2:^13}|".format("Índice","Valor","Siguiente"))
        print(header)
        i=0
        while i != self.__cant:
            if self.__items[i].getSig() != -2:
                print("|{0:^8}|{1:^12}|{2:^13}|".format(i,self.__items[i].getDato(),self.__items[i].getSig()))
            i+=1
        print(header)

        
 


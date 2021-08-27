class ColaSecuencial:
    __items = None
    __max = 0 #Cantidad max de elementos (estructura estática)
    __pr = 0 #Apunta al primer elemento
    __ul = 0 #Apunta al ultimo elemento
    __cant = 0 #Cantidad de elementos en un momento dado

    def __init__(self, xmax=0):
        __pr = 0
        __ul = 0
        __cant = 0
        __items = []
    
    def vacia(self):
        vacia = False
        if self.__cant == 0:
            vacia = True
        return vacia
    
    def llena(self):
        llena = False
        if self.__cant == self.__max:
            llena = True
        return llena
    
    def insertar(self,x):
        if not self.llena():
            self.__items.insert(self.__ul,x)
            #Para la referencia circular y que ul se ponga en 0 al llegar al final
            self.__ul = (self.__ul+1)%self.__max #Incremento usando aritmética modular
            self.__cant += 1
            return x
        else:
            return 0
    
    #Suprime el primero (primero en entrar, primero en salir)
    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
            return 0
        else:
            x = self.__items[self.__pr]
            self.__pr = (self.__pr+1)%self.__max #Incremento usando aritmética modular
            self.__cant -= 1
            return x
    
    #Incrementar 1 minuto en los elementos de la cola de espera
    #Tiene orden de comp lineal por la accion iterativa
    def recorrer(self):
        if not self.vacia():
            i = self.__pr
            for j in range(self.__cant):
                pass

class Nodo:
    __dato = None
    __sig = None

    def __init__(self,dato=0):
        self.__dato = dato
        self.__sig = None
    def setSiguiente(self,siguiente):
        self.__sig = siguiente
    def getSiguiente(self):
        return self.__sig
    def getDato(self):
        return self.__dato

class ColaEncadenada:
    __cant = 0
    __pr = None #Son de tipo Nodo
    __ul = None

    def __init__(self,nodoPr = None, nodoUl = None, xcant = 0):
        self.__pr = nodoPr
        self.__ul = nodoUl
        self.__cant = xcant

    def vacia(self):
        vacia = False
        if self.__cant == 0:
            vacia = True
        return vacia
     
    #Cola dinamica, no tiene max
    def insertar(self,x):
        newNodo = Nodo(x)
        if self.__ul == None: #si no hay nada ul y pr apuntan al mismo nodo
            self.__pr = newNodo
        else:
            self.__ul.setSiguiente(newNodo)
        self.__ul = newNodo
        self.__cant += 1
        return x
    
    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
            return 0
        else:
            aux = self.__pr #Para borrar el nodo
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            if self.__pr == None: #si el primero queda nulo, el ultimo debe quedar nulo
                self.__ul = None
            del aux
            return x
    
    def recuperarPr(self):
        return self.__pr
    
    def recorrer(self, auxPr):
        if type(auxPr) == Nodo:
            if auxPr != None:
                item = auxPr.getDato()
                print(item)
                self.recorrer(self,auxPr.getSiguiente())

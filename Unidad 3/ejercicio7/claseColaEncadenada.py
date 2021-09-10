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

    def __init__(self,xcant=0):
        self.__pr = None
        self.__ul = None
        self.__cant = xcant

    def vacia(self):
        return self.__cant == 0
     
    #Cola dinamica, no tiene max
    def insertar(self,x):
        newNodo = Nodo(x)
        if self.__ul == None: #si no hay nada ul y pr apuntan al mismo nodo
            self.__pr = newNodo #Mantiene siempre el primer nodo
        else:
            self.__ul.setSiguiente(newNodo) #lo agrega luego del ultimo
        self.__ul = newNodo #Queda apuntando al ultimo
        self.__cant += 1
        return x
    
    def suprimir(self):
        x =  None
        if not self.vacia():
            aux = self.__pr
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            if self.__pr == None: #si el primero queda nulo, el ultimo debe quedar nulo
                self.__ul = None
            del aux
        return x
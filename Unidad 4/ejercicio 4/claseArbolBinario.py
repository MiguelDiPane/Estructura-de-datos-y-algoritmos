class Nodo:
    __izq = None
    __der = None
    __char = None
    __frec = 0

    def __init__(self,char=None,frec=0):
        self.__izq = None
        self.__der = None
        self.__char = char
        self.__frec = frec
   
    def setIzq(self,izq):
        self.__izq = izq
    def setDer(self,der):
        self.__der = der
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def setChar(self,char):
        self.__char = char
    def getChar(self):
        return self.__char
    def getFrec(self):
        return self.__frec
    def setFrec(self,frec):
        self.__frec = frec


class ArbolBinario:
    __raiz = None

    def __init__(self,char,frec):
        self.__raiz = Nodo(char,frec)

    def getRaiz(self):
        return self.__raiz

    def insertar(self,nodo):
        if self.__raiz.getIzq() is None:
            self.__raiz.setIzq(nodo)
        else:
            self.__raiz.setDer(nodo)

    #-----------------------------------#
    #   CODIFICACIÓN Y DECODIFICACIÓN   #
    #-----------------------------------#
    
    def codCaracter(self,raiz,char):
        if raiz.getChar() != char:
            nodoIzq = raiz.getIzq()
            nodoDer = raiz.getDer()
            if char in nodoIzq.getChar():
                #Al ir por izquierda concateno un 0
                cod = '0' + self.codCaracter(nodoIzq,char)
            elif char in nodoDer.getChar():
                #Al ir por derecha concateno un 1
                cod = '1' + self.codCaracter(nodoDer,char)
            #No se encontro el caracter
            else:
                cod = 'x'
            return cod
        else:
            #Caso base
            return ''
    
    def decCaracter(self,raiz,cod,ant=None):
        if raiz != None:
            if cod != '':
                #Leo el primer digito
                primerDigito = cod[0]
                #Actualizo el codigo sacando el digito ya leido
                cod = cod[1:] 
                #Segun el valor del digito me voy por izquierda o derecha
                if primerDigito == '0':
                    char = self.decCaracter(raiz.getIzq(),cod,raiz)
                if primerDigito == '1':
                    char = self.decCaracter(raiz.getDer(),cod,raiz)
                return char
            else:
                #Caso base, veo el caracter en el nodo hoja
                char = raiz.getChar()
                return char
        else:
            #No se encontro una hoja con el codigo ingresado
            return 'Codigo desconocido'

    #----------------------------#
    #   MOSTRAR ARBOL GENERADO   #
    #----------------------------#
    def mostrar(self, raiz, nivel=0):
        if raiz is not None:
            self.mostrar(raiz.getDer(),  nivel+1)
            print(' ' *7 * nivel + '--> {0}'.format(raiz.getChar()))
            print(' ' *7 * nivel + '    {0}'.format(raiz.getFrec()))
            self.mostrar(raiz.getIzq(), nivel+1)

    #------------------------------#
    #   SOBRECARGA DE OPERADORES   #
    #------------------------------#
    #less than or equal to
    def __le__(self,arbol):
        result = False
        if type(arbol) == ArbolBinario:
            raiz = arbol.getRaiz()
            if self.__raiz.getFrec() <= raiz.getFrec():
                result = True
        return result

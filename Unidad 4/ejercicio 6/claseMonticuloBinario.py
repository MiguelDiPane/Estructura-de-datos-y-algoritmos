from rich import print

class MonticuloBinario:
    __items = None

    def __init__(self):
        self.__items = [None] #No trabajo con la posicion 0
    
    def vacio(self):
        return len(self.__items) == 1
    
    def insertar(self,item):
        if not self.vacio():
            #-------------------------#
            # Propiedad de estructura #
            #-------------------------#

            #Implica insertar al final (primer nodo hoja extremo derecho)
            self.__items.append(item)

            #-------------------------#
            #   Propiedad de orden    #
            #-------------------------#

            #Comparar el nodo con su padre, e intercambiar si es mayor
        
            posHijo = len(self.__items) - 1 
            posPadre = posHijo // 2

            #Intercambio si la priodiad del hijo es mayor a la del padre
            while self.__items[posPadre] != None and self.__items[posHijo] < self.__items[posPadre]:
                    aux = self.__items[posHijo]
                    self.__items[posHijo] = self.__items[posPadre]
                    self.__items[posPadre] = aux

                    #Actualizo posiciones
                    posHijo = posPadre
                    posPadre = posHijo // 2
        else:
            #Inserto el primer elemento del montículo binario
            self.__items.append(item)

    def eliminar_minimo(self):
        resultado = None
        if not self.vacio():
            #-------------------------#
            # Propiedad de estructura #
            #-------------------------#

            resultado = self.__items.pop(1)
            ultimo = self.__items.pop()

            #Reinserto el ultimo en el primer lugar
            self.__items.insert(1,ultimo)

            #-------------------------#
            #   Propiedad de orden    #
            #-------------------------#
            posPadre = 1
            posHIzq = posPadre * 2
            posHDer = posPadre * 2 + 1

            while posHDer < len(self.__items) and (self.__items[posPadre] > self.__items[posHIzq] or self.__items[posPadre] > self.__items[posHDer]):
                if self.__items[posHIzq] <= self.__items[posHDer]:
                    aux = self.__items[posHIzq]
                    self.__items[posHIzq] = self.__items[posPadre]
                    self.__items[posPadre] = aux
                    posPadre = posHIzq
                else:
                    aux = self.__items[posHDer]
                    self.__items[posHDer] = self.__items[posPadre]
                    self.__items[posPadre] = aux 
                    posPadre = posHDer

                posHIzq = posPadre * 2
                posHDer = posPadre * 2 + 1 
                                  
        return resultado

    #Sigo la logica inorden
    def mostrar(self,i=1,nivel=0):
        if not self.vacio():
            if i < len(self.__items):
                if len(self.__items) == 2:
                    print(self.__items[i])
                else:
                    #Hijo izquierdo
                    posHIzq = i*2
                    self.mostrar(posHIzq,nivel+1)
                    print(' ' *7 * nivel + '[bold cyan]--> [/bold cyan]{}'.format(self.__items[i]))
                    #Hijo derecho
                    posHDer = i*2+1
                    self.mostrar(posHDer, nivel+1)
        else:
            print('[bold cyan]vacio[/bold cyan]')



#----------------------------#
# Test del monticulo binario #
#----------------------------#

#monti = MonticuloBinario()
#for i in range(10):
#    monti.insertar((i+1)*10)

#monti.mostrar()

#monti.insertar(35)
#monti.mostrar()

#print("\n")
#result = monti.eliminar_minimo()
#monti.mostrar()

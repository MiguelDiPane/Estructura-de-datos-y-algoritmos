from clasePilaSecuencial import PilaSecuencial
class Torres():
    __pilas = None
    __tablero = None
    __n = 0

    def __init__(self,n):
        self.__pilas = []
        self.__tablero = []
        self.__n = n
        for i in range(3):
            self.__pilas.append(PilaSecuencial(n))
        
        #Inicialización de los discos en torre 1 (pila 1)
        for i in range(n,0,-1):
            self.__pilas[0].insertar(i)
        self.setTablero()
     
    #Inicialización del tablero (gráficos)
    def setTablero(self):
        for i in range(3):
            torre = []
            for j in range(self.__n):
                if i == 0:
                    torre.append("-"*(2*j+1)) #Para mostrar numero impar de -
                else:
                    torre.append("|")
            base = "="*(2*j+3)
            nombre = "Torre {}".format(i+1)
            torre.append(base)
            torre.append(nombre)
            self.__tablero.append(torre)

    def moverDisco(self,origen,destino):
        cont = 0
        if origen.isdigit() and destino.isdigit():
            origen = int(origen)-1
            destino = int(destino)-1
            if (origen >=0 and origen < 3) and (destino>=0 and destino < 3):
                x = self.__pilas[origen].suprimir()
                y = self.__pilas[destino].suprimir() #saber el valor del tope en destino para comparar
                if y != None: #Solo reinserto si tenia algo el destino en tope
                    self.__pilas[destino].insertar(y)
                if x == None:
                    print("No hay discos en la torre {}".format(str(origen+1)))
                    input("Presione una tecla para continuar...")
                else:
                    if self.__pilas[destino].vacia() or x < y:
                        self.__pilas[destino].insertar(x)
                        self.__tablero[origen][x-1] = "|"
                        self.__tablero[destino][x-1] = "-"*(x + (x-1))
                        cont = 1
                    else:
                        self.__pilas[origen].insertar(x) #reinserto en la torre original
                        print("No puede colocar el disco en la torre {}".format(str(destino+1)))
                        print("Solo puede apilar una pieza encima de una más grande")
                        input("Presione una tecla para continuar...")
            else:
                print("Error: Número de torre no válido")
                input("presione una tecla para continuar...")              
        else:
            print("Error: debe ingresar un número de torre")
            input("Presione una tecla para continuar...")
        return cont #Retorno si se hizo el movimiento (1) o (0) si no se hizo
    
    def mostrarTablero(self):
        data = self.__tablero
        for i in range(len(data[0])):
            print("|{0:^20}{1:^20}{2:^20}|".format(data[0][i],data[1][i],data[2][i]))
    
    def finJuego(self):
        fin = False
        if self.__pilas[2].llena():
            fin = True
        return fin
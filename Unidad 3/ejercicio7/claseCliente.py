class Cliente:
    __tLlegada = 0
    __num = 0
    def __init__(self,tLlegada):
        self.__tLlegada = tLlegada
        self.__num = 0
    def setNumero(self,num):
        self.__num = num
    def getNumero(self):
        return self.__num
    def getTiempoEspera(self,tAtencion):
        return (tAtencion - self.__tLlegada)
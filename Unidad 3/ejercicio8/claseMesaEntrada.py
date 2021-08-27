class MesaEntrada:
    __tAtencion = 0
    __timer = 0
    __libre = True

    def __init__(self,tAtencion):
        self.__tAtencion = tAtencion
        self.__timer = 0
        self.__libre = True
    def libre(self):
        return self.__libre
    def setOcupado(self):
        self.__libre = False
    def actualizar(self):
        self.__timer += 1
        if self.__timer == self.__tAtencion:
            self.__libre = True
            self.__timer = 0
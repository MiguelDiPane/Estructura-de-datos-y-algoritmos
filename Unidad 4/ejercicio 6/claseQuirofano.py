class Quirofano:
    __libre = True
    __tAtencion = 0
    __timer = 0

    def __init__(self):
        self.__libre = True
        self.__tAtencion = 0
        self.__timer = 0
    
    def libre(self):
        return self.__libre

    def setOcupado(self):
        self.__libre = False
    
    def setTAtencion(self,tAtencion):
        self.__tAtencion = tAtencion
    
    def actualizar(self):
        self.__timer += 1
        if self.__timer == self.__tAtencion:
            self.__timer = 0
            self.__libre = True
            
class Consultorio:
    __tAtencion = 0
    __timer = 0
    __libre = True
    __especialidad = ""
    __atendidos = 0

    def __init__(self,tAtencion,especialidad,atendidos=0):
        self.__tAtencion = tAtencion
        self.__timer = 0
        self.__libre = True
        self.__especialidad = especialidad
        self.__atendidos = atendidos

    def libre(self):
        return self.__libre
    def setOcupado(self):
        self.__libre = False
    def actualizar(self):
        self.__timer += 1
        if self.__timer == self.__tAtencion:
            self.__libre = True
            self.__timer = 0
    def getEspecialidad(self):
        return self.__especialidad
    def getAtendidos(self):
        return self.__atendidos
    def addAtendido(self):
        self.__atendidos += 1

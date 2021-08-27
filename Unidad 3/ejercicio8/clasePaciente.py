class Paciente:
    __nombre = ""
    __dni = ""
    __especialidad = ""
    __numConsultorio = 0
    __tLlegada = 0
    __tObtieneTurno = 0 #Almacena el instante en que se le entrega el turno
    
    def __init__(self,nom,dni,esp,numCons,tllegada,tObtieneTurno = 0):
        self.__nombre = nom 
        self.__dni = dni
        self.__especialidad = esp
        self.__numConsultorio = numCons
        self.__tLlegada = tllegada
        self.__tObtieneTurno = tObtieneTurno
    
    def setTiempoObtieneTurno(self,tObtieneTurno):
        self.__tObtieneTurno = tObtieneTurno

    def getTiempoEspera(self,tAtencion):
        return tAtencion - self.__tLlegada
    def getTiempoEsperaCons(self,tAtencion):
        return tAtencion - self.__tObtieneTurno
    def getNumConsultorio(self):
        return self.__numConsultorio
    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getEsp(self):
        return self.__especialidad
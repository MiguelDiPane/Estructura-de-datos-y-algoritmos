class Incendio:
    __provincia = None
    __supAfectada = 0

    def __init__(self,prov,sup):
        self.__provincia = prov
        self.__supAfectada = sup
    
    def getProv(self):
        return self.__provincia
    def getHa(self):
        return self.__supAfectada
    def addSup(self,sup):
        self.__supAfectada += sup
        #Redondeo superficie a 2 decimales
        self.__supAfectada = round(self.__supAfectada,2)
class Designacion:
    __anio = 0
    __ambito = "" #Federal o nacional
    __cargo = ""
    __instancia = ""
    __materia = ""
    __cantVarones = 0
    __cantMujeres = 0

    def __init__(self,anio,ambito,cargo,instancia,materia,cantV,cantM):
        self.__anio = anio
        self.__ambito = ambito
        self.__cargo = cargo
        self.__instancia = instancia
        self.__materia = materia
        self.__cantVarones = cantV
        self.__cantMujeres = cantM
    
    def getAnio(self):
        return self.__anio
    def getAmbito(self):
        return self.__ambito
    def getCargo(self):
        return self.__cargo
    def getInstancia(self):
        return self.__instancia
    def getMateria(self):
        return self.__materia
    def getVarones(self):
        return self.__cantVarones
    def getMujeres(self):
        return self.__cantMujeres

    #Sobrecarga de operadores para comparación al insertar item en la lista
    def __lt__(self,myDesignacion):
        result = False
        if type(myDesignacion) == Designacion:
            if self.__anio < myDesignacion.getAnio():
                result = True
        return result

    
    

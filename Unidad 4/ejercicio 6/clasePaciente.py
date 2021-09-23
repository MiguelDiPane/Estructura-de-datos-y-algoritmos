class Paciente:
    __nombre = ''
    __prioridad = 0

    def __init__(self,nombre,prioridad):
        self.__nombre = nombre
        self.__prioridad = prioridad
    
    def getNombre(self):
        return self.__nombre
    
    def getPrioridad(self):
        return self.__prioridad

    # Sobrecara de operadores para comparar por claves
    def __ne__(self,paciente):
        if type(paciente) == Paciente:
            if self.__prioridad != paciente.getPrioridad():
                return True
            else:
                return False 
        elif paciente == None:
            return True       
    
    def __lt__(self,paciente):
        if type(paciente) == Paciente:
            if self.__prioridad < paciente.getPrioridad():
                return True
            else:
                return False

    def __le__(self,paciente):
        if type(paciente) == Paciente:
            if self.__prioridad <= paciente.getPrioridad():
                return True
            else:
                return False
    def __gt__(self,paciente):
        if type(paciente) == Paciente:
            if self.__prioridad > paciente.getPrioridad():
                return True
            else:
                return False
    
    def __str__(self):
        mensaje = '{0} - P: {1}'.format(self.__nombre,str(self.__prioridad))
        return mensaje
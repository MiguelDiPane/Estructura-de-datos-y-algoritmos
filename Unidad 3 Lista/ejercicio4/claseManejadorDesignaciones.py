from claseListaEncadenadaCont import ListaEncadenadaCont
from claseDesignacion import Designacion

class ManejadorDesignaciones:
    __lista = None

    def __init__(self):
        self.__lista = ListaEncadenadaCont()
    
    def agregar(self,anio,ambito,cargo,instancia,materia,cantV,cantM):
        newDesignacion = Designacion(anio,ambito,cargo,instancia,materia,cantV,cantM)
        self.__lista.insertar(newDesignacion)
    
    def mostrar(self):
        print("{0:5}|{1:10}|{2:10}|{3:10}|{4:30}|{5:10}|{6:10}".format("Año","Ámbito","Cargo",
                                                                "Instancia","Materia",
                                                                "Varones","Mujeres"))
        print("-"*91)                                               
        for i in range(self.__lista.len()):
            des= self.__lista.recuperar(i)
            print("{0:<5}|{1:10}|{2:10}|{3:10}|{4:30}|{5:<10}|{6:<10}".format(des.getAnio(),des.getAmbito(),
                                                                            des.getCargo(),des.getInstancia(),
                                                                            des.getMateria(),des.getVarones(),
                                                                            des.getMujeres()))
            
    #-----------------------------#
    #       FUNCIONALIDADES       #
    #-----------------------------#
    def calcularCantMujeres(self,myCargo):
        #Recupero los años disponibles para generar la planilla
        anios = self.getAnios()
        #Inicializo los diccionarios
        desMujeres = []
        for i in range(len(anios)):
            dic = {'anio':anios[i],'cantM':0}
            desMujeres.append(dic)
        
        for i in range(self.__lista.len()):
            #Recupero la designacion
            des = self.__lista.recuperar(i)
            cargo = des.getCargo()
            cantMujeres = des.getMujeres()
            anio = des.getAnio()
            #Solo opero si el cargo es igual al seleccionado
            if cargo == myCargo:
                i = anios.index(anio)
                desMujeres[i]['cantM'] += cantMujeres

        self.__mostrarMujeres(desMujeres,myCargo)
    
    def __mostrarMujeres(self,designaciones,cargo):
        encabezado = self.__header("Designaciones de mujeres por año")
        print('| Cargo: {0:34}|'.format(cargo))
        print(encabezado)
        print('|{0:^20}| {1:^20}|'.format('Año','Cantidad'))
        print(encabezado)
        for designacion in designaciones:
            print('|{0:^20}| {1:^20}|'.format(designacion['anio'],designacion['cantM']))
        print(encabezado)

    def calcularAgentes(self,myAnio,myMateria,myCargo):
        cantAgentes = 0
        i = 0
        des = self.__lista.recuperar(i)
        anio = des.getAnio()
        while i < self.__lista.len() and anio <= myAnio:
            if anio == myAnio:
                materia = des.getMateria()
                cargo = des.getCargo()
                if materia == myMateria and cargo == myCargo:
                    cantAgentes += des.getVarones()
                    cantAgentes += des.getMujeres()
            des = self.__lista.recuperar(i)
            anio = des.getAnio()
            i+=1
        self.__mostrarAgentes(cantAgentes,myAnio,myMateria,myCargo)

    def __mostrarAgentes(self,cantAgentes,anio,materia,cargo):
        encabezado = self.__header("Agentes designados - Año {0}".format(anio))
        print('|{0:42}|'.format(' Cargo: ' + cargo))
        print('|{0:42}|'.format(' Materia: ' + materia))
        print('|{0:42}|'.format(' Cantidad: ' + str(cantAgentes)))
        print(encabezado)
               

    #-----------------------------#
    #     METODOS AUXILIARES      #
    #-----------------------------#

    def getCargos(self):
        cargos = []
        i=0
        while i < self.__lista.len():
            des = self.__lista.recuperar(i)
            cargo = des.getCargo()
            if cargo not in cargos:
                cargos.append(cargo)
            i = i+1
        return cargos
    
    def getAnios(self):
        anios = []
        i = 0
        while i < self.__lista.len():
            des = self.__lista.recuperar(i)
            anio = des.getAnio()
            if anio not in anios:
                anios.append(anio)
            i = i+1
        return anios
    
    def getMaterias(self):
        materias = []
        i = 0
        while i < self.__lista.len():
            des = self.__lista.recuperar(i)
            materia = des.getMateria()
            if materia not in materias:
                materias.append(materia)
            i = i+1
        return materias      

    def __header(self,titulo):
        header = '+' + '-'*42 + '+'
        print(header)
        print('|{0:^42}|'.format(titulo))
        print(header) 
        return header
from claseIncendio import Incendio
from claseListaEncadenada import ListaEncadenada

class ManejadorProvincias:
    __lista = None

    def __init__(self):
        self.__lista = ListaEncadenada()
    
    #Agrega una nueva provincia a la lista, o acumula superficie a una provincia existente
    def agregar(self,prov,sup):
        i = 0
        esta = False
        while i < self.__lista.len() and not esta:
            incendio = self.__lista.recuperar(i)
            provAnalizar = incendio.getProv()
            if prov == provAnalizar:
                incendio.addSup(sup)
                esta = True
            else:
                i+=1    
        if i == self.__lista.len():
            incendio = Incendio(prov,sup)
            self.__lista.insertar(incendio,i)

    #Metodo de la burbuja
    def ordenarPorSup(self):
        for j in range(1,self.__lista.len()):
            for i in range(0,self.__lista.len()-j):
                incendio1 = self.__lista.recuperar(i)
                incendio2 = self.__lista.recuperar(i+1)
                if incendio1.getHa() < incendio2.getHa():
                    self.__lista.setNodo(incendio2,i)
                    self.__lista.setNodo(incendio1,i+1)

    def mostrarLista(self):
        print("\n{0:25}|{1:25}".format("Provincia","Superficie afectada [ha]"))
        print("-"*51)
        i=0
        while i < self.__lista.len():
            incendio = self.__lista.recuperar(i)
            prov = incendio.getProv()
            sup = incendio.getHa()
            print("{0:25}|{1:25}".format(prov,sup))
            i+=1
#-------------------------------#
#        CONSIDERACIONES        #
#-------------------------------#
# Política manejo de colisiones: Encadenamiento

# Función de transformación de claves: Método de plegado

import numpy as np
from claseListaEncadenada import ListaEncadenada

class TablaHash:

    def __init__(self,cantidad_claves,usar_primo=True):
        if usar_primo:
            self.__factor_carga = 0.7
            self.__M = self.obtener_primo(int(cantidad_claves/self.__factor_carga))
        else:
            self.__M = cantidad_claves

        #Arreglo inicializado en None (todas las componentes desocupadas)
        self.__datos = np.full(self.__M,None)
    
    def insertar(self,clave):
        pos_original = self.obtener_pos_inicial_por_plegado(clave)
        pos_insercion = self.obtener_pos_insercion_por_encadenamiento(clave,pos_original)
        return pos_insercion
    
    #Devuelve la lista de claves dada una posición
    def buscar_claves(self,pos):
        lista_claves = None
        if pos >= 0 and pos  < self.__M:
            lista_claves = self.__datos[pos]
        lista_claves.recorrer()
    
    #Devuelve la posición en la tabla dada una clave
    def buscar_posicion(self,clave):
        pos_inicial_tabla = self.obtener_pos_inicial_por_plegado(clave)   
        if self.__datos[pos_inicial_tabla] == None: #si es == None, no está la lista creada
            pos_inicial_tabla = -1
            indice_en_lista = -1
        else:
            indice_en_lista = self.__datos[pos_inicial_tabla].buscar(clave)
        
        return pos_inicial_tabla, indice_en_lista
         
    #--------------------------------------#
    #   FUNCIONES DE TRANSFORMACIÓN h(k)   #
    #--------------------------------------#
    
    #Generación de posición por método de la división, retorna indice dentro del arreglo
    def obtener_pos_inicial_por_division(self,clave):
        return clave % self.__M
    
    #Generación de posición por método de plegado, retorna indice dentro del arreglo
    def obtener_pos_inicial_por_plegado(self,clave):
        clave_string = str(clave)
        lista_valores = []
        #Separar los dígitos en pares
        for i in range(0,len(clave_string),2): #paso de a dos
            if i+1 < len(clave_string):
                lista_valores.append(int(clave_string[i:i+2]))
            else:
                lista_valores.append(int(clave_string[i]))
        
        pos_inicial = sum(lista_valores)

        #Corregir por módulo M si excede la cantidad de listas disponibles
        if pos_inicial >= self.__M:
            pos_inicial = self.obtener_pos_inicial_por_division(pos_inicial)

        return pos_inicial

    #-------------------------------#
    # POLÍTICA MANEJO DE COLISIONES # 
    #-------------------------------#  
        
    def obtener_pos_insercion_por_encadenamiento(self,clave,pos):
        if self.__datos[pos] == None:
            self.__datos[pos] = ListaEncadenada() #Creo la lista si no está
        self.__datos[pos].insertar(clave,0) #Inserto por cabeza de la lista
        return pos

    #-----------------------#
    #   MÉTODOS AUXILIARES  #
    #-----------------------#

    def obtenerDatos(self):
        return self.__datos

    def obtener_primo(self,numero):
        encontro_primo = False

        while not encontro_primo:
            esPrimo = True
            i = 2
            while esPrimo and i < numero:
                if numero % i == 0:
                    esPrimo = False
                i+=1
            if not esPrimo:
                numero += 1
            else:
                encontro_primo = True
        
        return numero

    def calcular_factor_carga(self):
        contador = 0
        for i in range(len(self.__datos)):
            if self.__datos[i] != None:
                contador += 1
        factor_carga = contador / self.__M
        print(factor_carga)

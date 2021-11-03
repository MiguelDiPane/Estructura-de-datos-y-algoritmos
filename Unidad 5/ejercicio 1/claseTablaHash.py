#-------------------------------#
#        CONSIDERACIONES        #
#-------------------------------#
# Política manejo de colisiones: Direccionamiento abierto

# Función de transformación de claves: Método de la división

# Procesamiento de claves sinónimas: Secuencia de prueba lineal

import numpy as np

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
        pos_inicial = self.obtener_pos_inicial_por_division(clave)
        pos_insercion = self.obtener_pos_insercion_por_sec_prueba_lineal(pos_inicial,clave)
        
        if pos_insercion != -1:
            self.__datos[pos_insercion] = clave
        else:
            #Peor caso: recorrer todo el arreglo y no encontrar posición disponible
            print("Tabla saturada, no es posible almacenar la clave")
        
    #Devuelve la clave, dada su posicion
    def buscar_clave(self,pos):
        result = None
        if pos >= 0 and pos < self.__M:
            result = self.__datos[pos]
        return result
    
    #Devuelve la posicion de una clave
    def buscar_posicion(self,clave):
        pos_inicial = self.obtener_pos_inicial_por_division(clave)
        pos_insercion = self.obtener_pos_insercion_por_sec_prueba_lineal(pos_inicial,clave,True)
        result = -1

        if pos_insercion != -1:
            if self.__datos[pos_insercion] == clave: #si es == None, no está el valor buscado
                result = pos_insercion
        return result
         
    #----------------------------------#
    # FUNCIÓN DE TRANSFORMACIÓN H(K)   #
    #----------------------------------#
    
    #Generación de posición por método de la división, retorna indice dentro del arreglo
    def obtener_pos_inicial_por_division(self,clave):
        return clave % self.__M

    #------------------------------------#
    # POLÍTICA DE MANEJO DE COLISIONES   #
    #------------------------------------#
       
    #Secuencia de prueba lineal, recorrido CIRCULAR ASCENDENTE
    #Retorno la posición donde debe ir el elemento
    def obtener_pos_insercion_por_sec_prueba_lineal(self,pos,valor,mostrar_long=False):
        pos_insercion = -1
        cant_pruebas = 0 #Para cálculo de la longitud de la secuencia de prueba

        #Analizo las posiciones en forma circular ascendente
        while pos_insercion == -1 and cant_pruebas < self.__M:
            if  self.__datos[pos] == None or self.__datos[pos] == valor: 
                pos_insercion = pos
            else:
                #Incremento usando aritmética modular
                pos = (pos+1)%self.__M #dará resto 0 con pos = M, resetea la pos a 0
                cant_pruebas += 1
        
        if mostrar_long:
            print('Longitud de la secuencia de prueba: {}'.format(cant_pruebas))
        
        return pos_insercion

    #------------------------#
    #   MÉTODOS AUXILIARES   #
    #------------------------#

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
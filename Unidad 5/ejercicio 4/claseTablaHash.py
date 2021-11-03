#-------------------------------#
#        CONSIDERACIONES        #
#-------------------------------#
# Política manejo de colisiones: Uso de buckets

# Función de transformación de claves: Método de extracción
import numpy as np

class registro:
    def __init__(self,cantidad_elementos):
        #Arreglo inicializado en None (todas las componentes desocupadas)
        self.elementos = np.full(cantidad_elementos,None)
        self.contador = 0
    
    def obtener_elementos(self):
        return self.elementos
    def obtener_contador(self):
        return self.contador

class TablaHash:

    def __init__(self,cant_buckets,long_bucket,usar_primo=True):
        self.__long_bucket = long_bucket
        if usar_primo:
            self.__M = self.obtener_primo(cant_buckets) 
            #Multiplicado por 1.2 para considerar 20% area overflow
            self.__M_con_overflow = int(1.2 * self.__M)  
        else:
            self.__M = cant_buckets
            self.__M_con_overflow = int(1.2 * self.__M)

        
        self.__datos = []
        
        #Cargo buckets en la tabla
        for _ in range(self.__M_con_overflow):
            self.__datos.append(registro(long_bucket))

    #Política de manejo de colisiones: BUCKETS  
    def insertar(self,clave):
        pos_inicial = self.obtener_pos_inicial_por_extraccion(clave)
        pos_insercion = self.obtener_pos_insercion_por_uso_de_buckets(pos_inicial)

        if pos_insercion != -1:
            lugar = self.__datos[pos_insercion].contador
            self.__datos[pos_insercion].elementos[lugar] = clave
            self.__datos[pos_insercion].contador += 1
        return pos_insercion

    #Devuelve el arreglo de claves dada una posición
    def buscar_claves(self,pos):
        claves = None
        if pos >= 0 and pos  < self.__M:
            claves = self.__datos[pos].elementos
        return claves
    
    #Devuelve la posición dada una clave
    def buscar_posicion(self,clave):
        pos_inicial = self.obtener_pos_inicial_por_extraccion(clave)
        i = 0
        pos_buscada = -1

        #Verifico que la clave realmente esté en la posicion que se le asignaría en la tabla
        while i < self.__long_bucket and self.__datos[pos_inicial].elementos[i] != None:
            if self.__datos[pos_inicial].elementos[i] == clave:
                pos_buscada = pos_inicial
                i = self.__long_bucket
            else:
                i+=1
        #Si no la encontró, busco en el área de overflow
        if pos_buscada == -1:
            i = self.__M
            j = 0
            while i < self.__M_con_overflow and self.__datos[i].elementos[j] != None:
                if self.__datos[i].elementos[j] == clave:
                    pos_buscada = i
                    i = self.__M_con_overflow
                else:
                    j+=1
                    #Reseteo el j al llegar al tamaño del bucket y avanzo un lugar en la tabla
                    if j == self.__long_bucket:
                        j = 0
                        i += 1
                i+=1                    

        return pos_buscada
         
    #--------------------------------------#
    #   FUNCIONES DE TRANSFORMACIÓN h(k)   #
    #--------------------------------------#

    def obtener_pos_inicial_por_division(self,clave):
        return clave % self.__M

    #Generación de posición por método de extracción, retorna indice dentro del arreglo
    def obtener_pos_inicial_por_extraccion(self,clave):
        #Extraer de la clave, los ultimos dígitos (Varían más aleatoriamente)
        cant_digitos = len(str(self.__M)) #Cantidad de digitos a extraer = cant dígitos de M
        clave_string = str(clave)
        #Indexación negativa (para extraer los últimos digitos)
        pos = int(clave_string[-cant_digitos:])

        #En caso de que posición quede fuera del rango de 0 a M-1
        if pos >= self.__M:
            pos = self.obtener_pos_inicial_por_division(clave)
        return pos

    #--------------------------------------#
    #   POLÍTICA DE MANEJO DE COLISIONES   #
    #--------------------------------------#

    def obtener_pos_insercion_por_uso_de_buckets(self,pos_inicial):
        pos_insercion = -1 #En caso de que tambien este llena el área de overflow
        if self.__datos[pos_inicial].contador < self.__long_bucket:
            pos_insercion = pos_inicial
        else:
            #Si el bucket esta lleno, inserto en área de overflow
            for i in range(self.__M, self.__M_con_overflow):
                # print("Fila {0}: contador = {1}".format(i,self.__datos[i].contador))
                # if self.__datos[i].contador == 11:
                #     print(self.__datos[i].elementos[10])
                #input()
                if self.__datos[i].contador < self.__long_bucket:
                    pos_insercion = i
                    #input()
                    break
        return pos_insercion

    #Lee los datos de cada bucket y lo retorna en una lista
    def obtenerDatos(self):
        datos = []
        for i in range(self.__M):
            bucket = [self.__datos[i].elementos,self.__datos[i].contador]
            datos.append(bucket)
        return datos
    
    def obtener_datos_zona_overflow(self):
        datos = []
        for i in range(self.__M,self.__M_con_overflow):
            bucket = [self.__datos[i].elementos,self.__datos[i].contador]
            datos.append(bucket)
        return datos 

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

    def obtenerTam(self):
        return self.__M

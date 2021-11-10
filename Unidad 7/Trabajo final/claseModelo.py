from grafos.claseDigrafoEnlazado import DigrafoEnlazado
from grafos.claseDigrafoSecuencial import DigrafoSecuencial
from grafos.claseGrafoEnlazada import GrafoEnlazado
from grafos.claseGrafoSecuencial import GrafoSecuencial

class Relacion:
    def __init__(self,nodo_i,nodo_j,peso):
        self.i = nodo_i
        self.j = nodo_j
        self.peso = peso

class Modelo:
    
    def __init__(self):
        self.grafo = None
        self.cant_nodos = 0
        self.relaciones = None

    def crear_grafo(self,matriz,tipo,representacion):
        self.cant_nodos = len(matriz)
        self.relaciones = self.construir_relaciones(matriz)

        if tipo == "Grafo":
            if representacion == "Enlazada":
                self.grafo = GrafoEnlazado(self.cant_nodos)
            elif representacion == "Secuencial":

                self.grafo = GrafoSecuencial(self.cant_nodos)
        elif tipo == "Digrafo":
            if representacion == "Enlazada":
                self.grafo = DigrafoEnlazado(self.cant_nodos)
            elif representacion == "Secuencial":
                self.grafo = DigrafoSecuencial(self.cant_nodos)
        
        for i in range(self.cant_nodos):
            self.grafo.cargar_nodo(i)
        for rel in self.relaciones:
            self.grafo.relacionar_nodos(rel.i,rel.j,rel.peso)


    def construir_relaciones(self,matriz):
        relaciones = []
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                peso = matriz[i][j]
                nueva_relacion = Relacion(i,j,peso)
                relaciones.append(nueva_relacion)
        return relaciones
  
    def pedir_adyacentes(self,nodo):
        return self.grafo.adyacentes(nodo)
    
    def pedir_grado(self,nodo):
        return self.grafo.grado(nodo)
    
    def pedir_camino(self,nodo_origen,nodo_destino):
        return self.grafo.camino(nodo_origen,nodo_destino)
    def pedir_camino_min(self,nodo_origen,nodo_destino):
        return self.grafo.camino_minimo(nodo_origen,nodo_destino)
    
    def pedir_conexidad(self):
        return self.grafo.conexo()
    def pedir_aciclico(self):
        return self.grafo.aciclico()

    #--------------------------------------#
    #       MÉTODOS PARA EL COLOREADO      #
    #--------------------------------------#
    #USAR GRAFO NO PONDERADO REP SECUENCIAL
    #m: CANTIDAD DE COLORES, ES UN PARAMETRO DE ENTRADA!

    #El color 0 lo usa para un color vacio, no asignado

    # método para chequear que el color actual asignado sea seguro para el vértice v
    def es_adecuado(self, v, color, c):
        #A partir del nodo ingresado, controla todos los demas nodos para ver si hay relacion
        #Y para ver si el color de v es igual al de algun otro nodo i
        for i in range(self.cant_nodos):
            hay_relacion = self.grafo.obtener_relacion(v,i)
            if hay_relacion and color[i] == c:
                return False
        return True
    
    #Metodo recursivo para resolver el problema del coloreado de m vértices
    def pintado_recursivo(self, m, color, v):
        if v == self.cant_nodos:
            return True
 
        for c in range(1, m + 1):
            if self.es_adecuado(v, color, c) == True:
                color[v] = c
                if self.pintado_recursivo(m, color, v + 1) == True:
                    return True
                color[v] = 0
 
    def colorear_grafo(self, m):
        colores = [0] * self.cant_nodos
        if self.pintado_recursivo(m, colores, 0) == None:
            print("La solución no existe")
            return False

        #Resto 1 a todos los colores para usarlos como índices
        for i in range(self.cant_nodos):
            colores[i] -= 1
        # Retorno la lista con los colores para cada nodo, ordenados por su indice
        print("La solución existe")
        return colores
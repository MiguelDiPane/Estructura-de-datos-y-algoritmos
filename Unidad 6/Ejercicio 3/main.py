from claseGrafoSecuencial import GrafoSecuencial
import json

def leer_archivo_json():
    archivo = open("grafo_red_telefonica.json", "r")
    contenido = archivo.read()
    json_decodificado = json.loads(contenido)
    grafo = json_decodificado[0]
    nodos = grafo['nodos']
    relaciones = grafo['relaciones']
    return nodos,relaciones

def configurar_grafo(grafo,nodos,relaciones):
    for nodo in nodos:
        grafo.cargar_nodo(nodo-1)
    for relacion in relaciones:
        i = relacion[0] - 1
        j = relacion[1] - 1
        grafo.relacionar_nodos(i,j)
    return grafo

if __name__ == '__main__':

    #-------------------------------------------------#
    # Lectura del archivo JSON con el grafo original  #
    #-------------------------------------------------#

    #TAD: Grafo NO ponderado, representación secuencial

    nodos,relaciones = leer_archivo_json()
    grafo = GrafoSecuencial(len(nodos))
    grafo_configurado = configurar_grafo(grafo,nodos,relaciones)

    #-------------------------------------------#
    # Algoritmo para determinar nodos críticos  #
    #-------------------------------------------#
    
    # Nodo crítico: Al eliminarlo hace que algun nodo no sea alcanzable

    nodos_criticos = []
    nodo_origen = 1

    #Preparo los nodos a quitar, sin considerar el origen
    nodos_a_quitar = nodos[1:]
 
    #Quito las relaciones del grafo original que involucren al nodo a quitar
    for nodo_quitado in nodos_a_quitar:           
        nuevas_relaciones = []
        for relacion in relaciones:
            if nodo_quitado not in relacion:
                nuevas_relaciones.append(relacion)
        
        #Creo el grafo sin las relaciones al nodo que estoy quitando
        grafo = GrafoSecuencial(len(nodos))
        grafo_configurado = configurar_grafo(grafo,nodos,nuevas_relaciones)

        #Analisis de los caminos, si no hay es un nodo crítico
        for i in range(len(nodos)):
            if i != nodo_origen-1 and i != nodo_quitado-1:
                camino = grafo_configurado.camino(nodo_origen-1,i)
                if len(camino) == 1 and nodo_quitado not in nodos_criticos:
                    nodos_criticos.append(nodo_quitado)

    print("\nSitios críticos en la red telefónica: {}".format(nodos_criticos))

        




            
        
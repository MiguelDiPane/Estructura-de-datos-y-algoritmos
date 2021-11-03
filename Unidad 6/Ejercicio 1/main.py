from claseGrafoEnlazada import GrafoEnlazado
from claseGrafoSecuencial import GrafoSecuencial
from claseMenu import Menu
import json

def leer_archivo_json(ponderado):
    archivo = open("grafos.json", "r")
    contenido = archivo.read()
    json_decodificado = json.loads(contenido)
    if ponderado:
        grafo = json_decodificado[1]
    else:
        grafo = json_decodificado[0]
    nodos = grafo['nodos']
    relaciones = grafo['relaciones']
    return nodos,relaciones

def seleccionar_tipo_grafo():
    menu = Menu('TDA - Grafo - Lectura archivo JSON',False)
    menu.setOpciones(['Cargar grafo No ponderado','Cargar grafo ponderado'])
    op = menu.showMenu()
    while op != 0:
        if op == 1:
            nodos,relaciones = leer_archivo_json(False)
            es_ponderado = False
            op = 0          
        elif op == 2: 
            nodos,relaciones = leer_archivo_json(True)
            es_ponderado = True
            op = 0
        if op != 0:
            input("Presione una tecla para continuar...")
            op = menu.showMenu()
            
    return nodos,relaciones, es_ponderado
        
def configurar_grafo(grafo,nodos,relaciones,es_ponderado):
    for nodo in nodos:
        grafo.cargar_nodo(nodo)
    for relacion in relaciones:
        i = relacion[0]
        j = relacion[1]
        peso = 1
        if es_ponderado:
            peso = relacion[2]
        grafo.relacionar_nodos(i,j,peso)
    return grafo

def operaciones(grafo,es_ponderado):
    menu = Menu('TDA - Grafo NO Ponderado - Operaciones')
    if es_ponderado:
        menu.setTitulo('TDA - Grafo Ponderado - Operaciones')
    menu.setOpciones(['Mostrar Nodos',
                    'Mostrar relaciones',
                    'Mostrar adyacentes',
                    'Mostrar grado de un nodo',
                    'Camino entre dos nodos',
                    'Camino mínimo entre dos nodos',
                    'Determinar si es conexo',
                    'Determinar si es acíclico',
                    'Obtener árbol de recubrimiento'])

    op = menu.showMenu()

    while op != 0:
        if op == 1:
            grafo.mostrarNodos()
        elif op == 2:
            grafo.mostrar_relaciones()
        elif op == 3:
            nodo = int(input('Ingrese nodo: '))
            adyacentes = grafo.adyacentes(nodo)
            print('Nodos adyacentes a {0}: {1}'.format(nodo,adyacentes))
        elif op == 4:
            nodo = int(input('Ingrese nodo: '))
            grado = grafo.grado(nodo)
            print('El grado del nodo {0} es: {1}'.format(nodo,grado))
        elif op == 5:
            nodo_inicial = int(input('Ingrese nodo inicial: '))
            nodo_destino = int(input('Ingrese nodo destino: '))
            camino = grafo.camino(nodo_inicial,nodo_destino)
            print('El camino desde {0} a {1} es: {2}'.format(nodo_inicial,nodo_destino,camino))
        elif op == 6:
            nodo_inicial = int(input('Ingrese nodo inicial: '))
            nodo_destino = int(input('Ingrese nodo destino: '))
            camino = grafo.camino_minimo(nodo_inicial,nodo_destino)
            print('El camino mínimo desde {0} a {1} es: {2}'.format(nodo_inicial,nodo_destino,camino))
 
        elif op == 7:
            if grafo.conexo():
                print("El grafo es conexo")
            else:
                print('El grafo NO es conexo')

        elif op == 8:
            if grafo.aciclico():
                print("El grafo es acíclico")
            else:
                print('El grafo NO es acíclico')
        elif op == 9:
            nodo = int(input('Ingrese nodo origen: '))
            grafo.obtener_arbol_de_recubrimiento_minimo(nodo)

        input('\nPresione una tecla para continuar...')  
        op = menu.showMenu()

if __name__ == '__main__':

    menuPrincipal = Menu('TDA - Grafos - Seleccionar representación')
    menuPrincipal.setOpciones(['Representación secuencial','Representación enlazada'])
    op = menuPrincipal.showMenu()

    while op != 0:
        nodos,relaciones,es_ponderado = seleccionar_tipo_grafo()
        if op == 1:
            grafo = GrafoSecuencial(len(nodos),es_ponderado)
        elif op == 2:
            grafo = GrafoEnlazado(len(nodos),es_ponderado)

        grafo_configurado = configurar_grafo(grafo,nodos,relaciones,es_ponderado)
        operaciones(grafo_configurado,es_ponderado)
        op = menuPrincipal.showMenu()
            
        
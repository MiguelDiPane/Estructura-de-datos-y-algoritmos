from claseDigrafoEnlazado import DigrafoEnlazado
from claseDigrafoSecuencial import DigrafoSecuencial
from claseMenu import Menu
import json

def leer_archivo_json(ponderado):
    archivo = open("digrafos.json", "r")
    contenido = archivo.read()
    json_decodificado = json.loads(contenido)
    if ponderado:
        digrafo = json_decodificado[1]
    else:
        digrafo = json_decodificado[0]
    nodos = digrafo['nodos']
    relaciones = digrafo['relaciones']
    return nodos,relaciones

def seleccionar_tipo_digrafo():
    menu = Menu('TDA - Digrafo - Lectura archivo JSON',False)
    menu.setOpciones(['Cargar digrafo No ponderado','Cargar digrafo ponderado'])
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
        
def configurar_digrafo(digrafo,nodos,relaciones,es_ponderado):
    for nodo in nodos:
        digrafo.cargar_nodo(nodo)

    for relacion in relaciones:
        i = relacion[0]
        j = relacion[1]
        peso = 1
        if es_ponderado:
            peso = relacion[2]
        digrafo.relacionar_nodos(i,j,peso)
    return digrafo

def operaciones(digrafo,es_ponderado):
    menu = Menu('TDA - Digrafo NO Ponderado - Operaciones')
    if es_ponderado:
        menu.setTitulo('TDA - Digrafo Ponderado - Operaciones')
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
            digrafo.mostrarNodos()
        elif op == 2:
            digrafo.mostrar_relaciones()
        elif op == 3:
            nodo = int(input('Ingrese nodo: '))
            adyacentes = digrafo.adyacentes(nodo)
            print('Nodos adyacentes a {0}: {1}'.format(nodo,adyacentes))
        elif op == 4:
            nodo = int(input('Ingrese nodo: '))
            grado_salida, grado_entrada = digrafo.grado(nodo)
            print('El grado de salida nodo {0} es: {1}'.format(nodo,grado_salida))
            print('El grado de entrada nodo {0} es: {1}'.format(nodo,grado_entrada))
        elif op == 5:
            nodo_inicial = int(input('Ingrese nodo inicial: '))
            nodo_destino = int(input('Ingrese nodo destino: '))
            camino = digrafo.camino(nodo_inicial,nodo_destino)
            print('El camino desde {0} a {1} es: {2}'.format(nodo_inicial,nodo_destino,camino))
        elif op == 6:
            nodo_inicial = int(input('Ingrese nodo inicial: '))
            nodo_destino = int(input('Ingrese nodo destino: '))
            camino = digrafo.camino_minimo(nodo_inicial,nodo_destino)
            print('El camino mínimo desde {0} a {1} es: {2}'.format(nodo_inicial,nodo_destino,camino))
 
        elif op == 7:
            if digrafo.conexo():
                print("El grafo es conexo")
            else:
                print('El grafo NO es conexo')

        elif op == 8:
            if digrafo.aciclico():
                print("El grafo es acíclico")
            else:
                print('El grafo NO es acíclico')
        elif op == 9:
            nodo = int(input('Ingrese nodo origen: '))
            digrafo.obtener_arbol_de_recubrimiento_minimo(nodo)
        input('\nPresione una tecla para continuar...')  
        op = menu.showMenu()

if __name__ == '__main__':

    menuPrincipal = Menu('TDA - Digrafos - Seleccionar representación')
    menuPrincipal.setOpciones(['Representación secuencial','Representación enlazada'])
    op = menuPrincipal.showMenu()

    while op != 0:
        nodos,relaciones,es_ponderado = seleccionar_tipo_digrafo()
        if op == 1:
            digrafo = DigrafoSecuencial(len(nodos),es_ponderado)
        elif op == 2:
            digrafo = DigrafoEnlazado(len(nodos),es_ponderado)

        digrafo_configurado = configurar_digrafo(digrafo,nodos,relaciones,es_ponderado)
        operaciones(digrafo_configurado,es_ponderado)
        op = menuPrincipal.showMenu()
            
        
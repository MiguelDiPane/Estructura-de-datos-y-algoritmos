
from claseDigrafoSecuencial import DigrafoSecuencial
from claseMenu import Menu
import json
from rich import print

def leer_archivo_json():
    archivo = open("red_de_ciudades.json", "r")
    contenido = archivo.read()
    json_decodificado = json.loads(contenido)
    digrafo = json_decodificado[0]
    nodos = []
    ciudades = []
    for elemento in digrafo['nodos']:
        nodos.append(elemento[0])
        ciudades.append(elemento[1])
    relaciones = digrafo['relaciones']
    return nodos,relaciones,ciudades

def configurar_digrafo(digrafo,nodos,relaciones):
    for nodo in nodos:
        digrafo.cargar_nodo(nodo)

    for relacion in relaciones:
        i = relacion[0]
        j = relacion[1]
        digrafo.relacionar_nodos(i,j)
    return digrafo

if __name__ == '__main__':

    nodos,relaciones, ciudades = leer_archivo_json()
    digrafo = DigrafoSecuencial(len(nodos))
    digrafo_configurado = configurar_digrafo(digrafo,nodos,relaciones)
    
    menu = Menu('Rutas de vuelo')
    menu.setOpciones(['Viajar'])
    op = menu.showMenu()

    while op != 0:
        menuEmisor = Menu('Seleccione ciudad de origen')
        menuEmisor.setOpciones(ciudades)
        origen = menuEmisor.showMenu()

        if  origen  != 0:
            destinos = []
            ciudad_origen = ciudades[origen -1]
            for ciudad in ciudades:
                if ciudad != ciudad_origen:
                    destinos.append(ciudad)

            menuReceptor = Menu('Seleccione ciudad de destino')
            menuReceptor.setOpciones(destinos)
            destino = menuReceptor.showMenu() 
            ciudad_destino = destinos[destino-1]  

            if destino != 0:
                #Obtener indices para buscar el camino mínimo
                i = ciudades.index(ciudad_origen)
                j = ciudades.index(ciudad_destino)

                camino_minimo = digrafo.camino_minimo(i,j)
               
                print("\n[bold yellow]Ciudad origen:[/bold yellow] {}".format(ciudad_origen))
                print("[bold yellow]Ciudad destino:[/bold yellow] {}".format(ciudad_destino))
                
                print("\n[bold]Secuencia para menor cantidad de ciudades intermedias:[/bold]\n")
                
                for i in range(len(camino_minimo)):
                    indice_ciudad = camino_minimo[i]
                    print("{0}- {1}".format(i+1,ciudades[indice_ciudad]))
                
                input("\nPresione una tecla para continuar...")

        op = menu.showMenu()

    

            
        
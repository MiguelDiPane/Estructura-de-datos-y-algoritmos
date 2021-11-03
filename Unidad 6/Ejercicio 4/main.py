
from claseDigrafoSecuencial import DigrafoSecuencial
from claseMenu import Menu
import json
from rich import print

def leer_archivo_json():
    archivo = open("red_de_celulares.json", "r")
    contenido = archivo.read()
    json_decodificado = json.loads(contenido)
    digrafo = json_decodificado[0]
    nodos = []
    personas = []
    for elemento in digrafo['nodos']:
        nodos.append(elemento[0])
        personas.append(elemento[1])
    relaciones = digrafo['relaciones']
    return nodos,relaciones,personas

     
def configurar_digrafo(digrafo,nodos,relaciones):
    for nodo in nodos:
        digrafo.cargar_nodo(nodo)

    for relacion in relaciones:
        i = relacion[0]
        j = relacion[1]
        peso = relacion[2]
        digrafo.relacionar_nodos(i,j,peso)
    return digrafo


if __name__ == '__main__':

    nodos,relaciones, personas = leer_archivo_json()
    digrafo = DigrafoSecuencial(len(nodos),True)
    digrafo_configurado = configurar_digrafo(digrafo,nodos,relaciones)
    
    menu = Menu('Red de celulares')
    menu.setOpciones(['Enviar SMS'])
    op = menu.showMenu()

    while op != 0:
        menuEmisor = Menu('Seleccione emisor del SMS')
        menuEmisor.setOpciones(personas)
        emisor = menuEmisor.showMenu()

        if emisor != 0:
            receptores = []
            persona_emisor = personas[emisor-1]
            for persona in personas:
                if persona != persona_emisor:
                    receptores.append(persona)

            menuReceptor = Menu('Seleccione receptor del SMS')
            menuReceptor.setOpciones(receptores)
            receptor = menuReceptor.showMenu() 
            persona_receptor = receptores[receptor-1]  

            if receptor != 0:
                #Obtener indices para buscar el camino mínimo
                i = personas.index(persona_emisor)
                j = personas.index(persona_receptor)

                camino_minimo, Q = digrafo.camino_minimo(i,j)
               
                print("\n[bold yellow]Emisor:[/bold yellow] {}".format(persona_emisor))
                print("[bold yellow]Receptor[/bold yellow] {}".format(persona_receptor))
                
                print("\n[bold]Secuencia para el SMS más económico:[/bold]\n")
                
                for i in range(len(camino_minimo)):
                    indice_persona = camino_minimo[i]
                    if i == 0:
                        print("{}- {}".format(i+1,personas[indice_persona]))
                        costoAnterior = 0
                    else:
                        nuevoCosto = (Q[emisor-1][indice_persona] - costoAnterior)
                        costoAnterior += nuevoCosto
                        print("{}- {} +{}$".format(i+1,personas[indice_persona],nuevoCosto))
                
                print('\n[bold]Costo total: {}$ (centavos)[/bold]'.format(Q[emisor-1][camino_minimo[-1]]))
                input("\nPresione una tecla para continuar...")

        op = menu.showMenu()

    

            
        
from claseTablaHash import TablaHash
from random import randint, seed
from rich.table import Table
from rich import print, box
from claseMenu import Menu

#Muestra las políticas usadas en el ejercicio
def mostrar_consideraciones():
    tabla = Table(title="Consideraciones")
    tabla.add_column("Característica", style="green")
    tabla.add_column("Método elegido", style="cyan")
    
    tabla.add_row("Política manejo de colisiones","Encadenamientoo")
    tabla.add_row("Función de transformación de claves","Método de plegado")
    print(tabla)

#Genera e inserta las claves en la tabla hash
def cargar_tabla(tablaH):
    #incializo semilla para generar siempre los mismos numeros aleatorios y poder comparar
    seed(23)
    claves = []
    for i in range(cant_claves):
        #Evito valores repetidos
        nuevaClave = randint(5000,9999)
        while nuevaClave in claves:
            nuevaClave = randint(5000,9999)
        claves.append(nuevaClave)
        tablaH.insertar(nuevaClave)
    return tablaH

#Muestra la tabla generada
def mostrar_tabla(tablaH):
    clavesH = tablaH.obtenerDatos()

    tabla = Table(title="TDA Tabla Hash")
    tabla.add_column("N° Lista", style="green")
    tabla.add_column("Claves")
    tabla.add_column("Longitud")
    
    acum = 0
    cont = 0

    #Muestro longitud de las listas con claves sinónimas
    for i in range(len(clavesH)):
        #Solo muestro claves con listas asignadas
        if clavesH[i] != None:
            tabla.add_row("{}".format(i),"{}".format(clavesH[i].obtenerElementos()),"{}".format(clavesH[i].len()))
            acum += clavesH[i].len()
            cont += 1
        else:
            tabla.add_row("{}".format(i),"{}".format(clavesH[i]),"0",style="bold cyan")
    print(tabla)
    return acum,cont

def calcular_longitud_promedio(tablaH,acum,cont):
    clavesH = tablaH.obtenerDatos()

    longitud_promedio = acum // cont
    cant_listas = 0
    for i in range(len(clavesH)):
        if clavesH[i] != None:
            if clavesH[i].len() <= longitud_promedio + 3 and clavesH[i].len() >= longitud_promedio - 3:
                cant_listas += 1
    
    tabla = Table(show_header=False)
    tabla.box = box.ROUNDED
    tabla.add_row("Cantidad de listas con datos: {}".format(cont))
    tabla.add_row("Longitud de listas promedio: {}".format(longitud_promedio))
    tabla.add_row("Cantidad de listas que registran longitud +/-3")
    tabla.add_row("respecto de la longitud promedio: [bold cyan]{}[cyan]".format(cant_listas))
    print(tabla)

if __name__ == '__main__':
    cant_claves = 1000
    
    menu = Menu('TDA - Tabla Hash')
    menu.setOpciones(['Tamaño de la tabla Hash NO es un número primo (1000 claves)',
                    'Tamaño de la tabla Hash es primo (Usa factor de carga 0.7 y calcula el primo en exceso)'])
    
    mostrar_consideraciones()
    op = menu.showMenu(False)
    
    while op != 0:
        if op == 1:
            tablaH = TablaHash(cant_claves,False)
        elif op == 2:
            tablaH = TablaHash(cant_claves)
        
        tablaH_cargada = cargar_tabla(tablaH)
        acum,cont = mostrar_tabla(tablaH_cargada)
        calcular_longitud_promedio(tablaH_cargada,acum,cont)
        
        input("Presione una tecla para continuar...")
        menu.limpiar_pantalla()
        mostrar_consideraciones()
        op = menu.showMenu(False)
    

    


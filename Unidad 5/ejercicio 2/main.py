from claseTablaHash import TablaHash
from random import randint, seed
from rich.table import Table
from rich import print
from claseMenu import Menu

#Muestra las políticas usadas en el ejercicio
def mostrar_consideraciones():
    tabla = Table(title="Consideraciones")
    tabla.add_column("Característica", style="green")
    tabla.add_column("Método elegido", style="cyan")
    
    tabla.add_row("Política manejo de colisiones","Direccionamiento abierto")
    tabla.add_row("Función de transformación de claves","Método de la división")
    tabla.add_row("Procesamiento de claves sinónimas","Secuencia de prueba Pseudo Random")
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
    M = tablaH.obtener_M()
    tabla = Table(title="TDA Tabla Hash")
    tabla.add_column("MOD {}".format(M), style="green")
    tabla.add_column("Claves")
    
    for i in range(len(clavesH)):
        if clavesH[i] != None:
            tabla.add_row("{}".format(i),"{}".format(clavesH[i]))
        else:
            tabla.add_row("{}".format(i),"{}".format(clavesH[i]),style="bold cyan")
    print(tabla)

#Musca una clave y muestra la longitud de la secuencia de prueba
def buscar_claves(tablaH):
    valor = 's'
    while valor.lower() != 'q':
        try:
            valor = input("Ingrese clave para buscar su posición (Salir con Q): ")
            if valor.lower() != 'q':
                pos = tablaH.buscar_posicion(int(valor))
                if pos != -1:
                    print("Posición: {}".format(pos))
                else:
                    print("Clave no encontrada.")
        except ValueError:
            print('Error: Debe ingresar un entero')

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
        mostrar_tabla(tablaH_cargada)
        buscar_claves(tablaH_cargada)

        menu.limpiar_pantalla()
        mostrar_consideraciones()
        op = menu.showMenu(False)
    
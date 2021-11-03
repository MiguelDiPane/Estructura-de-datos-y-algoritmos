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
    
    tabla.add_row("Política manejo de colisiones","Uso de buckets")
    tabla.add_row("Función de transformación de claves","Método de extracción")
    print(tabla)

#Genera e inserta las claves en la tabla hash
def cargar_tabla(tablaH):
    #incializo semilla para generar siempre los mismos numeros aleatorios y poder comparar
    seed(23)
    claves = []
    for i in range(n):
        #Evito valores repetidos
        nuevaClave = randint(5000,9999)
        while nuevaClave in claves:
            nuevaClave = randint(5000,9999)
        claves.append(nuevaClave)
        tablaH.insertar(nuevaClave)
    return tablaH

#Muestra la tabla generada
def mostrar_tabla(tablaH):
    buckets = tablaH.obtenerDatos()
    buckets_overflow = tablaH.obtener_datos_zona_overflow()
    cant_buckets_desbordados = 0 #todas sus componentes ocupadas
    cant_buckets_subocupados = 0 #menos de la tercera parte ocupada

    tabla = Table(title="TDA Tabla Hash - Uso de buckets")
    tabla.add_column("Extracción", style="green")
    tabla.add_column("Claves")
    tabla.add_column("Contador")
    
    #Muestro los buckets y los contadores
    for i in range(len(buckets)):
        tabla.add_row("{}".format(i),
                    "{}".format(buckets[i][0]),
                    "{}".format(buckets[i][1]),style="bold cyan")
        if buckets[i][1] == long_bucket:
            cant_buckets_desbordados += 1
        elif buckets[i][1] < (long_bucket / 3):
            cant_buckets_subocupados += 1
    
    #Muestro la zona de overflow (No contribuye al cálculo de buckets desbordados y subocupados)
    tabla_overflow = Table(title="TDA Tabla Hash - Zona de Overflow")
    tabla_overflow.add_column("Extracción", style="green")
    tabla_overflow.add_column("Claves")
    tabla_overflow.add_column("Contador")
    for i in range(len(buckets_overflow)):
        tabla_overflow.add_row("{}".format(i+len(buckets)),
                    "{}".format(buckets_overflow[i][0]),
                    "{}".format(buckets_overflow[i][1]),style="bold red")

    print(tabla)
    print(tabla_overflow)
    return cant_buckets_desbordados,cant_buckets_subocupados

#Muestra los buckets desbordados y subocupados
def mostrar_resultados(cant_buckets_desbordados,cant_buckets_subocupados):
    tabla = Table(show_header=False)
    tabla.box = box.ROUNDED
    tabla.add_row("Cantidad de Buckets desbordados (todas las componentes ocupadas): [bold cyan]{}[cyan]".format(cant_buckets_desbordados))
    tabla.add_row("Cantidad de Buckets subocupados (menos de la tercera parte ocupada): [bold cyan]{}[cyan]".format(cant_buckets_subocupados))
    print(tabla)

if __name__ == '__main__':
    n = 1000 #Cantidad de claves
    long_bucket = 11
    cant_buckets = n // long_bucket

    menu = Menu('TDA - Tabla Hash')
    menu.setOpciones(['Número de buckets NO primo (90)',
                    'Número de buckets primo (97)'])
    
    mostrar_consideraciones()
    op = menu.showMenu(False)
    
    while op != 0:
        if op == 1:
            tablaH = TablaHash(cant_buckets,long_bucket,False)
        elif op == 2:
            tablaH = TablaHash(cant_buckets,long_bucket)
        
        tablaH_cargada = cargar_tabla(tablaH)
        cant_b_desb,cant_b_sub = mostrar_tabla(tablaH_cargada)
        mostrar_resultados(cant_b_desb,cant_b_sub)
        
        input("Presione una tecla para continuar...")
        menu.limpiar_pantalla()
        mostrar_consideraciones()
        op = menu.showMenu(False)

    
 


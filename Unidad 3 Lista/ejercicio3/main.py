import csv
from manejadorProvincias import ManejadorProvincias

if __name__ == '__main__':
    manejador = ManejadorProvincias()

    #Cargo incendios en la lista
    archivo = open('superficie-afectada-por-incendios-forestales-en-el-pais.csv',encoding="UTF-8")
    reader = csv.reader(archivo,delimiter=';')
    bandera = False
    for fila in reader:
        if not bandera:
            bandera = True
        else:
            if not (fila[6] == ""):
                manejador.agregar(fila[3],float(fila[6]))
    archivo.close() 

    #Mostrar lista generada sin ordenar
    mostrar = input("\nMostrar lista generada: [S/N]: ")
    if mostrar.lower() == "s":
        manejador.mostrarLista()
    
    #Ordeno la lista por superficie de mayor a menor
    manejador.ordenarPorSup()
    mostrar = input("\nMostrar lista ordenada por superficie afectada: [S/N]: ")
    if mostrar.lower() == "s":
        manejador.mostrarLista()   
    

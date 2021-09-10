from clasePilaEncadenada import PilaEncadenada

if __name__ == "__main__":
    viaje = PilaEncadenada()
    pilaAux = PilaEncadenada() #para viaje de ida

    #Carga de los pueblos en la pila "viaje"
    llego = 'n'
    while llego.lower() != 's':
        pueblo = input("Ingrese nombre pueblo: ")
        viaje.insertar(pueblo)
        llego = input("¿Llegó a destino? [S/N]: ")
   
    #Muestro recorrido de vuelta
    print("\nRecorrido de vuelta")
    print("Parte de: ",end="")
    while not viaje.vacia():
        x = viaje.suprimir()
        #Almaceno en aux para invertir las posiciones
        pilaAux.insertar(x) 
        print("{} -> ".format(x),end="")
    print("llegó a pueblo de origen")
    
    #Muestro recorrido de ida
    print("\nRecorrido de ida")
    print("Parte de: ",end="")
    while not pilaAux.vacia():
        x = pilaAux.suprimir()
        print("{} -> ".format(x),end="")
    print("llegó a pueblo de destino\n")
from clasePilaEncadenada import PilaEncadenada

if __name__ == "__main__":
    destino = False
    viaje = PilaEncadenada()
    pilaAux = PilaEncadenada() #para viaje de ida

    #Carga de los pueblos en la pila "viaje"
    while not destino:
        pueblo = input("Ingrese nombre pueblo: ")
        viaje.insertar(pueblo)
        llego = input("Llego a destino? [S/N]: ")
        if llego.upper() == 'S':
            destino = True
    
    #Muestro recorrido de vuelta
    print("\nRecorrido de vuelta")
    print("Parte de: ",end="")
    while not viaje.vacia():
        x = viaje.suprimir()
        #Almaceno en aux para invertir las posiciones
        pilaAux.insertar(x) 
        print("{} -> ".format(x),end="")
    print("llego a pueblo de origen")
    
    #Muestro recorrido de ida
    print("\nRecorrido de ida")
    print("Parte de: ",end="")
    while not pilaAux.vacia():
        x = pilaAux.suprimir()
        print("{} -> ".format(x),end="")
    print("llego a pueblo de destino\n")
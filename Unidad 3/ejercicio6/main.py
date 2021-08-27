from claseColas import ColaEncadenada,ColaSecuencial


if __name__ == "__main__":
    colaSec = ColaSecuencial(10)
    #Inserto elementos
    for i in range(11):
        colaSec.insertar(i)
    
    #Primero en llegar, primero en salir
    print("Cola secuencial")
    while not colaSec.vacia():
        valor = colaSec.suprimir()
        print(valor, end=" ")
    print("")

    colaEnc = ColaEncadenada()
    #Inserto elementos
    for i in range(11):
        colaEnc.insertar(i)
    
    #Primero en llegar, primero en salir
    print("Cola encadenada")
    while not colaEnc.vacia():
        valor = colaEnc.suprimir()
        print(valor, end=" ")
    print("")
        
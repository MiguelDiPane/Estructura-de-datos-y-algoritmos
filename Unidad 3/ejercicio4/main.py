from ClasePilaSecuencial import PilaSecuencial

if __name__ == "__main__":
    pilas = PilaSecuencial(20)
    
    for i in range(10):
        pilas.insertarInf(i)
        pilas.insertarSup(20-i)
    
    #No insertará porque ya estan llenas
    print("Inserto en pila inferior")
    pilas.insertarInf(20)
    print("Inserto en pila superior")
    pilas.insertarSup(30)
    
    #Muestro las pilas siguiendo la politica LIFO
    print("Pila Inferior")
    for i in range(10):
        x = pilas.suprimirInf()
        print(" {} ".format(str(x)),end="")

    print("\nPila Superior")
    for i in range(10):
        x = pilas.suprimirSup()
        print(" {} ".format(str(x)),end="")

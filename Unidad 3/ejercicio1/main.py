from ClasePilas import PilaEncadenada, PilaSecuencial

if __name__ == "__main__":
    n = 6
    print('Pila secuencial')
    pila = PilaSecuencial(n-1)
    for i in range(n):
        pila.insertar(i+1)

    #Metodo para mostrar en forma estricta siguiendo la logica de la pila
    while not pila.vacia():
        x = pila.suprimir()
        print(x)

    print('Pila Encadenada')
    pila = PilaEncadenada()
    for i in range(n):
        pila.insertar(i+1)
   
    #Metodo para mostrar en forma estricta siguiendo la logica de la pila
    while not pila.vacia():
        x = pila.suprimir()
        print(x)
       
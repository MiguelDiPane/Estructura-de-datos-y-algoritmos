from claseListaCursores import ListaCursores

if __name__ == '__main__':
    listaCursor = ListaCursores(10)
    for i in range(8):
        listaCursor.insertarPos(i*20,i)

    #Inserta en posicion no valida
    listaCursor.insertarCont(78)
    print("LISTA ENCADENADA CON CURSORES")
    listaCursor.recorrer()

    print("Test función siguiente() al elemento en posicion 1:")
    print(listaCursor.siguiente(1))
    
    print("Test función anterior() al elemento en posicion 2:")
    print(listaCursor.anterior(2))
    
    print("Test función buscar(), posicion valor 50: ")
    print(listaCursor.buscar(50))
    
    print("Test función primer_elemento()")
    print(listaCursor.primer_elemento())
    
    print("Test función ultimo_elemento()")
    print(listaCursor.ultimo_elemento())
    
    print("Test función recuperar(), elemento en posición 2")
    print(listaCursor.recuperar(2))

    print("Test función suprimir(), elemento en posicion 4 y 0")
    print(listaCursor.suprimir(4))
    input()
    listaCursor.recorrer()
    print(listaCursor.suprimir(0))
    input()
    listaCursor.recorrer()
    
    #Al eliminar se crea un espacio vacio que sera ocupado al insertar
    print("Inserto en la posicion 0 (cabeza)")
    listaCursor.insertarPos(999,0)
    listaCursor.insertarPos(999,0)
    listaCursor.recorrer()
    listaCursor.insertarPos(459,5)
    listaCursor.recorrer()
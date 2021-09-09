from claseListaSecuencial import ListaSecuencial
from claseListaSecuencialCont import ListaSecuencialCont
from claseListaEncadenada import ListaEncadenada
from claseListaEncadenadaCont import ListaEncadenadaCont

if __name__ == '__main__':
    print("\nLISTA SECUENCIAL POR POSICION")
    listaSec = ListaSecuencial(10)
    #Cargo la lista
    for i in range(5):
        listaSec.insertar(i*10,i)

    listaSec.insertar(234,5)
    listaSec.insertar(255,6)
    listaSec.insertar(85,2)
    listaSec.recorrer()
    
    listaSec.suprimir(4)
    listaSec.recorrer()
    print(listaSec.ultimo_elemento())

    print("\n\nLISTA SECUENCIAL POR CONTENIDO")
    listaCont = ListaSecuencialCont(5)
    for i in range(4):
        listaCont.insertar(i*8)
    listaCont.insertar(4)
    listaCont.recorrer()
    #Suprime por posicion
    listaCont.suprimir(3)
    listaCont.recorrer()
    #Suprime por contenido
    listaCont.suprimirCont(8)
    listaCont.recorrer()

    print("\nLISTA ENCADENADA POR POSICION")
    listaEncPos = ListaEncadenada()
    #Cargo la lista
    for i in range(5):
        listaEncPos.insertar(i*15,i)
    
    listaEncPos.insertar(23,5)
    listaEncPos.recorrer()

    listaEncPos.suprimir(1)
    listaEncPos.recorrer()
    listaEncPos.suprimir(1)
    listaEncPos.recorrer()
    print(listaEncPos.anterior(1))
    print(listaEncPos.siguiente(2))
    print(listaEncPos.ultimo_elemento())
    print(listaEncPos.primer_elemento())
    print(listaEncPos.buscar(23))
    print(listaEncPos.recuperar(2))

    print("\nLISTA ENCADENADA POR CONTENIDO")
    listaEncCont = ListaEncadenadaCont()
    #Cargo la lista
    for i in range(5):
        listaEncCont.insertar(i*15)
    listaEncCont.recorrer()
    listaEncCont.insertar(7)
    listaEncCont.recorrer()

    listaEncCont.suprimir(1)
    listaEncCont.recorrer()
    listaEncCont.suprimirCont(45)
    listaEncCont.recorrer()
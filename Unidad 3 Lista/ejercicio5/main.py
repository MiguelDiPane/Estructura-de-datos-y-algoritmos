from claseListaSecuencial import ListaSecuencial
from claseListaSecuencialCont import ListaSecuencialCont


if __name__ == '__main__':
    n = int(input('Ingrese cantidad de elementos: '))

    lista = ListaSecuencial(n)
    listaCont = ListaSecuencialCont(n)
    
    #Cargo las listas
    for i in range(n):
        valor = int(input('Ingrese valor {}: '.format(i+1)))
        lista.insertar(valor,i)
        listaCont.insertar(valor)

    #-------------------------------------------#
    # ALGORITMO - LISTA SECUENCIAL POR POSICIÓN #
    #-------------------------------------------#
    print("\nLista secuencial por posicion")
    lista.recorrer()
    i = 0
    #Orden cuadratico 
    while i < lista.len():
        valor1 = lista.recuperar(i)
        j = i+1
        while j < lista.len():
            valor2 = lista.recuperar(j)
            #Al suprimir no aumento j ya que los elementos se movieron un lugar hacia atras
            if valor1 == valor2:
                lista.suprimir(j)
            #Solo avanza si no elimino
            else:
                j += 1
        i+=1
    lista.recorrer()

    #--------------------------------------------#
    # ALGORITMO - LISTA SECUENCIAL POR CONTENIDO #
    #--------------------------------------------#
    print("\nLista secuencial por contenido")
    listaCont.recorrer()
    i = 0
    #Orden lineal
    while i < lista.len():
        valor1 = listaCont.recuperar(i)
        valor2 = listaCont.recuperar(i+1)
        if valor1 == valor2:
            listaCont.suprimir(i+1)
        else:
            i+=1
    
    listaCont.recorrer()
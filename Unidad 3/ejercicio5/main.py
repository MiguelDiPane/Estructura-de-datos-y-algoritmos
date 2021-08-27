from ClaseTorres import Torres
import os

def printHeader():
    header = '+' + '-'*60 + '+'
    print(header)
    print('|{0:^60}|'.format("Torres de Hanoi"))
    print(header)
    return header   

if __name__ == "__main__":
    os.system('cls')
    n = int(input("Ingrese cantidad de discos: "))
    os.system('cls')
    torres = Torres(n)
    origen = "n"
    cont = 0 #Contador de movimientos
    while origen.lower() != "s":
        separador = printHeader()
        torres.mostrarTablero()
        fin = torres.finJuego()
        if not fin:
            print(separador)
            origen = input("| Torre origen (Salir con S): ")
            if origen.lower() != "s":
                destino = input("| Torre destino: ")
                cont += torres.moverDisco(origen,destino)
                os.system('cls')
        else:
            origen = "s"
    
    print(separador)
    print("|{0:^60}|".format("JUEGO TERMINADO"))
    print(separador)
    print("| Movimientos óptimos: {0:38}|".format(2**n-1))
    print("| Movimientos realizados: {0:35}|".format(cont))
    print(separador)
    input("\nPresione una tecla para finalizar...")


    


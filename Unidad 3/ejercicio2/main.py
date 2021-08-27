from clasePilaEncadenada import PilaEncadenada

def dec2bin(num):
    cociente = None
    while cociente != 0:
        cociente = int(num / 2)
        resto = num % 2
        num = cociente
        binario1.insertar(resto)

if __name__ == "__main__":
    binario1 = PilaEncadenada()
    num = int(input("Ingrese numero: "))
    dec2bin(num)
    
    while not binario1.vacia():
        x = binario1.suprimir()
        print(x,end=" ")

    


from clasePilaEncadenada import PilaEncadenada

#Calculo con la pila encadenada
def factorial(num):
    while num > 0:
        pila.insertar(num)
        num -= 1

#Calculo recursivo
def factorialRec(num,fac):
    if num == 0:
        return fac
    else:
        fac = fac * num 
        return factorialRec(num-1,fac)

#Calculo iterativo
def factorialIter(num):
    fac = 1
    while num > 0:
        fac = fac * num
        num -= 1
    return fac

if __name__ == "__main__":
    num = int(input("Ingrese numero: "))
    pila = PilaEncadenada()
    
    #Calculo recursivo
    fac = factorialRec(num,1)
    print(fac)
    #Calculo iterativo
    fac = factorialIter(num)
    print(fac)
    #Calculo con pila encadenada
    factorial(num)
    fac = 1
    while not pila.vacia():
        x = pila.suprimir()
        fac = fac * x
    print(fac)
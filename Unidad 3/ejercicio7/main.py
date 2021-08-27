from claseCajero import Cajero
from claseColaEncadenada import ColaEncadenada #porque no se la cant de clientes
from claseCliente import Cliente
from claseCajero import Cajero
from random import randint

def header():
    header = '+' + '-'*83 + '+'
    print(header)
    print('|{0:^83}|'.format("Caja de atención al cliente"))
    print(header)
    print('|{0:^10}|{1:^20}|{2:^30}|{3:^20}|'.format("Min","Cliente","Cajero","Espera [Min]"))
    print(header)
    return header
   
def showEstado(i,mensaje,mensajeCajero,mensajeEspera):
    print("|{0:^10}|{1:^20}|{2:^30}|{3:^20}|".format(i,mensaje,mensajeCajero,mensajeEspera))

if __name__ == '__main__':
    tSimulacion = 50 #Minutos
    tCajero = int(input("Tiempo de atencion cajero: "))
    tCliente = int(input("Frecuencia llegada clientes: "))
    cola = ColaEncadenada()
    cajero = Cajero(tCajero)
    pCliente = 1 /tCliente
    tEsperaMax = 0
    numCliente = 1
    i = 1
    separador = header()
    while i <= tSimulacion:
        #Analizo llegada de cliente
        aleatorio = 1 /randint(1,tCliente)
        if pCliente == aleatorio:
            newCliente = Cliente(i)
            newCliente.setNumero(numCliente)
            cola.insertar(newCliente)
            mensaje = "Llegó cliente {}".format(str(numCliente))
            numCliente += 1
        else:
            mensaje = "No"
        
        #Atencion del cajero
        if cajero.libre():
            if not cola.vacia():
                clienteAtendido = cola.suprimir()
                tEspera = clienteAtendido.getTiempoEspera(i)
                #Actualizo maximo
                if tEspera > tEsperaMax:
                    tEsperaMax = tEspera
                cajero.setOcupado()
                mensajeCajero = "Libre, atiende cliente. "
                mensajeEspera = "Cliente N° {}: {}".format(str(clienteAtendido.getNumero()),str(tEspera))
            else:
                mensajeCajero = "Libre"
                mensajeEspera = "Sin clientes"                 
        
        #Actualizo el reloj
        showEstado(i,mensaje,mensajeCajero,mensajeEspera)
        i += 1
        if not cajero.libre():
            mensajeCajero = "Ocupado"
            mensajeEspera = ""
            cajero.actualizar()
    
    print(separador)         
    print("|{0:^83}|".format("Tiempo de espera máximo:"+ str(tEsperaMax)))
    print(separador)
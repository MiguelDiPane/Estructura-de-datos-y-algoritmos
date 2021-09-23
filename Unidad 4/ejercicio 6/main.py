from claseQuirofano import Quirofano
from clasePaciente import Paciente
from claseMonticuloBinario import MonticuloBinario
import csv
from random import randint
from rich import print


if __name__ == '__main__':
    pass


    #Podria calcular el tiempo de la operacion con un aleatorio
    #Para tener el tiempo en que se desocupa

    #Cargo nombres para generar pacientes aleatorios
    nombres = []
    archivo = open('listaPacientes.csv',encoding='UTF-8')
    reader = csv.reader(archivo,delimiter=';')
    bandera = False
    for fila in reader:
        if not bandera:
            bandera = True
        else:
            nombres.append(fila[0])     
    archivo.close() 

    #--------------#
    #  SIMULACIÓN  #
    #--------------#
    #Considero que llegan pacientes cada 30 min
    tPaciente = 30
    pPaciente = 1 / tPaciente

    tSim = 60 * 10 #10hs de simulación
    i = 0

    quirofano = Quirofano()
    monticulo = MonticuloBinario()

    while i < tSim:
        #Analizo llegada de un paciente
        if pPaciente == 1/randint(1,tPaciente):
            nombre = nombres[randint(0,len(nombres)-1)]

            #Considero prioridad de 1 (max prioridad) a 100 (min prioridad)
            prioridad = randint(1,100) 
            newPaciente = Paciente(nombre,prioridad)
            monticulo.insertar(newPaciente)
            #Muestro el montículo al insertar paciente
            print('\n[bold magenta]Min: {0}[/bold magenta][bold green] - Se inserta paciente[/bold green]'.format(i))
            if not quirofano.libre():
                print('\n[bold red]Quirófano ocupado[/bold red]')
            print('\n[bold red]Montículo binario[/bold red]')
            monticulo.mostrar()
        
        #Atencion del quirofano
        if quirofano.libre():
            if not monticulo.vacio():
                pacAtendido = monticulo.eliminar_minimo()
                nombre = pacAtendido.getNombre()               
                quirofano.setOcupado()
                #Tiempo de atencion aleatorio entre 1 y 2hs
                duracion = randint(60,120)
                quirofano.setTAtencion(duracion)
                #Muestro el montículo al sacar paciente
                print('\n[bold magenta]Min: {0}[/bold magenta]'.format(i)) 
                print('[bold blue]Paciente atendido:[/bold blue][bold yellow] {0}[/bold yellow]'.format(nombre))
                print('[bold blue]Duración operación:[/bold blue] [bold cyan]{0} min[/bold cyan]'.format(duracion))
                print('\n[bold red]Montículo binario[/bold red]')
                monticulo.mostrar()
            
        #Actualizo reloj
        i+=1
        #Actualizo quirofano
        if not quirofano.libre():
            quirofano.actualizar()


    
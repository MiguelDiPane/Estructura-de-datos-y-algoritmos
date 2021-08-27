from claseColaEncadenada import ColaEncadenada
from clasePaciente import Paciente
from claseMesaEntrada import MesaEntrada
from claseConsultorio import Consultorio
import random
import csv

def header(titulo,columnas=1):
    header = '+' + '-'*126 + '+'
    print("\n" + header)
    print('|{0:^126}|'.format(titulo))
    print(header)
    if columnas == 1:
        print('| {0:<5}| {1:<20}| {2:<11}| {3:<16}| {4:<65}|'.format("Min","Nombre","DNI","Especialidad","Mesa de entrada"))
        print(header)
        
    elif columnas == 2:
        print('| {0:<5}| {1:<16}| {2:<63}| {3:<35}|'.format("Min","Especialidad","Estado consultorio","Cupo de atención"))
        print(header)
    return header

def showEstado(i,nom,dni,esp,mesaEnt):
    print('| {0:<5}| {1:<20}| {2:<11}| {3:<16}| {4:<65}|'.format(i,nom,dni,esp,mesaEnt))

def showEstadoConsultorio(i,cons,estado,estadoAtendidos):
    print('| {0:<5}| {1:<16}| {2:<63}| {3:<35}|'.format(i,cons,estado,estadoAtendidos))


if __name__ == "__main__":
    #Inicializacion para numeros aleatorios
    random.seed(random.randint(1,999))
    
    #Tiempos
    tSimulacion = 4*60 #Cuatro horas de simulacion total
    tLlegada = 1
    pLlegada = 1/tLlegada 
    tMesaEntrada = 2
    mesaEntrada = MesaEntrada(tMesaEntrada)
    
    #Especialidades disponibles
    especialidades = ["Ginecología","Clínica Médica","Oftalmología","Pediatría"]
    tMedico = 20
    #Creo un consultorio por cada especialidad
    consultorios = []
    for i in range(len(especialidades)):
        consultorios.append(Consultorio(tMedico,especialidades[i]))

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

    #Acumuladores y contadores para tiempos promedio
    tEsperaTurnos = 0
    conTurno = 0
    contPac = 0
    #Un contador y acumulador para cada especialidad
    tEsperaEsp = []
    contPacAtendido = []
    for i in range(len(especialidades)):
        tEsperaEsp.append(0)
        contPacAtendido.append(0)

    
    #Creo las colas
    pacientes = ColaEncadenada()
    #Una cola para cada consultorio
    colasPacientesConTurno = []
    for i in range(len(especialidades)):
        colasPacientesConTurno.append(ColaEncadenada())

    #Para almacenar los valores durante la simulación y luego hace un print con los resultados
    estadoTurnos = []
    estadoConsultorios = []

    #--------------#
    #  SIMULACIÓN  #
    #--------------#
    i = 1
    while i < tSimulacion:
        #Se entregan turnos solo en la primer hora
        if i < 60:    
            #Analizo llegada de paciente
            aleatorio = 1 /random.randint(1,tLlegada)
            if pLlegada == aleatorio:
                #Genero paciente con datos aleatorios
                pos = random.randint(0,len(nombres)-1)
                nombre = nombres[pos]
                pos = random.randint(0,len(especialidades)-1)
                dni = random.randint(7000000,44000000)
                newPaciente = Paciente(nombre,dni,especialidades[pos],pos,i)
                pacientes.insertar(newPaciente)
                contPac += 1
            else:
                menPaciente = "No llegó paciente"        
            
            #Atencion de la mesa de entradas y asignacion de la cola de espera segun num de consultorio
            if mesaEntrada.libre():
                if not pacientes.vacia():
                    pacienteConTurno = pacientes.suprimir()
                    num = pacienteConTurno.getNumConsultorio()
                    pacienteConTurno.setTiempoObtieneTurno(i)
                    #Inserta paciente en cola correspondiente al consultorio de su especialidad
                    colasPacientesConTurno[num].insertar(pacienteConTurno)
                    espera = pacienteConTurno.getTiempoEspera(i)
                    tEsperaTurnos += espera
                    conTurno += 1
                    mesaEntrada.setOcupado()
                    nombre = pacienteConTurno.getNombre()
                    msjMesa = "Libre - Da turno a {} (esperó durante {} min)".format(nombre,espera)
                else:
                    msjMesa = "Libre - Sin pacientes"  
            else:
                msjMesa = "Mesa ocupada"     

            #Guardo el estado de la simulacion en cada instante para la mesa de entrada
            estadoTurnos.append([i,newPaciente.getNombre(),newPaciente.getDni(),newPaciente.getEsp(),msjMesa])

        #Atencion de pacientes en su respectivo consultorio
        for j in range(len(colasPacientesConTurno)):
            if consultorios[j].libre():
                if not colasPacientesConTurno[j].vacia() and consultorios[j].getAtendidos() < 10:
                    pacienteAtender = colasPacientesConTurno[j].suprimir()
                    espera = pacienteAtender.getTiempoEsperaCons(i)
                    tEsperaEsp[j] += espera
                    contPacAtendido[j] +=1
                    nombre = pacienteAtender.getNombre()
                    consultorios[j].setOcupado()
                    consultorios[j].addAtendido()
                    estado = "Libre, atiende a {} (esperó durante {} min)".format(nombre,espera)   
                else:
                    estado = "Libre - Sin pacientes"             
            else:
                estado = "Ocupado"
            if consultorios[j].getAtendidos() < 10:                   
                estadoAtendidos = "Aun puede atender {} pacientes".format(10-consultorios[j].getAtendidos())
            else:
                estadoAtendidos = "No puede atender más (max=10)"   
            
            #Guardo el estado de la simulación en cada instante para los consultorios
            estadoConsultorios.append([i,consultorios[j].getEspecialidad(),estado,estadoAtendidos])
             
        #Actualizo el reloj
        i+=1
        if not mesaEntrada.libre():
            mesaEntrada.actualizar() 
        for consultorio in consultorios: 
            if not consultorio.libre():               
                consultorio.actualizar()       


    #----------------------------------------------#
    #  SIMULACIÓN FINALIZADA - IMPRIMO RESULTADOS  #
    #----------------------------------------------#
    print("Simulación Finalizada")
    ver = input("¿Desea ver la planilla de turnos? [S/N]: ")
    if ver.lower() == "s":
        encabezado = header("Entrega de turnos",1)
        for i in range(len(estadoTurnos)):
            showEstado(estadoTurnos[i][0],estadoTurnos[i][1],estadoTurnos[i][2],estadoTurnos[i][3],estadoTurnos[i][4])
        print(encabezado)
    
    ver = input("¿Desea ver la planilla consultorios? [S/N]: ")
    if ver.lower() == "s":
        header("Atención consultorios",2)
        for i in range(len(estadoConsultorios)):
            if i%4 == 0 and i != 0: #Para separar en grupos de a cuatro 
                print(encabezado)
            showEstadoConsultorio(estadoConsultorios[i][0],estadoConsultorios[i][1],estadoConsultorios[i][2],estadoConsultorios[i][3])    
        print(encabezado)

    #Resultados
    header("RESULTADOS",3)
    #A- Tiempo promedio de espera en la cola de turnos
    tEsperaTurnos = tEsperaTurnos / conTurno
    print("|{0:<126}|".format(" Tiempo promedio de espera en la cola de turnos: " + str(tEsperaTurnos) + str(" min")))
    print(encabezado)
    #B- Tiempo promedio de espera de los pacientes en cada especialidad
    print("| {0:<16}| {1:<50}| {2:<55}|".format("Especialidad","Cantidad de pacientes","Espera promedio [min]"))
    print(encabezado)
    for i in range(len(especialidades)):
        esperaProm = tEsperaEsp[i] / contPacAtendido[i]
        print("| {0:<16}| {1:<50}| {2:<55}|".format( especialidades[i],contPacAtendido[i],esperaProm))
    print(encabezado)
    #C- Cantidad de personas que no pudieron obtener turno (Durante la hora de atención, por demora de mesa de entradas)
    sinTurno = contPac - conTurno
    print("|{0:<126}|".format(" Cantidad de personas sin turno: " + str(sinTurno)))
    print(encabezado) 
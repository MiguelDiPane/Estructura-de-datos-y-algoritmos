import csv
from claseManejadorDesignaciones import ManejadorDesignaciones
from claseMenu import Menu
if __name__ == '__main__':
    manejador = ManejadorDesignaciones()
    #Cargo incendios en la lista
    archivo = open('estadistica-designacion-magistrados-federal-nacional-por-genero.csv',encoding="UTF-8")
    reader = csv.reader(archivo,delimiter=',')
    bandera = False
    for fila in reader:
        if not bandera:
            bandera = True
        else:
            manejador.agregar(int(fila[0]), fila[1],
                            fila[2],fila[3],fila[4],
                            int(fila[5]),int(fila[6]))
    archivo.close()

    #--------------------------#
    #  DEFINO MENU Y SUBMENUS  #
    #--------------------------#
    menu = Menu()
    menu.define_menu('Menu de opciones',[
        '[1]- Mostrar lista',
        '[2]- Designaciones de mujeres por cargo',
        '[3]- Agentes designados segun materia, cargo y año',
        '[0]- Salir'])
    
    #Submenu cargos
    menuCargos = Menu()
    #Obtengo los cargos disponibles
    cargos = manejador.getCargos()
    #Agrego formato para el menu de cargos
    i = 0
    formato = []
    while i < len(cargos):
        formato.append('[{0}]- {1}'.format(i+1,cargos[i]))
        i+=1
    formato.append('[{0}]- {1}'.format(0,"Volver al menu anterior"))
    menuCargos.define_menu('Seleccione un cargo',formato)

    #Submenu Materias
    menuMaterias = Menu()
    #Obtengo los cargos disponibles
    materias = manejador.getMaterias()
    #Agrego formato para el menu de cargos
    i = 0
    formato = []
    while i < len(materias):
        formato.append('[{0}]- {1}'.format(i+1,materias[i]))
        i+=1
    formato.append('[{0}]- {1}'.format(0,"Volver al menu anterior"))
    menuMaterias.define_menu('Seleccione una materia',formato)    

    #Años
    anios = manejador.getAnios()
    
    #--------------------------#
    #     BUCLE PRINCIPAL      #
    #--------------------------#
    menu.showMenu()
    op = menu.selectOption() 

    while op != 0:
        if op==1:
            manejador.mostrar()
            input('\nPresione ENTER para continuar...')
        elif op == 2:
            menuCargos.showMenu()
            op2 = menuCargos.selectOption()
            while op2 != 0:    
                if op2 != 0: 
                    manejador.calcularCantMujeres(cargos[op2-1])
                    input('\nPresione ENTER para continuar...')   
                    menuCargos.showMenu()
                    op2 = menuCargos.selectOption()
        elif op == 3:
            menuCargos.showMenu()
            op3 = menuCargos.selectOption()
            while op3 != 0:    
                if op3 != None and op3 != 0:
                    menuMaterias.setTitulo('Seleccione una materia para cargo {0}'.format(cargos[op3-1])) 
                    menuMaterias.showMenu()
                    op4 = menuMaterias.selectOption()
                    while  op4 != 0:    
                        if op4 != None and op4 != 0:
                            print('Periodo disponible: {0} - {1}'.format(anios[0],anios[-1]))
                            anio = input('Ingrese un año: ')
                            while not anio.isdigit() or (int(anio) < anios[0] or int(anio) > anios[-1]):
                                print('Año no válido')
                                anio = input('Ingrese un año: ')
                            manejador.calcularAgentes(int(anio),materias[op4-1],cargos[op3-1])
                            
                            input('\nPresione ENTER para continuar...')   
                        menuMaterias.showMenu()
                        op4 = menuMaterias.selectOption()                     
                menuCargos.showMenu()
                op3 = menuCargos.selectOption()
  
        menu.showMenu()
        op = menu.selectOption()

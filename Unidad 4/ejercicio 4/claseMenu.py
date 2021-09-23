import os
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich import box



class Menu:
    __consola = None
    __titulo = ""
    __opciones = None
    __tema = None
    __salir = ""
    __tabla = None

    def __init__(self,titulo='MENU'):
        self.__opciones = []
        self.__titulo = titulo
        self.__salir = "Salir"
        
        #Tema para el menu
        self.__tema = Theme({"exito":"green", 
                            "error":"bold red",
                            "titulo": "bold black on white",
                            "opcion": "bold cyan",
                            "salir": "bold red",
                            "flecha":"bold cyan"})
        self.__consola = Console(theme=self.__tema)


    def setOpciones(self,opciones,fin="Salir"):
        self.__opciones = opciones
        self.__salir = fin

    def setTitulo(self,title):
        self.__titulo = title

    def showMenu(self):
        os.system('cls')

        #-------------------#
        #   SHOW  OPTIONS   #
        #-------------------#
        self.__tabla = Table()
        self.__tabla.box = box.ROUNDED
        self.__tabla.add_column(self.__titulo)
        
        for i in range(len(self.__opciones)):
             self.__tabla.add_row("[opcion][{0}][/] {1}".format(i+1,self.__opciones[i]))
        self.__tabla.add_row("[salir][{0}][/] {1}".format("Q",self.__salir))
        self.__consola.print(self.__tabla)

        #-------------------#
        #   SELECT OPTION   #
        #-------------------#
        op = self.__consola.input('\n[flecha]-->[/] ')
        if op.upper() == 'Q':
            op = 0
        else:
            if op.isdigit():
                op = int(op)
                if op > len(self.__opciones) or op < 0:
                    self.__consola.print('Opcion invalida, reintente',style="error")
                    self.__consola.input('\n[error]Presione ENTER para continuar...[/]')  
                    op = None      
            else:
                self.__consola.print('Error: Opcion invalida',style="error")
                self.__consola.input('\n[error]Presione ENTER para continuar...[/]')
                op = None
        return op 


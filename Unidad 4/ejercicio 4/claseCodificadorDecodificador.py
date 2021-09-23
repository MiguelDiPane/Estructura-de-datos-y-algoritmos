from claseListaEncadenadaCont import ListaEncadenadaCont
from claseArbolBinario import ArbolBinario
from rich.console import Console
from rich.table import Table
from rich import box

class CodificadorDecodificador:
    __lista = None
    __caracteres = None
    __frecuencias = None
    __arbolHuffman = None
    __archivo = None
    
    def __init__(self):
        self.__lista = ListaEncadenadaCont()
        self.__caracteres = []
        self.__frecuencias = []
        self.__archivo = None
    
    #Lectura del archivo, caracter a caracter para calcular su frecuencia
    def leerArchivo(self,nombre):
        try:
            nombre = nombre + '.txt'
            archivo = open(nombre, 'r')
            self.__caracteres = []
            self.__frecuencias = []
            for linea in archivo:
                for caracter in linea:
                    #Evito el caracter de salto de linea y el espacio
                    if caracter != '\n' and caracter != ' ':
                        if caracter not in self.__caracteres:
                            self.__caracteres.append(caracter)
                            self.__frecuencias.append(1)
                        else:
                            indice = self.__caracteres.index(caracter)
                            self.__frecuencias[indice] += 1
            archivo.close()
            self.__archivo = nombre
        except:
            print('Error: Archivo no encontrado')

    def mostrarFrecuencias(self):
        if self.__archivo != None:
            consola = Console()
            titulo = 'Diccionario - Archivo {}'.format(self.__archivo)
            tabla = Table(title=titulo)
            tabla.box = box.ROUNDED
            columnas = ['Caracter','Frecuencia']
            estilos = ["cyan","green"]
            alineacion = ["center","center"]
            for i in range(len(columnas)):
                tabla.add_column(columnas[i],justify = alineacion[i],style=estilos[i],width=20)                             
            for i in range(len(self.__caracteres)):
                tabla.add_row(self.__caracteres[i],str(self.__frecuencias[i]))
            consola.print(tabla)

        else:
            print('Error: Debe leer un archivo primero')
    
    def crearArbol(self):
        if self.__archivo != None:
            #Creo los objetos de la clase caracter
            #Creo el arbol cuya raiz es el objeto caracter
            #Lo coloco en la lista 
            for i in range(len(self.__caracteres)):
                newArbol = ArbolBinario(self.__caracteres[i],self.__frecuencias[i])
                self.__lista.insertar(newArbol)
            
            #El procedimiento se realiza hasta que la lista tiene una sola celda
            #Esta celda corresponde a la raiz del arbol binario que contiene a todos los
            #caracteres del diccionario de entrada como hojas
            while self.__lista.len() > 1:
                #Tomo de a pares, desde las frecuencias menores y creo un nuevo arbol
                #Tendra como raiz la suma de las frec y los dos chars juntos

                #Suprimo de la lista los de menor frec, obtengo los nodos
                primero = self.__lista.suprimir(0)
                segundo = self.__lista.suprimir(0)

                #De cada nodo obtengo el dato, es el arbol en sí
                arbol1 = primero.getDato()
                arbol2 = segundo.getDato()

                #De cada árbol obtengo su raiz, es el nodo con caracter y frec
                raiz1 = arbol1.getRaiz()
                raiz2 = arbol2.getRaiz()

                #Concateno los caracteres y sumo las frecuencias
                newChar = raiz1.getChar() + raiz2.getChar()
                newFrec = raiz1.getFrec() + raiz2.getFrec()

                #Creo el nuevo arbol
                newArbol = ArbolBinario(newChar,newFrec)
                
                #Coloco los hijos izquierdo y derecho
                #Tendra como hijo izq al de menor frec, y como hijo der al de mayor frec
                newArbol.insertar(raiz1)
                newArbol.insertar(raiz2)
                
                #Vuelvo a insertar en la lista
                self.__lista.insertar(newArbol)
        
            #Obtengo el árbol generador de codigos de huffman
            elemento = self.__lista.suprimir(0)
            self.__arbolHuffman = elemento.getDato()
            print('\nÁrbol binario generado')


    def mostrarArbol(self):
        if self.__archivo != None:
            raiz = self.__arbolHuffman.getRaiz()
            self.__arbolHuffman.mostrar(raiz)
        else:
            print('Error: Primero debe leer un archivo')
    
    #Codifico el archivo entero
    def comprimirArchivo(self):
        if self.__archivo != None:
            raiz = self.__arbolHuffman.getRaiz()
            archivo = open(self.__archivo, 'r')
            comprimido = ''
            for linea in archivo:
                for caracter in linea:
                    #Evito el caracter de salto de linea
                    if caracter == '\n':
                        comprimido += '\n'
                    elif caracter == ' ':
                        comprimido += ' '
                    else:
                        comprimido += self.__arbolHuffman.codCaracter(raiz,caracter)
                     
            archivo.close()
            print(comprimido)
            newNombre = 'comprimido_' + self.__archivo
            archivo = open (newNombre,'w')
            archivo.write(comprimido)
            archivo.close()
        else:
            print('Error: Primero debe leer un archivo')
    
    #Codificar mostrar el codigo de texto ingresado por teclado
    def codificar(self,texto):
        if self.__archivo != None:
            raiz = self.__arbolHuffman.getRaiz()
            codigo = ''
            while texto != '':
                char = texto[0]
                texto = texto[1:]
                if char != ' ':
                    cod = self.__arbolHuffman.codCaracter(raiz,char) 
                    codigo += cod
                else:
                    codigo += ' '
            print(codigo)
            return codigo
        else:
            print('Error: Debe leer un archivo para usarlo como diccionario')

    #Decodificar para mostrar el texto de un codigo ingresado por teclado
    def decodificar(self,codigo):
        if self.__archivo != None:
            raiz = self.__arbolHuffman.getRaiz()
            palabra = ''
            #Separo los saltos de linea por un espacio
            codigo.replace('\n',' ')
            #Separo los codigos en una lista, con la funcion split
            codigos = codigo.split(' ')
            for codigo in codigos:
                char = self.__arbolHuffman.decCaracter(raiz,codigo)
                palabra += char
            print('Texto decodificado: {}'.format(palabra))
        else:
            print('Error: Debe leer un archivo para usarlo como diccionario')
 
    def mostrarCodigosDisponibles(self):
            consola = Console()
            titulo = 'Caracteres y códigos disponibles - Archivo {}'.format(self.__archivo)
            tabla = Table(title=titulo)
            tabla.box = box.ROUNDED
            columnas = ['Caracter','Código']
            estilos = ["cyan","green"]
            alineacion = ["center","center"]
            raiz = self.__arbolHuffman.getRaiz()
            codigos = []
            for caracter in self.__caracteres:
                codigo = self.__arbolHuffman.codCaracter(raiz,caracter)
                codigos.append(codigo)
            for i in range(len(columnas)):
                tabla.add_column(columnas[i],justify = alineacion[i],style=estilos[i],width=20)                             
            for i in range(len(self.__caracteres)):
                tabla.add_row(self.__caracteres[i],str(codigos[i]))
            consola.print(tabla)
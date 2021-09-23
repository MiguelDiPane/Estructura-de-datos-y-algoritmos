from claseCodificadorDecodificador import CodificadorDecodificador
from claseMenu import Menu

if __name__ == '__main__':
    codDec = CodificadorDecodificador()
    menu = Menu('Algoritmo de Huffman')
    menu.setOpciones(['Leer archivo',
                    'Comprimir archivo y mostrar texto codificado',
                    'Mostrar árbol binario',
                    'Mostrar frecuencia de caracteres',
                    'Codificar texto ingresado por teclado',
                    'Decodificar codigo ingresado por teclado'])
    
    op = menu.showMenu()
    while op != 0:
        if op == 1:
            nombre = input('Ingrese nombre de archivo: ')
            codDec.leerArchivo(nombre)
            codDec.crearArbol()
        elif op == 2:
            codDec.comprimirArchivo()
        elif op == 3:
            codDec.mostrarArbol()
        elif op == 4:
            codDec.mostrarFrecuencias()
        elif op == 5:
            codDec.mostrarCodigosDisponibles()
            texto = input('\nIngrese el texto: ')
            codDec.codificar(texto)
        elif op == 6:
            codDec.mostrarCodigosDisponibles()
            codigo = input('Ingrese un código: ')
            codDec.decodificar(codigo)
        input('Presione una tecla para continuar...')
        op = menu.showMenu()
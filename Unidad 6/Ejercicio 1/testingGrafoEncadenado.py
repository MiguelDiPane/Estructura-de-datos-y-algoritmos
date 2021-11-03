import unittest
from claseGrafoEnlazada import GrafoEnlazado as Grafo

class GrafoSecuencialTest(unittest.TestCase):

    def test_nodos_adyacentes(self):
        #Condición inicial
        self.__grafo = Grafo(4,True)
        self.__grafo.cargar_nodo(0,20)
        self.__grafo.cargar_nodo(1,34)
        self.__grafo.cargar_nodo(2,45)
        self.__grafo.cargar_nodo(3,415)

        #Cambio o solicitud
        self.__grafo.relacionar_nodos(0,1,3)
        self.__grafo.relacionar_nodos(0,3,3)

        self.__grafo.relacionar_nodos(1,2,1)

        #Verificación
        self.assertEqual(self.__grafo.adyacentes(0),[3,1])
     
    def test_grado_de_un_nodo(self):
        #Condición inicial
        self.__grafo = Grafo(3)
        self.__grafo.cargar_nodo(0,20)
        self.__grafo.cargar_nodo(1,34)
        self.__grafo.cargar_nodo(2,45)

        #Cambio o solicitud
        self.__grafo.relacionar_nodos(0,1)
        self.__grafo.relacionar_nodos(0,2)

        #Verificación
        self.assertEqual(self.__grafo.grado(0),2)

    def test_determinar_conexidad_del_grafo(self):
        #Condición inicial
        self.__grafo = Grafo(3)
        self.__grafo.cargar_nodo(0,20)
        self.__grafo.cargar_nodo(1,34)
        self.__grafo.cargar_nodo(2,45)

        #Cambio o solicitud
        self.__grafo.relacionar_nodos(0,1)
        self.__grafo.relacionar_nodos(0,2)

        #Verificación
        self.assertEqual(self.__grafo.conexo(),True) #es conexo

    def test_camino_grafo_no_ponderado(self):
        #Condición inicial
        self.__grafo = Grafo(6)
        self.__grafo.cargar_nodo(0,2)
        self.__grafo.cargar_nodo(1,5)
        self.__grafo.cargar_nodo(2,6)
        self.__grafo.cargar_nodo(3,7)
        self.__grafo.cargar_nodo(4,3)
        self.__grafo.cargar_nodo(5,9)
        
        #Cambio o solicitud
        self.__grafo.relacionar_nodos(0,3)
        self.__grafo.relacionar_nodos(0,4)

        self.__grafo.relacionar_nodos(1,3)
        self.__grafo.relacionar_nodos(1,5)

        self.__grafo.relacionar_nodos(2,4)
        self.__grafo.relacionar_nodos(4,5)

        self.assertEqual(self.__grafo.camino(0,5,True),[0,4,5])

        #self.assertEqual()

    def test_camino_minimo_grafo_no_ponderado(self):
        #Condición inicial
        self.__grafo = Grafo(6)
        self.__grafo.cargar_nodo(0,2)
        self.__grafo.cargar_nodo(1,5)
        self.__grafo.cargar_nodo(2,6)
        self.__grafo.cargar_nodo(3,7)
        self.__grafo.cargar_nodo(4,3)
        self.__grafo.cargar_nodo(5,9)
        
        #Cambio o solicitud
        self.__grafo.relacionar_nodos(0,3)
        self.__grafo.relacionar_nodos(0,4)

        self.__grafo.relacionar_nodos(1,3)
        self.__grafo.relacionar_nodos(1,5)

        self.__grafo.relacionar_nodos(2,4)
        self.__grafo.relacionar_nodos(4,5)

        self.assertEqual(self.__grafo.camino_minimo(2,3,True),[2,4,0,3])

    def test_camino_minimo_grafo_ponderado(self):
        #Condición inicial
        self.__grafo = Grafo(7,True)
        self.__grafo.cargar_nodo(0,20)
        self.__grafo.cargar_nodo(1,34)
        self.__grafo.cargar_nodo(2,45)
        self.__grafo.cargar_nodo(3,415)
        self.__grafo.cargar_nodo(4,435)
        self.__grafo.cargar_nodo(5,475)
        self.__grafo.cargar_nodo(6,135)

        #Cambio o solicitud
        self.__grafo.relacionar_nodos(0,1,3)
        self.__grafo.relacionar_nodos(0,3,3)

        self.__grafo.relacionar_nodos(1,2,1)

        self.__grafo.relacionar_nodos(1,4,2)

        self.__grafo.relacionar_nodos(2,3,2)
        self.__grafo.relacionar_nodos(2,4,3)
        self.__grafo.relacionar_nodos(2,5,2)

        self.__grafo.relacionar_nodos(3,5,1)
        self.__grafo.relacionar_nodos(3,6,3)

        self.__grafo.relacionar_nodos(4,5,3)
        
        self.__grafo.relacionar_nodos(5,6,2)


        #Verificación
        self.assertEqual(self.__grafo.camino_minimo(0,6,True),[0,3,6])

    def test_aciclico_grafo(self):
        #Condición inicial
        self.__grafo = Grafo(7)
        self.__grafo.cargar_nodo(0,20)
        self.__grafo.cargar_nodo(1,34)
        self.__grafo.cargar_nodo(2,45)


        #Cambio o solicitud
        self.__grafo.relacionar_nodos(0,1)
        self.__grafo.relacionar_nodos(0,2)

        #Verificación
        self.assertEqual(self.__grafo.aciclico(),False)

    def test_aciclico_grafo_ponderado(self):
        #Condición inicial
        self.__grafo = Grafo(7,True)
        self.__grafo.cargar_nodo(0,20)
        self.__grafo.cargar_nodo(1,34)
        self.__grafo.cargar_nodo(2,45)
        self.__grafo.cargar_nodo(3,415)
        self.__grafo.cargar_nodo(4,435)
        self.__grafo.cargar_nodo(5,475)
        self.__grafo.cargar_nodo(6,135)

        #Cambio o solicitud
        self.__grafo.relacionar_nodos(0,1,3)
        self.__grafo.relacionar_nodos(0,3,3)

        self.__grafo.relacionar_nodos(1,2,1)

        self.__grafo.relacionar_nodos(1,4,2)

        self.__grafo.relacionar_nodos(2,3,2)
        self.__grafo.relacionar_nodos(2,4,3)
        self.__grafo.relacionar_nodos(2,5,2)

        self.__grafo.relacionar_nodos(3,5,1)
        self.__grafo.relacionar_nodos(3,6,3)

        self.__grafo.relacionar_nodos(4,5,3)
        
        self.__grafo.relacionar_nodos(5,6,2)

        #Verificación
        self.assertEqual(self.__grafo.aciclico(),False)

if __name__ == '__main__':
    unittest.main()
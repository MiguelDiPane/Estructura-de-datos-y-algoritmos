from claseTablaHash import TablaHash
import unittest

class TestTablaH(unittest.TestCase):

    def test_insertar_con_uso_de_buckets(self):
        #Condición inicial
        self.__tablaH = TablaHash(10,3)

        #Cambio o solicitud
        self.__tablaH.insertar(304)      
        self.__tablaH.insertar(404)
        self.__tablaH.insertar(504)

        #Verificación
        self.assertEqual(self.__tablaH.buscar_posicion(304),4)       
        self.assertEqual(self.__tablaH.buscar_posicion(404),4)
        self.assertEqual(self.__tablaH.buscar_posicion(504),4)


    def test_insertar_con_uso_de_buckets_con_overflow(self):
        #Condición inicial
        self.__tablaH = TablaHash(11,3)
        self.__tablaH.insertar(304)      
        self.__tablaH.insertar(404)
        self.__tablaH.insertar(504)

        #Cambio o solicitud
        self.__tablaH.insertar(604)

        #Verificación
        #Bucket lleno, debería insertar en área de overflow, primer bucket overflow en pos 11
        self.assertEqual(self.__tablaH.buscar_posicion(604),11)
 

if __name__ == '__main__':
    unittest.main()

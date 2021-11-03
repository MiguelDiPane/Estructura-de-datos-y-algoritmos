from claseTablaHash import TablaHash
import unittest

class TestTablaH(unittest.TestCase):

    def test_buscar_clave_dada_posicion(self):
        #Condición inicial
        self.__tablaH = TablaHash(5)

        #Cambio o solicitud
        self.__tablaH.insertar(15)
        self.__tablaH.insertar(23)
        self.__tablaH.insertar(11)
        self.__tablaH.insertar(25)

        #Verificación
        self.assertEqual(self.__tablaH.buscar_posicion(25),6)
        self.assertEqual(self.__tablaH.buscar_clave(6),25)

    def test_buscar_clave_dada_clave_inexistente(self):
        #Condición inicial
        self.__tablaH = TablaHash(5)

        #Cambio o solicitud
        self.__tablaH.insertar(15)
        self.__tablaH.insertar(23)
        self.__tablaH.insertar(11)
        self.__tablaH.insertar(25)

        #Verificación
        self.assertEqual(self.__tablaH.buscar_clave(45),-1)

    def test_buscar_pos_1_elemento(self):
        #Condición inicial
        self.__tablaH = TablaHash(5)

        #Cambio o solicitud
        self.__tablaH.insertar(15)

        #Verificación
        self.assertEqual(self.__tablaH.buscar_posicion(15),1)


    def test_buscar_pos_2_elementos(self):
        #Condición inicial
        self.__tablaH = TablaHash(5)

        #Cambio o solicitud
        self.__tablaH.insertar(15)
        self.__tablaH.insertar(25)

        #Verificación
        self.assertEqual(self.__tablaH.buscar_posicion(15),1)
        self.assertEqual(self.__tablaH.buscar_posicion(25),4)


    def test_buscar_pos_3_elementos(self):
        #Condición inicial
        self.__tablaH = TablaHash(5)

        #Cambio o solicitud
        self.__tablaH.insertar(15)
        self.__tablaH.insertar(23)
        self.__tablaH.insertar(11)

        #Verificación
        self.assertEqual(self.__tablaH.buscar_posicion(15),1)
        self.assertEqual(self.__tablaH.buscar_posicion(23),2)
        self.assertEqual(self.__tablaH.buscar_posicion(11),4)

    def test_buscar_pos_4_elementos(self):
        #Condición inicial
        self.__tablaH = TablaHash(5)

        #Cambio o solicitud
        self.__tablaH.insertar(15)
        self.__tablaH.insertar(23)
        self.__tablaH.insertar(11)
        self.__tablaH.insertar(25)

        #Verificación
        self.assertEqual(self.__tablaH.buscar_posicion(15),1)
        self.assertEqual(self.__tablaH.buscar_posicion(23),2)
        self.assertEqual(self.__tablaH.buscar_posicion(11),4)
        self.assertEqual(self.__tablaH.buscar_posicion(25),6)

if __name__ == '__main__':
    unittest.main()

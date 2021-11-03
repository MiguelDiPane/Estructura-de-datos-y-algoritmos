from claseTablaHash import TablaHash
import unittest

class TestTablaH(unittest.TestCase):

    def test_generar_pos_por_plegado_cant_digitos_impar(self):
        #Condición inicial
        self.__tablaH = TablaHash(109)

        #Cambio o solicitud
        
        #Verificación
        self.assertEqual(self.__tablaH.obtener_pos_inicial_por_plegado(13456),64)

    def test_generar_pos_por_plegado__cant_digitos_par(self):
        #Condición inicial
        self.__tablaH = TablaHash(109)

        #Cambio o solicitud
        
        #Verificación
        self.assertEqual(self.__tablaH.obtener_pos_inicial_por_plegado(1345),58)


    def test_buscar_claves_por_posicion_con_colision(self):
        '''Documentación del test'''
        
        #Condición inicial
        self.__tablaH = TablaHash(109)

        #Cambio o solicitud
        self.__tablaH.insertar(1345)
        self.__tablaH.insertar(1444)
        self.__tablaH.insertar(1543)

        #Verificación
        #Las tres claves se encuentran en la misma lista en posición 58
        #[1345,1444,1543]
        self.__tablaH.buscar_claves(58)

    def test_buscar_posicion_e_indice_de_una_clave(self):
        '''Documentación del test'''
        
        #Condición inicial
        self.__tablaH = TablaHash(109)

        #Cambio o solicitud
        self.__tablaH.insertar(1345)
        self.__tablaH.insertar(1444)
        self.__tablaH.insertar(1543)

        #Verificación
        #Las tres claves se encuentran en la misma lista en posición 58 [1345,1444,1543]
        self.__tablaH.buscar_posicion(144)

    def test_esta_la_lista_y_la_clave(self):
        '''Busca una clave que existe en una lista'''
        
        #Condición inicial
        self.__tablaH = TablaHash(109)

        #Cambio o solicitud
        self.__tablaH.insertar(1444)

        #Verificación 
        #En lista con posición 58, índice 0 dentro de la lista
        self.assertEqual(self.__tablaH.buscar_posicion(1444),(58,0))

    def test_esta_la_lista_y_no_la_clave(self):
        '''Busca una clave que no existe en una lista, pero al insertarla debería ir en dicha lista'''
        
        #Condición inicial
        self.__tablaH = TablaHash(109)

        #Cambio o solicitud
        self.__tablaH.insertar(1444)

        #Verificación
        self.assertEqual(self.__tablaH.buscar_posicion(1345),(58,-1))

    def test_no_esta_la_lista_ni_clave(self):
        '''Busca una clave en una lista aun no creada'''
        #Condición inicial
        self.__tablaH = TablaHash(109)

        #Cambio o solicitud

        #Verificación
        self.assertEqual(self.__tablaH.buscar_posicion(1345),(-1,-1))

if __name__ == '__main__':
    unittest.main()

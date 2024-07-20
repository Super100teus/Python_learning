import unittest
import cambia_texto


class Probando(unittest.TestCase):

    def test_mayusculas(self):
        """
        Todas las funciones que hagas en una clase que hereda de unittest deben de llevar como nombre
         de funcion la palabra test al comienzo despues pueden llevar lo que sea
        :return:Nada
        """
        palabra = 'pakala'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'PAKAlA')


if __name__ == '__main__':
    unittest.main()

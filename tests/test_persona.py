import unittest
import datetime
from src.modules.persona import Persona

class PersonasTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.persona1=Persona(nombre='Alejandra',edad=25)
        self.persona2=Persona(nombre='Diego',edad=22)
        self.persona3=Persona(nombre='Alejandra',edad=25)
        self.persona4=Persona(nombre='Diana',edad=25)
        self.grupo=[self.persona1,self.persona2,self.persona3]

    def test_constructor(self):
        self.assertEqual(self.persona1.dar_nombre(),'Alejandra')
        self.assertEqual(self.persona1.dar_edad(),25)

    def test_anio_nacimiento(sefl):
        sefl.assertEqual(sefl.persona1.calcular_anio_nacimiento(True),datetime.datetime.now().year-25)
        sefl.assertNotEqual(sefl.persona1.calcular_anio_nacimiento(False),datetime.datetime.now().year-25)
        sefl.assertEqual(sefl.persona1.calcular_anio_nacimiento(False),datetime.datetime.now().year-25+1)
        sefl.assertNotEqual(sefl.persona1.calcular_anio_nacimiento(True),datetime.datetime.now().year-25+1)

    def test_asignacion(self):
        self.persona2.asignar_edad(28)
        self.persona2.asignar_nombre('Felipe')
        self.assertFalse(self.persona2.dar_nombre()=="Diego")
        self.assertFalse(self.persona2.dar_edad()==25)
        self.assertTrue(self.persona2.dar_nombre()=="Felipe")
        self.assertTrue(self.persona2.dar_edad()==28)

    def test_objetos_iguales(self):
        persona_nueva=self.persona1
        self.assertIsNot(self.persona1,self.persona3)
        self.assertIs(self.persona1,persona_nueva)

    def test_elemento_en_conjunto(self):
        self.assertIn(self.persona3,self.grupo)
        self.assertNotIn(self.persona4,self.grupo)
    
    def test_instancia_clase(self):
        self.assertIsInstance(self.persona1,Persona)
        self.assertNotIsInstance(self.grupo,Persona)


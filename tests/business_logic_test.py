import unittest
from src.proyecto_algoritmos.business_logic import Pedido, note

class TestPedido(unittest.TestCase):

    def setUp(self):
        self.pedido = Pedido(
            id_note=1,
            quantity=2,
            glass_type='lun 10',
            length=2.0,
            width=3.0,
            includes_glass=True,
            barrenos=4,
            barrenos_type='barreno 37',
            sandblasted=True,
            canteado=True,
            extra=50.0
        )

    def test_calculate_price(self):
        self.pedido.calculate_price()
        self.assertGreater(self.pedido.total, 0)

    def test_pack(self):
        packed = self.pedido.pack()
        self.assertIsInstance(packed, list)

class TestNote(unittest.TestCase):

    def setUp(self):
        self.pedido1 = Pedido(
            id_note=1,
            quantity=2,
            glass_type='cla 4',
            length=2.0,
            width=3.0,
            includes_glass=True,
            barrenos=4,
            barrenos_type='barreno 19',
            sandblasted=True,
            canteado=True,
            extra=50.0
        )
        self.pedido2 = Pedido(
            id_note=2,
            quantity=1,
            glass_type='sol 3',
            length=1.0,
            width=1.5,
            includes_glass=False,
            barrenos=2,
            barrenos_type='barreno 37',
            sandblasted=False,
            canteado=False,
            extra=20.0
        )
        self.note = note(
            id=1,
            client='Cliente1',
            products=[self.pedido1, self.pedido2],
            typ='efectivo'
        )

    def test_note_total(self):
        self.assertGreater(self.note.note_total, 0)

    def test_get_resume(self):
        resume, note_total = self.note.get_resume()
        self.assertIsInstance(resume, list)
        self.assertEqual(note_total, self.note.note_total)

    def test_pack(self):
        packed = self.note.pack()
        self.assertIsInstance(packed, list)
        self.assertEqual(len(packed), 5)

if __name__ == '__main__':
    unittest.main()
import unittest
from Function import System, Sala

class TestSystem(unittest.TestCase):

    def setUp(self):
        self.system = System()

    def test_dodaj_sale(self):
        sala1 = Sala(101)
        self.system.dodaj_sale(sala1)
        self.assertIn(sala1, self.system.sale)

    def test_usun_sale(self):
        sala1 = Sala(101)
        self.system.dodaj_sale(sala1)
        self.system.usun_sale(101)
        self.assertNotIn(sala1, self.system.sale)

    def test_dodaj_skladnik(self):
        sala1 = Sala(101)
        self.system.dodaj_sale(sala1)
        self.system.dodaj_skladnik(101, 'sprzet', 'Komputer', 'Nowy')
        self.assertEqual(len(sala1.skladniki), 1)
        self.assertEqual(sala1.skladniki[0].nazwa, 'Komputer')

    def test_usun_skladnik(self):
        sala1 = Sala(101)
        self.system.dodaj_sale(sala1)
        self.system.dodaj_skladnik(101, 'sprzet', 'Komputer', 'Nowy')
        skladnik_id = sala1.skladniki[0].id
        self.system.usun_skladnik(101, skladnik_id)
        self.assertEqual(len(sala1.skladniki), 0)

    def test_wyszukaj_skladnik(self):
        sala1 = Sala(101)
        sala2 = Sala(102)
        self.system.dodaj_sale(sala1)
        self.system.dodaj_sale(sala2)
        self.system.dodaj_skladnik(101, 'meble', 'Krzesło', 'Dobry')
        self.system.dodaj_skladnik(102, 'meble', 'Krzesło', 'Zły')
        wyniki = self.system.wyszukaj_skladnik('Krzesło')
        self.assertEqual(len(wyniki), 2)

    def test_inwentaryzacja(self):
        sala1 = Sala(101)
        self.system.dodaj_sale(sala1)
        self.system.dodaj_skladnik(101, 'sprzet', 'Komputer', 'Nowy')
        raport = self.system.inwentaryzacja()
        self.assertIn('Brakujące składniki: Krzesło, Biurko', raport)

    def test_zapisz_i_wczytaj_raport(self):
        sala1 = Sala(101)
        self.system.dodaj_sale(sala1)
        self.system.dodaj_skladnik(101, 'sprzet', 'Komputer', 'Nowy')
        self.system.zapisz_raport('raport.txt')


        nowy_system = System()
        nowy_system.wczytaj_raport('raport.txt')
        self.assertEqual(len(nowy_system.sale), 1)
        self.assertEqual(nowy_system.sale[0].numer, 101)
        self.assertEqual(nowy_system.sale[0].skladniki[0].nazwa, 'Komputer')

    def test_przenies_skladnik(self):
        sala1 = Sala(101)
        sala2 = Sala(102)
        self.system.dodaj_sale(sala1)
        self.system.dodaj_sale(sala2)
        self.system.dodaj_skladnik(101, 'sprzet', 'Komputer', 'Nowy')
        skladnik_id = sala1.skladniki[0].id
        wynik = self.system.przenies_skladnik(101, 102, skladnik_id)
        self.assertIn('został przeniesiony', wynik)
        self.assertEqual(len(sala1.skladniki), 0)
        self.assertEqual(len(sala2.skladniki), 1)
        self.assertEqual(sala2.skladniki[0].nazwa, 'Komputer')

if __name__ == '__main__':
    unittest.main()

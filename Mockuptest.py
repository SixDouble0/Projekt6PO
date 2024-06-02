import unittest
from Function import Sala, System, Inwentaryzacja


class TestSystem(unittest.TestCase):
    def setUp(self):
        self.system = System()


        self.sala1 = Sala(1, [Sala.Sprzet(1, "Komputer"), Sala.Krzeslo(2, "Krzeslo")])
        self.sala2 = Sala(2, [Sala.Sprzet(3, "Projektor"), Sala.Stol(4, "Stol")])


        self.system.dodaj_sale(self.sala1)
        self.system.dodaj_sale(self.sala2)

    def test_dodaj_sale(self):
        self.assertEqual(len(self.system.sale), 2)
        self.assertEqual(self.system.sale[0].Numer, 1)
        self.assertEqual(self.system.sale[1].Numer, 2)

    def test_usun_sale(self):
        self.system.usun_sale(1)
        self.assertEqual(len(self.system.sale), 1)
        self.assertEqual(self.system.sale[0].Numer, 2)

    def test_przegladaj_sale(self):
        self.system.przegladaj_sale()

    def test_znajdz_skladnik(self):
        wynik = self.system.znajdz_skladnik("Komputer")
        self.assertEqual(len(wynik), 1)
        self.assertEqual(wynik[0].nazwa, "Komputer")

        wynik = self.system.znajdz_skladnik("Projektor", Sala.Sprzet)
        self.assertEqual(len(wynik), 1)
        self.assertEqual(wynik[0].nazwa, "Projektor")

    def test_przenies_skladnik(self):
        self.system.przenies_skladnik("Komputer", 1, 2)
        self.assertEqual(len(self.sala1.skladniki.skladniki), 1)
        self.assertEqual(len(self.sala2.skladniki.skladniki), 3)

    def test_inwentaryzacja(self):
        skladniki_do_sprawdzenia = [Sala.Sprzet(1, "Komputer"), Sala.Krzeslo(2, "Krzeslo")]
        inwentaryzacja = self.system.inwentaryzacja(1, skladniki_do_sprawdzenia)

        self.assertIsInstance(inwentaryzacja, Inwentaryzacja)
        self.assertEqual(len(inwentaryzacja.braki), 0)
        self.assertEqual(len(inwentaryzacja.kiepski_stan), 0)
        self.assertEqual(len(inwentaryzacja.nowe), 0)

        skladniki_do_sprawdzenia = [Sala.Sprzet(1, "Komputer", "zły"), Sala.Krzeslo(2, "Krzeslo")]
        inwentaryzacja = self.system.inwentaryzacja(1, skladniki_do_sprawdzenia)

        self.assertEqual(len(inwentaryzacja.kiepski_stan), 1)
        self.assertEqual(inwentaryzacja.kiepski_stan[0].stan, "zły")

    def test_zapisz_odczytaj_z_pliku(self):
        self.system.zapisz_do_pliku("sale_test.json")
        system_plik = System()
        system_plik.odczytaj_z_pliku("sale_test.json")

        self.assertEqual(len(system_plik.sale), 2)
        self.assertEqual(system_plik.sale[0].Numer, 1)
        self.assertEqual(system_plik.sale[1].Numer, 2)
        self.assertEqual(system_plik.sale[0].skladniki.skladniki[0]['skladnikmajatkowy'].nazwa, "Komputer")
        self.assertEqual(system_plik.sale[1].skladniki.skladniki[0]['skladnikmajatkowy'].nazwa, "Projektor")


if __name__ == '__main__':
    unittest.main()

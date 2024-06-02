class Sala:
    def __init__(self, Numer, skladniki=None):
        self.Numer = int(Numer)
        self.skladniki = self.Skladniki(Numer, skladniki if skladniki else [])

    class SkladnikMajatkowy:
        def __init__(self, id, nazwa, stan="dobry"):
            self.id = int(id)
            self.nazwa = str(nazwa)
            self.stan = stan

        def __repr__(self):
            return f"{self.__class__.__name__}(id={self.id}, nazwa='{self.nazwa}', stan='{self.stan}')"

    class Sprzet(SkladnikMajatkowy):
        def __init__(self, id, nazwa, stan="dobry"):
            super().__init__(id, nazwa, stan)

    class Komputer(Sprzet):
        def __init__(self, id, nazwa, stan="dobry"):
            super().__init__(id, nazwa, stan)

    class Drukarka(Sprzet):
        def __init__(self, id, nazwa, stan="dobry"):
            super().__init__(id, nazwa, stan)

    class Oscylator(Sprzet):
        def __init__(self, id, nazwa, stan="dobry"):
            super().__init__(id, nazwa, stan)

    class Mebel(SkladnikMajatkowy):
        def __init__(self, id, nazwa, stan="dobry"):
            super().__init__(id, nazwa, stan)

    class Krzeslo(Mebel):
        def __init__(self, id, nazwa, stan="dobry"):
            super().__init__(id, nazwa, stan)

    class Stol(Mebel):
        def __init__(self, id, nazwa, stan="dobry"):
            super().__init__(id, nazwa, stan)

    class Regal(Mebel):
        def __init__(self, id, nazwa, stan="dobry"):
            super().__init__(id, nazwa, stan)

    class Skladniki:
        def __init__(self, id, skladniki):
            self.id = int(id)
            self.skladniki = [{'id': i + 1, 'skladnikmajatkowy': skladnik} for i, skladnik in enumerate(skladniki)]

        def dodajSkladnik(self, skladnikmajatkowy):
            new_id = len(self.skladniki) + 1
            self.skladniki.append({'id': new_id, 'skladnikmajatkowy': skladnikmajatkowy})

        def usunSkladnik(self, skladnik_id):
            self.skladniki = [skladnik for skladnik in self.skladniki if skladnik['id'] != skladnik_id]

        def __repr__(self):
            return f"Skladniki(id={self.id}, skladniki={self.skladniki})"

    def __repr__(self):
        return f"Sala(Numer={self.Numer}, skladniki={self.skladniki})"

class Inwentaryzacja:
    def __init__(self):
        self.braki = []
        self.nowe = []
        self.kiepski_stan = []

    def dodaj_brak(self, skladnik):
        self.braki.append(skladnik)

    def dodaj_nowy(self, skladnik):
        self.nowe.append(skladnik)

    def dodaj_kiepski_stan(self, skladnik):
        self.kiepski_stan.append(skladnik)

    def __repr__(self):
        return (f"Inwentaryzacja(\n  braki={self.braki},\n  nowe={self.nowe},\n"
                f"  kiepski_stan={self.kiepski_stan}\n)")

class System:
    def __init__(self):
        self.sale = []

    def dodaj_sale(self, sala):
        self.sale.append(sala)

    def usun_sale(self, numer):
        self.sale = [sala for sala in self.sale if sala.Numer != numer]

    def przegladaj_sale(self):
        for sala in self.sale:
            print(sala)

    def znajdz_skladnik(self, nazwa, typ=None):
        wynik = []
        for sala in self.sale:
            for skladnik in sala.skladniki.skladniki:
                skladnik_obj = skladnik['skladnikmajatkowy']
                if skladnik_obj.nazwa == nazwa and (typ is None or isinstance(skladnik_obj, typ)):
                    wynik.append(skladnik_obj)
        return wynik

    def inwentaryzacja(self, numer_sali, skladniki_do_sprawdzenia):
        sala = next((s for s in self.sale if s.Numer == numer_sali), None)
        if not sala:
            print(f"Sala {numer_sali} nie istnieje.")
            return None

        inwentaryzacja = Inwentaryzacja()
        istniejace_skladniki = {s['skladnikmajatkowy'].nazwa: s['skladnikmajatkowy'] for s in sala.skladniki.skladniki}

        for skladnik in skladniki_do_sprawdzenia:
            if skladnik.nazwa not in istniejace_skladniki:
                inwentaryzacja.dodaj_brak(skladnik)
            else:
                istniejacy_skladnik = istniejace_skladniki[skladnik.nazwa]
                if istniejacy_skladnik.stan != skladnik.stan:
                    inwentaryzacja.dodaj_kiepski_stan(skladnik)

        for skladnik in sala.skladniki.skladniki:
            if skladnik['skladnikmajatkowy'].nazwa not in [s.nazwa for s in skladniki_do_sprawdzenia]:
                inwentaryzacja.dodaj_nowy(skladnik['skladnikmajatkowy'])

        return inwentaryzacja

    def przenies_skladnik(self, nazwa, numer_z, numer_do):
        sala_z = next((s for s in self.sale if s.Numer == numer_z), None)
        sala_do = next((s for s in self.sale if s.Numer == numer_do), None)
        if not sala_z or not sala_do:
            print(f"Sala {numer_z} lub {numer_do} nie istnieje.")
            return

        skladnik = next((s for s in sala_z.skladniki.skladniki if s['skladnikmajatkowy'].nazwa == nazwa), None)
        if not skladnik:
            print(f"Skladnik {nazwa} nie istnieje w sali {numer_z}.")
            return

        sala_do.skladniki.dodajSkladnik(skladnik['skladnikmajatkowy'])
        sala_z.skladniki.usunSkladnik(skladnik['id'])

    def zapisz_do_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, 'w') as plik:
            for sala in self.sale:
                plik.write(f"Sala: {sala.Numer}\n")
                for skladnik in sala.skladniki.skladniki:
                    skladnik_obj = skladnik['skladnikmajatkowy']
                    plik.write(f"  {skladnik_obj.__class__.__name__}: id={skladnik_obj.id}, nazwa='{skladnik_obj.nazwa}', stan='{skladnik_obj.stan}'\n")

    def odczytaj_z_pliku(self, nazwa_pliku):
        try:
            with open(nazwa_pliku, 'r') as plik:
                self.sale = []
                numer_sali = None
                skladniki = []
                for linia in plik:
                    if linia.startswith("Sala: "):
                        if numer_sali is not None:
                            sala = Sala(numer_sali, skladniki)
                            self.dodaj_sale(sala)
                        numer_sali = int(linia.split(": ")[1].strip())
                        skladniki = []
                    else:
                        typ, reszta = linia.strip().split(": ", 1)
                        id, nazwa_stan = reszta.split(", ")
                        id = int(id.split("=")[1])
                        nazwa = nazwa_stan.split(", ")[0].split("=")[1]
                        stan = nazwa_stan.split(", ")[1].split("=")[1].strip("'")
                        if typ == "Krzeslo":
                            skladnik = Sala.Krzeslo(id, nazwa, stan)
                        elif typ == "Stol":
                            skladnik = Sala.Stol(id, nazwa, stan)
                        elif typ == "Regal":
                            skladnik = Sala.Regal(id, nazwa, stan)
                        elif typ == "Komputer":
                            skladnik = Sala.Komputer(id, nazwa, stan)
                        elif typ == "Drukarka":
                            skladnik = Sala.Drukarka(id, nazwa, stan)
                        elif typ == "Oscylator":
                            skladnik = Sala.Oscylator(id, nazwa, stan)
                        skladniki.append({'id': id, 'skladnikmajatkowy': skladnik})
                    sala = Sala(numer_sali, skladniki)
                    self.dodaj_sale(sala)
        except FileNotFoundError:
            print(f"Plik {nazwa_pliku} nie istnieje.")


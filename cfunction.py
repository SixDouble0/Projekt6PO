from abc import ABC, abstractmethod

class SkladnikMajatkowy(ABC):
    _id_counter = 0  

    def __init__(self, nazwa, stan):
        self.id = SkladnikMajatkowy._id_counter
        SkladnikMajatkowy._id_counter += 1
        self.nazwa = nazwa
        self.stan = stan

    @abstractmethod
    def __str__(self):
        pass

class Sprzet(SkladnikMajatkowy):
    def __init__(self, nazwa, stan):
        super().__init__(nazwa, stan)

    def __str__(self):
        return f'ID: {self.id}, {self.nazwa} (stan: {self.stan})'

class Meble(SkladnikMajatkowy):
    def __init__(self, nazwa, stan):
        super().__init__(nazwa, stan)

    def __str__(self):
        return f'ID: {self.id}, {self.nazwa} (stan: {self.stan})'

class Sala:
    def __init__(self, numer):
        self.numer = numer
        self.skladniki = []

    def dodaj_skladnik(self, skladnik):
        self.skladniki.append(skladnik)

    def usun_skladnik(self, skladnik_id):
        self.skladniki = [s for s in self.skladniki if s.id != skladnik_id]

    def __str__(self):
        return f'Sala numer {self.numer}: {[str(s) for s in self.skladniki]}'

class System:
    def __init__(self):
        self.sale = []

    def dodaj_sale(self, sala):
        self.sale.append(sala)

    def usun_sale(self, numer):
        self.sale = [s for s in self.sale if s.numer != numer]

    def dodaj_skladnik(self, numer_sali, typ, nazwa, stan):
        for sala in self.sale:
            if sala.numer == numer_sali:
                if typ == 'sprzet':
                    skladnik = Sprzet(nazwa, stan)
                elif typ == 'meble':
                    skladnik = Meble(nazwa, stan)
                else:
                    return
                sala.dodaj_skladnik(skladnik)

    def usun_skladnik(self, numer_sali, skladnik_id):
        for sala in self.sale:
            if sala.numer == numer_sali:
                sala.usun_skladnik(skladnik_id)

    def wyszukaj_skladnik(self, nazwa_skladnika):
        wyniki = []
        for sala in self.sale:
            for skladnik in sala.skladniki:
                if skladnik.nazwa == nazwa_skladnika:
                    wyniki.append(f'Sala: {sala.numer}, ID: {skladnik.id}, Stan: {skladnik.stan}')
        return wyniki

    def inwentaryzacja(self):
        wymagane_skladniki = {
            'Krzesło': 'meble',
            'Biurko': 'meble',
            'Komputer': 'sprzet'
        }
        result = ""
        for sala in self.sale:
            result += f'Sala numer {sala.numer}:\n'
            obecne_skladniki = {skladnik.nazwa: skladnik for skladnik in sala.skladniki}
            brakujace_skladniki = [
                nazwa for nazwa, typ in wymagane_skladniki.items()
                if nazwa not in obecne_skladniki
            ]
            for skladnik in sala.skladniki:
                result += f'  {skladnik}\n'
            if brakujace_skladniki:
                result += f'  Brakujące składniki: {", ".join(brakujace_skladniki)}\n'
            else:
                result += '  Wszystkie wymagane składniki są obecne.\n'
        return result

    def zapisz_raport(self, nazwa_pliku):
        wymagane_skladniki = {
            'Krzesło': 'meble',
            'Biurko': 'meble',
            'Komputer': 'sprzet'
        }
        with open(nazwa_pliku, 'w') as plik:
            for sala in self.sale:
                plik.write(f'Sala numer {sala.numer}\n')
                obecne_skladniki = {skladnik.nazwa: skladnik for skladnik in sala.skladniki}
                brakujace_skladniki = [
                    nazwa for nazwa, typ in wymagane_skladniki.items()
                    if nazwa not in obecne_skladniki
                ]
                for skladnik in sala.skladniki:
                    plik.write(f'{skladnik.id}, {skladnik.nazwa}, {skladnik.stan}\n')
                if brakujace_skladniki:
                    plik.write(f'Brakujące składniki: {", ".join(brakujace_skladniki)}\n')
                else:
                    plik.write('Brakujące składniki: brak\n')
                plik.write('\n')

    def wczytaj_raport(self, nazwa_pliku):
        self.sale.clear()
        with open(nazwa_pliku, 'r') as plik:
            linie = plik.readlines()
        aktualna_sala = None
        for linia in linie:
            if linia.startswith('Sala numer'):
                numer_sali = int(linia.split()[2])
                aktualna_sala = Sala(numer_sali)
                self.sale.append(aktualna_sala)
            elif linia.startswith('Brakujące składniki:'):
                continue  # Ignore this line
            elif linia.strip():
                skladnik_id, nazwa, stan = linia.strip().split(', ')
                if aktualna_sala:
                    if 'sprzet' in nazwa.lower():
                        skladnik = Sprzet(nazwa, stan)
                    else:
                        skladnik = Meble(nazwa, stan)
                    skladnik.id = int(skladnik_id)
                    aktualna_sala.dodaj_skladnik(skladnik)

    def przenies_skladnik(self, numer_sali_z, numer_sali_do, skladnik_id):
        sala_z = None
        sala_do = None

        for sala in self.sale:
            if sala.numer == numer_sali_z:
                sala_z = sala
            if sala.numer == numer_sali_do:
                sala_do = sala

        if not sala_z or not sala_do:
            return "Jedna z sal nie istnieje."

        skladnik = None
        for s in sala_z.skladniki:
            if s.id == skladnik_id:
                skladnik = s
                break

        if not skladnik:
            return "Składnik nie istnieje w podanej sali."

        sala_z.usun_skladnik(skladnik_id)
        sala_do.dodaj_skladnik(skladnik)
        return "Składnik został przeniesiony."

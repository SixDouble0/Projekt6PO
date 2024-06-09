import customtkinter
from cfunction import Sala, System

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("800x850")

system = System()

def Clear_Window():
    for widget in root.winfo_children():
        widget.destroy()

def Okno_glowne():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    frame.pack_propagate(False)
    label = customtkinter.CTkLabel(master=frame, text="Budynek Uczelniany", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    ZarzadzanieSalami_button = customtkinter.CTkButton(master=frame, text="Zarządzanie salami", width=160, height=40, command=Zarzadzanie_Salami)
    ZarzadzanieSalami_button.pack(pady=12, padx=10)
    
    ZarzadanieSkladnikami_button = customtkinter.CTkButton(master=frame, text="Zarządzanie Składnikami", width=160, height=40, command=Zarzadzanie_Skladnikami)
    ZarzadanieSkladnikami_button.pack(pady=12, padx=10)

    Inwentaryzacja_button = customtkinter.CTkButton(master=frame, text="Inwentaryzacja", width=160, height=40, command=Inwentaryzacja)
    Inwentaryzacja_button.pack(pady=12, padx=10)

    Wyszukiwanie_Skladnikow_button = customtkinter.CTkButton(master=frame, text="Wyszukiwanie Składników", width=160, height=40, command=Wyszukiwanie_Skladnikow)
    Wyszukiwanie_Skladnikow_button.pack(pady=12, padx=10)

    Zapisz_Raport_button = customtkinter.CTkButton(master=frame, text="Zapisz Raport", width=160, height=40, command=Zapisz_Raport)
    Zapisz_Raport_button.pack(pady=12, padx=10)

    Wczytaj_Raport_button = customtkinter.CTkButton(master=frame, text="Wczytaj Raport", width=160, height=40, command=Wczytaj_Raport)
    Wczytaj_Raport_button.pack(pady=12, padx=10)

def Zarzadzanie_Salami():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Zarządzanie Salami", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    def Dodaj_Sale():
        Clear_Window()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Dodawanie Sal", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        numer_label = customtkinter.CTkLabel(master=frame, text="Numer sali:")
        numer_label.pack(pady=5, padx=10)
        numer_entry = customtkinter.CTkEntry(master=frame)
        numer_entry.pack(pady=5, padx=10)
        
        def submit():
            numer = numer_entry.get()
            if numer.isdigit():
                numer = int(numer)
                sala = Sala(numer)
                system.dodaj_sale(sala)
                success = customtkinter.CTkLabel(master=frame, text="Pomyslnie dodano sale.", text_color="green")
                success.pack(pady=5, padx=10)
            else:
                error = customtkinter.CTkLabel(master=frame, text="Błędny numer sali.", text_color="red")
                error.pack(pady=5, padx=10)
            
        submit_button = customtkinter.CTkButton(master=frame, text="Dodaj", command=submit)
        submit_button.pack(pady=12, padx=10)
        powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Zarzadzanie_Salami)
        powrot_button.pack(pady=12, padx=10)

    def Usun_sale():
        Clear_Window()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Usuwanie Sal", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        numer_label = customtkinter.CTkLabel(master=frame, text="Numer sali:")
        numer_label.pack(pady=5, padx=10)
        numer_entry = customtkinter.CTkEntry(master=frame)
        numer_entry.pack(pady=5, padx=10)

        def submit():
            numer = numer_entry.get()
            if numer.isdigit():
                numer = int(numer)
                system.usun_sale(numer)
                success = customtkinter.CTkLabel(master=frame, text="Pomyslnie usunięto sale.", text_color="green")
                success.pack(pady=5, padx=10)
            else:
                error = customtkinter.CTkLabel(master=frame, text="Błąd.", text_color="red")
                error.pack(pady=5, padx=10)
            
        submit_button = customtkinter.CTkButton(master=frame, text="Usuń", command=submit)
        submit_button.pack(pady=12, padx=10)
        powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Zarzadzanie_Salami)
        powrot_button.pack(pady=12, padx=10)

    def Przegladaj_Sale():
        Clear_Window()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Przegladanie Sal", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        sale_info = "\n".join(str(sala) for sala in system.sale)
        sale_label = customtkinter.CTkLabel(master=frame, text=sale_info)
        sale_label.pack(pady=12, padx=10)

        powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Zarzadzanie_Salami)
        powrot_button.pack(pady=12, padx=10)

    dodaj_button = customtkinter.CTkButton(master=frame, text="Dodaj Sale", width=160, height=40, command=Dodaj_Sale)
    dodaj_button.pack(pady=12, padx=10)
    usun_button = customtkinter.CTkButton(master=frame, text="Usuń Sale", width=160, height=40, command=Usun_sale)
    usun_button.pack(pady=12, padx=10)
    przegladaj_button = customtkinter.CTkButton(master=frame, text="Przegladaj Sale", width=160, height=40, command=Przegladaj_Sale)
    przegladaj_button.pack(pady=12, padx=10)
    powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Okno_glowne)
    powrot_button.pack(pady=12, padx=10)

def Zarzadzanie_Skladnikami():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="Zarządzanie Składnikami", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    def Dodaj_Skladnik():
        Clear_Window()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Dodawanie Składników", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        sala_label = customtkinter.CTkLabel(master=frame, text="Numer sali:")
        sala_label.pack(pady=5, padx=10)
        sala_entry = customtkinter.CTkEntry(master=frame)
        sala_entry.pack(pady=5, padx=10)

        typ_label = customtkinter.CTkLabel(master=frame, text="Typ składnika (sprzet/meble):")
        typ_label.pack(pady=5, padx=10)
        typ_entry = customtkinter.CTkEntry(master=frame)
        typ_entry.pack(pady=5, padx=10)

        nazwa_label = customtkinter.CTkLabel(master=frame, text="Nazwa składnika:")
        nazwa_label.pack(pady=5, padx=10)
        nazwa_entry = customtkinter.CTkEntry(master=frame)
        nazwa_entry.pack(pady=5, padx=10)

        stan_label = customtkinter.CTkLabel(master=frame, text="Stan składnika:")
        stan_label.pack(pady=5, padx=10)
        stan_entry = customtkinter.CTkEntry(master=frame)
        stan_entry.pack(pady=5, padx=10)
        
        def submit():
            numer_sali = sala_entry.get()
            typ = typ_entry.get()
            nazwa = nazwa_entry.get()
            stan = stan_entry.get()
            if numer_sali.isdigit() and typ in ["sprzet", "meble"] and nazwa and stan:
                numer_sali = int(numer_sali)
                system.dodaj_skladnik(numer_sali, typ, nazwa, stan)
                success = customtkinter.CTkLabel(master=frame, text="Pomyslnie dodano składnik.", text_color="green")
                success.pack(pady=5, padx=10)
            else:
                error = customtkinter.CTkLabel(master=frame, text="Błędne dane.", text_color="red")
                error.pack(pady=5, padx=10)
            
        submit_button = customtkinter.CTkButton(master=frame, text="Dodaj", command=submit)
        submit_button.pack(pady=12, padx=10)
        powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Zarzadzanie_Skladnikami)
        powrot_button.pack(pady=12, padx=10)

    def Usun_Skladnik():
        Clear_Window()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Usuwanie Składników", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        sala_label = customtkinter.CTkLabel(master=frame, text="Numer sali:")
        sala_label.pack(pady=5, padx=10)
        sala_entry = customtkinter.CTkEntry(master=frame)
        sala_entry.pack(pady=5, padx=10)

        skladnik_label = customtkinter.CTkLabel(master=frame, text="ID składnika:")
        skladnik_label.pack(pady=5, padx=10)
        skladnik_entry = customtkinter.CTkEntry(master=frame)
        skladnik_entry.pack(pady=5, padx=10)
        
        def submit():
            numer_sali = sala_entry.get()
            skladnik_id = skladnik_entry.get()
            if numer_sali.isdigit() and skladnik_id.isdigit():
                numer_sali = int(numer_sali)
                skladnik_id = int(skladnik_id)
                system.usun_skladnik(numer_sali, skladnik_id)
                success = customtkinter.CTkLabel(master=frame, text="Pomyslnie usunięto składnik.", text_color="green")
                success.pack(pady=5, padx=10)
            else:
                error = customtkinter.CTkLabel(master=frame, text="Błędne dane.", text_color="red")
                error.pack(pady=5, padx=10)
            
        submit_button = customtkinter.CTkButton(master=frame, text="Usuń", command=submit)
        submit_button.pack(pady=12, padx=10)
        powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Zarzadzanie_Skladnikami)
        powrot_button.pack(pady=12, padx=10)

    dodaj_button = customtkinter.CTkButton(master=frame, text="Dodaj Składnik", width=160, height=40, command=Dodaj_Skladnik)
    dodaj_button.pack(pady=12, padx=10)
    usun_button = customtkinter.CTkButton(master=frame, text="Usuń Składnik", width=160, height=40, command=Usun_Skladnik)
    usun_button.pack(pady=12, padx=10)
    powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Okno_glowne)
    powrot_button.pack(pady=12, padx=10)

def Inwentaryzacja():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="Inwentaryzacja", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    inwentaryzacja_info = system.inwentaryzacja()
    inwentaryzacja_label = customtkinter.CTkLabel(master=frame, text=inwentaryzacja_info)
    inwentaryzacja_label.pack(pady=12, padx=10)

    powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Okno_glowne)
    powrot_button.pack(pady=12, padx=10)

def Wyszukiwanie_Skladnikow():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="Wyszukiwanie Składników", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    nazwa_label = customtkinter.CTkLabel(master=frame, text="Nazwa składnika:")
    nazwa_label.pack(pady=5, padx=10)
    nazwa_entry = customtkinter.CTkEntry(master=frame)
    nazwa_entry.pack(pady=5, padx=10)
        
    def submit():
        nazwa_skladnika = nazwa_entry.get()
        if nazwa_skladnika:
            wyniki = system.wyszukaj_skladnik(nazwa_skladnika)
            wynik_info = "\n".join(wyniki)
            wynik_label = customtkinter.CTkLabel(master=frame, text=wynik_info)
            wynik_label.pack(pady=12, padx=10)
        else:
            error = customtkinter.CTkLabel(master=frame, text="Wpisz nazwe skladnika.", text_color="red")
            error.pack(pady=5, padx=10)
            
    submit_button = customtkinter.CTkButton(master=frame, text="Szukaj", command=submit)
    submit_button.pack(pady=12, padx=10)
    powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Okno_glowne)
    powrot_button.pack(pady=12, padx=10)


def Zapisz_Raport():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="Zapisz Raport", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    plik_label = customtkinter.CTkLabel(master=frame, text="Nazwa pliku:")
    plik_label.pack(pady=5, padx=10)
    plik_entry = customtkinter.CTkEntry(master=frame)
    plik_entry.pack(pady=5, padx=10)

    def submit():
        nazwa_pliku = plik_entry.get()
        if nazwa_pliku:
            system.zapisz_raport(nazwa_pliku)
            success = customtkinter.CTkLabel(master=frame, text="Raport zapisany pomyślnie.", text_color="green")
            success.pack(pady=5, padx=10)
        else:
            error = customtkinter.CTkLabel(master=frame, text="Podaj nazwę pliku.", text_color="red")
            error.pack(pady=5, padx=10)

    submit_button = customtkinter.CTkButton(master=frame, text="Zapisz", command=submit)
    submit_button.pack(pady=12, padx=10)
    powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Okno_glowne)
    powrot_button.pack(pady=12, padx=10)
def Wczytaj_Raport():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="Wczytaj Raport", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    plik_label = customtkinter.CTkLabel(master=frame, text="Nazwa pliku:")
    plik_label.pack(pady=5, padx=10)
    plik_entry = customtkinter.CTkEntry(master=frame)
    plik_entry.pack(pady=5, padx=10)

    def submit():
        nazwa_pliku = plik_entry.get()
        if nazwa_pliku:
            try:
                system.wczytaj_raport(nazwa_pliku)
                success = customtkinter.CTkLabel(master=frame, text="Raport wczytany pomyślnie.", text_color="green")
                success.pack(pady=5, padx=10)
            except Exception as e:
                error = customtkinter.CTkLabel(master=frame, text=f"Błąd: {str(e)}", text_color="red")
                error.pack(pady=5, padx=10)
        else:
            error = customtkinter.CTkLabel(master=frame, text="Podaj nazwę pliku.", text_color="red")
            error.pack(pady=5, padx=10)

    submit_button = customtkinter.CTkButton(master=frame, text="Wczytaj", command=submit)
    submit_button.pack(pady=12, padx=10)
    powrot_button = customtkinter.CTkButton(master=frame, fg_color="red", text="Wróć", command=Okno_glowne)
    powrot_button.pack(pady=12, padx=10)
Okno_glowne()
root.mainloop()

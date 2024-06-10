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
        numer_sali_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Numer sali")
        numer_sali_entry.pack(pady=12, padx=10)

        def Dodaj():
            numer = numer_sali_entry.get()
            if numer.isdigit():
                sala = Sala(int(numer))
                system.dodaj_sale(sala)
                customtkinter.CTkLabel(master=frame,text_color="green", text=f"Sala {numer} została dodana.", font=("Roboto", 16)).pack(pady=8, padx=8)
            else:
                customtkinter.CTkLabel(master=frame,text_color="red", text="Błąd", font=("Roboto", 16)).pack(pady=8, padx=8)
        dodaj_button = customtkinter.CTkButton(master=frame, text="Dodaj", width=120, height=40, command=Dodaj)
        dodaj_button.pack(pady=12, padx=10)

        back_button = customtkinter.CTkButton(master=frame,fg_color="red", text="Wróć", width=120, height=40, command=Zarzadzanie_Salami)
        back_button.pack(pady=12, padx=10)

    def Usun_Sale():
        Clear_Window()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Usuwanie Sal", font=("Roboto", 24))
        label.pack(pady=12, padx=10)
        numer_sali_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Numer sali")
        numer_sali_entry.pack(pady=12, padx=10)

        def Usun():
            try:
                numer = numer_sali_entry.get()
                if numer.isdigit():
                    system.usun_sale(int(numer))
                    customtkinter.CTkLabel(master=frame, text_color="green",text=f"Sala {numer} została usunięta.", font=("Roboto", 16)).pack(pady=12, padx=10)
            except Exception as e:
                customtkinter.CTkLabel(master=frame,text_color="green", text=e, font=("Roboto", 16)).pack(pady=8, padx=8)
        usun_button = customtkinter.CTkButton(master=frame, text="Usuń", width=120, height=40, command=Usun)
        usun_button.pack(pady=12, padx=10)

        back_button = customtkinter.CTkButton(master=frame, text="Wróć",fg_color="red", width=120, height=40, command=Zarzadzanie_Salami)
        back_button.pack(pady=12, padx=10)

    dodaj_sala_button = customtkinter.CTkButton(master=frame, text="Dodaj Salę", width=160, height=40, command=Dodaj_Sale)
    dodaj_sala_button.pack(pady=12, padx=10)
    
    usun_sala_button = customtkinter.CTkButton(master=frame, text="Usuń Salę", width=160, height=40, command=Usun_Sale)
    usun_sala_button.pack(pady=12, padx=10)
    
    back_button = customtkinter.CTkButton(master=frame, text="Wróć",fg_color="red", width=160, height=40, command=Okno_glowne)
    back_button.pack(pady=12, padx=10)

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

        numer_sali_entry = customtkinter.CTkEntry(master=frame,height=50,width=200, placeholder_text="Numer sali")
        numer_sali_entry.pack(pady=12, padx=10)
        typ_skladnika_entry = customtkinter.CTkEntry(master=frame, height=50,width=200,placeholder_text="Typ składnika (sprzet/meble)")
        typ_skladnika_entry.pack(pady=12, padx=10)
        nazwa_skladnika_entry = customtkinter.CTkEntry(master=frame,height=50,width=200, placeholder_text="Nazwa składnika")
        nazwa_skladnika_entry.pack(pady=12, padx=10)
        stan_skladnika_entry = customtkinter.CTkEntry(master=frame,height=50,width=200, placeholder_text="Stan składnika")
        stan_skladnika_entry.pack(pady=12, padx=10)

        def Dodaj():
            try:
                numer_sali = numer_sali_entry.get()
                typ_skladnika = typ_skladnika_entry.get()
                nazwa_skladnika = nazwa_skladnika_entry.get()
                stan_skladnika = stan_skladnika_entry.get()
                if numer_sali.isdigit() and typ_skladnika and nazwa_skladnika and stan_skladnika:
                    system.dodaj_skladnik(int(numer_sali), typ_skladnika, nazwa_skladnika, stan_skladnika)
                    customtkinter.CTkLabel(master=frame, text_color="green", text="Składnik został dodany.", font=("Roboto", 16)).pack(pady=12, padx=10)
            except Exception as e:
                customtkinter.CTkLabel(master=frame,text_color="red", text=e, font=("Roboto", 16)).pack(pady=8, padx=8)

        dodaj_button = customtkinter.CTkButton(master=frame, text="Dodaj", width=120, height=40, command=Dodaj)
        dodaj_button.pack(pady=12, padx=10)

        back_button = customtkinter.CTkButton(master=frame, text="Wróć", width=120, height=40,fg_color="red", command=Zarzadzanie_Skladnikami)
        back_button.pack(pady=12, padx=10)

    def Usun_Skladnik():
        Clear_Window()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Usuwanie Składników", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        numer_sali_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Numer sali")
        numer_sali_entry.pack(pady=12, padx=10)
        skladnik_id_entry = customtkinter.CTkEntry(master=frame, placeholder_text="ID składnika")
        skladnik_id_entry.pack(pady=12, padx=10)

        def Usun():
            try:
                numer_sali = numer_sali_entry.get()
                skladnik_id = skladnik_id_entry.get()
                if numer_sali.isdigit() and skladnik_id.isdigit():
                    system.usun_skladnik(int(numer_sali), int(skladnik_id))
                    customtkinter.CTkLabel(master=frame,text_color="green", text=f"Składnik {skladnik_id} został usunięty z sali {numer_sali}.", font=("Roboto", 16)).pack(pady=12, padx=10)
            except Exception as e:
                customtkinter.CTkLabel(master=frame,text_color="red", text=e, font=("Roboto", 16)).pack(pady=8, padx=8)
        usun_button = customtkinter.CTkButton(master=frame, text="Usuń", width=120, height=40, command=Usun)
        usun_button.pack(pady=12, padx=10)

        back_button = customtkinter.CTkButton(master=frame, text="Wróć", fg_color="red",width=120, height=40, command=Zarzadzanie_Skladnikami)
        back_button.pack(pady=12, padx=10)

    def Przenies_Skladnik():
        Clear_Window()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Przenoszenie Składników", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        numer_sali_z_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Numer sali źródłowej")
        numer_sali_z_entry.pack(pady=12, padx=10)
        numer_sali_do_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Numer sali docelowej")
        numer_sali_do_entry.pack(pady=12, padx=10)
        skladnik_id_entry = customtkinter.CTkEntry(master=frame, placeholder_text="ID składnika")
        skladnik_id_entry.pack(pady=12, padx=10)

        def Przenies():
            try:
                numer_sali_z = numer_sali_z_entry.get()
                numer_sali_do = numer_sali_do_entry.get()
                skladnik_id = skladnik_id_entry.get()
                
                if numer_sali_z.isdigit() and numer_sali_do.isdigit() and skladnik_id.isdigit():
                    wynik = system.przenies_skladnik(int(numer_sali_z), int(numer_sali_do), int(skladnik_id))
                    customtkinter.CTkLabel(master=frame, text_color="green",text=wynik, font=("Roboto", 16)).pack(pady=12, padx=10)
            except Exception as e:
                customtkinter.CTkLabel(master=frame,text_color="red", text=e, font=("Roboto", 16)).pack(pady=8, padx=8)
        
        przenies_button = customtkinter.CTkButton(master=frame, text="Przenieś", width=120, height=40, command=Przenies)
        przenies_button.pack(pady=12, padx=10)

        back_button = customtkinter.CTkButton(master=frame, text="Wróć", fg_color="red",width=120, height=40, command=Zarzadzanie_Skladnikami)
        back_button.pack(pady=12, padx=10)

    dodaj_skladnik_button = customtkinter.CTkButton(master=frame, text="Dodaj Składnik", width=160, height=40, command=Dodaj_Skladnik)
    dodaj_skladnik_button.pack(pady=12, padx=10)
    
    usun_skladnik_button = customtkinter.CTkButton(master=frame, text="Usuń Składnik", width=160, height=40, command=Usun_Skladnik)
    usun_skladnik_button.pack(pady=12, padx=10)
    
    przenies_skladnik_button = customtkinter.CTkButton(master=frame, text="Przenieś Składnik", width=160, height=40, command=Przenies_Skladnik)
    przenies_skladnik_button.pack(pady=12, padx=10)

    back_button = customtkinter.CTkButton(master=frame, text="Wróć", fg_color="red",width=160, height=40, command=Okno_glowne)
    back_button.pack(pady=12, padx=10)
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



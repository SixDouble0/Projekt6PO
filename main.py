import customtkinter
import Function

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")




def Clear_Window():
    for widget in root.winfo_children():
        widget.destroy()


def Okno_glowne():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill = "both", expand=True)
    frame.pack_propagate(False)
    label = customtkinter.CTkLabel(master=frame, text="Budynek Uczelniany",font=("Roboto",24))
    label.pack(pady=12,padx=10)


    ZarzadzanieSalami_button = customtkinter.CTkButton(master=frame, text="Zarządzanie salami", width=160,height=40,command=Zarzadzanie_Salami)
    ZarzadzanieSalami_button.pack(pady=12, padx=10)
    


    ZarzadanieSkladnikami_button = customtkinter.CTkButton(master=frame,text="Zarzadanie Składnikami",width=160,height=40,command=Zarzadzanie_Skladnikami)
    ZarzadanieSkladnikami_button.pack(pady=12,padx=10)

    Inwentaryzacja_button = customtkinter.CTkButton(master=frame, text="Inwentaryzacja",width=160,height=40,command=Inwentaryzacja)
    Inwentaryzacja_button.pack(pady=12,padx=10)

    Wyszukiwanie_Skladnikow_button = customtkinter.CTkButton(master=frame, text= "Wyszkiwanie Składników",width=160,height=40,command = Wyszukiwanie_Skladnikow)
    Wyszukiwanie_Skladnikow_button.pack(pady=12,padx=10)

def Zarzadzanie_Salami():
    #print("dziala")
    
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20,padx=60,fill="both",expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Zarządzanie Salami",font = ("Roboto",24))
    label.pack(pady=12,padx=10)

    #Dodawanie_Sal_button = customtkinter.CTkButton(master=frame, text="Dodaj Sale",font=("Roboto",12))
    #Dodawanie_Sal_button.pack(pady=12,padx=10)


    Wroc_button = customtkinter.CTkButton(master=frame, text="Wróc",command=Okno_glowne)
    Wroc_button.pack(pady=12,padx=10)

def Zarzadzanie_Skladnikami():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20,padx=60,fill="both",expand=True)

    label = customtkinter.CTkLabel(master=frame,text="Zarządzanie Składników",font=("Roboto",24))
    label.pack(pady=12,padx=10)

    Wroc_button = customtkinter.CTkButton(master=frame, text="Wróc",command=Okno_glowne)
    Wroc_button.pack(pady=12,padx=10)

def Inwentaryzacja():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=30,padx=30,fill="both",expand=True)

    label = customtkinter.CTkLabel(master=frame,text="Inwentaryzacja",font=("Roboto",24))
    label.pack(pady=12,padx=10)
        
    
    Wroc_button = customtkinter.CTkButton(master=frame, text="Wróc",command=Okno_glowne)
    Wroc_button.pack(pady=12,padx=10)

def Wyszukiwanie_Skladnikow():
    Clear_Window()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20,padx=60,fill="both",expand=True)
    
    label = customtkinter.CTkLabel(master=frame,text="Wyszukiwanie Składników",font=("Roboto",24))
    label.pack(pady=12,padx=10)

    Wroc_button = customtkinter.CTkButton(master=frame, text="Wróc",command=Okno_glowne)
    Wroc_button.pack(pady=12,padx=10)

Okno_glowne()
root.mainloop()
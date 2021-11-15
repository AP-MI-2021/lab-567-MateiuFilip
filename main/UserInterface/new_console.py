from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, modifica_obiect, sterge_obiect
from UserInterface.console import show_all


def menu(lista):
    while True:
        comanda = input("Introduceti comanda: ")
        optiuni = comanda.split(";")
        if comanda == "help":
            print("Add, id, nume, descriere, pret, locatie: adauga obiect")
            print("Delete, id: sterge obiect")
            print("Update, id: modifica obiect")
            print("Showall: afiseaza toate obiectele")
            print("Exit: opreste programul")
        elif optiuni[0] == "Exit":
                break
        else:
            for optiune in optiuni:
                functie = optiune.split(",")
                if functie[0] == "Add":
                    lista = adauga_obiect(functie[1], functie[2], functie[3], functie[4], functie[5], lista)
                elif functie[0] == "Showall":
                    show_all(lista)
                elif functie[0] == "Update":
                    lista = modifica_obiect(functie[1], functie[2], functie[3], functie[4], functie[5], lista)
                elif functie[0] == "Delete":
                    lista = sterge_obiect(functie[1], lista)
                else:
                    print("Optiune gresita. Utilizati comanda 'Help'!")

from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, modifica_obiect, sterge_obiect
from UserInterface.console import show_all


def menu(lista):
    while True:
        comanda = input()
        if comanda == "help":
            print("Adauga, id, nume, descriere, pret, locatie: adauga obiect")
            print("Sterge, id: sterge obiect")
            print("Update, id: modifica obiect")
            print("Afisare: afiseaza toate obiectele")
            print("Iesire: opreste programul")
        else:
            optiuni = comanda.split(";")
            if optiuni[0] == "Iesire":
                break
            else:
                for optiune in optiuni:
                    functie = optiune.split(",")
                    if functie[0] == "Adauga":
                        lista = adauga_obiect(functie[1], functie[2], functie[3], functie[4], functie[5], lista)
                    elif functie[0] == "Afisare":
                        show_all(lista)
                    elif functie[0] == "Update":
                        lista = modifica_obiect(functie[1], functie[2], functie[3], functie[4], functie[5], lista)
                    elif functie[0] == "Sterge":
                        lista = sterge_obiect(functie[1], lista)
                    else:
                        print("Optiune gresita. Utilizati comanda 'help'!")

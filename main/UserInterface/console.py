from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect


def print_menu():
    print("1.Adaugare obiect.")
    print("2.Stergere obiect.")
    print("3.Modificare obiect.")
    print("4.Afisare obiecte.")
    print("5.Modificare locatia obiectelor.")
    print("-1.Iesire")


def ui_adaugare_obiect(lista):
    id = input("Dati id: ")
    nume = input("Dati nume: ")
    descriere = input("Dati descriere: ")
    pret = float(input("Dati pret: "))
    locatie = input("Dati locatie: ")
    return adauga_obiect(id, nume, descriere, pret, locatie, lista)

def ui_stergere_obiect(lista):
    id = input("Dati id-ul obiectului de sters: ")
    return sterge_obiect(id,lista)

def ui_modifica_obiect(lista):
    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input("Dati noul pret: "))
    locatie = input("Dati noua locatie: ")
    return modifica_obiect(id, nume, descriere, pret, locatie, lista)


def show_all(lista):
    '''
    :param lista: lista
    :return: afiseaza obiectele din lista
    '''
    for obiect in lista:
        print(toString(obiect))


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Alegeti optiune: ")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista)
        elif optiune == "4":
            show_all(lista)
        elif optiune == "-1":
            break
        else:
            print("Optiune gresita. Reincercati: ")




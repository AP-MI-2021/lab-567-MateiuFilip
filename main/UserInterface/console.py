from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.functionalitati import modifica_locatii, obiecte_mai_scumpe_decat_valoare, pret_maxim_per_locatie, \
    ordonare_dupa_pret, suma_preturi_locatie


def print_menu():
    print("1.Adaugare obiect.")
    print("2.Stergere obiect.")
    print("3.Modificare obiect.")
    print("4.Afisare obiecte.")
    print("5.Modificare locatia obiectelor.")
    print("6.Concatenarea unui string descrierile obiectelor cu prețul mai mare decât o valoare")
    print("7.Determinarea celui mai mare preț pentru fiecare locație")
    print("8.Ordonarea obiectelor crescător după prețul de achiziție.")
    print("9.Afișarea sumelor prețurilor pentru fiecare locație.")
    print("u.Undo.")
    print("r.Redo.")
    print("-1.Iesire")


def ui_adaugare_obiect(lista, undo_list, redo_lista):
    try:
        id = input("Dati id: ")
        nume = input("Dati nume: ")
        descriere = input("Dati descriere: ")
        pret = float(input("Dati pret: "))
        locatie = input("Dati locatie: ")
        rezultat = adauga_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_lista.clear()
        return rezultat

    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_stergere_obiect(lista, undo_list, redo_lista):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        rezultat = sterge_obiect(id, lista)
        undo_list.append(lista)
        redo_lista.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare; {}".format(ve))
        return lista


def ui_modifica_obiect(lista, undo_list, redo_lista):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret: "))
        locatie = input("Dati noua locatie: ")
        rezultat = modifica_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_lista.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    '''
    :param lista: lista
    :return: afiseaza obiectele din lista
    '''
    for obiect in lista:
        print(toString(obiect))


def ui_modifica_locatii(lista, undo_list, redo_list):
    try:
        locatie = input("Dati locatia curenta a obiectelor: ")
        locatie_noua = input("Dati noua locatie a obiectelor: ")
        rezultat= modifica_locatii(locatie,locatie_noua,lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_obiecte_mai_scumpe_decat_valoare(lista,undo_list,redo_list):
    try:
        pret = float(input("Dati valoarea cu care se compara preturile: "))
        string = input("Dati string-ul de concatenat: ")
        rezultat = obiecte_mai_scumpe_decat_valoare(pret, lista, string)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_pret_maxim_per_locatie(lista):
    rezultat = pret_maxim_per_locatie(lista)
    for locatie in rezultat:
        print("In locatia {} pretul cel mai mare este {}.".format(locatie, rezultat[locatie]))


def ui_ordonare_dupa_pret(lista):
    show_all(ordonare_dupa_pret(lista))


def ui_suma_preturi_locatie(lista):
    rezultat = suma_preturi_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma totala de preturi de {}".format(locatie, rezultat[locatie]))


def run_menu(lista):
    undo_lista = []
    redo_lista = []
    while True:
        print_menu()
        optiune = input("Alegeti optiune: ")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista, undo_lista, redo_lista)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista, undo_lista, redo_lista)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista, undo_lista, redo_lista)
        elif optiune == "4":
            show_all(lista)
        elif optiune == "5":
            lista = ui_modifica_locatii(lista,undo_lista,redo_lista)
        elif optiune == "6":
            lista = ui_obiecte_mai_scumpe_decat_valoare(lista,undo_lista,redo_lista)
        elif optiune == "7":
            ui_pret_maxim_per_locatie(lista)
        elif optiune == "8":
            ui_ordonare_dupa_pret(lista)
        elif optiune == "9":
            ui_suma_preturi_locatie(lista)
        elif optiune == "u":
            if len(undo_lista) > 0:
                redo_lista.append(lista)
                lista = undo_lista.pop()
            else:
                print("Nu se poate executa 'undo'!")
        elif optiune == "r":
            if len(redo_lista) > 0:
                undo_lista.append(lista)
                lista = redo_lista.pop()
            else:
                print("Nu se poate executa functia 'redo'!")
        elif optiune == "-1":
            break
        else:
            print("Optiune gresita. Reincercati: ")

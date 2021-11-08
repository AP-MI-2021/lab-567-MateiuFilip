from Domain.obiect import getId, getLocatie, getDescriere
from Logic.CRUD import adauga_obiect
from Logic.functionalitati import modifica_locatii, pret_maxim_per_locatie, obiecte_mai_scumpe_decat_valoare, \
    ordonare_dupa_pret, suma_preturi_locatie


def test_modifica_locatii():
    lista = []
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Londra", lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Paris", lista)

    lista = modifica_locatii("Londra", "Dublin", lista)
    lista = modifica_locatii("Paris", "Berlin", lista)
    assert getLocatie(lista[0]) == "Dublin"
    assert getLocatie(lista[1]) == "Berlin"


def test_obiecte_mai_scumpe_decat_valoare():
    lista = []
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Londra", lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Paris", lista)
    lista = adauga_obiect("3", "caciula", "sport", 70, "Londra", lista)

    rezultat = obiecte_mai_scumpe_decat_valoare(10, lista, ".")
    assert getDescriere(rezultat[0]) == "minge de fotbal."
    assert getDescriere(rezultat[1]) == "minge de tenis"
    assert getDescriere(rezultat[2]) == "sport."


def test_pret_maxim_per_locatie():
    lista = []
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Londra", lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Paris", lista)
    lista = adauga_obiect("3", "caciula", "sport", 70, "Londra", lista)

    rezultat = pret_maxim_per_locatie(lista)

    assert len(rezultat) == 2
    assert rezultat["Londra"] == 120
    assert rezultat["Paris"] == 6


def test_ordonare_dupa_pret():
    lista = []
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Londra", lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Paris", lista)
    lista = adauga_obiect("3", "caciula", "sport", 70, "Londra", lista)

    rezultat = ordonare_dupa_pret(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "1"

def test_suma_preturi_locatie():
    lista = []
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Londra", lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Paris", lista)
    lista = adauga_obiect("3", "caciula", "sport", 70, "Londra", lista)

    rezultat=suma_preturi_locatie(lista)

    assert len(rezultat) == 2
    assert rezultat["Paris"] == 6
    assert rezultat["Londra"] == 190
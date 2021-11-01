from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adauga_obiect, sterge_obiect, getById, modifica_obiect


def test_adauga_obiecte():
    lista = []
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Londra",lista)
    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "minge"
    assert getDescriere(lista[0]) == "minge de fotbal"
    assert getPret(lista[0]) == 120
    assert getLocatie(lista[0]) == "Londra"

def test_sterge_obiect():
    lista=[]
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Londra",lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Paris",lista)

    lista= sterge_obiect("1",lista)
    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None


def test_modifica_obiect():
    lista=[]
    lista=adauga_obiect("1","zacusca","ciuperci","0","Nicolae Balcescu,Bacau",lista)
    lista=adauga_obiect("2","unt de arahide","Nutline","11","Oradea",lista)

    lista=modifica_obiect("1","cuptor","cu microunde",180,"Bucuresti",lista)

    assert getId(lista[0])== "1"
    assert getNume(lista[0]) == "cuptor"
    assert getDescriere(lista[0]) == "cu microunde"
    assert getPret(lista[0]) == 180
    assert getLocatie(lista[0]) == "Bucuresti"

    lista=modifica_obiect("2","rosii","Romania",5,"Iasi",lista)
    assert getId(lista[1])== "2"
    assert getNume(lista[1]) == "rosii"
    assert getDescriere(lista[1]) == "Romania"
    assert getPret(lista[1]) == 5
    assert getLocatie(lista[1]) == "Iasi"


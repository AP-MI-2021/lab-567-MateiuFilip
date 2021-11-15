from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adauga_obiect, sterge_obiect, getById, modifica_obiect


def test_adauga_obiecte():
    lista = []
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Cora",lista)
    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "minge"
    assert getDescriere(lista[0]) == "minge de fotbal"
    assert getPret(lista[0]) == 120
    assert getLocatie(lista[0]) == "Cora"

def test_sterge_obiect():
    lista=[]
    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Cora",lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Lidl",lista)

    lista= sterge_obiect("1",lista)
    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None


def test_modifica_obiect():
    lista=[]
    lista=adauga_obiect("1","zacusca","ciuperci","0","NBBC",lista)
    lista=adauga_obiect("2","unt de arahide","Nutline","11","Arad",lista)

    lista=modifica_obiect("1","cuptor","cu microunde",180,"Mall",lista)

    assert getId(lista[0])== "1"
    assert getNume(lista[0]) == "cuptor"
    assert getDescriere(lista[0]) == "cu microunde"
    assert getPret(lista[0]) == 180
    assert getLocatie(lista[0]) == "Mall"

    lista=modifica_obiect("2","rosii","Romania",5,"Iasi",lista)
    assert getId(lista[1])== "2"
    assert getNume(lista[1]) == "rosii"
    assert getDescriere(lista[1]) == "Romania"
    assert getPret(lista[1]) == 5
    assert getLocatie(lista[1]) == "Iasi"


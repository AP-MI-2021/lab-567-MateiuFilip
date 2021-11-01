from Domain.obiect import creeaza_obiect, getId


def adauga_obiect(id, nume, descriere, pret, locatie, lista):
    '''
    Adauga un obiect nou in lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: list
    :return: lista dupa adaugarea obiectului
    '''
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def getById(id,lista):
    '''
    :param id: string
    :param lista: list
    :return: obiectul cu id-ul introdus
    '''
    for obiect in lista:
        if getId(obiect) == id:
            return obiect
    return None

def sterge_obiect(id,lista):
    '''

    :param id: string
    :param lista: list
    :return: lista dupa stergerea obiectului
    '''
    return [obiect for obiect in lista if getId(obiect)  != id]

def modifica_obiect(id,nume,descriere,pret,locatie,lista):
    '''

    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: list
    :return: lista dupa modificare
    '''
    lista_noua=[]
    for obiect in lista:
        if getId(obiect) == id:
            obiect_nou=creeaza_obiect(id,nume,descriere,pret,locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


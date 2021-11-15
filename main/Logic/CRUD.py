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
    if getById(id,lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if len(locatie) != 4:
        raise ValueError("Locatia trebuie sa aiba 4 cifre!")
    if descriere is None:
        raise ValueError("Descrierea nu poate fi nenula!")
    if float(pret) < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    if nume is None:
        raise ValueError("Obiectul nu are nume!")
    if id is None:
        raise ValueError("Id-ul nu poate fi nul!")
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
    if getById(id, lista) is None:
        raise ValueError("Id-ul nu exista")
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
    if getById(id, lista) is None:
        raise ValueError("Id-ul nu exista")
    lista_noua=[]
    for obiect in lista:
        if getId(obiect) == id:
            if len(locatie) != 4:
                raise ValueError("Locatia trebuie sa aiba 4 cifre!")
            if descriere is None:
                raise ValueError("Descrierea nu poate fi nenula!")
            if float(pret) < 0:
                raise ValueError("Pretul nu poate fi negativ!")
            if nume is None:
                raise ValueError("Obiectul nu are nume!")
            obiect_nou=creeaza_obiect(id,nume,descriere,pret,locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


from Domain.obiect import getNume, creeaza_obiect, getLocatie, getPret, getId, getDescriere


def modifica_locatii(locatie, locatie_noua, lista):
    '''
    transfera obiectele dintr-o locatie intr-o locatie noua
    :param locatie: string
    :param locatie_noua: string
    :param lista: list
    :return: lista actualizata cu obiectele modificate
    '''
    lista_noua = []
    for obiect in lista:
        if len(locatie) != 4:
            raise ValueError("Locatia trebuie sa aiba 4 cifre!")
        if getLocatie(obiect) == locatie:
            obiect[4] = locatie_noua
            lista_noua.append(obiect)
        else:
            lista_noua.append(obiect)
    return lista_noua


def obiecte_mai_scumpe_decat_valoare(pret, lista, string):
    '''
    concateneaza un string in descrierea obiectelor cu pretul mai mare decat un float dat
    :param pret: float
    :param lista: list
    :param string: string
    :return: lista actualizata cu obiectele modificate
    '''
    lista_noua = []
    for obiect in lista:
        if getPret(obiect) > pret:
            obiect_nou = creeaza_obiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect) + string,
                getPret(obiect),
                getLocatie(obiect)

            )
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def pret_maxim_per_locatie(lista):
    '''
    :param lista: list
    :return: pretul cel mai mare din fiecare locatie din lista
    '''
    rezultat = {}
    for obiect in lista:
        pret = getPret(obiect)
        locatie = getLocatie(obiect)
        if locatie in rezultat:
            if pret > rezultat[locatie]:
                rezultat[locatie] = pret
        else:
            rezultat[locatie] = pret
    return rezultat


def ordonare_dupa_pret(lista):
    '''

    :param lista: list
    :return: lista ordonata crescator dupa pret
    '''
    return sorted(lista, key=lambda obiect: getPret(obiect))

def suma_preturi_locatie(lista):
    '''

    :param lista: list
    :return: suma preturilor obiectelor din fiecare locatie
    '''
    rezultat={}
    for obiect in lista:
        locatie=getLocatie(obiect)
        if locatie in rezultat:
            rezultat[locatie] += getPret(obiect)
        else:
            rezultat[locatie] = getPret(obiect)

    return rezultat







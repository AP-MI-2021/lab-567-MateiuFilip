from Domain.obiect import getNume, creeaza_obiect, getLocatie, getPret, getId, getDescriere


def modifica_locatii(locatie, locatie_noua, lista):
    lista_noua = []
    for obiect in lista:
        if getLocatie(obiect) == locatie:
            obiect[4] = locatie_noua
            lista_noua.append(obiect)
        else:
            lista_noua.append(obiect)
    return lista_noua


def obiecte_mai_scumpe_decat_valoare(pret, lista, string):
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
    return sorted(lista, key=lambda obiect: getPret(obiect))

def suma_preturi_locatie(lista):
    rezultat={}
    for obiect in lista:
        locatie=getLocatie(obiect)
        if locatie in rezultat:
            rezultat[locatie] += getPret(obiect)
        else:
            rezultat[locatie] = getPret(obiect)

    return rezultat







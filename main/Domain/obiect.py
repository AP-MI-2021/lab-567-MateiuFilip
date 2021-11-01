def creeaza_obiect(id,nume,descriere,pret,locatie):
    '''
    creeaza o lista pentru obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: lista obiectului
    '''
    return [id,nume,descriere,pret,locatie]

def getId(obiect):
    return obiect[0]

def getNume(obiect):
    return obiect[1]

def getDescriere(obiect):
     return obiect[2]

def getPret(obiect):
    return obiect[3]

def getLocatie(obiect):
    return obiect[4]

def toString(obiect):
    '''

    :return: obiectul sub forma de string
    '''
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )
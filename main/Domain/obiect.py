def creeaza_obiect(id,nume,descriere,pret,locatie):
    '''
    creeaza un dictionar pentru obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: dictionarul obiectului
    '''
    return{
        "id":id,
        "nume":nume,
        "descriere":descriere,
        "pret":pret,
        "locatie":locatie
    }

def getId(obiect):
    return obiect["id"]

def getNume(obiect):
    return obiect["nume"]

def getDescriere(obiect):
     return obiect["descriere"]

def getPret(obiect):
    return obiect["pret"]

def getLocatie(obiect):
    return obiect["locatie"]

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
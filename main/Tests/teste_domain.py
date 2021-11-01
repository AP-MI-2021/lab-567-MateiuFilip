from Domain.obiect import creeaza_obiect, getId, getNume, getDescriere, getPret, getLocatie


def test_obiect():
    obiect = creeaza_obiect("1", "Lapte", "1,5% grasime", 5, "Sibiu")
    assert getId(obiect) == "1"
    assert getNume(obiect) == "Lapte"
    assert getDescriere(obiect) == "1,5% grasime"
    assert getPret(obiect) == 5
    assert getLocatie(obiect) == "Sibiu"

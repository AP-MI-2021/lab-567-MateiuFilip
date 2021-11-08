from Tests.test_crud import test_adauga_obiecte, test_sterge_obiect, test_modifica_obiect
from Tests.teste_domain import test_obiect
from Tests.teste_functionalitati import test_modifica_locatii, test_obiecte_mai_scumpe_decat_valoare, \
    test_pret_maxim_per_locatie, test_ordonare_dupa_pret, test_suma_preturi_locatie


def test_all():
    test_obiect()
    test_adauga_obiecte()
    test_sterge_obiect()
    test_modifica_obiect()
    test_modifica_locatii()
    test_obiecte_mai_scumpe_decat_valoare()
    test_pret_maxim_per_locatie()
    test_ordonare_dupa_pret()
    test_suma_preturi_locatie()
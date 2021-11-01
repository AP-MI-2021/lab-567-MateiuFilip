from Tests.test_crud import test_adauga_obiecte, test_sterge_obiect, test_modifica_obiect
from Tests.teste_domain import test_obiect


def test_all():
    test_obiect()
    test_adauga_obiecte()
    test_sterge_obiect()
    test_modifica_obiect()
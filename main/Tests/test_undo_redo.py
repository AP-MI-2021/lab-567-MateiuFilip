from Logic.CRUD import adauga_obiect


def test_undo_redo():
    lista = []
    undo_lista = []
    redo_lista = []

    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Cora", lista)
    undo_lista.append(lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Lidl", lista)
    undo_lista.append(lista)
    lista = adauga_obiect("3", "iaurt", "grecesc", 7, "Real", lista)
    undo_lista.append(lista)

    assert len(lista) == 3
    assert len(undo_lista) == 3

    undo_lista.pop()
    redo_lista.append(lista)

    assert len(undo_lista) == 2
    assert len(redo_lista) == 1

    undo_lista.pop()
    redo_lista.append(lista)

    assert len(undo_lista) == 1
    assert len(redo_lista) == 2

    undo_lista.pop()
    redo_lista.append(lista)

    assert len(undo_lista) == 0
    assert len(redo_lista) == 3

    redo_lista.clear()
    lista.clear()

    lista = adauga_obiect("1", "minge", "minge de fotbal", 120, "Cora", lista)
    undo_lista.append(lista)
    lista = adauga_obiect("2", "minge", "minge de tenis", 6, "Lidl", lista)
    undo_lista.append(lista)
    lista = adauga_obiect("3", "iaurt", "grecesc", 7, "Real", lista)
    undo_lista.append(lista)

    assert len(undo_lista) == 3
    assert len(redo_lista) == 0

    undo_lista.pop()
    redo_lista.append(lista)

    assert len(undo_lista) == 2
    assert len(redo_lista) == 1

    undo_lista.pop()
    redo_lista.append(lista)

    assert len(undo_lista) == 1
    assert len(redo_lista) == 2

    redo_lista.pop()
    undo_lista.append(lista)
    assert len(undo_lista) == 2
    assert len(redo_lista) == 1


    redo_lista.pop()
    undo_lista.append(lista)
    assert len(undo_lista) == 3
    assert len(redo_lista) == 0

    undo_lista.pop()
    redo_lista.append(lista)
    assert len(undo_lista) == 2
    assert len(redo_lista) == 1


    undo_lista.pop()
    redo_lista.append(lista)
    assert len(undo_lista) == 1
    assert len(redo_lista) == 2

    lista = adauga_obiect("4","lumanari","parfumate",20,"cora",lista)
    undo_lista.append(lista)
    redo_lista.clear()

    assert len(undo_lista) == 2
    assert len(redo_lista) == 0

    undo_lista.pop()
    redo_lista.append(lista)
    assert len(undo_lista) == 1
    assert len(redo_lista) == 1

    undo_lista.pop()
    redo_lista.append(lista)
    assert len(undo_lista) == 0
    assert len(redo_lista) == 2

    redo_lista.pop()
    undo_lista.append(lista)
    assert len(undo_lista) == 1
    assert len(redo_lista) == 1

    redo_lista.pop()
    undo_lista.append(lista)
    assert len(undo_lista) == 2
    assert len(redo_lista) == 0




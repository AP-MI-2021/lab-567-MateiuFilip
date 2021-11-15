from UserInterface.console import run_menu
from UserInterface.new_console import menu


def console_choice(lista):
    optiune = input("Alegeti Consola 1 sau Consola 2:")
    if optiune == "Consola 1":
        run_menu(lista)
    if optiune == "Consola 2":
        menu(lista)
    else:
        print("Optiune gresita. Reincercati!")

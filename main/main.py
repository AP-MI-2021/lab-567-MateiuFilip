from Tests.testAll import test_all
from Tests.teste_domain import test_obiect
from UserInterface.console import run_menu
from UserInterface.new_console import menu


def main():
    test_all()
    lista=[]
    run_menu(lista)

main()
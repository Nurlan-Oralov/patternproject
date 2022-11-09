import os
import rich
import abc
import reglog
import observer
import strategy
import decorator
from rich.console import Console
from rich.table import Table


def income():
    boolean = "no"
    table = Table(title="Income")
    print ("trigger2")
    while True:

        name = input("Добавьте свой пункт дохода\n")
        if name == "no" :
            break
        value = input("Добавьте сумму дохода")
        if boolean == "no":
            create_table(name, value, table, boolean)
            boolean = "yes"
        else:
            create_table(name, value, table, boolean)


def create_table(name, value, table, boolean):

    if boolean == "no":
        table.add_column("Type of Income", justify="right", style="cyan", no_wrap=True)
        table.add_column("Amount", style="magenta")
        table.add_column("needs", style="magenta")
        table.add_column("saves", style="magenta")
        table.add_column("wants", style="magenta")


    table.add_row(f"{name}", f"{value}", f"{int(value) * 0.5}", f"{int(value) * 0.3}", f"{int(value) * 0.2}")
    console = Console()
    console.print(table)



def loans():
    print('Loans')
    return menu()


def overall_report():

    return menu()


def menu():
    print('''Выберите пункт меню:
        1. Доходы
        2. Расходы
        3. Кредиты
        4. Накопления
        5. Отчет''')

    menu_input = input()
    match menu_input:
        case "1":
            return income()
        case "2":
            pass
        case "3":
            return loans()
        case "4":
            return saves()
        case "5":
            return overall_report()
        case _:
            print("такого нет")
            return menu()


def main():
    reglog.init_file()
    menu()


if __name__ == "__main__":
    main()
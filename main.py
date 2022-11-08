import os
import rich
import abc
import reglog


def income():
    while True:
        decision = input('Хотите добавить доход? Yes/No')

        if decision == "Yes":
            new_point = input("Добавьте свой пункт дохода\n"
                              'Пример: "Название дохода" "Сумма дохода"\n')
            print()
            income()


def loans():
    print('Loans')
    return menu()


def saves():
    print('saves')
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
            return outcome()
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
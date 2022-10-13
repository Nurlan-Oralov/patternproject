import os
import json

login = "json"
name_income = "salary"
unsorted_income = 100000


def read(login: str) -> dict:
    with open(f"{login}.json", 'r') as f:
        data = json.load(f)
    return data


def write(login: str, name_income: str, unsorted_income: int) -> None:
    data = read(login)

    income = data["income"]

    income["name_income"] = name_income
    income["needs"] = int(unsorted_income * 0.5)
    income["wants"] = int(unsorted_income * 0.3)
    income["saves"] = int(unsorted_income * 0.2)

    data["income"] = income

    print(income)
    print(type(income))

    print(data)
    with open(f'{login}.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == "__main__":
    write(login, name_income, unsorted_income)

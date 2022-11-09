from abc import ABC, abstractmethod


class IIncome(ABC):
    @abstractmethod
    def account(self) -> float:
        pass


class Income(IIncome):
    def __init__(self, account):
        self.__account = account

    def cost(self) -> float:
        return self.__account


class IDecorator(IIncome):
    @abstractmethod
    def name(self) -> str:
        pass


class Needs(IIncome):
    def __init__(self, wrapped: IIncome, result: float):
        self.__wrapped = wrapped
        self.__result = result
        self.__name = "Needs"

    def needs_result(self) -> float:
        return self.__wrapped.account() * self.__result


class Wants(IIncome):
    def __init__(self, wrapped: IIncome, result: float):
        self.__wrapped = wrapped
        self.__result = result
        self.__name = "Wants"

    def needs_result(self) -> float:
        return self.__wrapped.account() * self.__result


class Saves(IIncome):
    def __init__(self, wrapped: IIncome, result: float):
        self.__wrapped = wrapped
        self.__result = result
        self.__name = "Needs"

    def needs_result(self) -> float:
        return self.__wrapped.account() * self.__result


if __name__ == "__main__":

    def print_result(result: IDecorator) -> None:
        print(f"Часть {result.name()} будет равна {result.account()}")

    income = Income(500000.0)

    print(f"Ваш доход: {income}")

    needs = Needs(income, 0.5)
    print(f"На необходимые расходы: {needs}тг")

    wants = Wants(income, 0.3)
    print(f"На свои желания: {wants}")

    saves = Saves(income, 0.2)
    print(f"Эту сумму нужно сохранить: {saves}")

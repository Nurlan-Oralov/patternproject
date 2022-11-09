import abc


class Reader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse(self, report):
        pass


class ResourceReader:
    def __init__(self, reader: Reader):
        self.__reader = reader

    def set_strategy(self, reader: Reader):
        self.__reader = reader

    def read(self, report: str):
        self.__reader.parse(report)


class Income(Reader):
    def parse(self, report: str):
        print("Отчет доходов: ", report)


class Outcome(Reader):
    def parse(self, report: str):
        print("Отчет с расходов: ", report)


class Loan_overall(Reader):
    def parse(self, report: str):
        print("Отчет общей суммы кредита/задолженности: ", report)


class Loan_need_to_pay(Reader):
    def parse(self, report: str):
        print("Отчет сколько осталось оплатить по кредиту/задолженности: ", report)


if __name__ == "__main__":
    income = 0
    outcome = 0
    loan_overall = 0
    loan_need_to_pay = 0


    resource_reader = ResourceReader(Income())
    report = "500000"
    resource_reader.read(report)

    resource_reader.set_strategy(Outcome())
    report = "100000"
    resource_reader.read(report)

    resource_reader.set_strategy(Loan_overall())
    report = "100000000"
    resource_reader.read(report)

    resource_reader.set_strategy(Loan_need_to_pay())
    report = "1000000"
    resource_reader.read(report)
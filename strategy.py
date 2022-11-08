from abc import ABC, abstractmethod


class CompanySystem:
    """'Система отчетов компании"""

    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def chief_order_notify(self):
        for observer in self._observers:
            observer.make_report()


class AbstractObserver(ABC):
    @abstractmethod
    def make_report(self):
        pass


class Department(AbstractObserver):
    """"Департамент компании"""

    def __init__(self, name):
        self.department_name = name

    def make_report(self):
        print("{} сделал отчет".format(self.department_name))


# Наши департаменты
preProduction = Department("Препродакшн")
production = Department("Продакшн")
postProduction = Department("Постпродакшн")
finances = Department("отдел финансов")
hrs = Department("Отдел кадров")

# Управление компанией
companySystem = CompanySystem()

# Шефу нужны все отчеты по продакшонам
companySystem.attach(preProduction)
companySystem.attach(production)
companySystem.attach(postProduction)

companySystem.chief_order_notify()

# Шефу нужен отчет по финансам
companySystem.detach(preProduction)
companySystem.detach(production)
companySystem.detach(postProduction)
companySystem.attach(finances)

companySystem.chief_order_notify()
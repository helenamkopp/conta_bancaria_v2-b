class Employee:

    def __init__(self, name, cpf, pay):
        self._name = str(name)
        self._cpf = str(cpf)
        self._pay = float(pay)

    def get_bonus(self):
        return self._pay * 0.10


class Manager(Employee):

    def __init__(self, name, cpf, pay, password, number_of_managed):
        super().__init__(name, cpf, pay)
        self._password = int(password)
        self._number_of_managed = int(number_of_managed)

    def get_bonus(self):
        return super().get_bonus() + 1000

    def authenticate(self, password):
        if self._password == password:
            print("access allowed")
            return True
        else:
            print("access denied")
            return False


class BonusControl:

    def __init__(self, bonus_total=0):
        self._bonus_total = bonus_total

    def register(self, employee):
        if hasattr(employee, "get_bonus"):
            self._bonus_total += employee.get_bonus
        else:
            print(f"Instance {self.__class__.__name__} does not implement the get_bonus() method")

    @property
    def bonus_total(self):
        return self._bonus_total


class Client:

    def __init__(self, name, cpf, password):
        self._name = name
        self._cpf = cpf
        self._password = password

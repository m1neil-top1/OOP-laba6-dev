class Person:
    def __init__(
        self, phone_numbe=str(), nama=None, document=None, work_place=None, work_position=None, salary=float()
    ) -> None:
        self._phone_number = phone_numbe
        self._name = nama
        self._document = document
        self._work_place = work_place
        self._work_position = work_position
        if salary < 0:
            print("Ошибка: зарплата не может иметь отрицательные значения!")
        self._salary = salary

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary


class Bank_worker(Person):
    def __init__(self, phone_numbe="None", nama="None", document=str(), work_position="None", salary=float()) -> None:
        super().__init__(phone_numbe, nama, document, "Alfa Bank", work_position, salary)

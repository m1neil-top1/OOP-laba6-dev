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

    def set_work_place(self, work_place):
        self._work_place = work_place

    def set_work_position(self, work_position):
        self._work_position = work_position

    def set_document(self, document):
        self._document = document

    def get_document(self):
        return self._document

    def get_work_place(self):
        return self._work_place

    def get_work_position(self):
        return self._work_position


class Bank_worker(Person):
    def __init__(self, phone_numbe="None", nama="None", document=str(), work_position="None", salary=float()) -> None:
        super().__init__(phone_numbe, nama, document, "Alfa Bank", work_position, salary)

    def info(self):
        print(
            "ФИО: " + self._name,
            "\nНомер паспорта: " + str(self._document),
            "\nНомер телефона: +380 " + self._phone_number,
            "\nМесто работы: " + self._work_place,
            "\nПозиция: " + self._work_position,
            "\nЗарплата: " + str(self._salary) + " грн.",
        )

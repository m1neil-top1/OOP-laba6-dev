import this
from person import Person
import random


class Client(Person):
    def __init__(
        self,
        phone_numbe=str(),  # Телефно
        nama=str(),  # Имя фамилия
        document=None,  # Номер документа
        work_place=None,  # Место работы
        work_position=None,  # Позиция на которой работает
        salary=0.0,  # Зарплата
        email=str(),
        password=str(),
        age=0,
    ) -> None:
        super().__init__(phone_numbe, nama, document, work_place, work_position, salary)
        self._email = email  # Почта
        self._password = password  # Пароль
        self._rating = 10  # Придумать реализацию с рейтингом.
        self._credit = float()  # Сумма Кредита
        self._credit_time = 0
        self._sum_use_credit = float()
        self._has_credit = False  # Наличие кредита на руках
        self._can_get_credit = False  # Может ли клиент получить кредит
        self._age = age

    # Кабинет пользователя
    def personal_area(self):
        while True:
            # TODO: Создать  Кошелёк + Создать класс виза карт и кредиток
            menu = "\t\t\tЛичный кабинет\n" + "1. Кошелек\n" + "2. Кредит\n" + "3. Аккаунт"
            print(menu)
            operation = int()
            while operation < 1 or operation > 3:
                operation = int(input("Операция: "))
                if operation < 1 or operation > 3:
                    print("Вы ошиблись повторите попытку!")
            if operation == 2:
                return operation
            elif operation == 3:
                print("Ваш аккаунт:")
                if self._age == 0:
                    print("Вам необходимо заполненные данные!")
                    choose = str()
                    while choose != "y" and choose != "n":
                        choose = input("Желаете заполнить их? y/n: ")
                    if choose.lower() == "y":
                        return operation
                    elif choose.lower == "n":
                        continue
                while operation != 2:
                    print("1. Информация об аккаунте\n" + "2. Вернуться в кабинет\n" + "3. Выйти из аккаунта")
                    operation = 0
                    while operation < 1 or operation > 3:
                        operation = int(input("Операция: "))
                        if operation < 1 or operation > 3:
                            print("Вы ошиблись повторите попытку!")
                    if operation == 1:
                        # TODO: Даработать момент, что мы не можем посмотреть всю инфу пока не заполним данные! Или не выводить этот фракмент вовсе.
                        print(
                            "ФИО: " + self._name,
                            "\nВозраст: " + str(self._age),
                            "\nНомер паспорта: " + str(self._document),
                            "\nНомер телефона: +380 " + self._phone_number,
                            "\nПочта: " + self._email,
                            "\nМесто работы: " + self._work_place,
                            "\nПозиция: " + self._work_position,
                            "\nЗарплата: " + str(self._salary) + " грн.",
                        )
                        if self._has_credit:
                            print("Сумма кредита: " + str(self._credit) + " грн.")
                        else:
                            print("Нет оформленного кредита")
                    elif operation == 2:
                        break
                    elif operation == 3:
                        return 4

    def set_email(self, email):
        self._email = email

    def set_sum_use_credit(self, sum_use_credit):
        self._sum_use_credit = sum_use_credit

    def set_has_credit(self, answer):
        self._has_credit = answer

    def get_sum_use_credit(self):
        return self._sum_use_credit

    def set_password(self, password):
        self._password = password

    def set_can_get_credit(self, answer):
        self._can_get_credit = answer

    def get_can_get_credit(self):
        return self._can_get_credit

    def get_password(self):
        return self._password

    def get_credit(self):
        return self._credit

    def set_age(self, age):
        self._age = age

    def set_credit(self, credit):
        self._credit = credit

    def set_credit_time(self, credit_time):
        self._credit_time = credit_time

    def get_credit_time(self):
        return self._credit_time

    def get_rating(self):
        return self._rating

    def get_email(self):
        return self._email

    # Данные необходимы Менеджеру
    def get_has_credit(self):
        return self._has_credit

    def get_can_get_credit(self):
        return self._can_get_credit

    def get_age(self):
        return self._age

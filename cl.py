from http import client
from person import Person
from card import Card
import time


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
        self._cards = []

    static_var_count_card = 0  # переменная которая считает количество карт

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
                if operation == 1:
                    self.purse()
                elif operation == 2:
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

    def purse(self):
        while True:
            exit = None
            if len(self._cards) == 0:
                print("У вас нету оформленных счетов.")
                user_input = str()
                while user_input.lower() != "y" and user_input.lower() != "n":
                    user_input = input("Желаете оформить карточку? y/n: ")
                    if user_input.lower() != "y" and user_input.lower() == "n":
                        print("Не корректный в вод!")
                if user_input == "y":
                    Client.static_var_count_card += 1
                    self._cards.append(Card(0, Client.static_var_count_card))
                    print("Ваш счёт открыт!")
            user_input = 0
            if len(self._cards) > 0:
                print("1. Открыть счёт\n" + "2. Посмотреть счета\n" + "3. Выйти")
                while user_input < 1 or user_input > 3:
                    user_input = int(input("Операция: "))
                    if user_input < 1 or user_input > 3:
                        print("Не корректный в вод!")
                if user_input == 1:
                    if len(self._cards) < 3:
                        Client.static_var_count_card += 1
                        self._cards.append(Card(0, Client.static_var_count_card))
                        print("Номер счёта успешно открыт!")
                    else:
                        print("В нашем банке можно открыть максимум 3 счёта!")     
                elif user_input == 2:
                    while True:
                        print("Количество счетов:", len(self._cards))
                        for i in range(0, len(self._cards)):
                            print(
                                str(i + 1) + ") Номер счёта: " + str(self._cards[i].get_number()),
                                "сумма счёта: " + str(self._cards[i].get_money()) + " грн.",
                            )
                            # Для отмены операции
                            if i == len(self._cards) - 1:
                                exit = i + 2
                                print(str(exit) + ") Выход")
                        number_card = 0
                        while number_card < 1 or number_card > exit:
                            number_card = int(input("Выберите картку: "))
                        if number_card == exit:
                            break
                        else:
                            print("1. Снять деньги\n" + "2. Пополнить счёт")
                            user_input1 = 0
                            while user_input1 < 1 or user_input1 > 2:
                                user_input1 = int(input("Операция: "))
                                if user_input1 < 1 or user_input1 > 2:
                                    print("Не корректный в вод!")
                            summa = 0
                            while summa < 0:
                                summa = float(input("Введите сумму: "))
                                if summa <= 0:
                                    print("Не корректный в вод!")
                            if user_input1 == 1:
                                self._cards[number_card - 1].withdrawals(summa)
                            elif user_input1 == 2:
                                self._cards[number_card - 1].replenishment_funds(summa)
                elif user_input == 3:
                    print("Возвращаюсь в кабинет...")
                    time.sleep(2)
                    return


    def get_cards(self):
        return self._cards

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

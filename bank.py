from pydoc import cli
from cl import Client
from manager import Manager
import time
from bossCD import BossCD
from lowyer import Lowyer


class MyBank:

    def __init__(self) -> None:
        self._name = "MyBank"
        self._list_clients = [
            Client("989830599", "Eric", 12345678, "Nix-solution",
                   "junior-web-development", 15500, "eric@gmail.com", "1111",
                   22),
            Client("989830620", str(), None, None, None, 0,
                   "ericalex0207@mail.ru", "1111", 0),
            Client()
        ]
        # TODO: По формату сделать номер паспорта
        self._manager = Manager("957459388", "Андрей Владимирович",
                                "Паспорт: №345234545", 12500)
        self._boss = BossCD("659863294", "Питер Квил", 93468216,
                            "piterKvil@admin.ua", "2222")
        self._lowyer = Lowyer("986236599", "Александр Васильков", "98425642")

    # Manager`s office
    def _manager_office(self, client=Client()):
        examination = self._manager.check_client_for_get_credit(client)
        if examination == False:
            return
        summa = 0.0
        days = 0
        percent = 2
        print("Минмальная сумма кредита - 600 грн.\n" +
              "Максимальная сумма кредита - 15 000 грн.\n" +
              "Кредитный процент составляет " + str(percent) + "% на день\n" +
              "Срок платежа максимум 30 дней.")
        while summa < 600 or summa > 15000:
            summa = float(input("Выберите сумму: "))
            if summa < 600:
                print("Минимальная сумма должна составлять - 600 грн.")
            elif summa > 15000:
                print("Мы не выдаем кредит больше чем на - 15 000 грн.")
        while days < 5 or days > 30:
            days = int(input("Введите срок платежа: "))
            if days < 5:
                print("Не корректный в вод.")
            elif days > 30:
                print(
                    "Мы не оформляем кредит со сроком платежа больше чем 30 дней."
                )
        print("Итого:")
        print("Сумма кредита без учёта процентов: " + str(summa) + " грн.")
        print("Кредит выдается на: " + str(days), end=(" "))
        if days == 21:
            print("день.")
        elif days >= 22 and days <= 24:
            print("дня.")
        elif days >= 5 and days <= 20 or days >= 25 and days <= 30:
            print("дней.")
        print("Ежедневная процентная ставка: " + str(percent) + '%')
        percent_one_day = (summa * 2) / 100
        print("Процент за 1 день: " + str(percent_one_day) + " грн.")
        print("Процент за " + str(days), end=(" "))
        if days == 21:
            print("день ", end=(""))
        elif days >= 22 and days <= 24:
            print("дня ", end=(""))
        elif days >= 5 and days <= 20 or days >= 25 and days <= 30:
            print("дней ", end=(""))
        summa_credit_on_days = percent_one_day * days
        print("составляет: " + str(summa_credit_on_days) + " грн.")
        total_credit = summa + summa_credit_on_days
        print("Итого к оплате кредита: " + str(total_credit) + " гнр.")
        user_answer = ""
        while user_answer != "y" and user_answer != "n":
            user_answer = input("Продолжим офрмлять кредить? y/n: ")
            if user_answer.lower() != "y" and user_answer.lower() != "n":
                print("Не корректный в вод!")
        if user_answer == "y":
            self._boss.check_user(total_credit, days, summa_credit_on_days,
                                  client)
        elif user_answer == "n":
            print("Операция отменена!\n" + "Возвращаемся в кабинет...")
            time.sleep(2)

    # lawyer consultancy office
    def _lowyer_consultancy_office(self, client=Client()):
        self._lowyer.treaty(client)

    # Main function
    def main(self):
        while True:
            print("1. Войти в аккаунт\n" + "2. Зарегистрироваться\n" +
                  "3. Выйти")
            choose = int()
            while choose < 1 or choose > 3:
                choose = int(input("Введите операцию: "))
                if choose < 1 or choose > 3:
                    print("Не корректный в вод!")
            # Вход в аккаунт
            if choose == 1:
                print("Вход в аккаунт")
                correct = False
                admin_accaunt = False
                not_exit = "y"
                index = int()
                while correct == False and not_exit == "y":  # Вход в акк обычного пользователя
                    email = input("email: ")
                    for i in range(0, len(email)):
                        if email[i] == "@":
                            if email[i + 1:] == "admin.ua":
                                admin_accaunt = True
                                break
                    if admin_accaunt == False:
                        for i in range(0, len(self._list_clients)):
                            if self._list_clients[i].get_email() == email:
                                # TODO: Дописать цикл
                                while not_exit == "y":
                                    not_exit = str()
                                    password = input("Введите пароль: ")
                                    if self._list_clients[i].get_password(
                                    ) == password:
                                        index = i
                                        correct = True
                                        break
                                    else:
                                        print("Вы ввели не правильный пароль!")
                                        while not_exit != "y" and not_exit != "n":
                                            not_exit = input(
                                                "Хотите повторить? y/n:")
                                            not_exit = not_exit.lower()
                                if not_exit == "n":
                                    break
                    elif admin_accaunt == True:
                        if self._boss.get_email() == email:
                            # TODO: Дописать цикл
                            while not_exit == "y":
                                not_exit = str()
                                password = input("Введите пароль: ")
                                if self._boss.get_password() == password:
                                    correct = True
                                    break
                                else:
                                    print("Вы ввели не правильный пароль!")
                                    while not_exit != "y" and not_exit != "n":
                                        not_exit = input(
                                            "Хотите повторить? y/n:")
                                        not_exit = not_exit.lower()
                    if not_exit == "n":
                        break
                    if correct == False:
                        print(
                            "Вы не правильно ввели свою почту. Повторите попытку!"
                        )
                        continue
                if correct and admin_accaunt != True:
                    self._user_area(self._list_clients[index])
                elif correct and admin_accaunt == True:
                    # TODO: Создаем окружение босса.
                    a = 2
                else:
                    continue
            # Регистрация аккаунта.
            elif choose == 2:
                result = self._registration()
                if result:
                    self._user_area(self._list_clients[-1])
                else:
                    print("Регистрация отменена!")
                    continue
            elif choose == 3:
                print("До свидания!")
                break

    def _registration(self):
        number_phone = str()
        while len(number_phone) < 9:
            number_phone = input("Ваш номер телефона: +380 ")
            if len(number_phone) < 9:
                print("Ошибка: Не корректный номер! Повторите попытку!")
        client = Client(
            number_phone)  # Сделать проверку нет ли такого уже номера
        correct_address = False
        while correct_address == False:  # Проверку на зарегистрированую почту, потом.
            email = input("Введите свой электронный адрес: ")
            for index in range(0, len(email)):
                if (email[0] == "@"):
                    break
                if email[index] == "@":
                    if email[index +
                             1:] == "gmail.com" or email[index +
                                                         1:] == "mail.ru":
                        correct_address = True
                        break
            if correct_address == False:
                print("Не корректный адрес электронной почты.")
        client.set_email(email)
        password = str()
        while len(password) < 4:
            password = input("Придумайт пароль: ")
            if len(password) < 4:
                print("Пароль слишком короткий")
        repeat_password = str()
        while repeat_password != password:
            repeat_password = input("Повторите пароль: ")
            if repeat_password != password:
                print("Пароли не совпадают!")
        client.set_password(password)
        name = input("Введите ФИО: ")
        client.set_name(name)
        agree = str()
        while agree != "y" and agree != "n":
            agree = input("Продолжить? y/n: ")
        if agree == 'y':
            self._list_clients.append(client)
            return True
        elif agree == 'n':
            del client
            return False

    # Функция связанная с клиентом
    def _user_area(self, user=Client):
        while True:
            user_operation = user.personal_area(
            )  # Попадаем в пользовательский кабинет.
            if user_operation == 2:  # Вызываем кредитный отдел
                self._credit_department(user)  #! Жду фикса бро аллё!!!!
            elif user_operation == 3:
                self._filling_user_data(user)
            elif user_operation == 4:
                print("Выхожу из аккаунта пользователя...")
                time.sleep(2)
                break

    def _credit_department(self, client=Client()):
        # TODO: Реализовать функцию: Оплатить кредит
        while True:
            print("\t\t\tКредитный отдел")
            menu = "1. Оформить кредит\n" + "2. Оплатить кредит\n" + "3. Вернуться в личный кабинет"
            print(menu)
            choose = int()
            while choose < 1 or choose > 3:
                choose = int(input("Операция: "))
                if choose < 1 or choose > 3:
                    print("Не корректный в вод!")
            if choose == 1:  # Прежде чем оформить крдеит, нам нужно пройти проверку у менеджера.
                self._manager_office(client)
                if client.get_can_get_credit() == True:
                    self._lowyer_consultancy_office(client)
                elif client.get_can_get_credit() == False:
                    print("Вам отказанно в оформление кредита!")
            if choose == 2:
                print(
                    "Попадаем в метод Менеджера который позволяет оплатить кредит."
                )
            if choose == 3:
                print("Возвращаюсь в личный кабинет...")
                time.sleep(2)
                break

    # Заполнение данных пользователя
    def _filling_user_data(self, client=Client()):
        if client.get_age() == 0:  # Возраст
            age = 0
            while age < 6 or age > 64:
                age = int(input("Введите ваш возраст: "))
                if age < 6 or age >= 65:
                    if age < 6:
                        print(
                            "Для оформления карты или кредита вам должно быть как минимум 6 лет!"
                        )
                    elif age >= 65:
                        print("Мы не обслуживаем клиентов вашего возратса.")
                    print("Возврат в пользовательский кабинет....")
                    time.sleep(3)
                    return
            else:
                client.set_age(age)
        if client.get_document() == None:  # Паспор
            document = int()
            repeat_document = True
            while repeat_document == True:
                document = int(input("Введите номер паспорта в нём 8 цифр: "))
                if len(str(document)) != 8:
                    print("Не коректный в вод паспорта. Повторите попытку.")
                    continue
                for i in range(0, len(self._list_clients)):
                    if document == self._list_clients[i].get_document():
                        print("Такой номер документа уже зарегистрирован")
                        break
                    else:
                        repeat_document = False
                if repeat_document == False:
                    client.set_document(document)
                    print("Мы успешно занесли данные!")
        if client.get_work_place() == None:
            client._work_place = input("Введите ваше место работы: ")
        if client.get_work_position() == None:
            client._work_position = input("Введите вашу должность: ")
        if client.get_salary() == 0.0:
            salary = float()
            while salary < 6500:
                salary = float(input("Введите вашу зарплату: "))
                if salary <= 0:
                    print("Введенные не корректные данныеж.")
                elif salary < 6500:
                    print(
                        "Не корретные данные в Украине минимальная ставка 6500 грн."
                    )
            client.set_salary(salary)
        print("Вы успешно заполнили данные! Подождите секунду...")
        time.sleep(1)

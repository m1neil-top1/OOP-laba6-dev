from person import Bank_worker
from cl import Client
import shape_day
import time


class BossCD(Bank_worker):
    def __init__(self, phone_numbe="None", nama="None", document="", email=str(), password=str()) -> None:
        super().__init__(phone_numbe, nama, document, "Начальник кредитного отдела", 25000)
        self._email = email  # Почта
        self._password = password  # Пароль

    def check_user(self, total_sum_credit, total_credit_time, summa_credit_on_days, user=Client()):
        if total_sum_credit > user.get_salary():
            print("В выдачи кредита отказано.\n" + "Ваша зарплата не способна покрыть кредит.")
        else:
            print(
                "Поздравляем вам данно разрешение на получение кредита в размере: "
                + str(total_sum_credit - summa_credit_on_days)
                + " грн.\n"
                + "За использование кредита нужно будет доплатить: "
                + str(summa_credit_on_days)
                + " грн.\n"
                + "Срок кредита: "
                + str(total_credit_time),
                end=(" "),
            )
            print(shape_day.day_shape(total_credit_time))
            user.set_can_get_credit(True)
            user.set_credit(total_sum_credit - summa_credit_on_days)
            user.set_sum_use_credit(summa_credit_on_days)
            user.set_credit_time(total_credit_time)
            print("Осталось заключить договор...")
            print("Обрабатываю данные....")
            time.sleep(2)

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def change_salary_worker(self, worker=Bank_worker()):
        print("Информация об работнике:")
        worker.info()
        new_salary = 0
        while new_salary < 6500:
            new_salary = float(input("Введите новую зарплату: "))
            if new_salary <= 0:
                print("Введенные не корректные данные.")
            elif new_salary < 6500:
                print("Не корретные данные в Украине минимальная ставка 6500 грн.")
        worker.set_salary(new_salary)
        print("\nВывожу обновленую информацию об работнике:")
        worker.info()
        print("Возвращаюсь в меню..")
        time.sleep(2)

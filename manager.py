from traceback import print_tb
from person import Bank_worker
from cl import Client
import time


class Manager(Bank_worker):

    def __init__(self,
                 phone_numbe="None",
                 nama="None",
                 document=str(),
                 salary=float()) -> None:
        super().__init__(phone_numbe, nama, document, "Менеджер", salary)

    def check_client_for_get_credit(self, client=Client()):
        if client.get_document() == None or client.get_work_place(
        ) == None or client.get_work_position() == None or client.get_salary(
        ) == 0.0 or client.get_age() == 0:
            print(
                "Вы не может оформить кдедить без не достающих данных у вас есть не заполненны данные!\n",
                "Перейдите в личный кабинет и заполните недостающие данные:")
            print("Вам нужно заполнить такие даные:")
            if client.get_age() == 0:
                print("Ваш возраст")
            if client.get_document() == None:
                print("Номер паспорта")
            if client.get_work_place() == None:
                print("Место работы")
            if client.get_work_position() == None:
                print("Должность на которой вы работаете")
            if client.get_salary() == 0.0:
                print("Вашу зарплату")
            print("Выхожу из оффиса менеджера...")
            time.sleep(10)
            return False
        if client.get_has_credit():
            print(
                "Вы сможите оформить кредит повторно когда оплате уже существующих."
            )
            return False
        elif client.get_age() < 18:
            print("Оформить кредит можно только с 18 лет.")
            return False
        elif client.get_rating() < 6:
            print(
                "У вас слишком плохая кредитная история. В возможности получить кредит отказанно."
            )
            return False
        else:
            print(
                "Все данные корректные! Поздравляем и переходим к следующему этапу!"
            )
            return True

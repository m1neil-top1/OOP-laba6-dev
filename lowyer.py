from person import Bank_worker
from cl import Client
import shape_day
import time


class Lowyer(Bank_worker):
    def __init__(self, phone_numbe="None", nama="None", document="", salary=10000) -> None:
        super().__init__(phone_numbe, nama, document, "Юрист консультант", salary)

    def treaty(self, client=Client()):
        print(
            "Кредитный договор (между банком и его клиентом)\n" + "Банк-кредитор: " + self._work_place + "\n",
            "Заемщик: " + client.get_name() + "\n",
            "1. Предмет договора\n",
            "1.1. Банк-кредитор  обязуется  предоставить  Заемщику  краткосрочный кредит, а последний обязуется использовать его  по  целевому  назначению, возвратить кредит в определенный  Настоящим  Договором  срок  и  уплатить Банку-кредитору обусловленное вознаграждение (проценты).\n",
            "1.2. В  процессе  исполнения  обязательств  по  Настоящему  Договору Заемщик обязан  соблюдать  следующие  принципы  кредитования:  срочность, возвратность, целевое использование, возмездность, обеспеченность.\n",
            "2. Размер кредита\n",
            "2.1 Сумма кредита составляет по Настоящему Договору:",
            str(client.get_credit()) + " грн.\n",
            "3. Срок кредита\n",
            "3.1 Кредит выдается Заемщику на срок: "
            + str(client.get_credit_time())
            + " "
            + shape_day.day_shape(client.get_credit_time())
            + "\n",
            "4 Цена договора и порядок расчетов\n",
            "4.1 Заемщик   обязуется   уплатить   Банку-кредитору  следующее вознаграждение в размере "
            + str(client.get_sum_use_credit())
            + " грн, за пользование кредитом под 2% в размере: "
            + str(client.get_credit())
            + " грн.\n",
            "5 Персональные данные\n",
            "5.1 Подписывая этот договор вы даете согласие на обработку и использование ваших персональных данных.",
        )
        user_signature = str()
        while user_signature.lower() != "y" and user_signature.lower() != "n":
            user_signature = input("Вы согласны со всеми условиями договора? y/n: ")
            if user_signature.lower() != "y" and user_signature.lower() != "n":
                print("Не корректынй ответ! Повторите попытку!")
        if user_signature.lower() == "y":
            print(
                "С настоящего момента договор вступает в силу!\n",
                "Поздравляем вы успешно оформили кредит!",
            )
            client.set_has_credit(True)
            client.set_can_get_credit(False)
        elif user_signature == "n":
            user_signature = str()
            print(
                "Вы хотите отказаться от оформления кредита? Имейте ввиде, что большинство процедур придется проходить заново."
            )
            while user_signature.lower() != "y" and user_signature.lower() != "n":
                user_signature = input("Вы отказываетесь от офрмления кредита? y/n: ")
                if user_signature.lower() != "y" and user_signature.lower() != "n":
                    print("Не корректынй ответ! Повторите попытку!")
            if user_signature.lower() == "y":
                client.set_credit(0)
                client.set_credit_time(0)
                client.set_sum_use_credit(0)
                print("Операция отменена. Возвращаюсь в меню.....")
                time.sleep(2)
                return
            elif user_signature.lower() == "n":
                print("Тогда мы его оформляем!!!!!")
                client.set_has_credit(True)
                client.set_can_get_credit(False)
                print(
                    "Поздравляем с успешным оформлением кредита!\n",
                    "Возвращаюсь в меню....",
                )
                time.sleep(2)
                return

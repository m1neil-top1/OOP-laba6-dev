class Card:
    def __init__(self, money, number):
        self._money = money
        self._number = number

    def get_money(self):
        return self._money

    def get_number(self):
        return self._number

    def withdrawals(self, summa):  # Снятие деньги
        if summa > self._money:
            print("На счету не достаточно средств")
        else:
            self._money -= summa
            print("С вашего счёта было снято: " + str(summa) + " грн.")
            print("На вашем счёте осталось: " + str(self._money) + " грн.")
            
    def replenishment_funds(self, summa): # Поплнить деньги
        self._money += summa
        print("Ваш счёта был пополнен на: " + str(summa) + " грн.")
        print("На вашем счёте теперь: " + str(self._money) + " грн.")

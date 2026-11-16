# Solution file
class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, pin):
        if pin == self.__pin:
            print(self.__balance)

atm = ATM(1234, 10000)
atm.check_balance(1234)
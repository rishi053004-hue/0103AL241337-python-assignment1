# Solution file
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def show(self):
        print(self.__salary)

e = Employee(50000)
e.show()
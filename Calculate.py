class Calculate():
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    # def __str__(self):
    #     return f'Результат операции {self.rez}'

    def addition(self):
        rez = self.first_number + self.second_number
        return rez

    def substraction(self):
        rez = self.first_number - self.second_number
        return rez

    def multiplication(self):
        rez = self.first_number * self.second_number
        return rez

    def division(self):
        rez = self.first_number / self.second_number
        return rez

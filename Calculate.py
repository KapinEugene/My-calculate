class Calculate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f'Результат операции {self.rez}'

    def addition(self):
        rez = self.x + self.y
        return rez

    def substraction(self):
        rez = self.x - self.y
        return rez

    def multiplication(self):
        rez = self.x * self.y
        return rez

    def division(self):
        rez = self.x / self.y
        return rez

import roman

class Calculate():
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

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

    def execute(self, operation, is_arabic):
        if operation == '+':
            if is_arabic:
                rez = self.addition()
            elif not is_arabic:
                rez = roman.toRoman(self.addition())
        elif operation == '-':
            if is_arabic:
                rez = self.substraction()
            elif not is_arabic:
                rez = roman.toRoman(self.substraction())
        elif operation == '*':
            if is_arabic:
                rez = self.multiplication()
            elif not is_arabic:
                rez = roman.toRoman(self.multiplication())
        elif operation == '/':
            try:
                self.division()
            except ZeroDivisionError as e:
                print('На ноль делить нельзя, попробуйте еще раз')
            if is_arabic:
                rez = self.division()
            else:
                rez = roman.toRoman(int(self.division()))
        return rez
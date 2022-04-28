from Calculate import Calculate
import roman
import re

operationsList = ['+', '-', '*', '/']
while(True):
    operationsCount = 0
    is_arabic = True
    expression = input('Введите выражение: ')
    expression = expression.replace(' ', '')
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*' or expression[i] == '/':
            if expression[0] == '-':
                continue
            operationsCount += 1
    if operationsCount > 1 or operationsCount == 0:
        print('Ошибка ввода выражения, попробуйте еще раз')
        continue
    for i in operationsList:
        if i in expression:
            expression = expression.split(i)
            first_number = expression[0]
            second_number = expression[1]
            operation = i
    if (first_number.isdigit() and not second_number.isdigit()) or \
            (not first_number.isdigit() and second_number.isdigit()):
        print('Нельзя производить операцию с арабским и римским числом')
        continue
    elif not first_number.isdigit() and not second_number.isdigit():
        first_number = roman.fromRoman(first_number.upper())
        second_number = roman.fromRoman(second_number.upper())
        is_arabic = False
    elif first_number.isdigit() and second_number.isdigit():
        first_number = int(first_number)
        second_number = int(second_number)
    entered_expression = Calculate(first_number, second_number)
    print(entered_expression.execute(operation, is_arabic))

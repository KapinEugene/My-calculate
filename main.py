from Calculate import Calculate
import roman


while(True):
    a = 0
    x = input("Введите первое число ")
    y = input("Введите второе число ")
    if x.isdigit() != True and y.isdigit() != True:
        x = roman.fromRoman(x.upper())
        y = roman.fromRoman(y.upper())
        a = 1
    elif x.isdigit() != True and y.isdigit() == True:
        x = roman.fromRoman(x.upper())
        y = int(y)
        a = 1
        print('Нельзя производить операцию с арабским и римским число, но если вы настаиваете, то')
    elif x.isdigit() == True and y.isdigit() != True:
        y = roman.fromRoman(y.upper())
        x = int(x)
        a = 1
        print('Нельзя производить операцию с арабским и римским число, но если вы настаиваете, то')
    elif x.isdigit() == True and y.isdigit() == True:
        x = int(x)
        y = int(y)
    test = Calculate(x, y)
    o = input("Введите операцию: ")
    if o == '+':
        if a == 0:
            print(test.addition())
        elif a == 1:
            print(roman.toRoman(test.addition()))
    elif o == '-':
        if a == 0:
            print(test.substraction())
        elif a == 1:
            print(roman.toRoman(test.substraction()))
    elif o == '*':
        if a == 0:
            print(test.multiplication())
        elif a == 1:
            print(roman.toRoman(test.multiplication()))
    elif o == '/':
        if a == 0:
            if y == 0:
                try:
                    test.division()
                except ZeroDivisionError as e:
                    print('На ноль делить нельзя, попробуйте еще раз')
            else:
                print(test.division())
        elif a == 1:
            if y == 0:
                try:
                    test.division()
                except ZeroDivisionError as e:
                    print('На ноль делить нельзя, попробуйте еще раз')
            else:
                print(roman.toRoman(test.division()))

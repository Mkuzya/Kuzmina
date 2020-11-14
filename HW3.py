def my_func (arg2, arg3):
    try:
        arg1 = arg2 / arg3
        return arg1
    except ZeroDivisionError:
        return "На 0 делить нельзя."
    except ValueError:
        return "Введите другое число."
print(my_func(int(input("Введите делимое число: ")), int(input("Введите делитель: "))))


def my_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)

my_func(name= 'Marina', surname='Kuzmina', year=1993, city='Moscow', email='abcd@mail.com', phone='737373')


def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Ответ - {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')


def my_func(x, y):
    return 1 / x ** abs(y)

print(my_func(5, -3))


def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа или S для вывода суммы - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'S' or number[el] == 's':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Ответ: {sum_res}')
    print(f'Финальная сумма: {sum_res}')


my_sum()


def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total
print(my_func("новый год"))

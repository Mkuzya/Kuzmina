a = 6
b = 10
print("Переменные a и b - ", a, b)
a = input("Ваше имя? ")
b = input("Ваша фамилия? ")
c = int(input("Сколько вам лет? "))
d = float(input("Введите любое число: "))
print(a, b, c, d)


time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")


n = int(input("Введите число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)


n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Большая цифра в числе ", max)
        break


profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Выручка составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")


a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете желаемых результатов на %.d день" % result_days)



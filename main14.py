n = int(input('Введите кол-во измерений: '))
summa = 0.0
for i in range(1, n+1):
    v = float(input(f'Введите значение измерения номер {i}:'))
    summa+= v

sr_arefm = summa/n
print(f'Сумма всех измерений: {summa}')
print(f'Среднее арифметическое: {sr_arefm:.2f}')
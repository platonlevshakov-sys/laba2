print('num 11:')
num11 = [-10, 3, -2, 8, -5]
sts =  sorted(num11)
print(F'Обычная сортировка: {sts}')
abss = sorted(num11, key=lambda x:abs(x))
print(f'Сортировка по модулю: {abss}')



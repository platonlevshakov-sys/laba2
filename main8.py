print('num 8: ')
def cs(num):
    total = 0
    for n in num:
        total += n
    return total
def fmn(num):
    mn = num[0]
    for n in num[1:]:
        if n < mn:
            mn = n
    return mn
def fmx(num):
    mx = num[0]
    for n in num[1:]:
        if n > mx:
            mx = n
    return mx
td = [15, 3, -8, 42, 0, 11]
print(f'Тестовые данные: {td}')
print(f'Собственная сумма: {cs(td)} | sum(): {sum(td)}')
print(f'Собственный минимум: {fmn(td)} | min(): {min(td)}')
print(f'Собственный максимум: {fmx(td)} | max(): {max(td)}')



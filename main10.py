print('num 10:')
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
def alz(num):
    mn = fmn(num)
    mx = fmx(num)
    av = cs(num) / len(num)
    return mn, mx, av
d10 = [10, 20, 30, 40, 50]
mnv, mxv, avv = alz(d10)
print(f'Анализ списка {d10}:')
print(f'Минимум - {mnv}')
print(f'Максимум - {mxv}')
print(f'Среднее арифм - {avv}')



def cal(m):
    t = 0
    for v in m:
        t += v
    return t / len(m)
def fmn(m):
    mn = m[0]
    for v in m[1:]:
        if v < mn:
            mn = v
    return mn
def fmx(m):
    mx = m[0]
    for v in m[1:]:
        if v > mx:
            mx = v
    return mx
def caa(m):
    avg = cal(m)
    c = 0
    for v in m:
        if v > avg:
            c +=1
    return c
def fv(m,t):
    for i in range(len(m)):
        if m[i] == t:
            return i
    return -1
def am(m):
    mnv = fmn(m)
    mxv = fmx(m)
    avv = cal(m)
    return mnv, mxv, avv
#Тест программы:
d = [23.5, 18.2, 31.1, 25.4, 19.8, 22.1, 28.6, 24.1, 17.5, 29.3]
ut = 25.4
#Получение результатов:
mmn, mmx, avvg = am(d)
aac = caa(d)
fi = fv(d, ut)
print(f'Исходник: {d}')
print(f'Кол-во измерений: {len(d)}')
print(f'Минимальное значение: {mmn}')
print(f'Максимальное значение: {mmx}')
print(f'Среднее значение: {avvg:.2f}')
print(f'Кол-во значений > среднего: {aac}')
if fi != -1:
    print(f'Поиск значения {ut}: найдено на позиции {fi}')
else: print(f'значение {ut} не найдено')
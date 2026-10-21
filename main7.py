print("num 7: ")
#Встроенные функции
sl = [14, 5, 25, 8, 12, 44, 7]
print(f'Исходный список - {sl}')
cnt = len(sl)
s = sum(sl)
mn = min(sl)
mx = max(sl)
avg = s/cnt
print(f'Кол-во: {cnt}')
print(f'Сумма: {s}')
print(f'Минималное число: {mn}')
print(f'Максимальное число: {mx}')
print(f'Среднее арифметическое: {avg:.2f}')
#Сортировка
sc = sorted(sl)
print(f'Отсортированная копия: {sc}')
print(f'Исходный список после сортирования (не изменился): {sl}')
sl.sort()
print(f'Исходный список после sort: {sl}')

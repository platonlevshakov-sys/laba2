def example():
    value = 20
    lh = 'секретная строка' #локальная переменная
    print('Внутри  функции: ', value, lh)

example()

#Попытка обратиться к локальной переменной вне функции:
try:
    print(lh)
except NameError as e:
    print('ошибка при обращении:', e)
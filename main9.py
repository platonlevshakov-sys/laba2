print('num 9: ')
def fe(num,tg):
    for inx in range(len(num)):
        if num[inx] == tg:
            return inx
    return -1

sl = [10, 20, 30, 40, 50]
print(f'Исходник - {sl}')
print(f'Поиск 30: {fe(sl,30)}')
print(f'Поиск 99: {fe(sl,99)}')
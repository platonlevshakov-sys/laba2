def g(name): #greet*
    print(f"Привет, {name}!")
def s(num): #square
    return num**2
def mft(x,y): # max of two (без использования max())
    if x>y:
        return x
    else: return y
# Вызовы
print('num 1:')
#greet
g('Платон')
g('Егор')
#square
res1= s(8)
res2= s(-6)
print(f"Квадрат 8:{res1}")
print(f"Квадрат -6:{res2}")
#max of two
print(f"10<>25? - {mft(10,25)}")
print(f"-115<>36? - {mft(-115,36)}")

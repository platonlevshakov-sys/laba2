# Площадь прмоугольника
def Spryam(w,h):
    return w*h
# Периметр прмоугольника
def Ppryam(w,h):
    return (w+h) * 2
# Описание прямоугольника по умолчанию(un = "см")
def Dpryam(w,h,un="см"):
    area = Spryam(w,h)
    perimeter = Ppryam(w,h)
    print(f"Прямоугольник: ширина = {w} {un}, высота = {h} {un}")
    print(f"Периметр = {perimeter} {un}, Площадь = {area} {un}^2")
#Вызовы
print("num 2:")
#Без un
Dpryam(15,30)
#изменение un
Dpryam(2,6,un='m')
Dpryam(200,360,un='mm')


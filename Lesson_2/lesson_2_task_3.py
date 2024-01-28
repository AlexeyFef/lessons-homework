# находим площадь квадрата
import math
def square(side):
    if side % 1 == 0:
        return(round(side*side))
    else:
        return(math.ceil(side*side))

side = float(input('Введите сторону квадрата: '))
print('Площадь квадрата:', square(side))
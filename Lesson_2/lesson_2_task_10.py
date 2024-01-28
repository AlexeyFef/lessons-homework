# расчёт суммы на вкладе через несколько лет
def bank(x, y):
    for i in range(y):
        x *= 1.1
    return(x)

x = int(input('Введите сумму вклада: '))
y = int(input('Введите срок вклада: '))
print('Сумма на счёте через', y, 'лет составит', round(bank(x, y), 2)) 

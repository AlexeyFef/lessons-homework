# расчёт суммы на вкладе через несколько лет
def bank(summa_deposit, period_deposit):
    for i in range(period_deposit):
        summa_deposit *= 1.1
    return(summa_deposit)

summa_deposit = int(input('Введите сумму вклада: '))
period_deposit = int(input('Введите срок вклада: '))
print('Сумма на счёте через', period_deposit, 'лет составит', round(bank(summa_deposit, period_deposit), 2)) 

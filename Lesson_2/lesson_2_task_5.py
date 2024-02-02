# сезон года в зависимости от месяца года
def month_to_season(number_month):
    if 1 > number_month or number_month > 12:
        print('Такого месяца не существует')
    elif number_month in (1, 2, 12):
        print('Зима')
    elif number_month in (3, 4, 5):
        print('Весна')
    elif number_month in (6, 7, 8):
        print('Лето')
    else:
        print('Осень')

month_to_season(int(input('Введите номер месяца: ')))

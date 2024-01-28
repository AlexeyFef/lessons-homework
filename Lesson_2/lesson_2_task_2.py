# определяем, високосный ли год
def is_year_leap(year):
    if year % 4 == 0:
        return(True)
    else: 
        return(False)
visok = is_year_leap(2000)
print('Год 2000:', visok)
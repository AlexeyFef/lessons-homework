def is_year_leap(year):
    year = int(year)
    if year % 4 == 0:
        res = True
    else: 
        res = False
    return(res)
vis = is_year_leap(2000)
print('Год 2000:', vis)
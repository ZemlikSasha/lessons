"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона, к которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".
"""

def month_to_season(month):
    if month == 1 or month == 2 or month == 12:
        season = "Winter"
    elif month == 3 or month == 4 or month == 5:
        season = "Spring"
    elif month == 6 or month == 7 or month == 8:
        season = "Summer"
    elif month == 9 or month == 10 or month == 11:
        season = "Autumn"
    return season

print(month_to_season(9))

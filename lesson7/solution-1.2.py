"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""


def country(city):
    for key, value in countries_city.items():
        if city in value:
            return key

if __name__ == "__main__":

    countries_city = {
        "Belarus": ["Minsk", "Grodno", "Brest" ],
        "France": ["Paris", "Marseille", "Nice"]
    }

    city = input("beautiful city: ")
    print(country(city))

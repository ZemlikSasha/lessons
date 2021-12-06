"""
Спортсмен поставил перед собой задачу пробежать в общей сложности Х километров. В первый день спортсмен пробежал
Y километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. Определите номер дня в который
спортсмен достигнет своей цели. Оформите решение в виде программы, которая на вход принимает числа X и Y и выводит
номер найденного дня.
"""



def days_to_goal(target_distance: int, daily_distance: int):
    """
    Calculate days to goal
    """
    result_days = 0
    current_distance = 0
    while current_distance < target_distance:
        current_distance += daily_distance
        daily_distance *= 1.1
        result_days += 1
    return result_days


def main():
    target_distance = int(input("Enter target distance (km): "))
    daily_distance = int(input("Enter daily distance (km): "))
    days = days_to_goal(target_distance, daily_distance)
    print("Days to goal: ", days)


if __name__ == "__main__":
    main()


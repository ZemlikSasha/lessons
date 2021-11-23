"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
Ваша программа должна используя список имен участников выдать на выходе пары, кто и кому будет дарить,
причем сам себе человек не может подарить, дубликаты тоже не допустимы.
"""

import random

player = []

while True:
    person = input("Enter a person participating.(end to exit):\n")
    if person=="end":
        break
    player.append(person)

random.shuffle(player)
for i in range(len(player)//2):
    print(player[i],"buys for",player[i+len(player)//2])
"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт, где на первом месте
номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""


import random

list1 = (6, 7, 8, 9, 10, "J", "D", "K", "A")
list2 = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

def my_list1(x):
    A = random.choice(x)
    return A


def my_list2(y):
    B = random.choice(y)
    return B

if __name__ == "__main__":

    print(my_list1(list1), my_list2(list2))





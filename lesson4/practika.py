"""
Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
"""

my_list = [1, 5, 6, 7, 12, 15]

result = 0

for x in my_list:
    if x > 10:
        result += x 

print(result)



"""
Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).
"""

n = int(input("Enter number: "))

for x in range(1, 101):
    if x % n == 0:
        print(x)
        

"""
Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.
"""

n = int(input("Enter number: "))

index = 0
result = 0

while index <= n:
    result += index **3;
    index += 1
print(result)


"""
Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
"""

import random

x = None
while True:
    x = random.randint(1,10)
    if x == 7:
        break
print(x)



"""
Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры.
"""

n = int(input("N: "))
m = int(input("M: "))

result = 0
for x in range(n, m + 1):
   result += x ** 3
   
print(result)



"""
Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m), а также количество x этих чисел.
"""

start_number = int(input("Enter start number:"))
end_number = int(input("Enter end number:"))

# Generate elements from start_number to end_number (including)
my_count = 0
for element in range(start_number, end_number + 1):
    # Check if this element is the prime number
    is_prime = True
    for divider in range(2, element):
        # If we've found any divider the remainder of which is zero
        # So current element is not the prime number
        if divider > 1 and element % divider == 0:
            is_prime = False
            break

    # Current element is the prime number
    if is_prime:
        print(element)
        my_count += 1

print("Total count of prime numbers")
print(my_count)



"""
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ, из этих чисел составляется первый список. Далее таким же образом вводятся второй и третий списки. Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем.
"""

my_list_01 = []
my_list_02 = []
my_list_03 = []

while True:
    x = input("Enter X1: ")
    try:
        my_number = int(x)
        my_list_01.append(my_number)
    except ValueError:
        break

while True:
    x = input("Enter X2: ")
    try:
        my_number = int(x)
        my_list_02.append(my_number)
    except ValueError:
        break
        
while True:
    x = input("Enter X3: ")
    try:
        my_number = int(x)
        my_list_03.append(my_number)
    except ValueError:
        break


for x in my_list_01:
    if x in my_list_02 and x not in my_list_03:
        print(x)










        

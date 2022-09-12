# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from decimal import Decimal, ROUND_DOWN
# вычисление цифры числа Пи без необходимости вычисления предыдущих по формуле Бэйли — Боруэйна — Плаффа https://ru.wikipedia.org/wiki/Формула_Бэйли_—_Боруэйна_—_Плаффа
# n = 5
# my_pi = Decimal(sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n)))
# print(my_pi)
# print(π = my_pi.quantize(Decimal('1.000'), ROUND_DOWN))





# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input("Введите число: "))
# i = 2  # первое простое число
# list = []
# dig = number
# while i <= number:
#     if number % i == 0:
#         list.append(i)
#         number //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {dig} равны: {list}")





# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list = [input('Введите элемент: ') for i in range(int(input('Введите количество элементов: ')))]
# print(f"Список: {list}")
# new_list = []
# [new_list.append(i) for i in list if i not in new_list]
# print(f"Неповторяющиеся элементы: {new_list}")



# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('uravnenie1.txt', 'r') as file:
    a = file.read()
print(f'Многочлен 1: ', end='')    
print(a)
with open('uravnenie2.txt', 'r') as file1:
    b = file1.read()
print(f'Многочлен 2: ', end='')    
print(b)
from sympy import *
x,y,z = symbols('x y z')
c= 5*x + 8*y + 10*z + (-8)*x - 12*y + 25*z
print(f'Результат: ', end='')  
print(c)
file3 = open("result.txt", "w") 
file3.write(f"{c}")







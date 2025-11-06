#Лабораторная работа №1
#1
'''a = 5
b = int(input())
print(a*b)'''

#2
'''a = int(input())
b = int(input())
s = (a + b)**2
print(s)'''

#3
'''a, b = 15, 10
c = int(input())
print((a + b)/c)'''

#4
'''l = []
for i in range(2):
    l.append(int(input()))
print(sum(l)**2)'''

#5
'''from math import *
l = []
for i in range(3):
    l.append(int(input()))
p = sum(l)
s = sqrt(p*(p-l[0])*(p-l[1])*(p-l[2]))
print(f'Периметр = {p}, площадь = {s}')'''

#6
'''a = int(input())
b = int(input())
print((a**3 + 14)/5 * b)'''

#7
'''a = int(input())
n = int(input())
print((a**2)//n)'''

#8
'''a = int(input())
b = int(input())
if a != int(a) and b != int(b):
    print(a//b)
if a > 0 and b > 0:
    print(a*b)
    print(a % b)'''

#Задача повышенной сложности
#1
n = int(input())
minutes = n // 60
hours = minutes // 60
days = hours // 24
print(f'В {n} секунд содержится {minutes} минут, {hours} часов и {days} дней')

#2
'''n = int(input())
print(n + n**2 + n**3)'''

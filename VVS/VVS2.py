# 1
n = int(input())
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май',
         'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
         'Ноябрь', 'Декабрь']
print(month[n-1])

# 2
print('Число чётное') if int(input()) % 2 == 0 else print('Число нечётное')

# 3
n = int(input())
print('stonks') if n > 40 else print('not stonks')

# 4
def is_year_leap(year):
    if year % 4 == 0:
        print('True')
    else:
        print('False')
is_year_leap(2024)

# 5
def is_prime(n):
    n = int(input())
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

# 6
def results(a, b):
    c = (-138/2)**1.3
    d = abs((-69/28**5.1)*4)
    if a / b >= 3.6 or (c <= b <= d):
        a, b = b, a
    return a, b

# 7
list = []
for i in range(5):
    a = int(input())
    list.append(a)
if len(list) == len(set(list)):
    print('Все числа уникальные')
else:
    print('Числа не уникальные')
c = [i for i in list if abs(i) % 2 == 0]
f = [i for i in list if i < 0]
p = [i for i in list if i in range(-256, 1025)]
print(f'Колчество чётных чисел = {len(c)}.',
      f'Количество отрицательных чисел = {len(f)}',
      f'Количество чисел, принадлежащих заданному диапазону = {len(p)}')

# Задание повышенной сложности
a = int(input())
b = int(input())
c = int(input())
res = ((a**2 + b**3) / (c + 3)) / 4
print(res)
if res % 2 == 0:
    print('Число чётное')
else:
    print('Число нечётное')







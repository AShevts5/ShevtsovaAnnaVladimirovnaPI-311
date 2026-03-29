#Код из теоретической части лабораторной работы
'''from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

celsius = [[-67.0], [-34.0], [0], [34.0], [54.0], [67.0], [100]]
fahrenheit = [[-88.6], [-29.2], [32.0], [93.2], [129.2], [152.6], [212.0]]
plt.figure(figsize=(15,8), dpi=50)
plt.scatter(celsius, fahrenheit, label = 'входные значения', color = 'green', marker = '$f$')
plt.xlabel('celsius')
plt.ylabel('fahrenheit')
plt.legend()
plt.grid(True)
plt.show()

for c, f in zip(celsius, fahrenheit):
    print(f'цельсия {c} = фаренгейт {f}')

lr = LinearRegression()
lr.fit(celsius, fahrenheit)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
celsius_test = [[-50], [10], [30], [20], [10], [70], [87]]
fahrenheit_test = lr.predict(celsius_test)
fahrenheit_test

for c, f in zip(celsius_test, fahrenheit_test):
    print(f'цельсия {c} фаренгейта {f}')

x_range = np.arange(-70, 120)
y_range = x_range*1.8+32
plt.figure(figsize=(15,8), dpi=280)
plt.plot(x_range, y_range, label = 'уравнение', linewidth = '1')
plt.scatter(celsius, fahrenheit, label = 'входные значения', color = 'green')
plt.scatter(celsius_test, fahrenheit_test, label = 'предсказанное значение', color = 'blue')
plt.xlabel('celsius')
plt.ylabel('fahrenheit')
plt.legend()
plt.grid(True)
plt.show()
'''

# Задания обычной сложности
# 1
'''from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

fahrenheit = [[-67.0], [-34.0], [0], [34.0], [54.0], [67.0], [100]]
kelvin = [[218.15], [236.48333], [255.37222], [274.26111], [285.37222], [292.59444], [310.92778]]
plt.figure(figsize=(15,8), dpi=50)
plt.scatter(fahrenheit, kelvin, label = 'входные значения', color = 'green', marker = '$f$')
plt.xlabel('fahrenheit')
plt.ylabel('kelvin')
plt.legend()
plt.grid(True)
plt.show()

for f, k in zip(fahrenheit, kelvin):
    print(f'фаренгейт {f} = кельвин {k}')

lr = LinearRegression()
lr.fit(fahrenheit, kelvin)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
fahrenheit_test = [[-50], [10], [30], [20], [10], [70], [87]]
kelvin_test = lr.predict(fahrenheit_test)
kelvin_test

for f, k in zip(fahrenheit_test, kelvin_test):
    print(f'фаренгейт {f} кельвин {k}')

x_range = np.arange(-70, 120)
y_range = ((x_range-32)*5)/9 + 273.15
plt.figure(figsize=(15,8), dpi=280)
plt.plot(x_range, y_range, label = 'уравнение', linewidth = '1')
plt.scatter(fahrenheit, kelvin, label = 'входные значения', color = 'green')
plt.scatter(fahrenheit_test, kelvin_test, label = 'предсказанное значение', color = 'blue')
plt.xlabel('fahrenheit')
plt.ylabel('kelvin')
plt.legend()
plt.grid(True)
plt.show()'''

#2
#График облако точек с цветовой градацией
'''from numpy import *
import matplotlib.pyplot as plt

random.seed(42)
ages = random.randint(low=18, high=40, size=100)
heights = random.uniform(low=150, high=200, size=100)
weights = random.uniform(low=50, high=100, size=100)

plt.scatter(heights, weights, c=ages, cmap='coolwarm', s=50, alpha=0.7)
plt.title('Диаграмма зависимости роста от веса, окрашенная в зависимости от возраста')
plt.xlabel('Рост (см)')
plt.ylabel('Вес (кг)')
cbar = plt.colorbar(label='Возраст', orientation='vertical')
plt.show()'''

#Построение 3D-модели
'''import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_title('График поверхности z = x² + y²')
plt.show()'''

#Круговой график
'''import matplotlib.pyplot as plt

activities = ['Сон', 'Работа/Учёба', 'Дорога', 'Еда', 'Отдых', 'Спорт']
time_hours = [8, 9, 1.5, 1.5, 3, 1]
colors = ['steelblue', 'lightcoral', 'lightgreen', 'gold', 'violet', 'darkorange']
explode = (0, 0, 0, 0, 0.1, 0.1)
fig, ax = plt.subplots(figsize=(9, 7))
wedges, texts, autotexts = ax.pie(time_hours, explode=explode, labels=activities,
                                   colors=colors, autopct='%1.1f%%', shadow=True,
                                   startangle=140, textprops={'fontsize': 11})

ax.set_title('Как проходит мой день (в часах)', fontsize=16, fontweight='bold', pad=20)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.tight_layout()
plt.show()'''

#4
'''import math
print(f'Число е = {math.e}, число pi = {math.pi}', f'Факториал номера в журнале (23) = {math.factorial(23)}', sep = '\n')
nan_value = math.nan
print(nan_value)
print(f'Наибольший общий делитель для номера в журнале (23) и памяти телефона (256) = {math.gcd(23,256)}')'''

#Задания повышенной сложности
#1
#Создаём фигуру гиперболического параболоида

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаем сетку значений x и y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Уравнение гиперболического параболоида: z = x^2 - y^2
z = x**2 - y**2

# Создаем 3D-график
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, cmap='coolwarm', alpha=0.9,
                       linewidth=0.2, antialiased=True)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title('Гиперболический параболоид: z = x² - y²', fontsize=14)
fig.colorbar(surf, shrink=0.5, aspect=10)

ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.show()

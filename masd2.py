# Частные и множественные коэффициенты корреляции
import numpy as np
import pingouin as pg
import pandas as pd
import scipy.stats as stats
from math import sqrt

n = 14
y = [40, 45, 55, 60, 70, 65, 65, 75, 75, 80, 100, 90, 95, 85]
x1 = [9, 8, 8, 7, 6, 6, 8, 5, 5, 5, 3, 4, 3, 4]
x2 = [400, 500, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]
data = {'y': y,
        'x1': x1,
        'x2': x2,
        }
alpha = 0.05

# С помощью библиотеки
data = pd.DataFrame(data, columns=['y', 'x1', 'x2'])
print(data)

r_y12 = pg.partial_corr(data, 'y', 'x1', 'x2')
r_y21 = pg.partial_corr(data, 'y', 'x2', 'x1')
print(f"\nЧастные коэффициенты корреляции (с помощью pingouin):\n"\
    f"r_y1,2 = {r_y12.loc['pearson'].at['r']}\t"\
    f"r_y2,1 = {r_y21.loc['pearson'].at['r']}")


# С помощью формул
r_y1, c = np.corrcoef(y, x1)
r_y2, c = np.corrcoef(y, x2)
r_12, c = np.corrcoef(x1, x2)
r_y12 = (r_y1[1] - r_y2[1] * r_12[1]) / sqrt((1 - r_y2[1]**2) * (1 - r_12[1]**2))
r_y21 = (r_y2[1] - r_y1[1] * r_12[1]) / sqrt((1 - r_y1[1]**2) * (1 - r_12[1]**2))
print(f'\nЧастные коэффициенты корреляции (с помощью формул):\n'\
    f'r_y1,2 = {r_y12}\tr_y2,1 = {r_y21}\n')

# проверка гипотез
if (abs(r_y12) * sqrt(n - 2) / sqrt(1 - r_y12 ** 2)) < stats.t.ppf(0.95, n-2):
    print('Гипотеза об отсутствии корреляционной связи (r_y12) принимается')
else:
    print('Гипотеза об отсутствии корреляционной связи (r_y12) отвергается')
if (abs(r_y21) * sqrt(n - 2) / sqrt(1 - r_y12 ** 2)) < stats.t.ppf(0.95, n-2):
    print('Гипотеза об отсутствии корреляционной связи (r_y21) принимается\n')
else:
    print('Гипотеза об отсутствии корреляционной связи (r_y21) отвергается\n')

# Множественный коэффициент корреляции
R_y12 = pg.linear_regression(data[['x1', 'x2']], data['y'])
print(f"Множественный коэффициент корреляции (с помощью pingouin): R_y12 = {sqrt(R_y12.loc[0].at['r2'])}")
print(f"Множественный коэффициент детерминации (с помощью pingouin): R_y12^2 = {R_y12.loc[0].at['r2']}")

R_y12 = sqrt(1 - (1 - r_y1[1]**2) * (1 - r_y21**2))
print(f'Множественный коэффициент корреляции (с помощью формул): R_y12 = {R_y12}')
print(f'Множественный коэффициент детерминации (с помощью формул): R_y12^2 = {R_y12**2}')

if (abs(R_y12) * sqrt(n - 2) / sqrt(1 - R_y12 ** 2)) < stats.t.ppf(0.95, n-2):
    print('Гипотеза об отсутствии корреляционной связи (R_y12) принимается')
else:
    print('Гипотеза об отсутствии корреляционной связи (R_y12) отвергается')
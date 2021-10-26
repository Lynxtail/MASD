import numpy as np
import pingouin as pg
from itertools import product

n = 16
q = 2
x = [2, 3, 4, 5]
y = np.array([96.3, 95.7, 99.9, 99.4, 95.1, 97.8, 99.3, 104.9, 
    96.2, 100.1, 103.2, 104.3, 97.8, 102.2, 104.7, 108.8])
x = np.array(list(product(x, x)))

ones = np.ones(n).reshape(-1, 1)
x = np.hstack((ones, x))
print(x)

xtx = x.T.dot(x)
print(xtx)
xty = x.T.dot(y)
print(xty)

theta = np.linalg.inv(xtx).dot(xty)
print(theta)

y_ = np.mean(y)

beta0 = theta[0]
beta1 = theta[1]
beta2 = theta[2]
print(f'beta_0 (по формулам) = {beta0}\n\
beta_1 (по формулам) = {beta1}\n\
beta_2 (по формулам) = {beta2}')

print(pg.linear_regression(x, y))

print(f"beta_0 (с помощью pingouin) = {pg.linear_regression(x, y).loc[0].at['coef']}\n\
beta_1 (с помощью pingouin) = {pg.linear_regression(x, y).loc[1].at['coef']}\n\
beta_2 (с помощью pingouin) = {pg.linear_regression(x, y).loc[2].at['coef']}")

print(f'\nОценка уравнения регрессии:\n\
y = {beta0:.2f} + {beta1:.2f}x^(1) + {beta2:.2f}x^(2)')
[print(f'{beta0 + beta1 * x[i][1] + beta2 * x[i][2]:.2f} = {beta0:.2f} + {beta1:.2f} * {x[i][1]} + {beta2:.2f} * {x[i][2]}, остаток {y[i] - (beta0 + beta1 * x[i][1]) + beta2 * x[i][2]:.2f}')
for i in range(n)]

# косяки с транспонированием
# thetat = theta.reshape(-1, 1)
# xty = xty.reshape(3, 1)
# thetat_xty = theta.dot(xty)
# print(thetat_xty)
# yty = y.reshape(-1, 1).dot(y)
# print(yty)

# R_2 = (thetat_xty - n * y_**2) / (yty - n * y_**2)
# print(f'R^2 = {R_2}')
# F = (R_2 * (n - q - 1)) / ((1 - R_2) * q)

# # v(2, 16 - 2 - 1) ~ 19.42
# v_alpha = 19.42
# if F > v_alpha:
#     print('Уравнение регрессии значимо')

alpha = 0.05
if pg.linear_regression(x, y).loc[0].at['pval'] < alpha:
    print('Уравнение регрессии значимо (с помощью pingouin)')
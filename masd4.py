import numpy as np
import pingouin as pg

n = 20
x = [1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 
    5, 5, 10, 10, 10, 10, 15, 15, 15, 15]
y = [1.1, .7, 1.8, .4, 3., 1.4, 4.9, 4.4, 4.5, 7.3, 
    8.2, 6.2, 12., 13.1, 12.6, 13.2, 18.7, 19.7, 17.4, 17.1]

x_ = np.mean(x)
y_ = np.mean(y)

beta1 = sum([(y[i] - y_) * (x[i] - x_) for i in range(n)]) / sum([(x[i] - x_)**2 for i in range(n)])
beta0 = y_ - beta1 * x_
print(f'beta_0 (по формулам) = {beta0}\n\
beta_1 (по формулам) = {beta1}')


print(f"beta_0 (с помощью pingouin) = {pg.linear_regression(x, y).loc[0].at['coef']}\n\
beta_1 (с помощью pingouin) = {pg.linear_regression(x, y).loc[1].at['coef']}")

print(f'\nОценка уравнения регрессии:\n\
y = {beta0:.2f} + {beta1:.2f}x')
[print(f'{beta0 + beta1 * x[i]:.2f} = {beta0:.2f} + {beta1:.2f} * {x[i]}, остаток {y[i] - (beta0 + beta1 * x[i]):.2f}')
for i in range(n)]
import numpy as np
import pingouin as pg
from math import sqrt

def sort_rank(first, second):
    ans = [first, second]
    

def get_i(arr):
    cnt = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                cnt[i] += 1
    return cnt

n = 7
first = [31, 82, 25, 26, 53, 30, 29]
second = [21, 55, 8, 27, 32, 42, 26]
alpha = 0.05
first_i = get_i(first)
second_i = get_i(second)
print(first, first_i, '', second, second_i, '\n', sep='\n')

# коэффициент Спирмэна
tau = pg.corr(first_i, second_i, 'two-sided', 'spearman')
print(tau, '\n')
print(f"Выборочный коэффициент ранговой корреляции Спирмэна (с помощью pingouin): {tau.loc['spearman'].at['r']}")
p_val = tau.loc['spearman'].at['p-val']

tau = 1 - 6/(n**3 - n) * sum([(first_i[i] - second_i[i])**2 for i in range(n)])
print(f'Выборочный коэффициент ранговой корреляции Спирмэна (с помощью формул): {tau}')

# при альфа = 0.05
if alpha < p_val:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) принимается при уровне значимости alpha = {alpha} (с помощью pingouin)\n')
else:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) отвергается при уровне значимости alpha = {alpha} (с помощью pingouin)\n')

# S_c (n,Q) ~ 100
tau_max = 2 * 100 / 112 - 1
print(f'tau_max = {tau_max}')
if tau_max > tau:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) принимается при уровне значимости alpha = {alpha} (с помощью таблицы)\n')
else:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) отвергается при уровне значимости alpha = {alpha} (с помощью таблицы)\n')

# при альфа = 0.1
alpha = 0.1
# p_val = pg.corr(first_i, second_i, 'two-sided', 'spearman').loc['spearman'].at['p-val']
if alpha < p_val:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) принимается при уровне значимости alpha = {alpha} (с помощью pingouin)\n')
else:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) отвергается при уровне значимости alpha = {alpha} (с помощью pingouin)\n')

# S_c (n,Q) ~ 74?
tau_max = 2 * 74 / 112 - 1
print(f'tau_max = {tau_max}')
if tau_max > tau:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) принимается при уровне значимости alpha = {alpha} (с помощью таблицы)\n')
else:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) отвергается при уровне значимости alpha = {alpha} (с помощью таблицы)\n')

# коэффициент Кендалла
alpha = 0.05
tau = pg.corr(first_i, second_i, 'two-sided', 'kendall')
print(tau, '\n')
print(f"Выборочный коэффициент ранговой корреляции Кендалла (с помощью pingouin): {tau.loc['kendall'].at['r']}")
p_val = tau.loc['kendall'].at['p-val']

v = np.zeros((n, n))

data = dict(zip(first_i, second_i))

# соответствие ранжировок
print(data)

# преобразование ранжировок к виду:
# x(k) = (1, 2, 3...)   x(j) = (x_1, x_2, x_3...)
newdata = {}
for i in sorted(data):
    newdata[i] = data[i]
print(newdata)

second_i = list(newdata.values())

for q in range(n):
    for l in range(q, n):
        if second_i[q] > second_i[l]:
            v[q][l] = 1
        else:
            v[q][l] = 0

V = 0
for q in range(n-1):
    for l in range(q+1, n):
        V += v[q][l]

tau = 1 - 4 * V / (n * (n-1))
print(f'Выборочный коэффициент ранговой корреляции Кендалла (с помощью формул): {tau}')

if alpha < p_val:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) принимается при уровне значимости alpha = {alpha} (с помощью pingouin)\n')
else:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) отвергается при уровне значимости alpha = {alpha} (с помощью pingouin)\n')

# S_k (n, Q) ~ 14
tau_max = 2 * 14 / (n * (n - 1))
print(f'tau_max = {tau_max}')
if tau_max > tau:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) принимается при уровне значимости alpha = {alpha} (с помощью таблицы)\n')
else:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) отвергается при уровне значимости alpha = {alpha} (с помощью таблицы)\n')

# при альфа = 0.1
alpha = 0.1
print(p_val,'\n', alpha)
# p_val = pg.corr(first_i, second_i, 'two-sided', 'kendall').loc['kendall'].at['p-val']
if alpha < p_val:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) принимается при уровне значимости alpha = {alpha} (с помощью pingouin)\n')
else:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) отвергается при уровне значимости alpha = {alpha} (с помощью pingouin)\n')

# S_k (n,Q) ~ 1?
tau_max = 2 * 1 / (n * (n - 1))
print(f'tau_max = {tau_max}')
if tau_max > tau:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) принимается при уровне значимости alpha = {alpha} (с помощью таблицы)\n')
else:
    print(f'Гипотеза об отсутствии корреляционной связи (tau) отвергается при уровне значимости alpha = {alpha} (с помощью таблицы)\n')

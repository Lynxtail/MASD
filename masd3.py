import numpy as np
import pingouin as pg

def get_i(arr):
    cnt = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                cnt[i] += 1
    return cnt

alpha = 0.05
n = 7
first = [31, 82, 25, 26, 53, 30, 29]
second = [21, 55, 8, 27, 32, 42, 26]

# n = 10
# first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# second = [2, 3, 1, 4, 6, 5, 9, 7, 8, 10]

first_i = get_i(first)
second_i = get_i(second)

# коэффициент Спирмэна
tau = 1 - 6/(n**3 - n) * sum([(first_i[i] - second_i[i])**2 for i in range(n)])
print(f'Выборочный коэффициент ранговой корреляции Спирмэна: {tau}')

# коэффициент Кендалла
v = np.zeros((n, n))
for q in range(n):
    for l in range(q, n):
        if second[q] > second[l]:
            v[q][l] = 1
        else:
            v[q][l] = 0
V = 0
for q in range(n-1):
    for l in range(q+1, n):
        V += v[q][l]
print(v)
tau = 1 - 4 * V / (n * (n-1))
print(f'Выборочный коэффициент ранговой корреляции Кендалла: {tau}')
print(pg.corr(first, second, 'two-sided', 'spearman'))
print(pg.corr(first, second, 'two-sided', 'kendall'))
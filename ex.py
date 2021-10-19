import scipy.stats as stats
import pingouin as pg

y = [40, 45, 55, 60, 70, 65, 65, 75, 75, 80, 100, 90, 95, 85]
x1 = [9, 8, 8, 7, 6, 6, 8, 5, 5, 5, 3, 4, 3, 4]

print(stats.t.ppf(0.95, 12))
print(pg.corr(y, x1, method='pearson'))
print(stats.norm.ppf(0.975))
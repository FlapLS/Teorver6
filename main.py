import math

from statistics import NormalDist
import scipy.stats as stats

from method_task_1 import *

y = 0.9
arr = [
    63.4, 64.5,
    57.1, 51.7,
    40.1, 37.7,
    45.8, 54.9,
    35.9, 31.0,
    35.5, 19.2,
    13.6, 31.4,
    40.1
]
X_av = average_x(arr)

Sum_x_multiply = x_multiply_x(arr)

D = dispersion(arr, X_av, Sum_x_multiply)

SS = corrected_deviation(arr, D)

S = math.sqrt(SS)

t = stats.t.ppf((1 + y) / 2, len(arr) - 1)

E = t * S / math.sqrt(len(arr))

m_min = round(X_av - E, 2)

m_max = round(X_av + E, 2)

print("Задание №1 "+str(m_min) + " < " + " m " + " < " + str(m_max))

n = 100

y2 = 0.98

X_av2 = 82

Sum_x_multiply_2 = 686800

t_y = (1 + y2) / 2

F_y = NormalDist().cdf(t_y)

deviation_2 = Sum_x_multiply_2 / n - X_av2 * X_av2

deviation = math.sqrt(deviation_2)

E=(F_y * deviation)/math.sqrt(n)

m_min_2=round(X_av2-E,2)

m_max_2=round(X_av2+E,2)

print("Задание №2 "+str(m_min_2) + " < " + " m " + " < " + str(m_max_2))
# f(x) = x^3 - 6x^2 + 4x + 12
#Определить корни
#Найти интервалы, на которых функция возрастает
#Найти интервалы, на которых функция убывает
#Построить график
#Вычислить вершину
#Определить промежутки, на котором f > 0
#Определить промежутки, на котором f < 0

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 4*x + 12

# Определение корней
def find_roots():
    roots = np.roots([1, -6, 4, 12])
    return roots

# Нахождение интервалов, на которых функция возрастает
def find_increasing_intervals():
    intervals = []
    x = sp.symbols('x')
    critical_points = sp.solve(sp.diff(f(x), x), x)

    if f(critical_points[0]) > f(critical_points[0] - 1):
        intervals.append((float('-inf'), critical_points[0]))

    for i in range(len(critical_points) - 1):
        interval_start = critical_points[i]
        interval_end = critical_points[i + 1]
        if f(interval_end) > f(interval_start):
            intervals.append((interval_start, interval_end))

    if f(critical_points[-1]) > f(critical_points[-1] + 1):
        intervals.append((critical_points[-1], float('inf')))

    return intervals

# Нахождение интервалов, на которых функция убывает
def find_decreasing_intervals():
    intervals = []
    x = sp.symbols('x')
    critical_points = sp.solve(sp.diff(f(x), x), x)

    if f(critical_points[0]) < f(critical_points[0] - 1):
        intervals.append((float('-inf'), critical_points[0]))

    for i in range(len(critical_points) - 1):
        interval_start = critical_points[i]
        interval_end = critical_points[i + 1]
        if f(interval_end) < f(interval_start):
            intervals.append((interval_start, interval_end))

    if f(critical_points[-1]) < f(critical_points[-1] + 1):
        intervals.append((critical_points[-1], float('inf')))

    return intervals

# Построение графика
def plot_graph():
    x = np.linspace(-2, 6, 100)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции f(x) = x^3 - 6x^2 + 4x + 12')
    plt.grid(True)
    plt.show()

# Вычисление вершины
def find_vertex():
    x = sp.symbols('x')
    derivative = sp.diff(f(x), x)
    critical_points = sp.solve(derivative, x)
    vertex_x = critical_points[0]
    vertex_y = f(vertex_x)
    return vertex_x, vertex_y

# Определение промежутков, на которых f > 0
def find_positive_intervals():
    x = sp.symbols('x')
    critical_points = sp.solve(sp.diff(f(x), x), x)
    intervals = []

    # Check intervals between critical points
    for i in range(len(critical_points) - 1):
        interval_start = critical_points[i]
        interval_end = critical_points[i + 1]
        interval = sp.Interval(interval_start, interval_end)
        if f(x).subs(x, interval_start) > 0:
            intervals.append(interval)

    # Check intervals beyond the first and last critical points
    if f(x).subs(x, critical_points[0]) > 0:
        intervals.insert(0, sp.Interval(float('-inf'), critical_points[0]))
    if f(x).subs(x, critical_points[-1]) > 0:
        intervals.append(sp.Interval(critical_points[-1], float('inf')))

    return intervals

# Определение промежутков, на которых f < 0
def find_negative_intervals():
    x = sp.symbols('x')
    critical_points = sp.solve(sp.diff(f(x), x), x)
    intervals = []

    # Check intervals between critical points
    for i in range(len(critical_points) - 1):
        interval_start = critical_points[i]
        interval_end = critical_points[i + 1]
        interval = sp.Interval(interval_start, interval_end)
        if f(x).subs(x, interval_start) < 0:
            intervals.append(interval)

    # Check intervals beyond the first and last critical points
    if f(x).subs(x, critical_points[0]) < 0:
        intervals.insert(0, sp.Interval(float('-inf'), critical_points[0]))
    if f(x).subs(x, critical_points[-1]) < 0:
        intervals.append(sp.Interval(critical_points[-1], float('inf')))

    return intervals

# Пример использования всех методов
print("Корни функции:", find_roots())
print("Интервалы возрастания:", find_increasing_intervals())
print("Интервалы убывания:", find_decreasing_intervals())
print("Вершина функции:", find_vertex())
print("Промежутки, на которых f > 0:", find_positive_intervals())
print("Промежутки, на которых f < 0:", find_negative_intervals())
plot_graph()
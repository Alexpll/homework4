import matplotlib.pyplot as plt
import numpy as np


def derivative_func1(func, x, eps):
    return (func(x + eps) - func(x)) / eps


def derivative_func2(func, x, eps):
    return (func(x) - func(x - eps)) / eps


def derivative_func3(func, x, eps):
    return (func(x + eps) - func(x - eps)) / (2 * eps)


def func(x):
    return x ** 3


eps = 1e-7
x = np.linspace(-5, 5, 100)
y = func(x)
# y_der = [derivative_func1(func, arg, eps) for arg in x]
# y_der = [derivative_func2(func, arg, eps) for arg in x]
y_der = [derivative_func3(func, arg, eps) for arg in x]

plt.plot(x, y_der, "r")
plt.show()

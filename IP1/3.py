import numpy as np


def func(x):
    return x ** 2


def integration1(func, a, b, eps):
    total = 0
    for x in np.arange(a, b, eps):
        total += func(x) * eps
    return total


def integration2(func, a, b, eps):
    total = 0
    for x in np.arange(a, b, eps):
        total += func(x + eps) * eps
    return total


def integration3(func, a, b, eps):
    total = 0
    for x in np.arange(a, b, eps):
        total += (func(x) + func(x + eps)) / 2 * eps
    return total


eps = 0.00001
a = -1
b = 2
print(integration1(func, a, b, eps))
print(integration2(func, a, b, eps))
print(integration3(func, a, b, eps))

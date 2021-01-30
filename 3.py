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
        total += func(x + eps) * eps  # вот здесь func(x + eps) func(x) + func(x +eps) / 2
    return total


def integration3(func, a, b, eps):
    total = 0
    for x in np.arange(a, b, eps):
        total += (func(x) + func(x + eps)) / 2 * eps  # вот здесь func(x + eps) func(x) + func(x +eps) / 2
    return total


eps = 0.00001
a = -1
b = 2
print(integration1(func, a, b, eps))
print(integration2(func, a, b, eps))
print(integration3(func, a, b, eps))
# схема следующей точки(передвинуть)(б) + схема трапеции(взять между двумя точками) (а + б / 2)
# трапеция полусуммы

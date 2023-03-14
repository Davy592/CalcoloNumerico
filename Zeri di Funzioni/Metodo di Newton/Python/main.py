from numpy import *


def f(x, ord=0):
    match ord:
        case 0:
            y = x - cos(x)
        case 1:
            y = 1 + sin(x)
        case _:
            raise Exception("Ordine di derivazione non implementato")
    return y


def newton(fun, x0, itmax=1e4, tol=1e-15):
    it = 0
    arresto = 0
    while (not arresto and it < itmax):
        it += 1
        x1 = x0 - fun(x0) / fun(x0, 1)
        arresto = abs(x1 - x0) < tol
        x0 = x1
    if not arresto:
        print("Precisione non raggiunta")
    return x1, it


print(newton(f, pi / 2))

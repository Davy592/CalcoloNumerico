from math import *
from errors import *


def f(x):
    return x - cos(x)


def g(x):
    return x - exp(-x)


def h(x):
    return 6 * x + 2


def zeros(fun, a, b, stopFun, itmax: int = 1e4, tol: float = 1e-15):
    exc = MyExc
    n = ceil(log2((b - a) / tol))
    fa = fun(a)
    fb = fun(b)
    c = (a + b) / 2
    fc = fun(c)
    it = 0
    exc.checkMulGreater0(fa, fb, "La funzione non cambia segno agli estremi dell'intervallo")
    while not stopFun(a, b, tol) and it < itmax:
        if fc == 0:
            break
        elif fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
        c = (a + b) / 2
        fc = fun(c)
        it += 1
    if not stopFun(a, b, tol):
        if stopFun == absoluteStop:
            print(f"Precisione non raggiunta, sono necessarie almeno {n} iterazioni")
        else:
            print("Precisione non raggiunta")
    return c, it


def zero(fun, a, b, option: str, itmax: int = 1e4, tol: float = 1e-15, ):
    errorDict = {"abs": absoluteStop, "rel": relativeStop, "mix": mixedStop}
    if option not in errorDict:
        option = "abs"
    return zeros(fun, a, b, errorDict[option], itmax, tol)


print(zero(f, 0, pi / 2, "abs"))
# print(zero(f, 0, pi/2, "rel"))
print(zero(f, 0, pi / 2, "mix"))
print(zero(g, 0, pi / 2, "abs"))
# print(zero(g, 0, pi/2, "rel"))
print(zero(g, 0, pi / 2, "mix"))
print(zero(h, -0.5, 0.5, "abs"))
# print(zero(h, -0.5, 0.5, "rel"))
print(zero(h, -0.5, 0.5, "mix"))

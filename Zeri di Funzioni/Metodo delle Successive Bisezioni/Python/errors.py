class MyExc(Exception):
    def checkMulGreater0(x: float, y: float, str):
        try:
            if x * y > 0:
                raise Exception(str)
        except:
            raise

    def checkEqual0(x, str):
        try:
            if x == 0:
                raise Exception(str)
        except:
            raise


def absoluteStop(a, b, tol):
    return max(a, b) - min(a, b) < tol


def relativeStop(a, b, tol):
    exc = MyExc
    exc.checkEqual0(min(abs(a), abs(b)),
                    "E' stata eseguita una divisione per 0 nel calcolo dell'errore, utilizzare la versione mista")
    return (max(a, b) - min(a, b)) / min(abs(a), abs(b)) < tol


def mixedStop(a, b, tol):
    return (max(a, b) - min(a, b)) / (1 + min(abs(a), abs(b))) < tol

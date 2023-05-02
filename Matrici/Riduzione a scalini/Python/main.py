from numpy import *


def scalini(A):
    n, m = A.shape
    tol = 1e-15
    i = j = 0
    trovato = True
    while i < n and j < m and trovato:
        trovato = False
        k = j
        while k < m and not trovato:
            h = i
            while h < n and not trovato:
                if abs(A[h, k]) > tol:
                    A[[i, h]] = A[[h, i]]
                    j = k
                    trovato = True
                h += 1
            k += 1
        if trovato:
            for k in range(i + 1, n):
                A[k] = A[k] - A[i] * (A[k, j] / A[i, j])
            i += 1
            j += 1
    return triu(A)


print(f"{scalini(array([[1, 2, 3], [0, 1, 2], [0, 0, 1]]))}\n")
print(scalini(array([[1, -2, -3, 0, 1, 0], [-2, 4, 6, 0, -1, 2], [1, 0, 1, -2, 1, 0], [0, -2, -4, 2, 2, 1]])))

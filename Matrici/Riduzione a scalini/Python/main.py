from numpy import *


def riduzioneScalini(A):
    A = copy(A)
    righe, colonne = shape(A)
    tol = 1e-15
    j = i = 0
    trovato = True
    while i < righe - 1 and trovato:
        trovato = abs(A[i, j]) > tol
        while j < colonne and not trovato:
            h = i
            while h < righe and not trovato:
                if abs(A[h, j]) > tol:
                    trovato = True
                    j -= 1
                    A[[h, i]] = A[[i, h]]
                h += 1
            j += 1
        if trovato:
            for k in range(i + 1, righe):
                A[k] = A[k] - A[i] * (A[k, j] / A[i, j])
        i += 1
        j += 1
    return triu(A)


print(f"{riduzioneScalini(array([[1, 2, 3], [0, 1, 2], [0, 0, 1]]))}\n")
print(riduzioneScalini(array([[1, -2, -3, 0, 1, 0], [-2, 4, 6, 0, -1, 2], [1, 0, 1, -2, 1, 0], [0, -2, -4, 2, 2, 1]])))

#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

def polinomio_lagrange(X, Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)

    def polinomio(x):
        result = 0;
        for (i, value1) in enumerate(X):
            currentY = Y[i]
            for (j, value2) in enumerate(X):
                if i != j:
                    currentY = currentY * (x - value2) / (value1 - value2)
            result += currentY
        return result       
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...
    X = [1,3,5,7]
    Y = [-2,1,2,-3]
    polinomio = polinomio_lagrange(X,Y)
    print(polinomio(3))

    
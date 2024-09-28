

def multiplicador(*args):
    multiplicador = 1
    for i in args:
        multiplicador *= i
    return multiplicador


def epar(x):
    return True if x % 2 == 0 else False


# forma empacotada
multiplication = multiplicador(1, 2, 3, 4, 5, 6, 7, 8, 9)

# forma desempacotada
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
multiplication2 = multiplicador(*numeros)
print(epar(multiplication2))

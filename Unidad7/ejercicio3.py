def sumarNaturales(n):
    if n == 0:
        return 0
    else:
        return n + sumarNaturales(n-1)

n = 9

resultado = sumarNaturales(n)

print(resultado)
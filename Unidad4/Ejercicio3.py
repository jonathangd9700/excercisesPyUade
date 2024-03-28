import random;

claveMaestra = str(random.randint(1000,99999))
print(f"La clave maestra es: {claveMaestra}")

def clave(claveMaestra):
    claveImpares = [claveMaestra[i] for i in range(len(claveMaestra)) if i % 2 == 0]
    clavePares = [claveMaestra[i] for i in range(len(claveMaestra)) if i % 2 != 0]
    return claveImpares, clavePares

claveUno, claveDos = clave(claveMaestra)
print(f"Clave impares: {claveUno}")
print(f"Clave pares: {claveDos}")
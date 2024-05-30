def crearCola():
    return []

def encolar(cola,elemento):
    cola.append(elemento)

def desencolar(cola):
    return cola.pop(0)

def primero(cola):
    return cola[0]

def estaVacia(cola):
    return len(cola) == 0
    
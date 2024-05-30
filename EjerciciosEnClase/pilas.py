
def crearPila():
    return []

def apilar(pila,elemento):
    pila.append(elemento)

def desapilar(pila):
    return pila.pop()

def tope(pila):
    return pila[-1]

def esVacia(pila):
    return len(pila) == 0
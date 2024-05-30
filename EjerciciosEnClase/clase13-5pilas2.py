from pilas import *

def cargarPueblo(pila):
    while True:
        pueblo = input("Ingrese el pueblo que desea cargar. -1 para finalizar: \n")
        if pueblo == "-1":
            break
        else:
            apilar(pila,pueblo)
    return pila
        
    
def caminoRegreso(pila):
    pilaAux = crearPila()
    print(f"El camino de regreso es: ", end="")
    while esVacia(pila) == False:
        pilaAux = desapilar(pila)
        print(f"{pilaAux}", end = " ")
def main():
    pila = crearPila()
    ciudades = cargarPueblo(pila)
    if esVacia(pila) == True:
        print("No se cargaron archivos")
    else:
        caminoRegreso(ciudades)
    
main()

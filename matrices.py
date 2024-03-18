def cargarMatriz(filas,columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for c in range(columnas):
            
            matriz[i].append(int(input("Ingrese un valor")))
        
    return matriz
def main():
    filas = int(input("Ingrese la cantidad de filas"))
    columnas = int(input("Ingrese la cantidad de columnas"))
    matriz_cargada = cargarMatriz(filas,columnas)
    return matriz_cargada
def recorrer_matriz(matriz):
    for f in range (len(matriz)):
        for c in range (len(matriz[f])):
            print(matriz[f][c], end = " ")
        print()
matriz = main()
print(matriz)
recorrer_matriz(matriz)
suma = 0
def calcularSuma(suma):
    for i in range(1,2):
        suma += i
        print(suma)
    if suma < 30:
        calcularSuma(suma)
    else:
        print("Fin del programa")
        
        
calcularSuma(suma)
#Unidad 4 ejercicio 1

cadena = "anita lava la tina";
largoCadena = len(cadena)-1
posInicio = 0
posFinal = largoCadena
capicua = True
while posInicio <= posFinal:
    while cadena[posInicio] == " ":
        posInicio+=1
    while cadena[posFinal] == " ":
        posFinal -=1
    if cadena[posInicio] != cadena[posFinal]:
        capicua = False
    posInicio+=1
    posFinal-=1
        
if capicua == True:
    print("Es capicua")
else:
    print("No es capicua")


cadena = "El número de teléfono es 4356-7890"

def cortarCadena(pos,caract,cadena):
    i=0
    frase = []
    while i <= caract:
        recorte = slice(pos,pos+i)
        i+=1
    return cadena[recorte]

recortado = cortarCadena(25,9,cadena)

print(recortado)

cadena = "El número de teléfono es 4356-7890"

"""
#Con slice()

def cortarCadena(pos,caract,cadena):
    i=0
    frase = []
    while i <= caract:
        recorte = slice(pos,pos+i)
        print(recorte)
        i+=1
    return cadena[recorte]

recortado = cortarCadena(25,9,cadena)

print(recortado)
"""

"""
def cortarCadena(inicio,caract,cadena):
    final = inicio + caract
    fraseFinal = cadena[inicio:final]
    return fraseFinal
"""

#Sin slice()

def cortarCadena(inicio,caract,cadena):

    frase = []
    fraseFinal = ""
    fin = (inicio + caract)-1
    while inicio <= fin:
        frase.append(cadena[inicio])
        inicio+=1
    for i in range(len(frase)):
        fraseFinal += frase[i]
    return fraseFinal

frase = cortarCadena(25,9,cadena)
print(frase)
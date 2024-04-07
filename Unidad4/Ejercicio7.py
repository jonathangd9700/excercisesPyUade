
cadena = "El número de teléfono es 4356-7890"
# Ejercicio 7

def eliminarSubcadena(inicio,caracteres,cadena):
    fin = inicio+caracteres
    listaCadena = []
    cadenaResultante = ""
    #Paso cada caracter de la cadena como un elemento en la lista para luego borrar por indices con del
    for i in range(len(cadena)):
        listaCadena.append(cadena[i])
    #Acá voy borrando caracter por caracter desde el inicio seleccionado hasta el final, como se van eliminando elementos, voy restandole 1 al final
    while inicio < fin:
        del listaCadena[inicio]
        fin-=1
    #De la lista resultante, paso cada elemento nuevamente a una cadena
    for i in range(len(listaCadena)):
        cadenaResultante += listaCadena[i]
    return cadenaResultante

frase = eliminarSubcadena(25,9,cadena)
print(frase)


def eliminarSubcadena(inicio,caract,cadena):
    



    
def ingresarNum():
    try:
        num = int(input("Ingrese un número entero"))
        return num
    except ValueError as e:
        raise ValueError("Número inválido ingresado")
        

def main():
    while True:
        try:
            resultado = ingresarNum()
            print(resultado)
            break;
        except ValueError as e:
            print(e)
    
    
main()


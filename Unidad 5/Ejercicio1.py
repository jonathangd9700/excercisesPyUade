def ingresarNum():
    try:
        num = int(input("Ingrese número"))
        return num
    except ValueError as e:
        raise ValueError ("Dato incorrecto ingresado")



        
def main():
    while True:
        try:
            result = ingresarNum()
            print(result)
            break
        except ValueError as e:
            print(e)


main()
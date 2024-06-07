def cargarHuespedes():
    lista = []
    dni = input("Ingrese su DNI. -1 para finalizar")
    while dni != "-1":
        lista.append(dni)
        nombre = input("Ingrese su nombre")
        apellido = input("Ingrese su apellido")
        fechaIngreso = input("Ingrese la fecha de ingreso. (DDMMAAAA)")
        fechaEgreso = input("Ingrese la fecha de egreso. (DDMMAAAA)")
        while int(fechaEgreso) <= int(fechaIngreso):
            fechaEgreso = input("Ingrese una fecha de egreso válida. (DDMMAAAA)")
        lista.append(nombre)
        lista.append(apellido)
        lista.append(fechaIngreso)
        lista.append(fechaEgreso)
        dni = input("Ingrese su DNI. -1 para finalizar")
    return lista

resultado = cargarHuespedes()

print(resultado)
    

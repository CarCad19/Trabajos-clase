#Tanque de agua

litros = float(input("Ingrese la cantidad de litros en el tanque: "))
if litros < 250:
    print("La llave debe estar abierta")
elif litros > 450:
    print("La llave debe estar cerrada")
else:
    print("El tanque está en el rango correcto")
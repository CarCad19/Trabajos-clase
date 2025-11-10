#Número primo entre 0 y 20

num = int(input("Ingrese un número entre 0 y 20: "))
if num in [2, 3, 5, 7, 11, 13, 17, 19]:
    print("Es un número primo")
else:
    print("No es un número primo")
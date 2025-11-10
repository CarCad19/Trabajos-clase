#Número dentro de tres intervalos abiertos

x = int(input("Ingrese el número: "))

a1 = int(input("Inicio del intervalo 1: "))
b1 = int(input("Fin del intervalo 1: "))

a2 = int(input("Inicio del intervalo 2: "))
b2 = int(input("Fin del intervalo 2: "))

a3 = int(input("Inicio del intervalo 3: "))
b3 = int(input("Fin del intervalo 3: "))

if (a1 < x < b1) or (a2 < x < b2) or (a3 < x < b3):
    print("El número está dentro de un intervalo")
else:
    print("El número está fuera de los intervalos")
#Número dentro del intervalo cerrado

minimo = int(input("Ingrese el valor mínimo: "))
maximo = int(input("Ingrese el valor máximo: "))
x = int(input("Ingrese el número: "))
if minimo <= x <= maximo:
    print("El número está dentro del intervalo")
else:
    print("El número está fuera del intervalo")

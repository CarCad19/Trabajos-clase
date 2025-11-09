#numero mayor entre 4

print("Ingrese 4 numeros y calcularemos cual es el mayor")

n1=float(input("Ingrese el numero 1: "))
n2=float(input("Ingrese el numero 2: "))
n3=float(input("Ingrese el numero 3: "))
n4=float(input("Ingrese el numero 4: "))

#If

if(n1>n2 and n1>n3 and n1>n4):
    print("El primer numero es el mayor")
elif(n2>n1 and n2>n3 and n2>n4):
    print("El segundo numero es el mayor")
elif(n3>n1 and n3>n2 and n3>n4):
    print("El tercer numero es el mayor")
else:
    print("El cuarto numero es el mayor")
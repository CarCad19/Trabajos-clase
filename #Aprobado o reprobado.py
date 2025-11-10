#Aprobado o reprobado

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))
definitiva = (n1 + n2 + n3 + n4 + n5) / 5
if definitiva > 3.5:
    print("Gana el curso")
else:
    print("Pierde el curso")
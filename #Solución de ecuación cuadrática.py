#Solución de ecuación cuadrática

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
discriminante = b**2 - 4*a*c
if a != 0 and discriminante >= 0:
    print("La ecuación tiene solución")
else:
    print("La ecuación no tiene solución")
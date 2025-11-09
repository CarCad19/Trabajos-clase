#Rango 35-78 y 93-45

print("vamos a ver si tu numero está dentro de los siguientes rangos")
print("(3.5,7.8], [9.3,4.5)[23.4,45.3]")
x=float(input("Ingrese un numero: "))

#if

if(x>3.5 and x<=7.8 or x>=9.3 and x<4.5 or x>=23.4 and x<=45.3):
    print("Está en el rango")
else:
    print("No está en el rango")
    
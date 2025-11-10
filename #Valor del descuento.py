#Valor del descuento

print("Dependiendo del tipo del articulo, habra un descuento diferente")

y=float(input("Ingrese el valor articulo: "))
x=int(input("Ingrese el tipo para ver su descuento: "))

descuento1=y*0.125
descuento2=y*0.083
descuento3=y*0.032
#if

if(x==1):
    print("Su articulo tiene un descuento de: ", descuento1)
elif(x==2):
    print("Su articulo tiene un descuento de: ", descuento2)
elif(x==3):
    print("Su articulo tiene un descuento de: ", descuento3)
else:
    print("Su estupido articulo no tiene descuento pedazo de lok")

#Mayor edad

nombre=str(input("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))


#If
if(edad>=18):
    MensajeEdad="mayor de edad"
else:
    mensajeEdad="menor de edad"

print("Hola", nombre,"Usted es ",mensajeEdad)

#valor descuento 8

tipo = input("Ingrese el tipo de artículo (textil, electrodoméstico, cocina, videojuego): ")
precio = float(input("Ingrese el precio del artículo: "))

if tipo.lower() == "textil":
    descuento = 0
elif tipo.lower() == "electrodoméstico":
    descuento = precio * 0.037
elif tipo.lower() == "cocina" or tipo.lower() == "elementos de cocina":
    descuento = precio * 0.042
elif tipo.lower() == "videojuego" or tipo.lower() == "video juego":
    descuento = precio * 0.078
else:
    descuento = 0

print("El valor del descuento es:", descuento)
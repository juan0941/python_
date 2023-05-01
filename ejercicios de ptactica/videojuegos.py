edad = int(input("ingrese la edad del cliente: "))
precio_entrada = 0
if edad <= 4:
    precio_entrada = 0
elif edad < 18:
    precio_entrada = 4000
else:
    precio_entrada = 6000

print("el precio de su entrada es de: ", precio_entrada)

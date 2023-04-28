nom_t = str(input("ingrese el nombre del trabajador: "))
codigo = str(input("ingrese el codigo de trabajador: "))
productos = int(input("ingrese cuantos productos vendio en el mes: "))
bonificacion = 0
if productos >= 35:
    bonificacion = 200000

if productos < 35:
    bonificacion = 100000

if productos < 10:
    bonificacion = 50000

print(nom_t, "su bonificacion por vender ",
      productos, "productos es de ", bonificacion)

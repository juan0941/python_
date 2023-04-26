num=int(input("ingrese la cantidad de kilos de harina que desea"))
kilo=500
if num>10:
    kilo=kilo-100
precio=kilo*num
print("el valor total de ",num," kilos de harina es: ",precio)
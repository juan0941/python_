lista_1 = []
for i in range(5):
    num1 = int(input("ingrese un numero para la lista numero 1: "))
    lista_1.append(num1)

print("                              ")

lista_2 = []
for i in range(5):
    num2 = int(input("ingrese un numero para la lista numero 2: "))
    lista_2.append(num2)

print("                              ")
lista_3 = []
for i in range(len(lista_2)):
    suma = lista_1[i]+lista_2[i]
    lista_3.append(suma)
print("LA LISTA NUMERO 1")
print(lista_1)
print("                              ")
print("LA LISTA NUMERO 2: ")
print(lista_2)
print("                              ")
print("EL RESULTADO DE LA SUMA DE LAS DOS LISTAS ES: ")
print(lista_3)

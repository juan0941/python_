lista = []
for i in range(5):
    frutas = str(
        input("ingrese una lista de frutas una por una y finalice con un guion: "))
    lista.append(frutas)
print(lista)

for a in lista:
    for l in a:
        print(l, end=("   "))

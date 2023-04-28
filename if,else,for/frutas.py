lista = []
for i in range(5):
    frutas = str(
        input("ingrese una lista de frutas una por una: "))
    lista.append(frutas)
    # la fruta finaliza en guion para separar cada fruta cuando se imprima letra por letra y se vea mas organizado
print("                           ")
print(lista)
print("                           ")
for a in lista:
    for l in a:
        print(l, end=(" - "))

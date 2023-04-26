# este programa tiene una cadena de palabras, el usuario ingresa una letra
# y imprime la palabra con la que se inicializa esa letra
palabras = ["piensa", "sueña", "cree", "atrévete",]

letra = str(input("ingrese una letra para buscar la palabra: "))
for i in palabras:
    if i[0] == letra:
        print(i)

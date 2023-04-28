num = int(input("ingrese un numero para imprimir la tabla de multiplicar: "))
print("LA TABLA DE MULTIPLICAR DEL NUMERO ", num, " ES: ")
for i in range(1, 11):
    print(f'{num} x {i} = {i * num}')

num=int(input("ingrese un numero"))

if num>1:
    cont=0
    for i in range(2,num):
      r=num%i
    if r==0:
         cont+=1
              
    if cont==0:
       print("el numero {} es un numero primo".format(num))
    else:
       print("el numero {} no es un numero primo".format(num))

else:
    print("el numero {} no es un numero primo".format(num))


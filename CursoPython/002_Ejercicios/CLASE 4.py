"""
numero = 0
lista=[]
while numero < 35:
    print (numero)
    numero = numero + 1
    lista.append (numero)
print(lista)


lista=[]
for numero in range (1,36):
    lista.append (numero)
print(lista)


limite_inf = int (input("ingrese en donde empezar: "))
limite_sup = int (input("ingrese donde terminar: "))

lista=[]
for numero in range (limite_inf,limite_sup+1):
    lista.append (numero)
print(lista)
"""

palabra = input("ingrese una palabra: ")
lista=[]

for numero in range (0,len(palabra)):
    lista.append(palabra[numero])
print= (lista)


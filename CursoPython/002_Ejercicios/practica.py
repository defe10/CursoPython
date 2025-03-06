""" lista = []
for numero in range (1,36):
    lista.append (numero)
print (lista) 

numero_inf= int(input("Inserte el número desde: "))
numero_sup= int(input("Inserte el número hasta: "))
lista = []
for numero in range (numero_inf, numero_sup +1):
    lista.append (numero)
print(lista)

palabra = input("ingrese una palabra: ")
lista=[]

for numero in range (0,len(palabra)):
    lista.append(palabra[numero])

print(lista)



cadena = input("Escribe una frase: ")
lista = []
for posicion in range (0, len(cadena)):
    caracter = cadena [posicion]
    if caracter != " ":
        lista.append (caracter)
        
print(lista)


numeros = [1,2,3,4,5,6,7,8,9,2,3,4,5,2,2]
tupla_numeros = tuple(numeros)

numero_usuario= int(input("Ingrese un número del 1 al 10: "))

contador= 0
for posicion in range (0,len(tupla_numeros)):
    numero = tupla_numeros [posicion]
    if numero == numero_usuario:
        contador = contador+1

print(f"El {numero_usuario} se repite {contador} veces en la lista")


meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


mes_usuario= int(input("Ingrese un número del 1 al 12: "))
if 1<= mes_usuario <= 12:
    contador= meses[mes_usuario-1]
    print (f"Su número corresponde al mes de {contador}")
else:
    print (f"Su número no está en el rango del 1 al 12")

numeros=[8,5,6,3,9,1,2,5,7,8,4,0,8,6,4,2,1,4,5,6]
tupla_numeros = tuple(numeros)

indice= int(input("ingrese una ubicación: "))

if 1 <= indice <= len(tupla_numeros): 
    ubicacion= tupla_numeros[indice-1]
    print (f"su ubicación corresponde al:  {ubicacion}")
else:
    print(f"su ubicación no corresponde")


mes = {"enero": 31, "febrero": 28, "marzo": 31, "abril": 30, "mayo": 31, "junio": 30, "julio": 31, "agosto": 30, "septiembre":31, "octubre": 30, "noviembre": 31, "diciembre":30}
mes_usuario = str(input("ingrese un mes: "))

print (f"el mes de {mes_usuario} tiene {mes [mes_usuario]} días")"""




alumno = {"nombre": "Casoni", }



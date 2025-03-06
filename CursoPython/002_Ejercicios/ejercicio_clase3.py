"""

"""
Ejercicio 1
"""

numero_cliente = int(input("Ingrese su número de cliente: "))
 if numero_cliente == 1000:
     print("Ganaste un premio")
 else:
     print("llorar")


 """
 Ejercicio 2
 """

 Numero_1 = int(input("Ingrese un número: "))
 Numero_2 = int(input("Ingrese un número: "))
 if Numero_1 > Numero_2:
     print(Numero_1 , "es mayor que" , Numero_2)
 else:
      print(Numero_2 , "es mayor que" , Numero_1)

 """
 Ejercicio 3
 """
 Numero_1 = int(input("Ingrese un número: "))
 Numero_2 = int(input("Ingrese un número: "))

 if Numero_1 > Numero_2:
     print("el número menor es: " , Numero_2)
 elif Numero_1 == Numero_2:
     print(Numero_1 , "y" , Numero_2 , "son iguales")
 else: 
     print("el número menor es: " , Numero_1)

"""
Ejercicio 4 : bucle
"""

contador = 100
while contador <= 200:
    print( contador)
    contador = contador + 1



while True:
    print("hola")

"""

orden = input("Quiere continuar con el programa?: ")
while orden == "si":
    print("continuar")
    orden = input("Quiere continuar con el programa?: ")
print("FIN")

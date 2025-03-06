"""1. Diseña una función que tome como parámetro 2 números, y que devuelva una lista que contenga TODOS los números enteros entre estos 2 incluyendo AMBOS parámetros.
Ejemplo: los parámetros para mi función son 1 y 9, por lo tanto, mi función retornara: [1,2,3,4,5,6,7,8,9]

def numeros (numero1, numero2):
    lista = []
    if numero1 <= numero2:

        for i in range (numero1, numero2 +1):
            lista.append(i)
    
    else:

        for i in range (numero1, numero2 -1, -1):
            lista.append(i)

    return lista



print (numeros (12, 9))
print (numeros (9, 12))


2. Escribir una función que tome como parámetro 2 números, y retorne una lista con todos los números pares entre estos, EXCLUYENDO a los parámetros.
Ejemplo: los parámetros son 4 y 9, por lo tanto, la función retornara: [6,8]"""


def numeros (numero1, numero2):
    lista=[]

    if numero1 <= numero2:

        if numero1 %2 != 0:
            numero1 = numero1 +1
        
        elif numero1 %2 == 0:
            numero1 = numero1 +2

        elif numero2 %2 != 0:
            numero2 = numero2 -1
        
        elif numero2 %2 == 0:
            numero2 = numero2 -2


        for i in range (numero1, numero2, 2):
                lista.append(i)
    
    else:
         
        if numero1 %2 != 0:
            numero1 = numero1 -1
        
        elif numero1 %2 == 0:
            numero1 = numero1 -2

        elif numero2 %2 != 0:
            numero2 = numero2 +1
        
        elif numero2 %2 == 0:
            numero2 = numero2 +2
         
        for i in range (numero1, numero2, -2):
                lista.append(i)



    return lista


print (numeros (1, 9))
print (numeros (9,1))



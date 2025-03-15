"""
Federico Casoni - Sabados presencial


1. Diseña una función que tome como parámetro 2 números, y que devuelva una lista que contenga TODOS los números enteros entre estos 2 incluyendo AMBOS parámetros.
Ejemplo: los parámetros para mi función son 1 y 9, por lo tanto, mi función retornara: [1,2,3,4,5,6,7,8,9]"""

def num_usuario (numero1, numero2):
    lista = []
    if numero1 <= numero2:

        for i in range (numero1, numero2 +1):
            lista.append(i)
    
    else:

        for i in range (numero1, numero2 -1, -1):
            lista.append(i)

    return lista



print (num_usuario (12, 9))
print (num_usuario (9, 12))


"""2. Escribir una función que tome como parámetro 2 números, y retorne una lista con todos los números pares entre estos, EXCLUYENDO a los parámetros.
Ejemplo: los parámetros son 4 y 9, por lo tanto, la función retornara: [6,8]"""


def num_usuario (numero1, numero2):
    lista=[]

    if numero1 < numero2:
        uno = numero1
        dos = numero2
    else:
        uno = numero2
        dos = numero1

    if uno % 2 != 0:
        uno = uno +1
    else:
        uno = uno +2

    if dos %2 !=0:
        dos = dos - 1
    else:
        dos = dos -2

    for i in range (uno, dos +1, 2):
        lista.append(i)

    return lista


print (num_usuario (2, 9))
print (num_usuario (-9,1))


"""3. Escribir una función que tome 2 parámetros, el primero que reciba una cadena, y el segundo que reciba un carácter. La función tendrá que retornar la cantidad de veces que aparece ese carácter en esa cadena.
Ejemplo: si los parámetros son “Hola mi nombre es Sebastián” y “s”, la función tendrá que retornar 3 ya que la “s” se encuentra 3 veces repetidas en mi cadena."""

def cantidad (cadena, caracter):
    contador = 0

    for i in range (0, len(cadena)):
        letra = cadena [i]

        if letra == caracter:
         contador = contador +1
    
    return contador

frase_usuario = input("Ingrese una frase: ")
letra_usuario = input("Ingrese una letra: ")
veces = cantidad (frase_usuario,letra_usuario)

print (f"{frase_usuario} contiene {veces} veces la letra {letra_usuario}")

"""4. Elaborar una función que tome como parámetro 2 números, y retorne una lista con todos los números primos entre ese rango de números.
Ejemplo: mis parámetros son 4 y 45, la función tendrá que retornar: [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]."""

def verificar_primo(numero):

    if numero <= 1:
        return False

    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False  
        

    return True

def primos (numero1, numero2):
    lista_primos = []

    for i in range(numero1, numero2 + 1):
        if verificar_primo(i):  
            lista_primos.append(i)  

    return lista_primos 


num1_usuario = int (input("Ingrese un número entero: "))
num2_usuario = int( input("Ingrese un número entero: "))

lista_entrega = primos(num1_usuario, num2_usuario)
print(lista_entrega)


"""5. Elaborar una función que tome como parámetro una lista, y devuelva un bool que diga si en esa lista TODOS sus números son pares."""

def validar_pares (lista_num_usuario):
 
    
    for numero in lista_num_usuario:
        if numero % 2 != 0:
            return False

 
    return True
           

        

lista = [2,4,6,8,10,222]

num_usuario_pares = validar_pares (lista)

print (num_usuario_pares)

"""6. Elaborar una función que tome como parámetro una lista y devuelva un bool que diga si en esa lista TODOS sus números son primos."""

def verificar_primo(numero):

    if numero <= 1:
        return False

    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False  
    return True


def validar_primos (lista_num_usuario):
  
    for numero in lista_num_usuario:
        if verificar_primo (numero) == False:
            return False

 
    return True

        

lista = [3,11]

num_usuario_primos = validar_primos (lista)

print (num_usuario_primos)


"""1. Hacer una calculadora, que tenga las siguientes operaciones.
a. Suma
b. Resta
c. Multiplicación
d. División
e. Potencia
El usuario podrá elegir qué operación hacer y con que números. En caso de que el usuario ingrese como opción “SALIR” la calculadora se cerrara."""

def suma (lista_suma):
    resultado = 0
    for i in range (0,len(lista_suma)):
      resultado = resultado + lista_suma[i]

    return resultado


def resta (lista_resta):
    resultado = lista_resta[0]
   
    for i in range (1,len(lista_resta)):
      resultado = resultado - lista_resta[i]
   

    return resultado
   


def mult (lista_mult):
    resultado = 1
    for i in range (0,len(lista_mult)):
      resultado = resultado * lista_mult[i]

    return resultado


def div (lista_div):
    resultado = lista_div[0]

    for i in range (1,len(lista_div)):
       resultado = resultado / lista_div [i]
    
    return resultado

def pot(lista_pot):
    
    resultado = lista_pot[0]
    for numero in lista_pot[1:]:
        resultado **= numero
    return resultado







while True:
    op_usuario = input("Ingrese una operación (+, -, *, /, **) o 'SALIR' para terminar: ")


    if op_usuario == "SALIR":
        print("Adiós")
        break


    
    numeros = []
    while True:
        num = input("Ingrese un número (o 'fin' para terminar): ")
        if num == "fin":
            break
   
    num = float(num)  # Convertir a número
    numeros.append(num)
       


 

  
if op_usuario == "+":
    resultado = suma(num_usuario)
elif op_usuario == "-":
    resultado = resta(num_usuario)
elif op_usuario == "*":
    resultado = mult(num_usuario)
elif op_usuario == "/":
    resultado = div(num_usuario)
elif op_usuario == "**":
    resultado = pot(num_usuario)


    print(f"El resultado es: {resultado}")



   



# No tuve tiempo de terminar, pero creo que estaba cerca.




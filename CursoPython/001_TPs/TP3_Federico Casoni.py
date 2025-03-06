"""Alumno: Federico Casoni / sabados presencial / TP 3"""


""" 1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo
para un rango de números indicado por un usuario. """ 

lista=[]
for numero in range (1,21):
    lista.append (numero)
print(lista)

# Cree una lista vacía para ingresar los números. Creé un bucle con for para recorrer del 1 al 20 inclusive. Con la variable "numero" cuando se recorre el bucle, se suma a la lista con append y se imprime.


lim_inf= int(input("Ingrese un rango de números desde el: "))
lim_sup= int(input("Hasta el: "))
lista= []
for numero in range(lim_inf,lim_sup+1):
    lista.append(numero)
print(lista)

# El mismo concepto que el anterior, pero el rango del for lo armo con las variables que se crean con dos input para el usuario (sup e inf). Al lim_sup le sumo 1 para que se incluya el último número. 

""" 2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por
ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50  """

numero_usuario = int (input("Ingrese un número del 1 al 10: "))
lista=[]

for multiplicador in range (1,11):
    lista.append (numero_usuario * multiplicador)
print (lista)


# El mismo concepto que el anterior, pero en este caso la variable "multiplicador" (del 1 al 10 inclusive) se multiplica con el numero ingresado por el usuario. Se suma a la lista con append y se imprime la lista.


"""3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
caracteres. """

cadena = str(input("Ingrese una frase: "))
lista_caracteres = []

for posicion_caracter in range(0, len(cadena)):
    caracter = cadena[posicion_caracter]
    contador = 0  
   
    for posicion_lista in range(0, len(lista_caracteres)):
        if lista_caracteres[posicion_lista] == caracter:
            contador = 1  

    if contador == 0:
        lista_caracteres.append(caracter)

print("Lista de caracteres únicos:", lista_caracteres)


# Creé una variable llamada "cadena" para que el usuario ingrese una frase. Creé una lista vacía para guardar los caracteres. Usé un "for" para recorrer cada carácter de la cadena, y la variable `posicion_caracter` para la posición de cada carácter. Dentro del bucle, guardé el carácter y creé la variable "contador" en cero, para ver si el carácter ya está en la lista. Usé un bucle interno para recorrer la `lista_caracteres` y verificar si el carácter actual ya está en la lista. Si el carácter ya está en la lista, el "contador" es 1. Si el contador es 0, el carácter no está en la lista, se agrega a  la lista  y la lista se muestra.

"""4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios."""

cadena = str (input("Ingrese una frase: "))
lista_caracteres = []

for posicion_caracter in range (0,len(cadena)):
    caracter = cadena[posicion_caracter]
    if caracter != " ":
        lista_caracteres.append (caracter)
print(lista_caracteres)

# cree una variable "cadena" para que el usuario ingrese una frase con input. Cree un bucle con for con la variable posicion_variable. Con len me aseguro que el bucle recorra el total de los carcteres ingresados por el usuario. Luego creé la variable "carcter" que es igual a la posición de cada carater de la cadena ingresada. Luego puse una condición if, si el caracter es distinto a un espacio, se suma a la lista con append. Luego se imprime la lista.

"""5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite."""

tupla_numeros = (1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8)
numero_usuario = int(input("Ingrese un número: "))
contador = 0 

for posicion_numero in range (0,len(tupla_numeros)):
    numero = tupla_numeros [posicion_numero]
    
    if numero == numero_usuario:
        contador = contador +1

print (f"El número ingresado se repite {contador} veces") 
        


# Creé una tupla con números y una variable con un input para que el usuario ingrese un número. También un contador, para contar cuantas veces se repite el número. Para recorrer cada número de la tupla hice un bucle con for y utilicé len para que el rango llegue a la totalidad de números en la tupla. Luego cree la variable número que es igual a la posición de cada número en la tupla. Por último puse una condición if, si número es igual a numero del usuario, el contador suma 1. Entonces en el recorrido, si conicide, el contador aumenta 1. Cuando termina el bucle, se imprime.

"""6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero"""


tupla_meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio","agosto", "septiembre", "octubre", "noviembre", "diciembre")


while True: 
    numero_usuario = int(input("Ingrese un número del 1 al 12 o 0 para salir: "))

    if numero_usuario == 0:
        print ("Hasta la próxima!")
        break
    
    elif numero_usuario <= len(tupla_meses):
        mes = tupla_meses[numero_usuario - 1]
        print(f" El número ingresado corresponde al mes de {mes}")
    else:
        print("Error, el número debe ser del 1 al 12")


# Hice una Tupla con los meses del año, luego un while true con la condición que se cierra con break si el número del usuario es igual a 0. Luego con elif defino que si es menor o igual a la cantidad de meses de la tupla se imprime el mes. Si es mayor da error. 

"""7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga."""

tupla_numeros = (12, 2, 3, 4, 11, 5, 6, 7, 8, 9, 10, 75)

numero_max = tupla_numeros[0] 
numero_min = tupla_numeros[0]  


for numero in tupla_numeros:
    if numero > numero_max:
        numero_max = numero
    if numero < numero_min:
        numero_min = numero


print(f"El número mayor es: {numero_max} y el menor es: {numero_min}")

# Hice una tupla con una serie de números y luego las variables numero_max y numero_min como contadores. En un primer momento le puse que eran igual a 0, pero me di cuenta que tenian que ser los números específicos de la tupla, entonces son igual a una posición en la tupla_numeros, al poner [0] empieza por el primer numero. Luego hice un for in. El índice "numero" recorre cada uno de los numero de la tupla. Si numero es mayor, es igual al max, si es menor es igual al min En el primer paso numero_max y numero_min van a ser el primer número, pero en el segundo ya se compara.


"""8) (Opcional)Escribir un programa que vaya solicitando al usuario que ingrese nombres. - Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. - Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la cadena "*", para salir del programa"""



nom_tel = {"adrian": "387 2221111", "andrea": "387 3334444", "jorge": "387 8889999"}


while True:
    nom_usuario = input("Ingrese el nombre de una persona para saber su teléfono o * para salir del programa: ")
    
    if nom_usuario == "*":
        print("Hasta la próxima")
        break

    elif nom_usuario in nom_tel:
        telefono = nom_tel[nom_usuario]
        print (telefono)
    
    else:
        nom_tel [nom_usuario] = input(f"Ingrese el teléfono de {nom_usuario}: ")
        
       
        print(f"Nuevo número ingresado: ")
        print(f"{nom_usuario}: {nom_tel [nom_usuario]}")

        
# Hice un diccionario con nombres y números de télefono. Luego hice un while true que se termina si el nombre de usuario es "*". Con el elif hice que si el nombre ingresado está en el diccionario, el teléfono será el que corresponde al usuario mencionado. Si nada de eso se cumple, es que el nombre no está, entonces se agrega. Pero puse un input para que pueda poner el número. 

"""9) Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor."""


lista_numeros = []

while True:
    num_usuario = int(input(f"Ingrese números de a uno (inserte 0 para terminar): "))

    if num_usuario != 0:
        lista_numeros.append(num_usuario)
    else:
        break

lista_ordenada = []
 

while lista_numeros: 
    numero_min = lista_numeros[0] 
    
    for numero in lista_numeros:
        if numero < numero_min:
         numero_min = numero
    
    
    lista_ordenada.append(numero_min)
    lista_numeros.remove(numero_min)

print(lista_ordenada)






"""11) Opcional: Codificador Morse: Desarrolle un programa en Python que permita al
usuario escribir un mensaje y convertirlo a código Morse. La codificación Morse se
presenta en la siguiente tabla: """


tracutor_morse = {"a":".-","b": "-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","@": " / "}
        

men_usuario = input("Ingrese un mensaje: ")
lista_caracteres = []
codigo = ""
frase_codigo = ""

for i in men_usuario:

    if i != " ":
        lista_caracteres.append(i)

    else:
        lista_caracteres.append("@")


for j in range (0,len(lista_caracteres)):
    letra = lista_caracteres [j]
    codigo = (tracutor_morse[letra])
    frase_codigo = frase_codigo + codigo

print(frase_codigo)


# el "@": " / ", lo sumé al diccionario directamente. Podría haber puesto en el programa "tracutor_morse[@] = " / " , pero considerando que es sumarle un proceso a la máquina, cuando podía editar el diccionario directamente, me pareción mejor. Entiendo que pueden existir situaciones en que editar el diccionario no sea una buena opción, en tal caso usaría la otra opción. Creo que en caso que editar el diccionario sea una cosa que no se puede hacer, agregaría un if en el segundo ciclo. Pero para este ejercicio, la opción que tomé es la más sencilla de todas. """




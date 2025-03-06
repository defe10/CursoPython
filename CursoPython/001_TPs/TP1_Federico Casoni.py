"""
Trabajo práctico Nro 1
Alumno: Federico Casoni
Comisión: Sábados - presencial
"""

"""
1. Almacene un mensaje en una variable e imprímalo en pantalla. Después cambie el valor
del mensaje e imprímalo nuevamente.
"""
mensaje = input("Escriba un mensaje ")
print(mensaje)
mensaje = input("Escriba otro mensaje ")
print (mensaje)

# En la primera parte, con input doy una entrada de información para la variable "mensaje" que luego la veo gracias a print. En la segunda parte reasigno otra información a la variable mensaje. 

"""
2. Almacene el nombre de una persona en una variable, imprima un mensaje para esa persona
"""
Nombre = input("Escriba su nombre ")
print("Hola " + Nombre + ",¿Te gustaría aprender a programar?")

# Con input doy información a la variable "Nombre". Con "+"" concateno la frase con la variable.

"""
3. El número ocho: Escriba una suma, resta, multiplicación y división que resulten cada una en el
número ocho. Asegúrese de utilizar la función print() para ver los resultados en pantalla.
"""

Suma = (4+4)
Resta = (16-8)
Multiplicacion = (4*2)
Division = (24//3)
print (Suma, Resta, Multiplicacion, Division)

# Realicé las cuatro operaciones matemáticas y las asigné a una variable con su nombre correspondiente. Para verlas, separaré las variables con comas.

"""
4. Cree cuatro variables llamadas mi_entero, mi_decimal, mi_string y mi_booleano. Asigne a cada
variable un valor del tipo que le corresponda. Luego muestre en pantalla el tipo de cada variable
usando la función type() combinando todo con la función print()
"""

mi_entero = 10
mi_decimal = 3.5
mi_string = "hola!"
mi_booleano = True

print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))

# Asigné un valor correspndiente a cada variable y con "type" mostré el tipo de cada variable.

"""
5. Escriba un programa que acepte un numero decimal como entrada y lo imprima sin lugares
decimales.
"""
numero = float(input("Ingrese un número con decimal: "))
print(int(numero))

# Con "float" convierto el valor que ingresa el usuario en un número con decimal. Con "int" le quito los decimales

"""
6. Escriba un programa que le pida al usuario que ingrese nombre y edad. Luego muestre un
mensaje donde le informe el año en que va a cumplir 100.
"""
Nombre = input("Escriba su Nombre: ")
Edad = int(input("Indique su edad: "))
Año = (100 - Edad) + 2025
print("Hola " + Nombre + ". Cumplirás 100 años en el año " + str(Año))

# Con input le asigno valor a las variables "Nombre" y "Edad". En "Edad" convierto el valor a un número entero con "int". En el print, con "str" convierto el valor en texto (esto es lo que más me costó darme cuenta).

"""
7. Escriba un programa que permita convertir una temperatura en Celsius a la escala Fahrenheit. La
fórmula es:
Fahrenheit = (9.0/5.0) x Celsius + 32
"""

Celsius = float(input("Grados Celsius: "))
Formula = (Celsius * 1.8) + 32
print("Grados Fahrenheit: " + str(Formula))

# Utilicé el mismo procedimiento que en el ejercicio anterior, solo que el dato ingresado lo convierto a "float" para que pueda admitir decimales.

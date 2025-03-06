"""
Trabajo práctico Nro 2
Alumno: Federico Casoni
Comisión: Sábados - presencial
"""
"""
1. Pida un número al usuario y determine si es par o impar
"""

Numero = int(input("Ingrese un número: "))
if Numero %2 == 0:
    print(f"El número {Numero} es par")
else:
    print(f"El número {Numero} es impar")

# Todo número par es múltiplo de 2. Por lo tanto, si divido un número por 2 y el resto es igual a cero, es par, sino es impar. l

"""
2. Escriba una cadena if-elif-else que determine el estado de vida de una persona
"""

nombre = input("Ingrese el nombre de una persona: ")
edad = int(input("Ingrese la edad de la persona: "))

if edad < 2:
    print(f"{nombre} es un bebé")
elif 2 <= edad < 4:
    print(f"{nombre} es un infante")
elif 4 <= edad < 12:
    print(f"{nombre} es un niño")
elif 12 <= edad < 20:
    print(f"{nombre} es un adolescente")
elif 20 <= edad < 65:
    print(f"{nombre} es un adulto")
else:
    print(f"{nombre} es un anciano")

# La primera condición es "si la edad es menor que dos". Luego se tienen que cumplir dos condiciones, entonces en elif utilicé <= y <

"""
3. Cree un ciclo que nunca termine y ejecútelo. Puede probarlo haciendo que muestre algo en
pantalla por cada pasada del ciclo. Para finalizarlo, presione Ctrl-C o el comando para detener la ejecución correspondiente a su editor
"""

while True:
    print("Este bucle no termina hasta que presione Ctrl-C")

# se genera un bucle infinito porque "mientras sea verdad" se va a imprimir hola

"""
4. Ejercicio 4
"""
numero=1
while numero <= 100:  
    linea = 0
    while linea < 10:  
        print(numero, numero+1, numero+2, numero+3, numero+4, numero+5, numero+6, numero+7, numero+8, numero+9)  
        numero += 10
        linea += 1

# primero me salió el ejercicio 5, despúes le sumé un while con la variable linea, para determinar los numero por línea, pero no suma mucho. 

"""
5. Ejercicio 5
"""
numero = 1
while numero <= 100:  
        print(numero, numero + 1, numero + 2, numero + 3, numero + 4, 
              numero + 5, numero + 6, numero + 7, numero + 8, numero + 9)  
        numero = numero + 10 

# use la variable "numero" para iniciar el conteo. En el print sumé hasta llegar a 10, y con numero= numero + 10, le sumo 10 a la siguiente linea.



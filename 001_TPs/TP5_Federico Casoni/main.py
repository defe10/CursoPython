"""1. Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si la parte decimal es mayo 0.5 (por
ejemplo 3.5), devolver el entero siguiente (en este caso, 4), si no devolver
el entero inmediatamente anterior."""


import time # importación de modulo time

inicio = time.time() #inicio de tiempo

def redondear(numero):
    num_ent = int(numero)
    num_dec = numero - num_ent
    
    if num_dec >= 0.5:
        return int(numero+1)
    else:
        return int(numero)

fin = time.time() #fin de tiempo
tiempo_1 = fin - inicio


num_usuario = float(input("Ingrese número con decimales: "))
num_redondeado = redondear(num_usuario)
print(num_redondeado)




"""2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado."""


from modulo_uno import redondear

inicio = time.time() #inicio de tiempo

def suma (num1, num2):
    return redondear(num1+num2)

fin = time.time() #fin de tiempo
tiempo_2 = fin - inicio

resultado = suma(12.3, 45.1)
print(resultado)




"""3. Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema."""

from datetime import datetime

inicio = time.time() #inicio de tiempo
def fecha_hora():
  
    fecha_hora_actual = datetime.now().replace(microsecond=0)
    return fecha_hora_actual

fin = time.time() #fin de tiempo
tiempo_3 = fin - inicio

fecha_hora = fecha_hora()
print("Fecha y hora actuales:", fecha_hora)




"""4. Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito)."""

import random

inicio = time.time() #inicio de tiempo

def aleatorio ():
   numero_random = (random.randint (1,5))*2
   return numero_random

fin = time.time() #fin de tiempo
tiempo_4 = fin - inicio

# while True: 
#     numero = aleatorio()
#     print (numero)





"""5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas"""

import time # importación de modulo time
import random

inicio = time.time() #inicio de tiempo

def bola_magica ():
   numero = random.randint (1,8)
   if numero ==1:
      return "Es seguro que sí"
   elif numero == 2:
      return "Las chances son buenas"
   elif numero == 3:
      return "Puedes contar con ello"
   elif numero == 4:
      return "Pregúntame de nuevo más tarde"
   elif numero == 5:
      return "Pregúntame de nuevo más tarde"
   elif numero == 6:
      return "No veo con claridad, intenta de nuevo"
   elif numero == 7:
      return "Mi respuesta es no"
   else:
      return "Mis fuentes me dicen que no"

fin = time.time() #fin de tiempo
tiempo_5 = fin - inicio

pregunta = input ("Hacele una pregunta a la Bola Mágica: ")
respuesta = bola_magica()
print (respuesta)




"""6. Encuentre el tiempo de ejecución de los programas de los ejercicios
anteriores (pista: use el módulo time)"""

# Puse solo un ejercicio a modo de ejemplo <--------------

import time # importación de modulo time
import random # importación del programa 

inicio = time.time() #inicio de tiempo

def bola_magica (): #declaración del programa
   numero = random.randint (1,8)
   if numero ==1:
      return "Es seguro que sí"
   elif numero == 2:
      return "Las chances son buenas"
   elif numero == 3:
      return "Puedes contar con ello"
   elif numero == 4:
      return "Pregúntame de nuevo más tarde"
   elif numero == 5:
      return "Pregúntame de nuevo más tarde"
   elif numero == 6:
      return "No veo con claridad, intenta de nuevo"
   elif numero == 7:
      return "Mi respuesta es no"
   else:
      return "Mis fuentes me dicen que no"

pregunta = input ("Hacele una pregunta a la Bola Mágica: ") #formulación del programa 
respuesta = bola_magica()

fin = time.time() #fin de tiempo
tiempo_programa = fin - inicio
print(tiempo_programa)




"""7. Sorteo: Escriba un programa que simule un sorteo donde toman uno o
más papeles al azar de un pozo para elegir los ganadores."""


import random

inicio = time.time() #inicio de tiempo

def ingresar_nombres():
 
    papeles = {}
    contador = 0

    while True:
        nombre = input("Ingrese un nombre para el sorteo (o * para terminar): ")
        if nombre == "*":
            break  
        contador += 1
        papeles[contador] = nombre  

    return papeles

def realizar_sorteo(papeles):
 
    while True:
        opcion = input("¿Sacamos papelito? (s/n): ")
        if opcion != "s":
            print("Adiós.")
            break  

        numero = random.randint(1, len(papeles))
        nombre_ganador = papeles[numero]
        print(f"¡El ganador es: {nombre_ganador}!")

fin = time.time() #fin de tiempo
tiempo_7 = fin - inicio

papeles = ingresar_nombres()  
realizar_sorteo(papeles)  


"""8. Escriba una función que pida al usuario ingresar su fecha de nacimiento y sea capaz de devolver la cantidad de días desde su nacimiento hasta hoy."""


from datetime import datetime

inicio = time.time() #inicio de tiempo

def calcular_dias():
    
    fecha_usuario = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
    fecha_nacimiento = datetime.strptime(fecha_usuario, "%d/%m/%Y")


    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_nacimiento
    dias_desde_nacimiento = diferencia.days

     
    print(f"Llevas {dias_desde_nacimiento} vividos.")
    return dias_desde_nacimiento

fin = time.time() #fin de tiempo
tiempo_8 = fin - inicio

calcular_dias()




"""9. Implemente el programa del ejercicio 6 usando un diccionario."""

tiempo_total = {1: tiempo_1, 2: tiempo_2, 3: tiempo_3, 4: tiempo_4, 5: tiempo_5, 6: tiempo_programa, 7: tiempo_7, 8: tiempo_8}    

ejercicio= int(input ("Ingrese el número de ejercicio para saber el tiempo de ejecución (del 1 al 8): "))
print(tiempo_total[ejercicio])


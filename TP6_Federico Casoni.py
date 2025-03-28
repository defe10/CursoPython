
datos = {"Alumnos": []} 


def guardar_datos():
    archivo = open("datos.txt", "w")
    for alumno in datos["Alumnos"]:
        archivo.write(f"{alumno['Nombre']},{alumno['Apellido']},{alumno['DNI']},{alumno['Fecha de nacimiento']},{alumno['Tutor']},{'|'.join(map(str, alumno['Notas']))},{alumno['Faltas']},{alumno['amonestaciones']}\n")
    archivo.close()


def cargar_datos():
    archivo = open("datos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    
    datos["Alumnos"] = []
    for linea in lineas:
        elementos = linea.strip().split(",")
        nombre, apellido, dni, fecha_nacimiento, tutor = elementos[:5]
        notas = list(map(int, elementos[5].split("|")))
        faltas, amonestaciones = map(int, elementos[6:8])
        
        datos["Alumnos"].append({
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
            "Fecha de nacimiento": fecha_nacimiento,
            "Tutor": tutor,
            "Notas": notas,
            "Faltas": faltas,
            "amonestaciones": amonestaciones
        })


cargar_datos()


def mostrar_alumno(alumno): 
    print(f"Nombre: {alumno['Nombre']}")
    print(f"Apellido: {alumno['Apellido']}")
    print(f"DNI: {alumno['DNI']}")
    print(f"Fecha de Nacimiento: {alumno['Fecha de nacimiento']}")
    print(f"Tutor: {alumno['Tutor']}")
    print(f"Notas: {', '.join(map(str, alumno['Notas']))}") 
    print(f"Faltas: {alumno['Faltas']}")
    print(f"Amonestaciones: {alumno['amonestaciones']}")
    print("------")

def modificar_alumno(alumno):  
    print("Agregue nuevo dato o aprete ENTER.")
    nombre = input(f"Nombre: ")
    apellido = input(f"Apellido: ")
    dni = input(f"DNI: ")
    fecha_nacimiento = input(f"Fecha de nacimiento: ")
    tutor = input(f"Tutor: ")
    notas = input(f"Notas: ")
    faltas = input(f"Faltas: ")
    amonestaciones = input(f"Amonestaciones: ")

    if nombre:
        alumno['Nombre'] = nombre
    if apellido:
        alumno['Apellido'] = apellido
    if dni:
        alumno['DNI'] = dni
    if fecha_nacimiento:
        alumno['Fecha de nacimiento'] = fecha_nacimiento
    if tutor:
        alumno['Tutor'] = tutor
    if notas:
        alumno['Notas'] = [int(nota) for nota in notas.split(',')]
    if faltas:
        alumno['Faltas'] = int(faltas)
    if amonestaciones:
        alumno['amonestaciones'] = int(amonestaciones)

    guardar_datos()  
    print("Datos actualizados")

def agregar_alumno():  
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
    tutor = input("Ingrese el nombre y apellido del tutor: ")
    notas = input("Ingrese las notas separadas por comas (ej: 7,8,9): ").split(',') 
    notas = [int(nota) for nota in notas]
    faltas = int(input("Ingrese las faltas: "))
    amonestaciones = int(input("Ingrese las amonestaciones: "))

    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "amonestaciones": amonestaciones
    }

    datos["Alumnos"].append(nuevo_alumno)
    guardar_datos()  
    print("Alumno agregado")

def expulsar_alumno(dni): 
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            datos["Alumnos"].remove(alumno)
            guardar_datos() 
            print(f"El alumno ha sido expulsado.")
            return
    print(f"No se encontró ningún alumno con DNI {dni}.")

def mostrar_todos_los_alumnos(): 
    if not datos["Alumnos"]:
        print("No hay alumnos registrados.")
    else:
        for alumno in datos["Alumnos"]:
            mostrar_alumno(alumno)

def opciones(): 
    while True:
        print("1. Mostrar todos los alumnos")
        print("2. Agregar alumnos")
        print("3. Modificar los datos de los alumno")
        print("4. Expulsar alumnoa")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_todos_los_alumnos()
        elif opcion == "2":
            agregar_alumno()
        elif opcion == "3":
            dni = input("Ingrese el DNI del alumno a modificar: ")
            for alumno in datos["Alumnos"]:
                if alumno["DNI"] == dni:
                    modificar_alumno(alumno)
                    break
            else:
                print(f"No hay alumno con ese número de DNI")
        elif opcion == "4":
            dni = input("Ingrese el DNI del alumno que quiere expulsar: ")
            expulsar_alumno(dni)
        elif opcion == "5":
            print("Adios")
            break
        else:
            print("No es opción válida.")


opciones()

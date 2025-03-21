
datos = {   # <---- Diccionario con datos de alumnos
    "Alumnos": [
        {
            "Nombre": "Federico",
            "Apellido": "Casoni",
            "DNI": "11222333",
            "Fecha de nacimiento": "14/08/1978",
            "Tutor": "Nico M",
            "Notas": [7, 8, 9],
            "Faltas": 3,
            "amonestaciones": 1
        },
        {
            "Nombre": "Juan",
            "Apellido": "García",
            "DNI": "22333444",
            "Fecha de nacimiento": "15/05/2011",
            "Tutor": "Pablo T",
            "Notas": [8, 9, 10],
            "Faltas": 1,
            "amonestaciones": 0
        }
    ]
}

def mostrar_alumno(alumno): # <-------- mostrar los datos de cada alumno
    print(f"Nombre: {alumno['Nombre']}")
    print(f"Apellido: {alumno['Apellido']}")
    print(f"DNI: {alumno['DNI']}")
    print(f"Fecha de Nacimiento: {alumno['Fecha de nacimiento']}")
    print(f"Tutor: {alumno['Tutor']}")
    print(f"Notas: {', '.join(map(str, alumno['Notas']))}") # <----- Esto lo saqué de un foro, con .join aplico la "," y el espacio y con map se lo aplico a cada elemento de la lista.
    print(f"Faltas: {alumno['Faltas']}")
    print(f"Amonestaciones: {alumno['amonestaciones']}")
    print("------")






def modificar_alumno(alumno): # <------- modificar datos de cada alumo
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

    print("Datos actualizados")






def agregar_alumno():  # <------ agregar alumnos
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
    print("Alumno agregado")




def expulsar_alumno(dni): # <---- expulsar a un alumnos
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            datos["Alumnos"].remove(alumno)
            print(f"El alumno ha sido expulsado.")
            return
    print(f"No se encontró ningún alumno con DNI {dni}.")


def mostrar_todos_los_alumnos(): # <----- mostrar todos los alumnos
    if not datos["Alumnos"]:
        print("No hay alumnos registrados.")
    else:
        for alumno in datos["Alumnos"]:
            mostrar_alumno(alumno)


def opciones(): # <------ opciones
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
            dni = input("Ingrese el DNI del alumno que quiere expulsar expulsar: ")
            expulsar_alumno(dni)
        elif opcion == "5":
            print("Adios")
            break
        else:
            print("No es opción válida.")


opciones()
listaEstudiantes = []

def escribirEdad():
    nombre = input("Escribe te nombre: ")
    edad = input("Escribe te edad: ")
    return nombre, edad

def totalEstudiantesEnClase():
    totalEstudiantes = input("Escriba los estudiantes que fueron a clase: ")
    i = 0
    while i < int(totalEstudiantes):
        listaEstudiantes.append(escribirEdad())
        i += 1

totalEstudiantesEnClase()
print(listaEstudiantes)
listaEstudiantes.sort(key=lambda edades: edades[1])
print(listaEstudiantes)
print(f"El profesor es {listaEstudiantes[-1]}")
print(f"El asistente es {listaEstudiantes[0]}")


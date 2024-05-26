# Funciones simples
def saludar():
    print("Hola mundo")
    
# saludar()


# Funciones con parametros

def saludarNombre(nombre, sexo):
    sexo = sexo.capitalize()
    if sexo == "Mujer":
        aux = "Mujer"
    elif sexo == "Hombre":
        aux = "Hombre"
    else:
        aux = "Escribe bien"
        
    print(f"{aux} - {nombre}")
        
    
# saludarNombre("Cami", "Mujer")
# saludarNombre("Sebas", "hombre")
# saludarNombre("Santi", "Hodsmbre")

# Funcion que nos retorne valores
def calculoPrimerNum(num):
    primerNumero = str(num)
    primerNumeroInt = int(primerNumero[0])
    # num*2 
    # print(type(primerNumeroInt))
    return num, primerNumeroInt

print(calculoPrimerNum(24))
numeroIngresado, numeroObtenido = calculoPrimerNum(24) 
print(f"Entrada {numeroIngresado}")
print(f"Salida {numeroObtenido}")
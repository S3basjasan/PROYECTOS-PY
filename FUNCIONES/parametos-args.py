# Usando listas
# def sumar(numeros):
#     return sum(numeros)
    
# print(f"La suma de los numeros es: {sumar([1, 2, 3, 4])}")

# Usando *args como parametros
def sumar(*numeros):
    return sum(numeros)
    
print(f"La suma de los numeros es: {sumar(1, 10, 1, 1, 1)}")

def saludar(nombre, apellido  = "sasa"):
    # apellido = "sa"
    print(f"Hola {nombre} {apellido}")

saludar("sebas", "1234")
# Lista con corchetes
lista = ["Sebas sanchez", 20, 1.75]
print("Lista")
print(lista)
lista[2] = 1
print(lista[2])

# Tupla con parentesis. No se puede modificar
print("Tupla")
tupla = ("Sebas sanchez", 20, 1.75)
print(tupla)
print(tupla[2])

# Conjunto (set). No se puede modificar ni muestra datos repetidos
# No se puede acceder por su posicion
print("Conjunto")
conjunto = {"Sebas sanchez", 20, 1.75}
print(conjunto)
print(type(conjunto))

# Diccionario
print("Diccionario")
diccionaro = {
    0 : "sebastian",
    "edad" : 20,
    "altura" : 1.75
}
print(diccionaro)
print(diccionaro[0])
print(diccionaro["edad"] + 1)
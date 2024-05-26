diccionario = {
    "nombre" : "sebas",
    "edad" : 20,
    "mascota": "perro"    
}
print(diccionario)

# Recorrido con items() para obtener la clave y el valor
for key in diccionario.items():
    print(key[1])
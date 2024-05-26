# Solo se puede crear listas, tuplas o diccionarios vacias con la funcion
diccionario = dict(nombre= "sebas", apellido= "sanchez")
print(diccionario)

diccionario2 = {(1, 2): "OK"}
print(diccionario2[(1,2)])

# Creando diccionaria con fromkeys()
diccionario = dict.fromkeys(["seba", "sebiasas"], "apellido")
print(diccionario)

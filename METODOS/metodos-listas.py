lista = list(["sebas", 20, "azul"])
lista2 = list([1, 20, 5, 8])
conjunto = set({1, 2, 3})

print(conjunto)

print(lista)
print(len(lista))   # Cantidad de elementos

# Agregar elementos
print("Metodos para agregar elementos a la lista")
lista.append("jajajaj")
print(lista)
lista.insert(1, "sanchez")
print(lista)
lista.extend([2024, "MAYO"])
print(lista)

# Elimina un elemento de la dista
print("Metodos para eliminar elementos a la lista")
#lista.pop(0)
# Elimina por posicion
print(lista.pop(0)) 
print(lista)
print(lista.pop(-1))
print(lista)

# Elimina por el nombre
print(lista.remove("azul")) 
print(lista)

# Elimina toda la lista
#lista.clear()

# Metodos para ordenar
# Solo numeros y boolean
print("Metodos para ordenar elementos a la lista")
lista2.sort()   # Mayor a menor
#lista2.sort(reverse=True)
#lista2.reverse()
print(lista2)

print(lista2.index(5))

# Conjuntos y tuplas inmutables
# Solo se puede buscar y contar 
# Se puede redeclararlos 
# No se puede cambiar elementos
# No se puede cambiar el orden



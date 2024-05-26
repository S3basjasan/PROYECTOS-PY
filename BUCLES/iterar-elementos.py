# Para listas, tuplas y conjuntos
numeros = [1, 2, 3, 4]
letras = ["a", "b", "c", "d"]
# for numero in numeros:
#     print(numero)
    
# Recorrer dos listas al mismo tiempo, pero tiene que tener igual numeros de elementos
# for numero, letra in zip(numeros, letras):
#     print(f"Lista numeros {numero}")
#     print(f"Lista letras {letra}")
    
# for num in range(5):
#     print(num)

# Forma para recorrer una lista
# enumerate() obtenemos los indices
for num in enumerate(numeros):
    print(num)
    
# Usando for else
for num in numeros:
    print(num)
else:
    print("El bucle termino")
# Cracion de funciones sin nombre, funciones anonimas
# No es apta para hacer mas de una instruccion
multiplicarPorDos = lambda num : num+2
print(multiplicarPorDos(10))


# El filter funciona como un bulce
# Los que devuelve True los agrega a la lista
numeros = [1, 2, 3, 4, 5, 6]
# def numerosPares(numero):
#     return numero % 2 == 0    
# numerosPares = filter(numerosPares, numeros)


numerosPares = filter(lambda num: num % 2 == 0, numeros)
print(type(numerosPares))
print(list(numerosPares))


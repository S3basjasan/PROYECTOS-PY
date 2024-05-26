letras = ["a", "b","c","d","e"]
cadena = "Buenas noches"
numeros = [1, 2, 3, 4, 5] 

# continue salta 
for letra in letras:
    if (letra == "a") | (letra == "d"):
        continue
    print(letra)
    
    
# break finaliza el bucle 
for letra in letras:
    if (letra == "b") | (letra == "d"):
        break
    print(letra)
    
    
for letra in cadena:
    print(letra)
    
    
# Duplicar numeros
print(numeros)
numerosDuplicados = [letra + "s" for letra in letras]
print(numerosDuplicados)
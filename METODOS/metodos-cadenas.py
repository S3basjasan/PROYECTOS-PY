cadena1 = "Soy sebas"
cadena2 = "Yo soy sophia"
cadena3 = "buenos dias"
cadena4 = "5354"

# Metodos
r1 = cadena1.upper()
r2 = cadena1.lower()
r3 = cadena2.capitalize() # La primera en mayuscula, trasnsforma a los otras en minusculas

r4 = cadena2.find("op") # Devuelva la posicion
#index

r5 = cadena4.isnumeric() # Verifica si es un numero en texto
r6 = cadena3.isalpha() # Solo caracteres no con espacios

r7 = cadena2.count(" sop") # Cuanto se repite un caracter

# Contar cuantos caracteres tiene una cadena
r8 = len(cadena4)
r9 = cadena2.__len__()

r10 = cadena3.startswith("buenosdia") # Verifica si empieza con algo en especifico
r11 = cadena3.endswith("diafs") # Verifica si termina con algo en especifico

r12 = cadena2.replace("o", "i") # Reemplaza 
r13 = cadena3.split("o") # Separa por cadena y lo transforma o tipo lista

print(r13)
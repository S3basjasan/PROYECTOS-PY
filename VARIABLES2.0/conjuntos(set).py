conjunto = frozenset({20, 2024})
conjunto2 = set({conjunto, "seba", "sanchez"})

print(conjunto)
print(conjunto2)

# Teoria de conjuntos
conjuntoNumImpares = {1,3,5}
conjuntoNumImpares2 = {1,3}

# Verificar si es subconjunto
print(conjuntoNumImpares2.issubset(conjuntoNumImpares))
print(conjuntoNumImpares2 <= conjuntoNumImpares)

# Verificar su es superconjunto
print(conjuntoNumImpares.issuperset(conjuntoNumImpares2))
print(conjuntoNumImpares > conjuntoNumImpares2)

# Verificar si son distintos, con un solo elemento en comun son iguales
print(conjuntoNumImpares2.isdisjoint(conjuntoNumImpares))
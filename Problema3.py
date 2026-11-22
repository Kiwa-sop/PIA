def conjuntos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    return {
        "interseccion": conjunto1 & conjunto2,
        "union": conjunto1 | conjunto2,
        "diferencia_simetrica": conjunto1 ^ conjunto2,
    }


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

datos = conjuntos(lista1, lista2)

print("Intersección:", datos["interseccion"])
print("Unión:", datos["union"])
print("Diferencia simétrica:", datos["diferencia_simetrica"])
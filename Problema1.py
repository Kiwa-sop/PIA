def lista (numeros):

    positivos=[]

    for numero in numeros:
        if numero > 0:
            positivos.append(numero)

    sin_repetidos=set(positivos)
    return sorted(sin_repetidos)

lista_numeros=[4,-1,2,4,3,-5,2]
print("Resultado:", lista(lista_numeros))
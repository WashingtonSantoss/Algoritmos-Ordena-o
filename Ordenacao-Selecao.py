#Ordenação por seleção

def separar(lista):
    indice = 0
    pivo = lista[0]

    for i in range(1, len(lista)):
        if pivo < lista[i]:
            indice = i
            pivo = lista[i]

    return indice

def ordenar(lista):
    novalista = []
    for i in range(len(lista)):
        numero_indice = separar(lista)
        novalista.append(lista[numero_indice])
        lista.pop(numero_indice)

    return novalista

print(ordenar([2,9,5,3,7,6]))
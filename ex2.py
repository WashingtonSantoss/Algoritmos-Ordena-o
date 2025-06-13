#Quick Sort

def quick(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]

    menores = []
    maiores = []

    for i in range(1,len(lista)):
        if pivo > lista[i]:
            menores.append(lista[i])
        else:
            maiores.append(lista[i])

    return quick(menores) + [pivo] + quick(maiores)

print(quick([2,5,3,9,6,1,7]))

#Outra forma

def quick(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]

    menores = []
    maiores = []

    for i in lista[1:]:
        if pivo > i:
            menores.append(i)
        else:
            maiores.append(i)

    return quick(menores) + [pivo] + quick(maiores)

print(quick([2,5,3,9,6,1,7]))

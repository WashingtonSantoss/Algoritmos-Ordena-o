#Algoritmo De Busca em largura

from collections import deque

fila = deque()


lista_nomes = {"eu":["marcos","joão","julio","redrick"],
               "marcos":["hugo",'vidal',"kaio"],
               "hugo":["guilherme", "brian","pupilo"]}

fila += lista_nomes['eu']

def pessoa_vendedor(nome):
    return nome[-1] == 'k'

def pesquisa_largura(nomes):
    verificados = []
    while fila:
        pessoa = fila.popleft()
        if not pessoa in verificados:
            if pessoa_vendedor(pessoa):
                print("Nome do vendedor {}".format(pessoa))
            else:
                verificados.append(pessoa)

    return pessoa
    
print(pesquisa_largura(lista_nomes))


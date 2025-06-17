#Algoritmo De Busca em largura

#Se baseia em uma busca onde faz uma pesquisa na minha lista de contatos, e nos contatos dos meus contatos.

from collections import deque

fila = deque() #Implantando uma estrutura de dados  FILA

#Minha lista de contatos, e a lista de contato dos meus contatos
lista_nomes = {"eu":["marcos","joão","julio","redrick"],
               "marcos":["hugo",'vidal',"kaio"],
               "hugo":["guilherme", "brian","pupilo"]}

fila += lista_nomes['eu'] #iniciando a fila com os "meus" amigos

#Condição que seleciona o contato procurado
def pessoa_vendedor(nome):
    return nome[-1] == 'k'

#Função para fazer a busca
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
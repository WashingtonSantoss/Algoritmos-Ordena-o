#Algoritmo de busca com grafos ponderados (Dijkstra)

#Imagine esse grafo
#
#
#              A 
#        6   / | \  1
#           /  |  \
#  inicio  /   |3  \  Fim
#          \   |   /
#        2  \  |  / 5
#            \ B /
#
#

grafo = {}
grafo['Inicio'] = {}
grafo['Inicio']['A'] = 6
grafo['Inicio']['B'] = 2

#print(grafo['Inicio'].keys()) #Testando para ver o return das chaves

#Adicionando o restante dos vértices e seus vizinhos do grafo

grafo['A'] = {}
grafo['A']['Fim'] = 1

grafo['B'] = {}
grafo['B']['A'] = 3
grafo['B']['Fim'] = 5

grafo['Fim'] = {} #Vertice 'Fim' não tem vizinhos

#Agora cria-se uma tabela hash dos custos

#Como representar infinito em py
infinito = float("inf")
custos = {} #Essa tabela representa os custo do inicio aos outros vértices e ao fim...
custos["A"] = 6
custos["B"] = 2
custos["Fim"] = infinito # Como aqui ainda é desconhecido, representa-se como infinito

#Agora cria uma tabela hash para os pais, responsavel para saber quem é o pai de cada vértice

pais = {}
pais['A'] = "Inicio"
pais['B'] = "Inicio"
pais['Fim'] = "None"

#Cria-se um array para não processar mais de uma vez o "Caminho percorrido"

processados = []

#Algoritmo

#1 Enquanto houver grafos a serem processados
#2 Pegue o vértice que está mais proximo do inicio
#3 Atualize os custos para os seus vizinhos
#4 Se qualquer um dos custos dos vizinhos for atualizado, atualize o pai também
#5 Marque o vértice como processado
# Voltar ao passo 1

def ache_no_menos_custo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_menos_custo(custos) 
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_menos_custo(custos)


print("Custo total até o fim:", custos["Fim"])
# Reconstruindo o caminho
caminho = []
nodo_atual = "Fim"
while nodo_atual != "Inicio":
    caminho.insert(0, nodo_atual)
    nodo_atual = pais[nodo_atual]
caminho.insert(0, "Inicio")
print("Caminho mais rapido:", " -> ".join(caminho))


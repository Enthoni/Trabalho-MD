import heapq

def adicionar_aresta(grafo, u, v, peso):
    grafo.append((peso, u, v))

def encontrar(pai, i):
    if pai[i] != i:
        pai[i] = encontrar(pai, pai[i])
    return pai[i]

def unir(pai, rank, x, y):
    raiz_x = encontrar(pai, x)
    raiz_y = encontrar(pai, y)
    if rank[raiz_x] < rank[raiz_y]:
        pai[raiz_x] = raiz_y
    elif rank[raiz_x] > rank[raiz_y]:
        pai[raiz_y] = raiz_x
    else:
        pai[raiz_y] = raiz_x
        rank[raiz_x] += 1

def kruskal(grafo, v):
    grafo.sort()
    pai = list(range(v))
    rank = [0] * v
    agm = []
    
    for peso, u, v in grafo:
        if encontrar(pai, u) != encontrar(pai, v):
            agm.append((u, v, peso))
            unir(pai, rank, u, v)
    return agm

def prim(grafo, v):
    fila_prioridade, agm, visitados = [(0, 0, -1)], [], set()
    
    while len(visitados) < v:
        peso, u, anterior = heapq.heappop(fila_prioridade)
        if u in visitados:
            continue
        visitados.add(u)
        if anterior != -1:
            agm.append((anterior, u, peso))
        for peso, origem, destino in grafo:
            if origem == u and destino not in visitados:
                heapq.heappush(fila_prioridade, (peso, destino, u))
    return agm

# Exemplo de uso:
grafo = []
v = 4
adicionar_aresta(grafo, 0, 1, 10)
adicionar_aresta(grafo, 0, 2, 6)
adicionar_aresta(grafo, 0, 3, 5)
adicionar_aresta(grafo, 1, 3, 15)
adicionar_aresta(grafo, 2, 3, 4)

print("Kruskal:", kruskal(grafo, v))
print("Prim:", prim(grafo, v))

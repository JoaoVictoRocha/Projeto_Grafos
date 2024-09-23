import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("../rsc/arestas.csv")

# Cria o grafo
G = nx.Graph()

for _, linha in df.iterrows():
    orgao_superior: str = linha['Source']
    empresa: str = linha['Target']
    valor_gasto: float = linha['Weight']
    # Adiciona o vertice e arestas ao grafo
    G.add_edge(orgao_superior, empresa, weight=valor_gasto)

pesos_totais = {}

# Calcular o peso total das arestas onde cada vértice está em 'Source'
for u, v, data in G.edges(data=True):
    if u not in pesos_totais:
        pesos_totais[u] = 0
    pesos_totais[u] += data['weight']

# Encontrar os 5 vértices com os maiores pesos totais
maiores_pesos = sorted(pesos_totais.items(), key=lambda x: x[1], reverse=True)[:5]

# Exibir os resultados
print("Os 5 vértices com os maiores pesos totais das arestas onde estão em 'Source':")
for vertice, peso in maiores_pesos:
    print(f"Vértice: {vertice}, Peso Total: {peso}")
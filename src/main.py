import pandas as pd
import networkx as nx

df = pd.read_csv("../rsc/arestas.csv")

# Cria o grafo
G = nx.Graph()

for _, linha in df.iterrows():
    orgao_superior: str = linha['Source']
    empresa: str = linha['Target']
    valor_gasto: float = linha['Weight']
    # Adiciona o vertice e arestas ao grafo
    G.add_edge(orgao_superior, empresa, weight=valor_gasto)

# Criação do arquivo .gexf
nx.write_gexf(G, "../rsc/Grafo.gexf")

# 1. Grau de centralidade
centralidade_grau = nx.degree_centrality(G)

# 3. Componentes conexas
componentes_conexas = list(nx.connected_components(G))

# 4. Identificação de comunidades
comunidades = nx.algorithms.community.greedy_modularity_communities(G)
# for i, comunidade in enumerate(comunidades):
#     print(f"Comunidade {i + 1}:", comunidade)
print(len(comunidades))
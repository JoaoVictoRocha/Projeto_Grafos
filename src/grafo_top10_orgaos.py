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

vertices_unicos = df['Source'].unique()
pesos_totais = {}

# Calcular o peso total das arestas para cada elemento único
for elemento in vertices_unicos:
    peso_total = sum(data['weight'] for u, v, data in G.edges(data=True) if u == elemento or v == elemento)
    pesos_totais[elemento] = peso_total

# Encontrar os 10 maiores pesos
maiores_pesos = sorted(pesos_totais.items(), key=lambda x: x[1], reverse=True)[:10]

# Separar os elementos e seus pesos
elementos, pesos = zip(*maiores_pesos)

# Criar gráfico
plt.figure(figsize=(12, 6))
bars = plt.bar(elementos, pesos, color='skyblue')
# Adicionar rótulos de peso em cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:,.0f}', ha='center', va='bottom')

plt.ylabel('Gasto Total')
plt.xlabel('Órgão Superior')
plt.title('10 orgãos com maiores gastos')
plt.xticks(rotation=45, ha='right')  # Rotacionar rótulos dos elementos
plt.tight_layout()  # Ajustar layout para não cortar elementos
plt.show()
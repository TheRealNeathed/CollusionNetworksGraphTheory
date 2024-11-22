import networkx as nx
import random

def generate_graph_without_clique():
    G = nx.Graph()
    vertices = list('abcdefghijklmnopqrst')
    G.add_nodes_from(vertices)
    
    # Generate random edges
    for _ in range(20):
        u, v = random.sample(vertices, 2)
        weight = random.randint(1, 10)
        G.add_edge(u, v, weight=weight)
    
    return G

def graph_to_dict(G):
    return {
        'vertices': list(G.nodes()),
        'edges': [(u, v, d['weight']) for u, v, d in G.edges(data=True)]
    }

# Generate 50 graphs without cliques
graphs_without_cliques = []
for _ in range(50):
    G = generate_graph_without_clique()
    graphs_without_cliques.append(graph_to_dict(G))

# You can now save or process graphs_without_cliques as needed
# For example, to save to a file:
import json
with open('graphs_without_cliques.json', 'w') as f:
    json.dump(graphs_without_cliques, f)

print("50 graphs without cliques have been generated and saved to 'graphs_without_cliques.json'")
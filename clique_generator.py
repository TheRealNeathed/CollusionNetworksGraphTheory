import networkx as nx
import random

def generate_graph_with_clique():
    G = nx.Graph()
    vertices = list('abcdefghijklmnopqrst')
    G.add_nodes_from(vertices)
    
    # Generate random edges
    for _ in range(20):
        u, v = random.sample(vertices, 2)
        weight = random.randint(1, 10)
        G.add_edge(u, v, weight=weight)
    
    # Generate a clique
    clique_size = random.randint(3, 5)
    clique_nodes = random.sample(vertices, clique_size)
    for i in range(len(clique_nodes)):
        for j in range(i+1, len(clique_nodes)):
            G.add_edge(clique_nodes[i], clique_nodes[j], weight=10)
    
    return G, clique_nodes

def graph_to_dict(G, clique_nodes):
    return {
        'vertices': list(G.nodes()),
        'edges': [(u, v, d['weight']) for u, v, d in G.edges(data=True)],
        'clique': clique_nodes
    }

# Generate 50 graphs with cliques
graphs_with_cliques = []
for _ in range(50):
    G, clique = generate_graph_with_clique()
    graphs_with_cliques.append(graph_to_dict(G, clique))

# You can now save or process graphs_with_cliques as needed
# For example, to save to a file:
import json
with open('graphs_with_cliques.json', 'w') as f:
    json.dump(graphs_with_cliques, f)

print("50 graphs with cliques have been generated and saved to 'graphs_with_cliques.json'")
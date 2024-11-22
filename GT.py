import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add nodes
nodes = [
    "Philip Morris", "CIBA-Geigy", "Altria", "Cronos", "Dow Chemical",
    "RJ Reynolds", "Mongoven, Biscoe and Duchin", "GGOOB", "Action Corps & Truth Squads",
    "BAT", "Reynolds American", "Brown & Williamson", "Procordia AB",
    "Pharmaceutical Company", "Tobacco Company", "Imperial Brands",
    "Premium Cigar Business", "Lorillard", "Tobacco Institute",
    "Marion Merrell Dow", "Ag Chemicals Division"
]

G.add_nodes_from(nodes)

# Add edges with weights
edges = [
    ("Philip Morris", "CIBA-Geigy", 8),
    ("Philip Morris", "Altria", 9),
    ("Altria", "Cronos", 7),
    ("Philip Morris", "Dow Chemical", 6),
    ("RJ Reynolds", "Mongoven, Biscoe and Duchin", 8),
    ("RJ Reynolds", "GGOOB", 9),
    ("GGOOB", "Action Corps & Truth Squads", 7),
    ("BAT", "Reynolds American", 8),
    ("BAT", "Brown & Williamson", 6),
    ("Procordia AB", "Pharmaceutical Company", 9),
    ("Procordia AB", "Tobacco Company", 9),
    ("Imperial Brands", "Premium Cigar Business", 3),
    ("Lorillard", "Tobacco Institute", 5),
    ("Marion Merrell Dow", "Dow Chemical", 7),
    ("CIBA-Geigy", "Ag Chemicals Division", 6)
]

G.add_weighted_edges_from(edges)

# Add a clique (fully connected subgraph)
clique_nodes = ["Philip Morris", "RJ Reynolds", "BAT", "Lorillard", "Imperial Brands"]
for i in range(len(clique_nodes)):
    for j in range(i+1, len(clique_nodes)):
        G.add_edge(clique_nodes[i], clique_nodes[j], weight=10)

# Set up the plot
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, k=4, iterations=50)

# Draw the graph
nx.draw(G, pos, with_labels=True, 
        node_size=3000, font_size=8, font_weight='bold')

# Highlight the clique
nx.draw_networkx_nodes(G, pos, nodelist=clique_nodes, node_size=3000)

# Add edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.title("Weighted Graph of Tobacco Industry Relationships with Clique", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json
import random
import os

# Part 1: Graph Generation

def generate_graph_with_clique(num_nodes=20, clique_size=7):
    G = nx.Graph()
    nodes = [chr(i) for i in range(97, 97 + num_nodes)]  # a to t
    G.add_nodes_from(nodes)
    
    # Generate random edges
    for _ in range(num_nodes * 2):
        u, v = random.sample(nodes, 2)
        if not G.has_edge(u, v):
            weight = random.randint(1, 10)
            G.add_edge(u, v, weight=weight)
    
    # Generate a clique
    clique_nodes = random.sample(nodes, clique_size)
    for i in range(len(clique_nodes)):
        for j in range(i+1, len(clique_nodes)):
            G.add_edge(clique_nodes[i], clique_nodes[j], weight=10)
    
    # Ensure clique is connected to main graph
    non_clique_nodes = list(set(nodes) - set(clique_nodes))
    for _ in range(2):
        clique_node = random.choice(clique_nodes)
        other_node = random.choice(non_clique_nodes)
        G.add_edge(clique_node, other_node, weight=random.randint(1, 10))
    
    return G, clique_nodes

def generate_graph_without_clique(num_nodes=20):
    G = nx.Graph()
    nodes = [chr(i) for i in range(97, 97 + num_nodes)]  # a to t
    G.add_nodes_from(nodes)
    
    # Generate random edges
    for _ in range(num_nodes * 2):
        u, v = random.sample(nodes, 2)
        if not G.has_edge(u, v):
            weight = random.randint(1, 10)
            G.add_edge(u, v, weight=weight)
    
    return G

# Part 2: Saving to JSON

def save_graph_to_json(G, filename, clique=None):
    data = nx.node_link_data(G)
    if clique:
        data['clique'] = clique
    with open(filename, 'w') as f:
        json.dump(data, f)

# Generate and save graphs
if not os.path.exists('graphs'):
    os.makedirs('graphs')

for i in range(50):
    G, clique = generate_graph_with_clique()
    save_graph_to_json(G, f'graphs/graph_with_clique_{i}.json', clique)
    
    G = generate_graph_without_clique()
    save_graph_to_json(G, f'graphs/graph_without_clique_{i}.json')

print("100 graphs generated and saved in the 'graphs' folder.")

# Part 3: Displaying Graphs

def load_graph_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    G = nx.node_link_graph(data)
    clique = data.get('clique', None)
    return G, clique

def display_graph(filename):
    G, clique = load_graph_from_json(filename)
    plt.figure(figsize=(16, 14))
    
    pos = nx.spring_layout(G, k=1.5, iterations=50)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, alpha=0.3, width=1, edge_color='gray')
    
    # Draw non-clique nodes
    non_clique_nodes = list(set(G.nodes()) - set(clique)) if clique else list(G.nodes())
    nx.draw_networkx_nodes(G, pos, nodelist=non_clique_nodes, node_size=700, node_color='lightblue', edgecolors='black')
    
    # Highlight clique if present
    if clique:
        # Draw clique nodes
        nx.draw_networkx_nodes(G, pos, nodelist=clique, node_size=1000, node_color='red', edgecolors='black', linewidths=3)
        
        # Draw edges within the clique
        clique_edges = [(u, v) for u, v in G.edges() if u in clique and v in clique]
        nx.draw_networkx_edges(G, pos, edgelist=clique_edges, edge_color='darkred', width=3, alpha=1)
        
        # Annotate clique nodes
        for node in clique:
            x, y = pos[node]
            plt.annotate(f"Clique: {node}", (x, y), xytext=(5, 5), textcoords="offset points", 
                         bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", alpha=1),
                         fontsize=12, fontweight='bold')
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    # Add legend
    red_node = mpatches.Patch(color='red', label='Clique Node')
    blue_node = mpatches.Patch(color='lightblue', label='Non-Clique Node')
    plt.legend(handles=[red_node, blue_node], loc='upper left', fontsize=12)
    
    if clique:
        plt.title(f"Graph from {filename}\nClique Nodes: {', '.join(clique)}", fontsize=16)
    else:
        plt.title(f"Graph from {filename}\nNo Clique", fontsize=16)
    
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Display all graphs
graph_files = [f for f in os.listdir('graphs') if f.endswith('.json')]
for file in graph_files:
    display_graph(os.path.join('graphs', file))
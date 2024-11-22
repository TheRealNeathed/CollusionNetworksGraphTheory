import json
import networkx as nx
import matplotlib.pyplot as plt

def load_graph_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return nx.node_link_graph(data)

def display_graphs(graph_files):
    num_graphs = len(graph_files)
    fig, axes = plt.subplots(1, num_graphs, figsize=(8*num_graphs, 6))
    
    if num_graphs == 1:
        axes = [axes]
    
    for i, file in enumerate(graph_files):
        G = load_graph_from_json(file)
        nx.draw(G, ax=axes[i], with_labels=True, node_color='lightblue', 
                node_size=500, font_size=10, font_weight='bold')
        axes[i].set_title(f"Graph from {file}")
    
    plt.tight_layout()
    plt.show()

# Example usage
graph_files = ["graphs_with_cliques.json"]
display_graphs(graph_files)
import os
import networkx as nx
from networkx.algorithms.community import louvain_communities
import json


# Function to load a graph from JSON
def load_graph_from_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    G = nx.Graph()
    for node in data['nodes']:
        G.add_node(node['id'])
    for link in data['links']:
        G.add_edge(link['source'], link['target'], weight=link['weight'])
    return G, data.get('clique', [])


# Modularity maximization to detect communities
def modularity_maximization_communities(G):
    return louvain_communities(G, weight='weight')


# Apply antitrust measures
def apply_fines_realistic(G, fine_threshold=8):
    for u, v, data in G.edges(data=True):
        if data['weight'] > fine_threshold:
            data['weight'] = max(1, data['weight'] - 3)
    return G


def apply_market_breakup_realistic(G, clique):
    if clique:
        nodes_to_isolate = clique[:2]  # Isolate up to 2 nodes
        edges_to_remove = []
        for node in nodes_to_isolate:
            edges_to_remove.extend(G.edges(node))
        G.remove_edges_from(edges_to_remove)
    return G


def apply_penalties_realistic(G, dampening_factor=0.7):
    for u, v, data in G.edges(data=True):
        data['weight'] = max(1, int(data['weight'] * dampening_factor))
    return G


# Calculate average community size
def calculate_average_size(communities):
    return sum(len(c) for c in communities) / len(communities)


# Process a folder of graph JSONs
def simulate_realistic_antitrust_measures_folder(folder_path):
    results = {"Fines (Realistic)": [], "Market Breakup (Realistic)": [], "Penalties (Realistic)": []}

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            filepath = os.path.join(folder_path, filename)

            # Load graph and clique
            G, clique = load_graph_from_json(filepath)

            # Original graph communities
            original_communities = modularity_maximization_communities(G)
            avg_original = calculate_average_size(original_communities)

            # After applying realistic fines
            G_fines = apply_fines_realistic(G.copy())
            fines_communities = modularity_maximization_communities(G_fines)
            avg_fines = calculate_average_size(fines_communities)
            results["Fines (Realistic)"].append(avg_original - avg_fines)

            # After realistic market breakup
            G_market_breakup = apply_market_breakup_realistic(G.copy(), clique)
            breakup_communities = modularity_maximization_communities(G_market_breakup)
            avg_breakup = calculate_average_size(breakup_communities)
            results["Market Breakup (Realistic)"].append(avg_original - avg_breakup)

            # After applying realistic penalties
            G_penalties = apply_penalties_realistic(G.copy())
            penalties_communities = modularity_maximization_communities(G_penalties)
            avg_penalties = calculate_average_size(penalties_communities)
            results["Penalties (Realistic)"].append(avg_original - avg_penalties)

    # Calculate overall averages
    overall_results = {measure: sum(values) / len(values) for measure, values in results.items()}

    return overall_results


# Example usage
if __name__ == "__main__":
    folder_path = "graphs"  # Replace with the actual folder path
    overall_results = simulate_realistic_antitrust_measures_folder(folder_path)

    # Display the overall results
    for measure, avg_reduction in overall_results.items():
        print(f"Average Reduction in Community Size ({measure}): {avg_reduction:.2f}")
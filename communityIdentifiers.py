import networkx as nx
import numpy as np
from sklearn.cluster import SpectralClustering
from collections import defaultdict
import json
import os
from networkx.algorithms.community import louvain_communities

def load_graph_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    G = nx.node_link_graph(data)
    clique = data.get('clique', None)
    return G, clique

def modularity_maximization(G):
    """
    Detect communities using modularity maximization (Louvain method).
    """
    try:
        # Apply Louvain method using NetworkX's implementation
        communities = louvain_communities(G, weight='weight', resolution=1, threshold=1e-07)
        
        # Find the maximum community size
        max_community_size = max(len(community) for community in communities)
        
        return max_community_size
    except Exception as e:
        print(f"Error in modularity maximization: {e}")
        return None

def spectral_clustering(G):
    """
    Detect communities using spectral clustering.
    """
    # Convert graph to adjacency matrix
    A = nx.adjacency_matrix(G).todense()
    
    # Determine the number of communities (you may need to adjust this)
    n_clusters = min(len(G) // 2, 10)  # Example: half of nodes or 10, whichever is smaller
    
    # Apply spectral clustering
    sc = SpectralClustering(n_clusters=n_clusters, affinity='precomputed', n_init=100, assign_labels='discretize')
    sc.fit(A)
    
    # Count community sizes
    community_sizes = defaultdict(int)
    for node, label in enumerate(sc.labels_):
        community_sizes[label] += 1
    
    # Find the maximum community size
    max_community_size = max(community_sizes.values())
    
    return max_community_size

def label_propagation(G):
    """
    Detect communities using label propagation.
    """
    # Apply label propagation
    communities = nx.algorithms.community.label_propagation_communities(G)
    
    # Find the maximum community size
    max_community_size = max(len(community) for community in communities)
    
    return max_community_size

def detect_max_community_size(G, actual_clique_size):
    mod_max = modularity_maximization(G)
    spec_clust = spectral_clustering(G)
    label_prop = label_propagation(G)
    
    print(f"Actual Clique Size: {actual_clique_size}")
    print(f"Modularity Maximization: {mod_max}")
    print(f"Spectral Clustering: {spec_clust}")
    print(f"Label Propagation: {label_prop}")

# Process all graphs
graph_files = [f for f in os.listdir('graphs') if f.endswith('.json')]
for file in graph_files:
    print(f"\nProcessing {file}")
    G, clique = load_graph_from_json(os.path.join('graphs', file))
    actual_clique_size = len(clique) if clique else 0
    detect_max_community_size(G, actual_clique_size)
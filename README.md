# Graph Generation, Analysis, and Visualization

## Overview

This project includes three Python scripts:
1. `blahblah.py`: For generating, saving, and visualizing graphs with or without cliques.
2. `CentralityIndicator.py`: For analyzing graph centrality and clustering, condensing graphs into a simplified structure.
3. `PolicyTester.py`: For testing and simulating the impact of antitrust measures on graphs.

## Features

### `blahblah.py`

- **Random Graph Generation**: Generates graphs with user-defined parameters like the number of nodes and clique size.
- **Clique Highlighting**: Identifies and visually highlights cliques in graphs.
- **JSON Export/Import**: Enables saving and loading of graph data in JSON format.
- **Interactive Visualization**: Uses Matplotlib and NetworkX to display graphs with detailed annotations.

### `CentralityIndicator.py`

- **Eigenvector Centrality Calculation**: Measures the influence of nodes using eigenvector centrality, falling back to degree centrality if needed.
- **Spectral Clustering**: Clusters nodes based on the adjacency matrix of the graph.
- **Graph Condensation**: Simplifies the graph by grouping nodes into clusters and connecting clusters based on inter-cluster edges.
- **Analysis Output**: Saves clustering results, centrality measures, and the condensed graph structure to a JSON file.

### `PolicyTester.py`

- **Community Detection**: Uses modularity maximization (via the Louvain algorithm) to identify communities in the graph.
- **Realistic Antitrust Measures**:
  - **Fines**: Reduces the weights of edges exceeding a threshold.
  - **Market Breakup**: Isolates specific nodes in the clique, removing their edges.
  - **Penalties**: Dampens edge weights using a scaling factor.
- **Community Size Analysis**: Calculates the average size of communities before and after applying measures.
- **Simulation Results**: Compares the impact of each measure on the average community size.

## Requirements

Ensure you have the following Python libraries installed:
- `networkx`
- `matplotlib`
- `numpy`
- `scikit-learn`
- `json`
- `os`

To install required packages, run:
```bash
pip install networkx matplotlib numpy scikit-learn
